# Module build system relies on this
%define _disable_ld_no_undefined 1

Summary:	Screen grabber
Name:		screengrab
Version:	2.4.0
Release:	1
Group:		Graphical desktop/Other
License:	GPLv2
URL:		http://screengrab.doomer.org/
Source0:	https://github.com/lxqt/screengrab/releases/download/%{version}/screengrab-%{version}.tar.xz
Source100:	%{name}.rpmlintrc
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(qt5xdg)

%description
ScreenGrab -- program getting screenshots working in Linux and Windows. 
The program uses Qt and is independent from any desktop environment.
Main features:
    * grab screenshot of desktop
    * working on Window and Linux operating systems
    * save screenshots in PNG and JPEG format
    * grab screenshot with delay (1 - 90 sec)
    * hide its window
    * minimize to system tray and work from at (tray menu) 

%prep
%autosetup -p1
find . -type f | xargs chmod 644
%autopatch -p1
rm -rf src/3rdparty

%build
%cmake_qt5	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
		-DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
		-DBUILD_SHARED_LIBS:BOOL=OFF \
		-DCMAKE_BUILD_TYPE=release \
		-G Ninja
%ninja_build

%install
%ninja_install -C build

%files
%doc docs/*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.metainfo.xml
%{_datadir}/%{name}
%{_libdir}/%{name}/*.so*
%{_datadir}/icons/hicolor/scalable/apps/*.svg
