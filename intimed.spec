Summary:	A time server for synchronizing networked machines' clocks
Summary(de):	Zeit-Server zum Synchronisieren von Uhren
Summary(es):	Time server para sincronizaci�n de hora
Summary(pl):	Serwer czasu do synchronizacji zegar�w komputer�w w sieci
Summary(pt):	Time server para sincroniza��o de hora
Summary(ru):	������ ��� ������������� ��������� ����� ����� � ����
Summary(tr):	Saat e�zamanlamas� i�in time sunucusu
Summary(uk):	������ ��� ������Φ��æ� ��������� �������˦� ����� � ����֦
Name:		intimed
Version:	1.10
Release:	15
License:	Freeware
Group:		Daemons
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/network/sunacm/Other/intimed/%{name}-%{version}.tar.gz
# Source0-md5:	78610c4580f5839640eb22d34f0f3643
Source1:	timedt.inetd
Source2:	timedu.inetd
Prereq:		rc-inetd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	timed

%description
The intimed package contains a server (in.timed), which keeps
networked machines' clocks correctly synchronized to the server's
time.

%description -l de
intimed ist ein Server, der an vernetzte Computer die Zeit ausgibt.
N�tzlich zur Synchronisation eines Netzwerks.

%description -l es
intimed es un servidor que ir� informar la hora a las m�quinas de la
red. Es �til para mantener las m�quinas de la red en sincron�a.

%description -l fr
intimed est un serveur qui indique aux machines connect�es l'heure
qu'il est. Utile pour synchroniser les r�seaux de machines sur l'heure
correcte.

%description -l pl
Pakiet intimed zawiera serwer (in.timed), kt�ry utrzymuje zegary
maszyn w sieci zsynchronizowane z czasem serwera.

%description -l pt
intimed � um servidor que ir� informar �s m�quinas da rede que horas
ele possui no momento. Ele � �til para manter as m�quinas da rede em
sincronia.

%description -l ru
����� intimed �������� ������, ������� ������ ��� ����������� ����
����� � ����������� � �������� �������.

%description -l tr
intimed, istemci makinalara saatinin ka� oldu�unu s�yleyen bir
sunucudur. Bilgisayar a��ndaki makinalar� e� zamanl� tutmak
yararl�d�r.

%description -l uk
����� intimed ͦ����� ������, ���� ������� ��� Ц��������� ����֦
����� � ������Φ�ͦ � ����� �������.

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
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet server" 1>&2
fi

%postun
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/in.timed
%attr(640,root,root) %config(noreplace) %verify(not mtime md5 size) /etc/sysconfig/rc-inetd/*
