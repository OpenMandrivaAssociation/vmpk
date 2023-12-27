Summary:	Virtual MIDI Piano Keyboard
Name:		vmpk
Version:	0.8.10
Release:	1
License:	GPLv3+
Group:		Sound
URL:            https://vmpk.sourceforge.io
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Help)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(xcb)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(drumstick-rt)
BuildRequires:  qt6-qtbase-theme-gtk3

%description
VMPK is a MIDI event generator/receiver. It doesn't produce any sound by
itself, but can be used to drive a MIDI synthesizer (either hardware or
software, internal or external). You can use the computer's keyboard to
play MIDI notes, and also the mouse. You can use the Virtual MIDI Piano
Keyboard to display the played MIDI notes from another instrument or
MIDI file player.

%files
%doc NEWS ChangeLog AUTHORS TODO COPYING
%doc %{_mandir}/man1/*
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/metainfo/net.sourceforge.VMPK.metainfo.xml
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/applications/net.sourceforge.VMPK.desktop

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake -DUSE_QT=6
%make_build

%install
%make_install -C build
desktop-file-install --add-category="X-MandrivaLinux-Multimedia-Sound;" \
                     --remove-category="Education;" \
                     --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*
