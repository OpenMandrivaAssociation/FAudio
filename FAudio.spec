# Wine uses FAudio
%ifarch %{x86_64}
%bcond_without compat32
%endif

%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d
%define lib32name %mklib32name %{name} %{major}
%define dev32name %mklib32name %{name} -d

Summary:	A free reimplementation of the DirectX XAudio APIs
Name:		FAudio
Version:	21.12
Release:	1
License:	MIT
Group:		System/Libraries
Url:		http://fna-xna.github.io/
Source0:	https://github.com/FNA-XNA/FAudio/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		faudio-19.03-compile.patch
BuildRequires:	cmake ninja
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(libunwind-llvm)
%if %{with compat32}
BuildRequires:	devel(libavcodec)
BuildRequires:	devel(libdbus-1)
BuildRequires:	devel(libSDL2-2.0)
BuildRequires:	devel(libunwind)
%endif

#----------------------------------------------------------------------------

%description
This is FAudio, an XAudio reimplementation that focuses solely on developing
fully accurate DirectX Audio runtime libraries for the FNA project, including
XAudio2, X3DAudio, XAPO, and XACT3.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n	%{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

FAudio is an XAudio reimplementation that focuses solely on developing
fully accurate DirectX Audio runtime libraries for the FNA project, including
XAudio2, X3DAudio, XAPO, and XACT3.

%files -n %{libname}
%{_libdir}/libFAudio.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

FAudio is an XAudio reimplementation that focuses solely on developing
fully accurate DirectX Audio runtime libraries for the FNA project, including
XAudio2, X3DAudio, XAPO, and XACT3.

%files -n %{devname}
%{_includedir}/*
%{_libdir}/libFAudio.so
%{_libdir}/cmake/FAudio
%{_libdir}/pkgconfig/*.pc

#----------------------------------------------------------------------------
%if %{with compat32}
%package -n %{lib32name}
Summary:	Main library for %{name} (32-bit)
Group:		System/Libraries

%description -n	%{lib32name}
This package contains the library needed to run programs dynamically
linked with %{name}.

FAudio is an XAudio reimplementation that focuses solely on developing
fully accurate DirectX Audio runtime libraries for the FNA project, including
XAudio2, X3DAudio, XAPO, and XACT3.

%files -n %{lib32name}
%{_prefix}/lib/libFAudio.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{dev32name}
Summary:	Headers for developing programs that will use %{name} (32-bit)
Group:		Development/C
Requires:	%{devname} = %{version}-%{release}
Requires:	%{lib32name} = %{version}-%{release}

%description -n	%{dev32name}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

FAudio is an XAudio reimplementation that focuses solely on developing
fully accurate DirectX Audio runtime libraries for the FNA project, including
XAudio2, X3DAudio, XAPO, and XACT3.

%files -n %{dev32name}
%{_prefix}/lib/libFAudio.so
%{_prefix}/lib/cmake/FAudio
%{_prefix}/lib/pkgconfig/*.pc
%endif

%prep
%autosetup -p1

%if %{with compat32}
%cmake32 \
	-DBUILD_TESTS:BOOL=ON \
	-DBUILD_UTILS:BOOL=ON \
	-DFFMPEG:BOOL=ON \
	-DXNASONG:BOOL=ON \
	-G Ninja
cd ..
%endif

%cmake \
	-DBUILD_TESTS:BOOL=ON \
	-DBUILD_UTILS:BOOL=ON \
	-DFFMPEG:BOOL=ON \
	-DXNASONG:BOOL=ON \
	-G Ninja

%build
%if %{with compat32}
%ninja_build -C build32
%endif
%ninja_build -C build

%install
%if %{with compat32}
%ninja_install -C build32
%endif
%ninja_install -C build
