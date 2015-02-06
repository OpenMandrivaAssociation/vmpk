Summary:	Virtual MIDI Piano Keyboard
Name:		vmpk
Version:	0.5.1
Release:	2
License:	GPLv3+
Group:		Sound
Url:		http://vmpk.sourceforge.net
Source0:	http://sourceforge.net/projects/VMPK/files/%name-%version.tar.bz2
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(jack)

%description
VMPK is a MIDI event generator/receiver. It doesn't produce any sound by
itself, but can be used to drive a MIDI synthesizer (either hardware or
software, internal or external). You can use the computer's keyboard to
play MIDI notes, and also the mouse. You can use the Virtual MIDI Piano
Keyboard to display the played MIDI notes from another instrument or
MIDI file player.

%files
%doc NEWS README ChangeLog AUTHORS TODO COPYING
%doc %{_mandir}/man1/*
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/applications/%{name}.desktop

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_qt4
%make

%install
%makeinstall_std -C build
desktop-file-install --add-category="X-MandrivaLinux-Multimedia-Sound;" \
                     --remove-category="Education;" \
                     --remove-category="Midi;" \
                     --remove-category="Music;" \
                     --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*


