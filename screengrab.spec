%define debug_package %nil

Name:		screengrab
Version:	1.0
Release: 	4
License:	GPLv2
URL:		http://screengrab.doomer.org/
Source0:	http://screengrab.doomer.org/download//%{name}-%{version}.tar.gz
Summary:	Screen grabber
Group:		Graphical desktop/Other
Patch0:		screengrab-1.0-detect-lib64.patch
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	qt4-linguist
BuildRequires:	libqxt-devel
BuildRequires:	qtsingleapplication-devel

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
#cmake_qt4 -DBUILD_SHARED_LIBS:BOOL=OFF -DCMAKE_BUILD_TYPE=release -DSG_USE_SYSTEM_QXT=ON
mkdir build
pushd build
%{__cmake} ../  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
		-DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
		-DBUILD_SHARED_LIBS:BOOL=OFF \
		-DCMAKE_BUILD_TYPE=release \
		-DSG_USE_SYSTEM_QXT=ON
%make
popd

%install
%makeinstall_std -C build

%files
%doc docs/*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}
%{_libdir}/%{name}/*.so*
