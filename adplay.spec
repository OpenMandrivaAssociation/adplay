%define name adplay
%define version 1.7
%define release 5

Summary: 	AdLib music player for the command line
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	http://prdownloads.sourceforge.net/adplug/%{name}-%{version}.tar.bz2
License: 	GPLv2+
Group: 		Sound
URL: 		http://adplug.sourceforge.net

BuildRequires: pkgconfig(adplug) >= 2.2
BuildRequires: pkgconfig(sdl)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(esound)
BuildRequires: pkgconfig(ao)
BuildRequires: pkgconfig(zlib)
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
%makeinstall_std
chrpath -d %buildroot%_bindir/adplay

%files
%defattr(-,root,root)
%doc README NEWS TODO AUTHORS ChangeLog
%_bindir/adplay
%_mandir/man1/adplay.1*


