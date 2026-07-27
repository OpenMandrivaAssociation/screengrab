# Module build system relies on this
%define _disable_ld_no_undefined 1

Summary:	Screen grabber
Name:		screengrab
Version:	3.2.0
Release:	2
Group:		Graphical desktop/Other
License:	GPLv2
URL:		https://screengrab.doomer.org/
Source0:	https://github.com/lxqt/screengrab/releases/download/%{version}/screengrab-%{version}.tar.xz
Source100:	%{name}.rpmlintrc
BuildSystem:	cmake
BuildOption:	-DBUILD_SHARED_LIBS:BOOL=OFF
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6WaylandClient)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(qt6xdg)
BuildRequires:	cmake(VulkanHeaders)
BuildRequires:	cmake(LayerShellQt)
BuildRequires:	cmake(lxqt2-build-tools)
BuildRequires:	pkgconfig(libpng)

%patchlist

%description
ScreenGrab -- program getting screenshots working in Linux and Windows.
The program uses Qt and is independent from any desktop environment.

%prep -a
find . -type f | xargs chmod 644
rm -rf src/3rdparty

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.metainfo.xml
%{_datadir}/%{name}
%{_iconsdir}/hicolor/scalable/apps/*.svg
