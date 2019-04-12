Summary:	ninja-compatible build tool written in C
Name:		samurai
Version:	0.6
Release:	1
License:	APL2+
Group:		Development/Other
URL:		https://github.com/michaelforney/samurai
Source0:	https://github.com/michaelforney/samurai/releases/%{name}-%{version}.tar.gz

%description
samurai is a ninja-compatible build tool written in
C99 with a focus on simplicity, speed, and portability.

%prep
%autosetup -p1

%build
%global optflags %{optflags} -O3

%make_build CC="%{__cc}" CFLAGS="%{optflags}" LDFLAGS="%{optflags}"

%install
%make_install PREFIX="%{_prefix}"

%files
%{_bindir}/samu
%{_mandir}/man1/samu.1.*
