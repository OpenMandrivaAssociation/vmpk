Summary:	Virtual MIDI Piano Keyboard
Name:		vmpk
Version:	0.8.0
Release:	1
License:	GPLv3+
Group:		Sound
URL:            https://vmpk.sourceforge.io
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	qt5-devel
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(xcb)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(drumstick-rt)

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
%{_datadir}/metainfo/net.sourceforge.VMPK.appdata.xml
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/applications/net.sourceforge.VMPK.desktop

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_qt5
%make

%install
%make_install -C build
desktop-file-install --add-category="X-MandrivaLinux-Multimedia-Sound;" \
                     --remove-category="Education;" \
                     --remove-category="Midi;" \
                     --remove-category="Music;" \
                     --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*
