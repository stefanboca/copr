choose:
  @just --choose

dev-zen:
  #!/bin/bash
  rpmdev-setuptree
  cd zen-browser
  ln -sf $PWD/*.spec ~/rpmbuild/SPECS/
  ln -sf $PWD/policies.json $PWD/zen-browser.sh.in $PWD/zen-browser.desktop.in $PWD/zen-twilight.desktop.in ~/rpmbuild/SPECS/

