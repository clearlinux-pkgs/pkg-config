#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x023A4420C7EC6914 (dbn.lists@gmail.com)
#
Name     : pkg-config
Version  : 0.29.2
Release  : 17
URL      : http://pkgconfig.freedesktop.org/releases/pkg-config-0.29.2.tar.gz
Source0  : http://pkgconfig.freedesktop.org/releases/pkg-config-0.29.2.tar.gz
Source99 : http://pkgconfig.freedesktop.org/releases/pkg-config-0.29.2.tar.gz.asc
Summary  : Dummy pkgconfig test package for testing pkgconfig
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: pkg-config-bin
Requires: pkg-config-doc
BuildRequires : gettext
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(glib-2.0)

%description
pkg-config is a script to make putting together all the build
flags when compiling/linking a lot easier.

%package bin
Summary: bin components for the pkg-config package.
Group: Binaries

%description bin
bin components for the pkg-config package.


%package dev
Summary: dev components for the pkg-config package.
Group: Development
Requires: pkg-config-bin
Provides: pkg-config-devel

%description dev
dev components for the pkg-config package.


%package doc
Summary: doc components for the pkg-config package.
Group: Documentation

%description doc
doc components for the pkg-config package.


%prep
%setup -q -n pkg-config-0.29.2

%build
export LANG=C
export SOURCE_DATE_EPOCH=1490212656
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1490212656
rm -rf %{buildroot}
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
%defattr(-,root,root,-)
%doc /usr/share/doc/pkg\-config/*
%doc /usr/share/man/man1/*
