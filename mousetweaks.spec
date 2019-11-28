# TODO:
# * Fix depracated schema paths, throws warnings on RPM install
#
Summary:	Mouse accessibility enhancements for GNOME
Summary(pl.UTF-8):	Rozszerzenia dostępności myszy dla GNOME
Name:		mousetweaks
Version:	3.32.0
Release:	1
License:	GPL v3
Group:		X11/Applications/Accessibility
Source0:	http://ftp.gnome.org/pub/GNOME/sources/mousetweaks/3.32/%{name}-%{version}.tar.xz
# Source0-md5:	aa671b0c7278a92c12f061d129af1454
URL:		https://wiki.gnome.org/Projects/Mousetweaks
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gsettings-desktop-schemas-devel >= 3.2.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xz
Requires(post,preun):	glib2 >= 1:2.26.0
Requires:	glib2 >= 1:2.26.0
Requires:	gsettings-desktop-schemas >= 3.2.0
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
%{__aclocal} -I m4
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

%find_lang %{name} --with-gnome

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
