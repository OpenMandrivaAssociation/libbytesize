%define realname bytesize
%define with_python2 0
%define with_gtk_doc 1

%define major 1
%define libname	%mklibname bytesize %{major}
%define devname	%mklibname -d bytesize

Name:        libbytesize
Version:     1.0
Release:     1
Summary:     A library for working with sizes in bytes
License:     LGPLv2+
URL:         https://github.com/rhinstaller/libbytesize
Source0:     https://github.com/rhinstaller/libbytesize/archive/%{name}-%{version}.tar.gz

BuildRequires: gmp-devel
BuildRequires: mpfr-devel
BuildRequires: pcre-devel
BuildRequires: gettext-devel
BuildRequires: python-devel
%if %{with_python2}
BuildRequires: python2-devel
%endif
%if %{with_gtk_doc}
BuildRequires: gtk-doc
%endif

%description
The libbytesize is a C library that facilitates work with sizes in
bytes. Be it parsing the input from users or producing a nice human readable
representation of a size in bytes this library takes localization into
account. It also provides support for sizes bigger than MAXUINT64.

%package -n	%{libname}
Summary:	A library for working with sizes in bytes
Group:		System/Libraries

%description -n	%{libname}
The libbytesize is a C library that facilitates work with sizes in
bytes. Be it parsing the input from users or producing a nice human readable
representation of a size in bytes this library takes localization into
account. It also provides support for sizes bigger than MAXUINT64.

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package includes the development files for %{name}.

%package -n python-%{realname}
Summary: Python 3 bindings for libbytesize
Requires: %{libname} = %{version}-%{release}
Provides: python-%{realname} = %{EVRD}
Requires: python-six

%description -n python-%{realname}
This package contains Python 3 bindings for libbytesize making the use of
the library from Python 3 easier and more convenient.

%if %{with_python2}
%package -n python2-%{realname}
Summary:	Python 2 bindings for libbytesize
Requires:	%{libname} = %{version}-%{release}
Requires:	python2-six

%description -n python2-%{realname}
This package contains Python 2 bindings for libbytesize making the use of
the library from Python 2 easier and more convenient.
%endif

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
%configure %{?configure_opts}
%make

%install
%makeinstall_std
find %{buildroot} -type f -name "*.la" | xargs %{__rm}


%find_lang %{name} || touch %{name}.lang

%if %{with_python2}
pushd src/python
%make clean
%makeinstall_std PYTHON=/usr/bin/python2
%endif

%files -n %{libname}
%{_libdir}/libbytesize.so.%{major}*

%files -n %{devname} -f %{name}.lang
%doc README.md
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_libdir}/libbytesize.so
%dir %{_includedir}/bytesize
%{_includedir}/bytesize/bs_size.h
%{_libdir}/pkgconfig/bytesize.pc
%if %{with_gtk_doc}
%{_datadir}/gtk-doc/html/libbytesize
%endif

%files -n python-%{realname}
%dir %{python_sitearch}/bytesize
%{python_sitearch}/bytesize/*

%if %{with_python2}
%files -n python2-%{realname}
%dir %{python2_sitearch}/bytesize
%{python2_sitearch}/bytesize/*
%{python2_sitearch}/bytesize/__pycache__/*
%endif
