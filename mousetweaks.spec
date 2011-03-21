Summary:	Mouse accessibility enhancements for GNOME
Summary(pl.UTF-8):	Rozszerzenia dostępności myszy dla GNOME
Name:		mousetweaks
Version:	2.91.92
Release:	1
License:	GPL v3
Group:		X11/Applications/Accessibility
Source0:	http://ftp.gnome.org/pub/GNOME/sources/mousetweaks/2.91/%{name}-%{version}.tar.bz2
# Source0-md5:	012b29e9a88f6d4364c68ea022cdb238
URL:		http://live.gnome.org/Mousetweaks/Home
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gsettings-desktop-schemas-devel >= 2.91.90
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	xorg-lib-libXtst-devel
Requires(post,preun):	glib2 >= 1:2.26.0
Requires:	gsettings-desktop-schemas >= 2.91.90
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
	--disable-schemas-compile \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/mousetweaks
%{_datadir}/GConf/gsettings/mousetweaks.convert
%{_datadir}/glib-2.0/schemas/org.gnome.mousetweaks.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.mousetweaks.gschema.xml
%{_datadir}/mousetweaks
%{_mandir}/man1/mousetweaks.1*
