# No build ID note found in
%define debug_package %{nil}

Name:           consul
Version:        0.6.4
Release:        1%{?dist}
Summary:        Consul is a tool for service discovery and configuration.

Group:          System Environment/Daemons
License:        MPLv2.0
URL:		https://www.%{name}.io
Source0:        https://releases.hashicorp.com/%{name}/%{version}/%{name}_%{version}_linux_amd64.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if %centos_ver == 7
BuildRequires:  systemd-units
Requires:       systemd
%endif
Requires(pre): shadow-utils

%description
Consul is a tool for service discovery and configuration.
Consul is distributed, highly available, and extremely scalable.

%prep
%setup -q -c

%build

%install
if [ ! -z ${RPM_BUILD_ROOT} ] && [ "${RPM_BUILD_ROOT}" != "/" ]; then
        rm -rf ${RPM_BUILD_ROOT}/*
fi

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/{bootstrap,client,server,ssl}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
%{__install} -p -m 0755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%pre
groupadd -r %{name}
useradd -r -g %{name} -d /var/lib/%{name} -s /sbin/nologin %{name}

#%post -p /sbin/ldconfig
#%postun -p /sbin/ldconfig

%clean
if [ ! -z ${RPM_BUILD_ROOT} ] && [ "${RPM_BUILD_ROOT}" != "/" ]; then
        rm -rf ${RPM_BUILD_ROOT}
fi

%files
%defattr(-,root,root,-)
%dir %attr(750, root, consul) %{_sysconfdir}/%{name}.d
%dir %attr(750, root, consul) %{_sysconfdir}/%{name}.d/bootstrap
%dir %attr(750, root, consul) %{_sysconfdir}/%{name}.d/client
%dir %attr(750, root, consul) %{_sysconfdir}/%{name}.d/server
%dir %attr(750, root, consul) %{_sysconfdir}/%{name}.d/ssl
#%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%attr(755, root, root) %{_bindir}/%{name}


%changelog
* Mon May 16 2016 - Cedric DELGEHIER <cedric.delgehier@gmail.com>  - 0.6.4-1%{?dist}
- Update to 0.6.4

