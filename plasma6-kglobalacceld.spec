%define libname %mklibname KGlobalAccelD
%define devname %mklibname KGlobalAccelD -d
%define git 20230518

Name: kf6-kglobalacceld
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/plasma/kglobalacceld/-/archive/master/kglobalacceld-master.tar.bz2#/kglobalacceld-%{git}.tar.bz2
Summary: Daemon providing Global Keyboard Shortcut (Accelerator) functionality
URL: https://invent.kde.org/plasma/kglobalacceld
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: pkgconfig(x11-xcb)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-xkb)
Requires: %{libname} = %{EVRD}

%description
Daemon providing Global Keyboard Shortcut (Accelerator) functionality

%package -n %{libname}
Summary: Daemon providing Global Keyboard Shortcut (Accelerator) functionality
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Daemon providing Global Keyboard Shortcut (Accelerator) functionality

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Daemon providing Global Keyboard Shortcut (Accelerator) functionality

%prep
%autosetup -p1 -n kglobalacceld-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_sysconfdir}/xdg/autostart/kglobalacceld.desktop
%{_prefix}/lib/systemd/user/plasma-kglobalaccel.service
%{_libdir}/libexec/kglobalacceld
%{_qtdir}/plugins/org.kde.kglobalacceld.platforms

%files -n %{devname}
%{_includedir}/KGlobalAccelD
%{_libdir}/cmake/KGlobalAccelD

%files -n %{libname}
%{_libdir}/libKGlobalAccelD.so*
