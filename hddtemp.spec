%define		_beta	beta8
Summary:	HDD temperature sensor
Summary(pl):	Czujka temperatury dysku twardego
Name:		hddtemp
Version:	0.3
Release:	0.%{_beta}.1
License:	GPL
Group:		Applications/System
Source0:	http://coredump.free.fr/linux/%{name}-%{version}-%{_beta}.tar.bz2
# Source0-md5:	3b823db40872efdc03a00b7170e28b23
Source1:	http://coredump.free.fr/linux/%{name}.db
# NoSource1-md5: 33b51858f61cd4ca1756d0396c9d6714
URL:		http://coredump.free.fr/linux/hddtemp.php
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hddtemp is tool that gives you the temperature of your IDE hard drive
by reading S.M.A.R.T. informations. Only modern hard drives have a
temperature sensor. hddtemp doesn't support reading S.M.A.R.T.
informations from SCSI devices.

%description -l pl
hddtemp jest narz�dziem sprawdzaj�cym temperatur� dysku twardego IDE
korzystaj�c z technologii S.M.A.R.T. Tylko nowoczesne dyski twarde
posiadaj� czujnik temperatury. hddtemp nie potrafi odczyta� informacji
S.M.A.R.T. z urz�dze� SCSI.

%prep
%setup -q -n %{name}-%{version}-%{_beta}

%build
%configure --with-db-path=/usr/share/misc/hddtemp.db
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},/usr/share/misc/}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/usr/share/misc/hddtemp.db

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post

echo "Recognised hdd's with S.M.A.R.T support & temperature sensors are:"
/usr/sbin/hddtemp  /dev/hd[a-z] 2>/dev/null

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man1/*
/usr/share/misc/*
