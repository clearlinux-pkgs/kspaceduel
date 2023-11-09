#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v2
# autospec commit: 250a666
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kspaceduel
Version  : 23.08.3
Release  : 59
URL      : https://download.kde.org/stable/release-service/23.08.3/src/kspaceduel-23.08.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.08.3/src/kspaceduel-23.08.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.08.3/src/kspaceduel-23.08.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0
Requires: kspaceduel-bin = %{version}-%{release}
Requires: kspaceduel-data = %{version}-%{release}
Requires: kspaceduel-license = %{version}-%{release}
Requires: kspaceduel-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libkdegames-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n kspaceduel-23.08.3
cd %{_builddir}/kspaceduel-23.08.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1699554955
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1699554955
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kspaceduel
cp %{_builddir}/kspaceduel-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kspaceduel/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kspaceduel-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kspaceduel/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kspaceduel-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kspaceduel/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kspaceduel-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kspaceduel/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/kspaceduel-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kspaceduel/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang kspaceduel
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kspaceduel
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
/usr/share/metainfo/org.kde.kspaceduel.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kspaceduel/index.cache.bz2
/usr/share/doc/HTML/ca/kspaceduel/index.docbook
/usr/share/doc/HTML/ca/kspaceduel/kspaceduel3.png
/usr/share/doc/HTML/de/kspaceduel/index.cache.bz2
/usr/share/doc/HTML/de/kspaceduel/index.docbook
/usr/share/doc/HTML/de/kspaceduel/kspaceduel3.png
/usr/share/doc/HTML/en/kspaceduel/bullet.png
/usr/share/doc/HTML/en/kspaceduel/energy.png
/usr/share/doc/HTML/en/kspaceduel/index.cache.bz2
/usr/share/doc/HTML/en/kspaceduel/index.docbook
/usr/share/doc/HTML/en/kspaceduel/kspaceduel3.png
/usr/share/doc/HTML/en/kspaceduel/mine.png
/usr/share/doc/HTML/en/kspaceduel/shield.png
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
/usr/share/package-licenses/kspaceduel/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kspaceduel/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kspaceduel/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/kspaceduel/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kspaceduel/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files locales -f kspaceduel.lang
%defattr(-,root,root,-)

