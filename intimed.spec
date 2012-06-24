Summary:	A time server for synchronizing networked machines' clocks
Summary(de):	Zeit-Server zum Synchronisieren von Uhren
Summary(es):	Time server para sincronizaci�n de hora
Summary(pt):	Time server para sincroniza��o de hora
Summary(tr):	Saat e�zamanlamas� i�in time sunucusu
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
intimed es un servidor que ir� informar la hora a las m�quinas de la
red. Es �til para mantener las m�quinas de la red en sincron�a.

%description -l de
intimed ist ein Server, der an vernetzte Computer die Zeit ausgibt.
N�tzlich zur Synchronisation eines Netzwerks.

%description -l fr
intimed est un serveur qui indique aux machines connect�es l'heure
qu'il est. Utile pour synchroniser les r�seaux de machines sur l'heure
correcte.

%description -l pt
intimed � um servidor que ir� informar �s m�quinas da rede que horas
ele possui no momento. Ele � �til para manter as m�quinas da rede em
sincronia.

%description -l tr
intimed, istemci makinalara saatinin ka� oldu�unu s�yleyen bir
sunucudur. Bilgisayar a��ndaki makinalar� e� zamanl� tutmak
yararl�d�r.

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
