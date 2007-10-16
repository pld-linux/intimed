Summary:	A time server for synchronizing networked machines' clocks
Summary(de.UTF-8):	Zeit-Server zum Synchronisieren von Uhren
Summary(es.UTF-8):	Time server para sincronización de hora
Summary(pl.UTF-8):	Serwer czasu do synchronizacji zegarów komputerów w sieci
Summary(pt.UTF-8):	Time server para sincronização de hora
Summary(ru.UTF-8):	Сервер для синхронизации системных часов машин в сети
Summary(tr.UTF-8):	Saat eşzamanlaması için time sunucusu
Summary(uk.UTF-8):	Сервер для синхронізації системних годинників машин в мережі
Name:		intimed
Version:	1.10
Release:	17
License:	Freeware
Group:		Daemons
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/network/sunacm/Other/intimed/%{name}-%{version}.tar.gz
# Source0-md5:	78610c4580f5839640eb22d34f0f3643
BuildRequires:	rpmbuild(macros) >= 1.268
Source1:	timedt.inetd
Source2:	timedu.inetd
Requires:	rc-inetd
Obsoletes:	timed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The intimed package contains a server (in.timed), which keeps
networked machines' clocks correctly synchronized to the server's
time.

%description -l de.UTF-8
intimed ist ein Server, der an vernetzte Computer die Zeit ausgibt.
Nützlich zur Synchronisation eines Netzwerks.

%description -l es.UTF-8
intimed es un servidor que irá informar la hora a las máquinas de la
red. Es útil para mantener las máquinas de la red en sincronía.

%description -l fr.UTF-8
intimed est un serveur qui indique aux machines connectées l'heure
qu'il est. Utile pour synchroniser les réseaux de machines sur l'heure
correcte.

%description -l pl.UTF-8
Pakiet intimed zawiera serwer (in.timed), który utrzymuje zegary
maszyn w sieci zsynchronizowane z czasem serwera.

%description -l pt.UTF-8
intimed é um servidor que irá informar às máquinas da rede que horas
ele possui no momento. Ele é útil para manter as máquinas da rede em
sincronia.

%description -l ru.UTF-8
Пакет intimed содержит сервер, который служит для поддержания сети
машин в синхронизме с временем сервера.

%description -l tr.UTF-8
intimed, istemci makinalara saatinin kaç olduğunu söyleyen bir
sunucudur. Bilgisayar ağındaki makinaları eş zamanlı tutmak
yararlıdır.

%description -l uk.UTF-8
Пакет intimed містить сервер, який служить для підтримання мережі
машин в синхронізмі с часом сервера.

%prep
%setup -q -c

%build
%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="-L%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/etc/sysconfig/rc-inetd}

install in.timed $RPM_BUILD_ROOT%{_sbindir}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/timedt
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/timedu

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q rc-inetd reload

%postun
if [ "$1" = 0 ]; then
	%service -q rc-inetd reload
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/in.timed
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/*
