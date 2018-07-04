%define debug_package %nil
# Module build system relies on this
%define _disable_ld_no_undefined 1

Name:		screengrab
Version:	1.98
Release: 	1
License:	GPLv2
URL:		http://screengrab.doomer.org/
Source0:	https://downloads.lxqt.org/downloads/screengrab/%{version}/screengrab-%{version}.tar.xz
Source100:	%{name}.rpmlintrc
Summary:	Screen grabber
Group:		Graphical desktop/Other
BuildRequires:	cmake ninja
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
%setup -q
find . -type f | xargs chmod 644
%apply_patches
%{__rm} -rf src/3rdparty

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
%{_datadir}/%{name}
%{_libdir}/%{name}/*.so*
%{_datadir}/icons/hicolor/32x32/apps/screengrab.png
