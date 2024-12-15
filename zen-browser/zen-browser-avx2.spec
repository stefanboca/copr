%global             full_name zen-browser
%global             application_name zen

Name:               zen-browser-avx2
Version:            1.0.2.b.2
Release:            4%{?dist}
Summary:            Zen Browser

License:            MPLv2.0
URL:                https://github.com/zen-browser/desktop
Source0:            https://github.com/zen-browser/desktop/releases/download/1.0.2-b.2/zen.linux-specific.tar.bz2
Source1:            %{full_name}.desktop.in
Source2:            policies.json
Source3:            zen-browser.sh.in

ExclusiveArch:      x86_64

Requires(post):     gtk-update-icon-cache
Conflicts:          zen-browser

%description
Zen Browser

%include zen-common.spec
