#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : pkg-config
Version  : 1.9.5
Release  : 27
URL      : https://gitea.treehouse.systems/ariadne/pkgconf/archive/pkgconf-1.9.5.tar.gz
Source0  : https://gitea.treehouse.systems/ariadne/pkgconf/archive/pkgconf-1.9.5.tar.gz
Summary  : a library for accessing and manipulating development framework configuration
Group    : Development/Tools
License  : ISC
Requires: pkg-config-bin = %{version}-%{release}
Requires: pkg-config-lib = %{version}-%{release}
Requires: pkg-config-license = %{version}-%{release}
Requires: pkg-config-man = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(glib-2.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# pkgconf [![test](https://github.com/pkgconf/pkgconf/actions/workflows/test.yml/badge.svg)](https://github.com/pkgconf/pkgconf/actions/workflows/test.yml)

%package bin
Summary: bin components for the pkg-config package.
Group: Binaries
Requires: pkg-config-license = %{version}-%{release}

%description bin
bin components for the pkg-config package.


%package dev
Summary: dev components for the pkg-config package.
Group: Development
Requires: pkg-config-lib = %{version}-%{release}
Requires: pkg-config-bin = %{version}-%{release}
Provides: pkg-config-devel = %{version}-%{release}
Requires: pkg-config = %{version}-%{release}

%description dev
dev components for the pkg-config package.


%package doc
Summary: doc components for the pkg-config package.
Group: Documentation
Requires: pkg-config-man = %{version}-%{release}

%description doc
doc components for the pkg-config package.


%package lib
Summary: lib components for the pkg-config package.
Group: Libraries
Requires: pkg-config-license = %{version}-%{release}

%description lib
lib components for the pkg-config package.


%package license
Summary: license components for the pkg-config package.
Group: Default

%description license
license components for the pkg-config package.


%package man
Summary: man components for the pkg-config package.
Group: Default

%description man
man components for the pkg-config package.


%prep
%setup -q -n pkgconf
cd %{_builddir}/pkgconf

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1683654064
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs

%install
mkdir -p %{buildroot}/usr/share/package-licenses/pkg-config
cp %{_builddir}/pkgconf/COPYING %{buildroot}/usr/share/package-licenses/pkg-config/a8f3f302ab9f09a35914db53eb3fc9cb72810dac || :
DESTDIR=%{buildroot} ninja -C builddir install
## install_append content
ln -s pkgconf %{buildroot}/usr/bin/pkg-config
ln -s pkgconf %{buildroot}/usr/bin/x86_64-generic-linux-gnu-pkg-config
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pkg-config
/usr/bin/pkgconf
/usr/bin/x86_64-generic-linux-gnu-pkg-config

%files dev
%defattr(-,root,root,-)
/usr/include/pkgconf/libpkgconf/bsdstubs.h
/usr/include/pkgconf/libpkgconf/iter.h
/usr/include/pkgconf/libpkgconf/libpkgconf-api.h
/usr/include/pkgconf/libpkgconf/libpkgconf.h
/usr/include/pkgconf/libpkgconf/stdinc.h
/usr/lib64/libpkgconf.so
/usr/lib64/pkgconfig/libpkgconf.pc
/usr/share/aclocal/*.m4

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/pkgconf/AUTHORS
/usr/share/doc/pkgconf/README.md

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpkgconf.so.4
/usr/lib64/libpkgconf.so.4.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pkg-config/a8f3f302ab9f09a35914db53eb3fc9cb72810dac

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/pkgconf.1
/usr/share/man/man5/pc.5
/usr/share/man/man5/pkgconf-personality.5
/usr/share/man/man7/pkg.m4.7
