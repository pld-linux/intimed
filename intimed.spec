Summary:	A time server for synchronizing networked machines' clocks.
Name:		intimed
Version:	1.10
Release:	10
Copyright:	freeware
Group:		System Environment/Daemons
Source:		ftp://sunsite.unc.edu/pub/Linux/system/network/sunacm/Other/intimed/intimed-1.10.tar.gz
BuildRoot:	/tmp/%{named}-%{version}-root

%description
The intimed package contains a server (in.timed), which keeps networked
machines' clocks correctly synchronized to the server's time.  

Install intimed if you need a network time server.

%prep
%setup -q -c

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install -s in.timed $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(755,root,root) %{_sbindir}/in.timed
