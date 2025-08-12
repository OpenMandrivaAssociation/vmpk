Summary:	Virtual MIDI Piano Keyboard
Name:	vmpk
Version:	0.9.1
Release:	1
License:	GPLv3+
Group:	Sound
Url:	https://vmpk.sourceforge.io
Source0:	https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:	cmake >= 3.16
BuildRequires:	desktop-file-utils
BuildRequires:	gzip-utils
BuildRequires:	qt6-qtbase-theme-gtk3
BuildRequires:xsltproc
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Help)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(drumstick-rt) >= 2.10.0
BuildRequires:	pkgconfig(drumstick-widgets)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xkbcommon-x11)
BuildRequires:	pkgconfig(vulkan)

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
%{_datadir}/applications/net.sourceforge.VMPK.desktop
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/metainfo/net.sourceforge.VMPK.metainfo.xml

#----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
%cmake
%make_build


%install
%make_install -C build

# Fix desktop file
desktop-file-edit --add-category="X-OpenMandrivaLinux-Multimedia-Sound;" \
							--remove-category="Education;" \
							%{buildroot}%{_datadir}/applications/net.sourceforge.VMPK.desktop

# Fix gzipped-svg-icon
(
cd %{buildroot}%{_iconsdir}/hicolor/scalable/apps/
zcat %{name}.svgz > %{name}.svg && rm -f %{name}.svgz
)

