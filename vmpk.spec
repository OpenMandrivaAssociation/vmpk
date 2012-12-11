Name:           vmpk
Summary:        Virtual MIDI Piano Keyboard
Version:        0.5.0
Release:        1

Source:         http://sourceforge.net/projects/VMPK/files/%name-%version.tar.bz2
URL:            http://vmpk.sourceforge.net
License:        GPLv3+
Group:          Sound
BuildRequires:  cmake
BuildRequires:  pkgconfig(alsa)
BuildRequires:  qt4-devel
BuildRequires:  pkgconfig(jack)
BuildRequires:  desktop-file-utils

%description
VMPK is a MIDI event generator/receiver. It doesn't produce any sound by
itself, but can be used to drive a MIDI synthesizer (either hardware or
software, internal or external). You can use the computer's keyboard to
play MIDI notes, and also the mouse. You can use the Virtual MIDI Piano
Keyboard to display the played MIDI notes from another instrument or
MIDI file player.
Authors: Pedro Lopez-Cabanillas <plcl@users.sourceforge.net>

%prep
%setup -q

%build
CXXFLAGS="$RPM_OPT_FLAGS -g -fexceptions" cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix}
%make

%install
rm -rf %{buildroot}
%makeinstall_std
desktop-file-install --add-category="X-MandrivaLinux-Multimedia-Sound;" \
                     --remove-category="Education;" \
                     --remove-category="Midi;" \
                     --remove-category="Music;" \
                     --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc NEWS README ChangeLog AUTHORS TODO COPYING
%doc %{_mandir}/man1/*
%dir %{_datadir}/%name
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/16x16
%dir %{_datadir}/icons/hicolor/32x32
%dir %{_datadir}/icons/hicolor/48x48
%dir %{_datadir}/icons/hicolor/64x64
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/16x16/apps
%dir %{_datadir}/icons/hicolor/32x32/apps
%dir %{_datadir}/icons/hicolor/48x48/apps
%dir %{_datadir}/icons/hicolor/64x64/apps
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_bindir}/%name
%{_datadir}/%name/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/applications/%name.desktop



%changelog
* Sat Aug 04 2012 Frank Kober <emuse@mandriva.org> 0.5.0-1
+ Revision: 811740
- Qt BR reverted to qt4-devel
- new version 0.5.0

* Sun Jun 12 2011 Frank Kober <emuse@mandriva.org> 0.4.0-1
+ Revision: 684330
- new version 0.4.0
  o jackit-devel added (new jack MIDI support)
  o desktop-file-utils added

* Sat Oct 09 2010 Frank Kober <emuse@mandriva.org> 0.3.3-1mdv2011.0
+ Revision: 584335
- new version 0.3.3

* Mon Jul 19 2010 Frank Kober <emuse@mandriva.org> 0.3.2-1mdv2011.0
+ Revision: 554950
- new version 0.3.2

* Tue Mar 02 2010 Frank Kober <emuse@mandriva.org> 0.3.1-2mdv2010.1
+ Revision: 513317
- better destkop file install, spec cleanups

* Fri Dec 18 2009 Stéphane Téletchéa <steletch@mandriva.org> 0.3.1-1mdv2010.1
+ Revision: 479930
- Adjust group tag

  + Frank Kober <emuse@mandriva.org>
    - import vmpk


* Thu Dec 17 2009 Frank Kober <emuse@users.sourceforge.net> 0.3.1-1mdv2010.0
- import vmpk
