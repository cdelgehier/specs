Name:           traffic-shaping
Version:       	1.1.0
Release:        1%{?dist}
Summary:	Init script for BW limiting
Group:		Applications/System
URL: 		http://mirrors-atosworldline-com.priv.atos.fr/private/redhat/trp-pm
Source0:       	traffic-shaping-1.1.0.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
#Requires:	

%description
This script enhances bandwidth and rate limiting
on network interfaces.
Traffic can be modded on a specific interface and
on a upload/download basis.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
/bin/cp -axv ${RPM_BUILD_DIR}/%{name}-%{version}/* ${RPM_BUILD_ROOT}/

%post
/bin/chmod 755 /etc/init.d/traffic-shaping
/sbin/chkconfig --add traffic-shaping
echo "-------------------------------------------------------------------"
echo "Installation of Traffic Shaping finished"
echo "Please edit /etc/traffic-shaping.conf file                         "
echo "-------------------------------------------------------------------"

%files 
%defattr(644,root,root,-)
%attr(755,root,root)/etc/init.d/traffic-shaping
%attr(644,root,root)/etc/traffic-shaping.conf
#{%defattr(644,root,root,-)

%preun
/sbin/chkconfig --del traffic-shaping

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Apr 03 2015 - Cedric DELGEHIER <cedric.delgehier@gmail.com> - 1.1.0-1
- Adding management ip range
* Thu Oct 09 2014 - Baptiste Thonnard <baptiste.thonnard@atos.net> - 1.0.1-1
- Initial release
- Configuration is sourced from /etc/traffic-shaping.conf

