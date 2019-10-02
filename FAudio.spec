%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	A free reimplementation of the DirectX XAudio APIs
Name:		FAudio
Version:	19.10
Release:	1
License:	MIT
Group:		System/Libraries
Url:		http://fna-xna.github.io/
Source0:	https://github.com/FNA-XNA/FAudio/archive/%{version}.tar.gz
Patch0:		faudio-19.03-compile.patch
BuildRequires:	cmake ninja
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(libavutil)
BuildRequires:	pkgconfig(libswresample)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(vpx)
BuildRequires:	pkgconfig(libwebpmux)
BuildRequires:	pkgconfig(libwebp)
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	pkgconfig(celt)
BuildRequires:	pkgconfig(zvbi-0.2)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	gsm-devel
BuildRequires:	pkgconfig(libilbc)
BuildRequires:	pkgconfig(libopenjp2)
BuildRequires:	pkgconfig(speex)
BuildRequires:	pkgconfig(theoradec)
BuildRequires:	pkgconfig(theoraenc)
BuildRequires:	pkgconfig(twolame)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(vorbisenc)
BuildRequires:	pkgconfig(wavpack)
BuildRequires:	pkgconfig(xavs)
BuildRequires:	pkgconfig(libva)
BuildRequires:	pkgconfig(libva-drm)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(vdpau)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(soxr)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xau)
BuildRequires:	pkgconfig(xdmcp)
BuildRequires:	pkgconfig(dbus-1)

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

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake \
	-DBUILD_TESTS:BOOL=ON \
	-DBUILD_UTILS:BOOL=ON \
	-DFFMPEG:BOOL=ON \
	-DXNASONG:BOOL=ON \
	-G Ninja
%ninja_build

%install
%ninja_install -C build
