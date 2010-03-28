%define name adplay
%define version 1.7
%define release %mkrel 2

Summary: AdLib music player for the command line
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/adplug/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: Sound
URL: http://adplug.sourceforge.net
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libadplug-devel >= 2.2
BuildRequires: libSDL-devel
BuildRequires: alsa-lib-devel
BuildRequires: esound-devel
BuildRequires: libao-devel
BuildRequires: zlib-devel
BuildRequires: chrpath

%description
AdPlay/UNIX is AdPlug's UNIX console-based frontend. AdPlug is a free,
universal OPL2 audio playback library. AdPlay/UNIX supports the full range
of AdPlug's file format playback features. Despite this, at the moment, only
emulated OPL2 output is supported by AdPlay/UNIX, but this on a wide range
of output devices.

%prep
%setup -q
touch *

%build
export CPPFLAGS="-I%_includedir/libbinio"
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
chrpath -d %buildroot%_bindir/adplay

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README NEWS TODO AUTHORS ChangeLog
%_bindir/adplay
%_mandir/man1/adplay.1*
