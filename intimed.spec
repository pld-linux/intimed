Summary:	A time server for synchronizing networked machines' clocks.
Name:		intimed
Version:	1.10
Release:	11
Copyright:	freeware
Group:		Daemons
Group(pl):	Servery
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/network/sunacm/Other/intimed/intimed-1.10.tar.gz
Source1:	timedt.inetd
Source2:	timedu.inetd
Prereq:		rc-inetd
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
install -d $RPM_BUILD_ROOT{%{_sbindir},/etc/sysconfig/rc-inetd}

install -s in.timed $RPM_BUILD_ROOT%{_sbindir}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/timedt
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/timedu

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd restart 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet sever" 1>&2
fi

%postun
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd restart
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/in.timed
