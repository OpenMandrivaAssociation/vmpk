%define name    vmpk
%define version 0.3.1
%define release %mkrel 2 

Name:           %{name} 
Summary:        Virtual MIDI Piano Keyboard
Version:        %{version} 
Release:        %{release}

Source:         http://sourceforge.net/projects/VMPK/files/%name-%version.tar.bz2
URL:            http://vmpk.sourceforge.net
License:        GPLv3+
Group:          Sound
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot 
BuildRequires:  cmake alsa-lib-devel qt4-devel

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
%doc %{_mandir}/*
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
%dir %{_datadir}/locale
%{_bindir}/%name
%{_datadir}/%name/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/applications/%name.desktop
%{_datadir}/locale/*

%changelog
