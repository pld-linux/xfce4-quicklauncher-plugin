Summary:	Multiline launcher plugin for Xfce panel
Summary(pl):	Wieloliniowa wtyczka do uruchamiania dla panelu Xfce
Name:		xfce4-quicklauncher-plugin
Version:	0.81
Release:	0.1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.gz
# Source0-md5:	98231ea7afe226ca7cbdc5c51ea3d16e
URL:		http://xfce-goodies.berlios.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	libxfce4util-devel >= 3.99
BuildRequires:	libxfcegui4-devel >= 3.99
BuildRequires:	pkgconfig
BuildRequires:	xfce4-panel-devel >= 4.1.9.0
Requires:	xfce4-panel >= 4.1.9.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin allows you to have lots of launchers in the panel,
displaying them on several lines.

%description -l pl
Ta wtyczka umo¿liwia posiadanie wielu narzêdzi do uruchamiania w
panelu, wy¶wietlaj±c je w kilku liniach.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
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
%doc ChangeLog TODO
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
