#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kspaceduel
Version  : 20.12.1
Release  : 26
URL      : https://download.kde.org/stable/release-service/20.12.1/src/kspaceduel-20.12.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.12.1/src/kspaceduel-20.12.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.12.1/src/kspaceduel-20.12.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: kspaceduel-bin = %{version}-%{release}
Requires: kspaceduel-data = %{version}-%{release}
Requires: kspaceduel-license = %{version}-%{release}
Requires: kspaceduel-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libkdegames-dev
BuildRequires : qtbase-dev mesa-dev

%description
KSpaceduel
----------
KSpaceduel is an arcade two-player space game for KDE.
Two ships fly around the sun and have to shoot the other ship.

%package bin
Summary: bin components for the kspaceduel package.
Group: Binaries
Requires: kspaceduel-data = %{version}-%{release}
Requires: kspaceduel-license = %{version}-%{release}

%description bin
bin components for the kspaceduel package.


%package data
Summary: data components for the kspaceduel package.
Group: Data

%description data
data components for the kspaceduel package.


%package doc
Summary: doc components for the kspaceduel package.
Group: Documentation

%description doc
doc components for the kspaceduel package.


%package license
Summary: license components for the kspaceduel package.
Group: Default

%description license
license components for the kspaceduel package.


%package locales
Summary: locales components for the kspaceduel package.
Group: Default

%description locales
locales components for the kspaceduel package.


%prep
%setup -q -n kspaceduel-20.12.1
cd %{_builddir}/kspaceduel-20.12.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610038692
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1610038692
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kspaceduel
cp %{_builddir}/kspaceduel-20.12.1/COPYING %{buildroot}/usr/share/package-licenses/kspaceduel/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/kspaceduel-20.12.1/COPYING.DOC %{buildroot}/usr/share/package-licenses/kspaceduel/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
pushd clr-build
%make_install
popd
%find_lang kspaceduel

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kspaceduel

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kspaceduel.desktop
/usr/share/config.kcfg/kspaceduel.kcfg
/usr/share/icons/hicolor/128x128/apps/kspaceduel.png
/usr/share/icons/hicolor/16x16/apps/kspaceduel.png
/usr/share/icons/hicolor/22x22/apps/kspaceduel.png
/usr/share/icons/hicolor/32x32/apps/kspaceduel.png
/usr/share/icons/hicolor/48x48/apps/kspaceduel.png
/usr/share/icons/hicolor/64x64/apps/kspaceduel.png
/usr/share/kspaceduel/icons/hicolor/16x16/actions/spnewgame.png
/usr/share/kspaceduel/icons/hicolor/16x16/actions/spnewround.png
/usr/share/kspaceduel/icons/hicolor/16x16/actions/sppausegame.png
/usr/share/kspaceduel/icons/hicolor/22x22/actions/spnewgame.png
/usr/share/kspaceduel/icons/hicolor/22x22/actions/spnewround.png
/usr/share/kspaceduel/icons/hicolor/22x22/actions/sppausegame.png
/usr/share/kspaceduel/icons/hicolor/32x32/actions/spnewgame.png
/usr/share/kspaceduel/icons/hicolor/32x32/actions/spnewround.png
/usr/share/kspaceduel/icons/hicolor/32x32/actions/sppausegame.png
/usr/share/kspaceduel/sprites/backgr.png
/usr/share/kspaceduel/sprites/default_theme.svgz
/usr/share/kspaceduel/sprites/playerinfo/energy.png
/usr/share/kspaceduel/sprites/playerinfo/mine.png
/usr/share/kspaceduel/sprites/playerinfo/ship10.png
/usr/share/kspaceduel/sprites/playerinfo/ship11.png
/usr/share/kspaceduel/sprites/playerinfo/ship12.png
/usr/share/kspaceduel/sprites/playerinfo/ship13.png
/usr/share/kspaceduel/sprites/playerinfo/ship20.png
/usr/share/kspaceduel/sprites/playerinfo/ship21.png
/usr/share/kspaceduel/sprites/playerinfo/ship22.png
/usr/share/kspaceduel/sprites/playerinfo/ship23.png
/usr/share/kspaceduel/sprites/playerinfo/win.png
/usr/share/kxmlgui5/kspaceduel/kspaceduelui.rc
/usr/share/metainfo/org.kde.kspaceduel.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/de/kspaceduel/index.cache.bz2
/usr/share/doc/HTML/de/kspaceduel/index.docbook
/usr/share/doc/HTML/de/kspaceduel/kspaceduel3.png
/usr/share/doc/HTML/en/kspaceduel/index.cache.bz2
/usr/share/doc/HTML/en/kspaceduel/index.docbook
/usr/share/doc/HTML/en/kspaceduel/kspaceduel3.png
/usr/share/doc/HTML/es/kspaceduel/index.cache.bz2
/usr/share/doc/HTML/es/kspaceduel/index.docbook
/usr/share/doc/HTML/et/kspaceduel/index.cache.bz2
/usr/share/doc/HTML/et/kspaceduel/index.docbook
/usr/share/doc/HTML/fr/kspaceduel/index.cache.bz2
/usr/share/doc/HTML/fr/kspaceduel/index.docbook
/usr/share/doc/HTML/fr/kspaceduel/kspaceduel1.png
/usr/share/doc/HTML/fr/kspaceduel/kspaceduel2.png
/usr/share/doc/HTML/fr/kspaceduel/kspaceduel3.png
/usr/share/doc/HTML/it/kspaceduel/index.cache.bz2
/usr/share/doc/HTML/it/kspaceduel/index.docbook
/usr/share/doc/HTML/nl/kspaceduel/index.cache.bz2
/usr/share/doc/HTML/nl/kspaceduel/index.docbook
/usr/share/doc/HTML/nl/kspaceduel/kspaceduel3.png
/usr/share/doc/HTML/pt/kspaceduel/index.cache.bz2
/usr/share/doc/HTML/pt/kspaceduel/index.docbook
/usr/share/doc/HTML/pt_BR/kspaceduel/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kspaceduel/index.docbook
/usr/share/doc/HTML/pt_BR/kspaceduel/kspaceduel3.png
/usr/share/doc/HTML/ru/kspaceduel/index.cache.bz2
/usr/share/doc/HTML/ru/kspaceduel/index.docbook
/usr/share/doc/HTML/sv/kspaceduel/index.cache.bz2
/usr/share/doc/HTML/sv/kspaceduel/index.docbook
/usr/share/doc/HTML/sv/kspaceduel/kspaceduel3.png
/usr/share/doc/HTML/uk/kspaceduel/index.cache.bz2
/usr/share/doc/HTML/uk/kspaceduel/index.docbook
/usr/share/doc/HTML/uk/kspaceduel/kspaceduel3.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kspaceduel/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/kspaceduel/bd75d59f9d7d9731bfabdc48ecd19e704d218e38

%files locales -f kspaceduel.lang
%defattr(-,root,root,-)

