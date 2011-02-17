Summary:	Multiline launcher plugin for Xfce panel
Summary(pl.UTF-8):	Wieloliniowa wtyczka do uruchamiania dla panelu Xfce
Name:		xfce4-quicklauncher-plugin
Version:	1.9.4
Release:	4
License:	GPL v2+
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-quicklauncher-plugin/%{name}-%{version}.tar.bz2
# Source0-md5:	299e17f196ecfa5fb018cf65abb19b56
Patch0:		%{name}-missing-english-translation.patch
Patch1:		%{name}-multiscreen.patch
Patch2:		%{name}-parameters-launcher.patch
Patch3:		%{name}-save-settings.patch
Patch4:		%{name}-startup.patch
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-quicklauncher-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
Requires:	xfce4-panel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin allows you to have lots of launchers in the panel,
displaying them on several lines.

%description -l pl.UTF-8
Ta wtyczka umożliwia posiadanie wielu narzędzi do uruchamiania w
panelu, wyświetlając je w kilku liniach.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
%{_datadir}/xfce4/panel-plugins/*.desktop
