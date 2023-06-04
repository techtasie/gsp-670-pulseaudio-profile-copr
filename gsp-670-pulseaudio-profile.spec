%undefine _arch
Name:           gsp-670-pulse 
Version:        1.2
Release:        1
Epoch:          1
Summary:        PulseAudio profile for the Sennheiser GSP 670 wireless gaming headset 
License:        MIT
URL:            https://github.com/szszoke/sennheiser-gsp670-pulseaudio-profile
BuildArch: noarch

%description
Linux kernel 5.15 and newer should support the dongle with updated firmware. PipeWire 0.3.38 or newer should have the required audio profiles. PulseAudio 16.0 or newer should have the required audio profiles.

%prep
# Initialize the submodule
git submodule init

%install

cp 91-pulseaudio-sennheiser-gsp670.rules %{buildroot}}/etc/udev/rules.d/
cp sennheiser-gsp670-usb-audio.conf %{buildroot}}/usr/share/alsa-card-profile/mixer/profile-sets/
cp sennheiser-gsp670-output-main.conf %{buildroot}}/usr/share/alsa-card-profile/mixer/paths/
cp sennheiser-gsp670-output-comm.conf %{buildroot}}/usr/share/alsa-card-profile/mixer/paths/
cp sennheiser-gsp670-input-comm.conf %{buildroot}}/usr/share/alsa-card-profile/mixer/paths/

%files
%defattr(-,root,root,-)
/etc/udev/rules.d/91-pulseaudio-sennheiser-gsp670.rules
/usr/share/alsa-card-profile/mixer/profile-sets/sennheiser-gsp670-usb-audio.conf
/usr/share/alsa-card-profile/mixer/paths/sennheiser-gsp670-output-main.conf
/usr/share/alsa-card-profile/mixer/paths/sennheiser-gsp670-output-comm.conf
/usr/share/alsa-card-profile/mixer/paths/sennheiser-gsp670-input-comm.conf

%requires
BuildRequires: git
Requires: kernel >= 5.15.0
Requires: pulseaudio | pipewire-pulseaudio
