%define realname bytesize
%define with_gtk_doc 1

%define major 1
%define libname %mklibname bytesize %{major}
%define devname %mklibname -d bytesize

Name:		libbytesize
Version:	2.0
Release:	1
Summary:	A library for working with sizes in bytes
License:	LGPLv2+
URL:		https://github.com/rhinstaller/libbytesize
Source0:	https://github.com/rhinstaller/libbytesize/archive/%{name}-%{version}.tar.gz

BuildRequires:	gmp-devel
BuildRequires:	mpfr-devel
BuildRequires:	pkgconfig(libpcre2-8)
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(python)
%if %{with_gtk_doc}
BuildRequires:	gtk-doc
%endif

%description
The libbytesize is a C library that facilitates work with sizes in
bytes. Be it parsing the input from users or producing a nice human readable
representation of a size in bytes this library takes localization into
account. It also provides support for sizes bigger than MAXUINT64.

%package -n %{libname}
Summary:	A library for working with sizes in bytes
Group:		System/Libraries

%description -n %{libname}
The libbytesize is a C library that facilitates work with sizes in
bytes. Be it parsing the input from users or producing a nice human readable
representation of a size in bytes this library takes localization into
account. It also provides support for sizes bigger than MAXUINT64.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package includes the development files for %{name}.

%package -n python-%{realname}
Summary:	Python 3 bindings for libbytesize
Requires:	%{libname} = %{version}-%{release}
Provides:	python-%{realname} = %{EVRD}
Requires:	python-six

%description -n python-%{realname}
This package contains Python 3 bindings for libbytesize making the use of
the library from Python 3 easier and more convenient.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete

%find_lang %{name} || touch %{name}.lang

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
