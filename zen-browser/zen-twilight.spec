%global             full_name zen-twilight
%global             application_name zen-twilight
%global             debug_package %{nil}

%global             appdir %{_libdir}/%{application_name}

Name:               zen-twilight
Version:            1.11.3t
Release:            1%{?dist}
Summary:            Zen Browser (Twilight)

License:            MPLv2.0
URL:                https://github.com/zen-browser/desktop
Source0:            https://github.com/zen-browser/desktop/releases/download/twilight/zen.linux-x86_64.tar.xz
Source1:            %{full_name}.desktop.in
Source2:            policies.json
Source3:            zen-browser.sh.in

ExclusiveArch:      x86_64

Requires(post):     gtk-update-icon-cache

%description
Zen Browser Twilight

%prep
%setup -q -n zen

%install
%__rm -rf %{buildroot}

%__install -d %{buildroot}%{appdir} %{buildroot}%{_bindir} %{buildroot}%{_datadir}/applications

%__cp -r * %{buildroot}%{appdir}

sed -e 's@__LIB_DIR__@%{_libdir}@g' %{SOURCE1} > %{full_name}.desktop
%__install -D -m 0644 %{full_name}.desktop -t %{buildroot}%{_datadir}/applications

%__install -D -m 0444 %{SOURCE2} -t %{buildroot}%{appdir}/distribution

sed -e 's@__LIB_DIR__@%{_libdir}@g' -e 's@__APP_NAME__@%{application_name}@g' -e 's@__FULL_NAME__@%{full_name}@g' %{SOURCE3} > %{full_name}.sh
%__install -D -m 0755 %{full_name}.sh -T %{buildroot}%{_bindir}/%{full_name}

for s in 16 32 48 64 128; do
    %__install -d %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps
    %__cp -p browser/chrome/icons/default/default${s}.png %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/%{full_name}.png
done

%post
gtk-update-icon-cache -q -f -t %{_datadir}/icons/hicolor

%files
%{_datadir}/applications/%{full_name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{full_name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{full_name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{full_name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{full_name}.png
%{_datadir}/icons/hicolor/16x16/apps/%{full_name}.png
%{_bindir}/%{full_name}
%{appdir}
