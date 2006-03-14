Summary:	A time server for synchronizing networked machines' clocks
Summary(de):	Zeit-Server zum Synchronisieren von Uhren
Summary(es):	Time server para sincronizaciСn de hora
Summary(pl):	Serwer czasu do synchronizacji zegarСw komputerСw w sieci
Summary(pt):	Time server para sincronizaГЦo de hora
Summary(ru):	Сервер для синхронизации системных часов машин в сети
Summary(tr):	Saat eЧzamanlamasЩ iГin time sunucusu
Summary(uk):	Сервер для синхрон╕зац╕╖ системних годинник╕в машин в мереж╕
Name:		intimed
Version:	1.10
Release:	16
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

%description -l de
intimed ist ein Server, der an vernetzte Computer die Zeit ausgibt.
NЭtzlich zur Synchronisation eines Netzwerks.

%description -l es
intimed es un servidor que irА informar la hora a las mАquinas de la
red. Es Зtil para mantener las mАquinas de la red en sincronМa.

%description -l fr
intimed est un serveur qui indique aux machines connectИes l'heure
qu'il est. Utile pour synchroniser les rИseaux de machines sur l'heure
correcte.

%description -l pl
Pakiet intimed zawiera serwer (in.timed), ktСry utrzymuje zegary
maszyn w sieci zsynchronizowane z czasem serwera.

%description -l pt
intimed И um servidor que irА informar Юs mАquinas da rede que horas
ele possui no momento. Ele И Зtil para manter as mАquinas da rede em
sincronia.

%description -l ru
Пакет intimed содержит сервер, который служит для поддержания сети
машин в синхронизме с временем сервера.

%description -l tr
intimed, istemci makinalara saatinin kaГ olduПunu sЖyleyen bir
sunucudur. Bilgisayar aПЩndaki makinalarЩ eЧ zamanlЩ tutmak
yararlЩdЩr.

%description -l uk
Пакет intimed м╕стить сервер, який служить для п╕дтримання мереж╕
машин в синхрон╕зм╕ с часом сервера.

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
