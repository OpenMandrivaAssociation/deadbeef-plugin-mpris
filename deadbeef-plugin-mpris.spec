%if %{_use_internal_dependency_generator}
%define __noautoprov 'mpris\\.so(.*)'
%endif

Summary:	MPRIS support plugin for DeaDBeeF
Name:		deadbeef-plugin-mpris
Version:	2.1.5
Release:	1
License:	GPLv3+
Group:		Sound
Url:		https://github.com/kernelhcy/DeaDBeeF-MPRIS-plugin
# Snapshot from git, version from configure.ac
Source0:	deadbeef-mpris-plugin-%{version}.tar.bz2
BuildRequires:	deadbeef-devel
BuildRequires:	pkgconfig(glib-2.0)
Requires:	deadbeef

%description
MPRIS support plugin for DeaDBeeF.

%files
%doc README COPYING
%{_libdir}/deadbeef/mpris.so*

#----------------------------------------------------------------------------

%prep
%setup -qn deadbeef-mpris-plugin-%{version}
sed s,"/lib/","/%{_lib}/",g -i configure.ac

%build
autoreconf -fi
%configure2_5x --disable-static
%make

%install
%makeinstall_std

