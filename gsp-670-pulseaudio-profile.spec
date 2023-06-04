Name:           gsp-670-pulse 
Version:        1.2
Release:        1
Epoch:		1
Summary:        PulseAudio profile for the Sennheiser GSP 670 wireless gaming headset 
License:        MIT
URL:            https://github.com/szszoke/sennheiser-gsp670-pulseaudio-profile
BuildArch: noarch
BuildRequires: git
Requires: kernel >= 5.15.0
Requires: pulseaudio|pipewire-pulseaudio

%description
Linux kernel 5.15 and newer should support the dongle with updated firmware. PipeWire 0.3.38 or newer should have the required audio profiles. PulseAudio 16.0 or newer should have the required audio profiles.

%prep
# Initialize the submodule
git clone https://github.com/szszoke/sennheiser-gsp670-pulseaudio-profile.git %{_buildrootdir}/sennheiser-gsp670-pulseaudio-profile


%install
cd %{_buildrootdir}/sennheiser-gsp670-pulseaudio-profile

mkdir -p %{buildroot}/%{_sysconfdir}/udev/rules.d/
mkdir -p %{buildroot}/%{_datarootdir}/alsa-card-profile/mixer/profile-sets/
mkdir -p %{buildroot}/%{_datarootdir}/alsa-card-profile/mixer/paths/

cp 91-pulseaudio-sennheiser-gsp670.rules %{buildroot}/%{_sysconfdir}/udev/rules.d/
cp sennheiser-gsp670-usb-audio.conf %{buildroot}/%{_datarootdir}/alsa-card-profile/mixer/profile-sets/
cp sennheiser-gsp670-output-main.conf %{buildroot}/%{_datarootdir}/alsa-card-profile/mixer/paths/
cp sennheiser-gsp670-output-comm.conf %{buildroot}/%{_datarootdir}/alsa-card-profile/mixer/paths/
cp sennheiser-gsp670-input-comm.conf %{buildroot}/%{_datarootdir}/alsa-card-profile/mixer/paths/


%files
%defattr(-,root,root,-)
%{_sysconfdir}/udev/rules.d/91-pulseaudio-sennheiser-gsp670.rules
%{_datarootdir}/alsa-card-profile/mixer/profile-sets/sennheiser-gsp670-usb-audio.conf
%{_datarootdir}/alsa-card-profile/mixer/paths/sennheiser-gsp670-output-main.conf
%{_datarootdir}/alsa-card-profile/mixer/paths/sennheiser-gsp670-output-comm.conf
%{_datarootdir}/alsa-card-profile/mixer/paths/sennheiser-gsp670-input-comm.conf

%changelog
* Mon Jun 05 2023 Tim Wendt <techtasie@gmail.com> - 1:1.2-1
- First working version still a bit scuffed but it is working
