Name:           gsp-670-pulse 
BuildRoot: 	/tmp
Version:        1.2
Release:        1
Epoch:		1
Summary:        PulseAudio profile for the Sennheiser GSP 670 wireless gaming headset 
License:        MIT
%define NVdir   %{name}-%{version}
URL:            https://github.com/szszoke/sennheiser-gsp670-pulseaudio-profile
Source0:	sennheiser-gsp670-pulseaudio-profile.tar.gz
BuildRequires: git
BuildArch: noarch
Requires: kernel >= 5.15.0

%description
Linux kernel 5.15 and newer should support the dongle with updated firmware. PipeWire 0.3.38 or newer should have the required audio profiles. PulseAudio 16.0 or newer should have the required audio profiles.

%prep
%setup -q -c -n sennheiser-gsp670-pulseaudio-profile

%install
mkdir -p $RPM_BUILD_ROOT/etc/udev/rules.d/
mkdir -p $RPM_BUILD_ROOT/usr/share/alsa-card-profile/mixer/profile-sets/
mkdir -p $RPM_BUILD_ROOT/usr/share/alsa-card-profile/mixer/paths/
cd sennheiser-gsp670-pulseaudio-profile
./install $RPM_BUILD_ROOT/

%files
/etc/udev/rules.d/91-pulseaudio-sennheiser-gsp670.rules
/usr/share/alsa-card-profile/mixer/profile-sets/sennheiser-gsp670-usb-audio.conf
/usr/share/alsa-card-profile/mixer/paths/sennheiser-gsp670-output-main.conf
/usr/share/alsa-card-profile/mixer/paths/sennheiser-gsp670-output-comm.conf
/usr/share/alsa-card-profile/mixer/paths/sennheiser-gsp670-input-comm.conf


%changelog
* Mon Jun 05 2023 Tim Wendt <techtasie@gmail.com> - 1:1.2-1
- First working version still a bit scuffed but it is working
