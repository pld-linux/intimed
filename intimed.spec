Summary:	A time server for synchronizing networked machines' clocks
Summary(de):	Zeit-Server zum Synchronisieren von Uhren
Summary(es):	Time server para sincronización de hora
Summary(pt):	Time server para sincronização de hora
Summary(tr):	Saat eþzamanlamasý için time sunucusu
Name:		intimed
Version:	1.10
Release:	13
License:	Freeware
Group:		Daemons
Group(de):	Server
Group(pl):	Serwery
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/network/sunacm/Other/intimed/%{name}-%{version}.tar.gz
Source1:	timedt.inetd
Source2:	timedu.inetd
Prereq:		rc-inetd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsolets:	timed

%description
The intimed package contains a server (in.timed), which keeps
networked machines' clocks correctly synchronized to the server's
time.

%description -l es
intimed es un servidor que irá informar la hora a las máquinas de la
red. Es útil para mantener las máquinas de la red en sincronía.

%description -l de
intimed ist ein Server, der an vernetzte Computer die Zeit ausgibt.
Nützlich zur Synchronisation eines Netzwerks.

%description -l fr
intimed est un serveur qui indique aux machines connectées l'heure
qu'il est. Utile pour synchroniser les réseaux de machines sur l'heure
correcte.

%description -l pt
intimed é um servidor que irá informar às máquinas da rede que horas
ele possui no momento. Ele é útil para manter as máquinas da rede em
sincronia.

%description -l tr
intimed, istemci makinalara saatinin kaç olduðunu söyleyen bir
sunucudur. Bilgisayar aðýndaki makinalarý eþ zamanlý tutmak
yararlýdýr.

%prep
%setup -q -c

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/etc/sysconfig/rc-inetd}

install in.timed $RPM_BUILD_ROOT%{_sbindir}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/timedt
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/timedu

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet sever" 1>&2
fi

%postun
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/in.timed
%attr(640,root,root) %config(noreplace) %verify(not mtime md5 size) /etc/sysconfig/rc-inetd/*
