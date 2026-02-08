Summary:		AdLib music player for the command line
Name:	adplay
Version:		1.9
Release:		1
License:		GPLv2+
Group:	Sound
Url:		https://adplug.sourceforge.net
Source0:	http://prdownloads.sourceforge.net/adplug/%{name}-%{version}.tar.bz2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires: chrpath
BuildRequires:	libtool-base
BuildRequires:	make
BuildRequires:	slibtool
BuildRequires: pkgconfig(adplug) >= 2.4
BuildRequires: pkgconfig(sdl)
BuildRequires: pkgconfig(alsa)
#BuildRequires: pkgconfig(esound)
BuildRequires: pkgconfig(ao)
BuildRequires: pkgconfig(zlib)

%description
AdPlay/UNIX is AdPlug's UNIX console-based frontend. AdPlug is a free,
universal OPL2 audio playback library. AdPlay/UNIX supports the full range
of AdPlug's file format playback features. Despite this, at the moment, only
emulated OPL2 output is supported by AdPlay/UNIX, but this on a wide range
of output devices.

%files
%doc README NEWS TODO AUTHORS ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1
touch *


%build
# FIXME: Build cannot find system libao nor system esdound libraries
#export CPPFLAGS="-I%%{_includedir}/ao"
%configure --disable-output-esound --disable-output-ao
%make_build


%install
%make_install

chrpath -d %{buildroot}%{_bindir}/%{name}
