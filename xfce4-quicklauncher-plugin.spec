Summary:	Multiline launcher plugin for Xfce panel
Name:		xfce4-quicklauncher-plugin
Version:	0.5
Release:	0.1
License:	BSD-like (see COPYING)
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.gz
# Source0-md5:	7b02eb6e8ae2b685be67637c0034b158
URL:		http://xfce-goodies.berlios.de/
BuildRequires:	libxfce4util-devel >= 3.99
BuildRequires:	libxfcegui4-devel >= 3.99
BuildRequires:	pkgconfig
BuildRequires:	xfce4-panel-devel >= 3.99
Requires:	xfce4-panel >= 3.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin allows you to have lots of launchers in the panel,
displaying them on several lines.

%prep
%setup -q -n %{name}

%build
#cp -f /usr/share/automake/config.sub .
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc AUTHORS ChangeLog COPYING
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
