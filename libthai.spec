%define major 0
%define libname %mklibname thai %{major}
%define devname %mklibname -d thai

Summary:	Thai language support routines
Name:		libthai
Version:	0.1.19
Release:	2
License:	LGPL
Group:		System/Libraries
Url:		http://linux.thai.net
Source0:	http://linux.thai.net/pub/thailinux/software/libthai/%{name}-%{version}.tar.xz
# for trietool:
BuildRequires:	trietool
BuildRequires:	pkgconfig(datrie-0.2)

%description
LibThai is a set of Thai language support routines aimed to ease
developers' tasks to incorporate Thai language support in their applications.
It includes important Thai-specific functions e.g. word breaking, input and
output methods as well as basic character and string supports.

%package -n %{libname}
Summary:	Thai language support routines
Group:		System/Libraries
Requires:	thai-data

%description -n %{libname}
LibThai is a set of Thai language support routines aimed to ease
developers' tasks to incorporate Thai language support in their applications.
It includes important Thai-specific functions e.g. word breaking, input and
output methods as well as basic character and string supports.

%package -n thai-data
Summary:	Thai language support data 
Group:		System/Libraries
Requires:	thai-data

%description -n thai-data
Data stuff for libthai.

%package -n %{devname}
Summary:	Thai language support routines
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	thai-devel = %{version}

%description -n %devname
The libthai-devel package includes the header files and developer docs 
for the libthai package.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static \
	--disable-doxygen-doc
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libthai.so.%{major}*

%files -n %{devname}
%doc README AUTHORS COPYING ChangeLog
%{_includedir}/thai
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

%files -n thai-data
%{_datadir}/libthai

