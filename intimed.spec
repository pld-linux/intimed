Summary: A time server for synchronizing networked machines' clocks.
Name: intimed
Version: 1.10
Release: 9
Copyright: freeware
Group: System Environment/Daemons
Source: ftp://sunsite.unc.edu/pub/Linux/system/network/sunacm/Other/intimed/intimed-1.10.tar.gz
BuildRoot: /var/tmp/intimed-root

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
mkdir -p $RPM_BUILD_ROOT/usr/sbin

install -s -m 755 in.timed $RPM_BUILD_ROOT/usr/sbin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/sbin/in.timed
