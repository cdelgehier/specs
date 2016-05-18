Name:           tomcat-connectors
Version:        1.2.41
Release:        1%{?dist}
Summary:        Tomcat mod_jk connector for the Apache httpd

Group:          System Environment/Daemons
License:        ASL 2.0
URL:		http://tomcat.apache.org/connectors-doc            
Source0:        http://www.apache.org/dist/tomcat/tomcat-connectors/jk/tomcat-connectors-%{version}-src.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	httpd-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++

Requires:	httpd

%description
AJP connector for Apache httpd

%prep
%setup -q -n %{name}-%{version}-src

%build
cd native
%if %centos_ver == 7
%configure --with-apxs=/usr/bin/apxs
%else
%configure --with-apxs=/usr/sbin/apxs
%endif
make %{?_smp_mflags}


%install
if [ ! -z ${RPM_BUILD_ROOT} ] && [ "${RPM_BUILD_ROOT}" != "/" ]; then
        rm -rf ${RPM_BUILD_ROOT}/*
fi

mkdir -p $RPM_BUILD_ROOT%{_libdir}/httpd/modules

%{__install} -p -m 0755 native/apache-2.0/mod_jk.so $RPM_BUILD_ROOT%{_libdir}/httpd/modules/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
if [ ! -z ${RPM_BUILD_ROOT} ] && [ "${RPM_BUILD_ROOT}" != "/" ]; then
        rm -rf ${RPM_BUILD_ROOT}
fi

%files
%defattr(-,root,root,-)
%{_libdir}/httpd/modules/mod_jk.so



%changelog
* Mon May 16 2016 - Cedric DELGEHIER <cedric.delgehier@gmail.com>  - 1.2.41-1%{?dist}
- Update to 1.2.41
* Wed Mar 04 2015 - Cedric DELGEHIER <cedric.delgehier@gmail.com>  - 1.2.40-1%{?dist}
- Update to 1.2.40
* Thu Dec 08 2011 - Cedric DELGEHIER <cedric.delgehier@gmail.com>  - 1.2.37-1%{?dist}
- Initial release
