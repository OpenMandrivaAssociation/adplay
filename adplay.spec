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
URL: 		https://adplug.sourceforge.net

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


%changelog
* Tue Dec 06 2011 GÃ¶tz Waschk <waschk@mandriva.org> 1.7-4mdv2012.0
+ Revision: 738092
- yearly rebuild

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.7-3mdv2011.0
+ Revision: 609906
- rebuild

* Sun Mar 28 2010 Funda Wang <fwang@mandriva.org> 1.7-2mdv2010.1
+ Revision: 528358
- rebuild

* Wed Feb 10 2010 GÃ¶tz Waschk <waschk@mandriva.org> 1.7-1mdv2010.1
+ Revision: 503835
- fix license
- add zlib dep
- new version
- bump libadplug dep
- update build deps

* Fri May 22 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.6-5mdv2010.0
+ Revision: 378724
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.6-4mdv2009.0
+ Revision: 243043
- rebuild
- rebuild

* Thu Dec 20 2007 Olivier Blin <blino@mandriva.org> 1.6-2mdv2008.1
+ Revision: 135817
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jun 01 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1.6-2mdv2008.0
+ Revision: 34289
- Rebuild with libslang2.

* Tue Apr 17 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.6-1mdv2008.0
+ Revision: 14077
- new version
- fix buildrequires


* Fri Aug 25 2006 Götz Waschk <waschk@mandriva.org> 1.5-6mdv2007.0
- remove rpath

* Sat Aug 05 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.5-1mdv2007.0
- Rebuild

* Mon Jul 17 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.5-1mdv2007.0
- rebuild for new adplug

* Wed Jun 28 2006 Lenny Cartier <lenny@mandriva.com> 1.5-3mdv2007.0
- rebuild

* Fri May 05 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.5-2mdk
- rebuild for new adplug

* Tue Apr 25 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.5-1mdk
- New release 1.5

* Fri Jan 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.4-4mdk
- Rebuild
- use mkrel

* Mon Sep 19 2005 Götz Waschk <waschk@mandriva.org> 1.4-3mdk
- adapt for new libbinio header location

* Sun May 15 2005 Götz Waschk <waschk@mandriva.org> 1.4-2mdk
- rebuild for new adplug

* Sun Oct 03 2004 Götz Waschk <waschk@linux-mandrake.com> 1.4-1mdk
- fix buildrequires
- New release 1.4

* Sat Oct 02 2004 Götz Waschk <waschk@linux-mandrake.com> 1.3-4mdk
- rebuild

* Mon Jun 07 2004 Götz Waschk <waschk@linux-mandrake.com> 1.3-3mdk
- new g++
- drop prefix

