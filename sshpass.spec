Name:      sshpass
Version:   1.05
Release:   1
Summary:   noninteractive ssh password provider
URL:       http://sourceforge.net/projects/sshpass
Source0:   %{name}-%{version}.tar.gz
License:   GPL
Group:     System Environment/Libraries
Prefix:    /usr/bin
BuildRoot: %{_tmppath}/%{name}-root

%description
sshpass  is  a utility designed for running ssh using the mode referred to as "keyboard-interactive" password authentication, but in non-interactive mode.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"


%clean
if [ ! -z ${RPM_BUILD_ROOT} ] && [ "${RPM_BUILD_ROOT}" != "/" ]; then
        rm -rf ${RPM_BUILD_ROOT}
fi

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS
%doc %{_mandir}/man1/sshpass.1*
%{_bindir}/sshpass

%changelog
* Wed Nov 28 2012 - Cedric DELGEHIER <cedric.delgehier@gmail.com>  - 1.05-1%{?dist}
- Update to 1.05

