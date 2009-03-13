Summary:	Mouse accessibility enhancements for GNOME
Summary(pl.UTF-8):	Rozszerzenia dostępności myszy dla GNOME
Name:		mousetweaks
Version:	2.25.91
Release:	1
License:	GPL v3
Group:		X11/Applications/Accessibility
Source0:	http://ftp.gnome.org/pub/GNOME/sources/mousetweaks/2.25/%{name}-%{version}.tar.bz2
# Source0-md5:	db6e6d50d18006f1fddebcc1609e5981
URL:		http://live.gnome.org/Mousetweaks/Home
BuildRequires:	GConf2-devel >= 2.25.0
BuildRequires:	at-spi-devel >= 1.25.0
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gnome-panel-devel >= 2.25.90
BuildRequires:	gtk+2-devel >= 2:2.15.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.198
Requires(post,preun):	GConf2
Requires:	libgail-gnome
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The mousetweaks package provides the functions offered by the
Accessibility tab of the Mouse control panel of the GNOME Control
Center. It also contains two panel applets related to the mouse
accessibility.

%description -l pl.UTF-8
Pakiet mousetweaks udostępnia funkcje oferowane przez zakładkę
Dostępność w panelu sterowania myszy w Centrum Sterowania GNOME.
Zawiera także dwa aplety panelu związane z dostępnością myszy.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install mousetweaks.schemas
%gconf_schema_install pointer-capture-applet.schemas

%preun
%gconf_schema_uninstall mousetweaks.schemas
%gconf_schema_uninstall pointer-capture-applet.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/dwell-click-applet
%attr(755,root,root) %{_bindir}/mousetweaks
%attr(755,root,root) %{_bindir}/pointer-capture-applet
%{_sysconfdir}/gconf/schemas/mousetweaks.schemas
%{_sysconfdir}/gconf/schemas/pointer-capture-applet.schemas
%{_libdir}/bonobo/servers/DwellClick_Factory.server
%{_libdir}/bonobo/servers/PointerCapture_Factory.server
%{_datadir}/mousetweaks
%{_mandir}/man1/dwell-click-applet.1*
%{_mandir}/man1/mousetweaks.1*
%{_mandir}/man1/pointer-capture-applet.1*
