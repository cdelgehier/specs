Summary:			Tunnel SSH through HTTP Proxies
Name:				corkscrew
Version:			2.0
Release:			1
URL:				http://www.agroman.net/corkscrew/
Source0:       		 	http://www.agroman.net/corkscrew/corkscrew-%{version}.tar.gz
Group:				Productivity/Security
License:        		GPLv2
BuildRoot:      		%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:			gcc make glibc-devel autoconf automake libtool
#Recommends: i			ssh


%description
Corkscrew is a tool for tunneling SSH through HTTP proxies.
Corkscrew has been tested against several proxies requiring HTTP
authentication. Several flaws exist as only basic authentication is currently
supported. Digest authentication may be supported in the future. NTLM
authentication will most likely never be supported.

%prep
%setup -q

%build
%configure
make

%install
mkdir -p ${RPM_BUILD_ROOT}/usr/bin
install -m755 corkscrew ${RPM_BUILD_ROOT}/usr/bin


%clean
rm -rf $RPM_BUILD_ROOT


#%files -f /tmp/%{name}-%{version}.list
%files 
%defattr(-,root,root)
%doc AUTHORS README ChangeLog TODO COPYING
%{_bindir}/%{name}


%changelog
* Thu Feb 29 2012 - Cedric DELGEHIER <cedric.delgehier@gmail.com> - 2.0.0-1.awl6
- Initial release

