#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	5.27.7
%define		qtver		5.15.2
%define		kpname		aura-browser
Summary:	Browser for a fully immersed Big Screen experience
Name:		kp5-%{kpname}
Version:	5.27.7
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	2b1b01328d062d6d9c3d92daaa26d13c
URL:		http://www.kde.org/
BuildRequires:	Qt5WebEngine-devel
BuildRequires:	cmake >= 3.16.0
BuildRequires:	kf5-extra-cmake-modules
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Browser for a fully immersed Big Screen experience allowing you to
navigate the world wide web using just your remote control.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	 -G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir}
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aura-browser
%{_iconsdir}/hicolor/128x128/apps/aura-browser.png
%{_iconsdir}/hicolor/256x256/apps/aura-browser.png
%{_datadir}/metainfo/org.kde.invent.aura_browser.metainfo.xml
%{_desktopdir}/org.kde.aura-browser.desktop
