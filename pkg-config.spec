#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x023A4420C7EC6914 (dbn.lists@gmail.com)
#
Name     : pkg-config
Version  : 0.29.2
Release  : 22
URL      : http://pkgconfig.freedesktop.org/releases/pkg-config-0.29.2.tar.gz
Source0  : http://pkgconfig.freedesktop.org/releases/pkg-config-0.29.2.tar.gz
Source1 : http://pkgconfig.freedesktop.org/releases/pkg-config-0.29.2.tar.gz.asc
Summary  : Dummy pkgconfig test package for testing pkgconfig
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: pkg-config-bin = %{version}-%{release}
Requires: pkg-config-license = %{version}-%{release}
Requires: pkg-config-man = %{version}-%{release}
BuildRequires : gettext
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(glib-2.0)
Patch1: 0001-Disable-list-all-test.patch

%description
pkg-config is a script to make putting together all the build
flags when compiling/linking a lot easier.

%package bin
Summary: bin components for the pkg-config package.
Group: Binaries
Requires: pkg-config-license = %{version}-%{release}

%description bin
bin components for the pkg-config package.


%package dev
Summary: dev components for the pkg-config package.
Group: Development
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
%setup -q -n pkg-config-0.29.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1566865002
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1566865002
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pkg-config
cp COPYING %{buildroot}/usr/share/package-licenses/pkg-config/COPYING
cp glib/COPYING %{buildroot}/usr/share/package-licenses/pkg-config/glib_COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pkg-config
/usr/bin/x86_64-generic-linux-gnu-pkg-config

%files dev
%defattr(-,root,root,-)
/usr/share/aclocal/*.m4

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/pkg\-config/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pkg-config/COPYING
/usr/share/package-licenses/pkg-config/glib_COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/pkg-config.1
