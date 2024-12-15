%global             full_name zen-twilight
%global             application_name zen-twilight

Name:               zen-twilight-avx2
Version:            1.0.2.t.3
Release:            4%{?dist}
Summary:            Zen Browser (Twilight)

License:            MPLv2.0
URL:                https://github.com/zen-browser/desktop
Source0:            https://github.com/zen-browser/desktop/releases/download/twilight/zen.linux-specific.tar.bz2
Source1:            zen-common.spec
Source2:            %{full_name}.desktop.in
Source3:            policies.json
Source4:            zen-browser.sh.in

ExclusiveArch:      x86_64

Requires(post):     gtk-update-icon-cache
Conflicts:          zen-twilight

%description
Zen Browser

%include %{SOURCE1}
