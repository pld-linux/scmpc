#
Summary:	Client for MPD which submits your tracks to last.fm.
Summary(pl.UTF-8):	Klient MPD wysyłający słuchane utwory do last.fm.
Name:		scmpc
Version:	0.2.2
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://download.berlios.de/scmpc/%{name}-%{version}.tar.bz2
# Source0-md5:	f42482e4dbf398df92a36d5610b403e5
#Patch0:		%{name}-DESTDIR.patch
URL:		http://scmpc.berlios.de/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Client for MPD which submits your tracks to last.fm.

%description -l pl.UTF-8
Klient MPD wysyłający słuchane utwory do last.fm.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/*/*
