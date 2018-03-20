%define _disable_rebuild_configure 1
%define ppl_major 14
%define libppl %mklibname ppl %ppl_major
%define libppl_devel %mklibname -d ppl
%define libppl_static_devel %mklibname -d -s ppl

%define ppl_c_major 4
%define libppl_c %mklibname ppl_c %ppl_c_major
%define libppl_c_devel %mklibname -d ppl_c
%define libppl_c_static_devel %mklibname -d -s ppl_c

%define pwl_major 5
%define libpwl %mklibname pwl %pwl_major
%define libpwl_devel %mklibname -d pwl
%define libpwl_static_devel %mklibname -d -s pwl
%bcond_with java
%bcond_with crosscompile

Summary:	The Parma Polyhedra Library: a library of numerical abstractions
Name:		ppl
Version:	1.2
Release:	3
Group:		Development/C
License:	GPLv3+
URL:		http://www.cs.unipr.it/ppl/
Source0:	ftp://ftp.cs.unipr.it/pub/ppl/releases/%{version}/%{name}-%{version}.tar.xz
Source1:	ppl.hh
Source2:	ppl_c.h
BuildRequires:	m4 >= 1.4.8
BuildRequires:	gmp-devel >= 4.1.3
BuildRequires:	gmpxx-devel >= 4.1.3
%if %{with java}
BuildRequires:	java-devel
%endif

%description
The Parma Polyhedra Library (PPL) is a library for the manipulation of
(not necessarily closed) convex polyhedra and other numerical
abstractions.  The applications of convex polyhedra include program
analysis, optimized compilation, integer and combinatorial
optimization and statistical data-editing.  The Parma Polyhedra
Library comes with several user friendly interfaces, is fully dynamic
(available virtual memory is the only limitation to the dimension of
anything), written in accordance to all the applicable standards,
exception-safe, rather efficient, thoroughly documented, and free
software.  This package provides all what is necessary to run
applications using the PPL through its C and C++ interfaces.

#-----------------------------------------------------------------------
%package -n %{libppl}
Group:		Development/C
Summary:	The Parma Polyhedra Library: a library of numerical abstractions
# Merged into ppl as of 0.12
%rename %{libpwl}

%description -n %{libppl}
The Parma Polyhedra Library (PPL) is a library for the manipulation of
(not necessarily closed) convex polyhedra and other numerical
abstractions.  The applications of convex polyhedra include program
analysis, optimized compilation, integer and combinatorial
optimization and statistical data-editing.  The Parma Polyhedra
Library comes with several user friendly interfaces, is fully dynamic
(available virtual memory is the only limitation to the dimension of
anything), written in accordance to all the applicable standards,
exception-safe, rather efficient, thoroughly documented, and free
software.  This package provides all what is necessary to run
applications using the PPL through its C and C++ interfaces.

%files -n %{libppl}
%dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/BUGS
%doc %{_docdir}/%{name}-%{version}/COPYING
%doc %{_docdir}/%{name}-%{version}/CREDITS
%doc %{_docdir}/%{name}-%{version}/NEWS
%doc %{_docdir}/%{name}-%{version}/README
%doc %{_docdir}/%{name}-%{version}/README.configure
%doc %{_docdir}/%{name}-%{version}/TODO
%doc %{_docdir}/%{name}-%{version}/gpl.txt
%{_libdir}/libppl.so.%{ppl_major}*
%if !%{with crosscompile}
%ifnarch %armx
%dir %{_libdir}/%{name}
%endif
%endif

#-----------------------------------------------------------------------
%package -n %{libppl_devel}
Summary:	Development tools for the Parma Polyhedra Library C and C++ interfaces
Group:		Development/C
Requires:	%{libppl} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%release
Conflicts:	%{_lib}ppl7-devel < 0.11-3
# Merged into ppl as of 0.12
%rename %{libpwl_devel}

%description -n %{libppl_devel}
The header files, Autoconf macro and minimal documentation for
developing applications using the Parma Polyhedra Library through
its C and C++ interfaces.

%files -n %{libppl_devel}
%{_bindir}/ppl-config
%{_includedir}/ppl*.hh
%{_libdir}/libppl.so
%{_mandir}/man1/ppl-config.1*
%{_mandir}/man3/libppl.3*
%{_datadir}/aclocal/ppl.m4

#-----------------------------------------------------------------------
%package -n %{libppl_static_devel}
Summary:	Static archives for the Parma Polyhedra Library C and C++ interfaces
Group:		Development/C
Requires:	%{name}-devel = %{version}-%{release}
Provides:	libppl-static-devel = %{version}-%{release}
Obsoletes:	%{_lib}ppl7-static-devel < 0.11-3

%description -n %{libppl_static_devel}
The static archives for the Parma Polyhedra Library C and C++ interfaces.

%files -n %{libppl_static_devel}
%{_libdir}/libppl.a

#-----------------------------------------------------------------------
%package -n %{libppl_c}
Group:		Development/C
Summary:	The Parma Polyhedra Library: a library of numerical abstractions
%if %mdkversion == 201100
Conflicts:	%{mklibname ppl_c 2} = 0.11
%endif

%description -n %{libppl_c}
The Parma Polyhedra Library (PPL) is a library for the manipulation of
(not necessarily closed) convex polyhedra and other numerical
abstractions.  The applications of convex polyhedra include program
analysis, optimized compilation, integer and combinatorial
optimization and statistical data-editing.  The Parma Polyhedra
Library comes with several user friendly interfaces, is fully dynamic
(available virtual memory is the only limitation to the dimension of
anything), written in accordance to all the applicable standards,
exception-safe, rather efficient, thoroughly documented, and free
software.  This package provides all what is necessary to run
applications using the PPL through its C and C++ interfaces.

%files -n %{libppl_c}
%{_libdir}/libppl_c.so.%{ppl_c_major}*

#-----------------------------------------------------------------------
%package -n %{libppl_c_devel}
Summary:	Development tools for the Parma Polyhedra Library C and C++ interfaces
Group:		Development/C
Requires:	%{libppl_c} = %{version}-%{release}
Conflicts:	%{_lib}ppl-devel < 0.11-3
Provides:	ppl_c-devel = %{version}-%{release}

%description -n %{libppl_c_devel}
The header files, Autoconf macro and minimal documentation for
developing applications using the Parma Polyhedra Library through
its C and C++ interfaces.

%files -n %{libppl_c_devel}
%{_includedir}/ppl_c*.h
%{_libdir}/libppl_c.so
%{_mandir}/man3/libppl_c.3.*
%{_datadir}/aclocal/ppl_c.m4

#-----------------------------------------------------------------------
%package -n %{libppl_c_static_devel}
Summary:	Static archives for the Parma Polyhedra Library C and C++ interfaces
Group:		Development/C
Requires:	%{libppl_c_devel} = %{version}-%{release}
Provides:	libppl_c-static-devel = %{version}-%{release}
Provides:	ppl_c-static-devel = %{version}-%{release}
Conflicts:	%{_lib}ppl7-static-devel

%description -n %{libppl_c_static_devel}
The static archives for the Parma Polyhedra Library C and C++ interfaces.

%files -n %{libppl_c_static_devel}
%{_libdir}/libppl_c.a

#-----------------------------------------------------------------------
%package	utils
Summary:	Utilities using the Parma Polyhedra Library
Group:		Development/C
Requires:	%{libppl} = %{version}-%{release}
BuildRequires:	glpk-devel >= 4.13

%description	utils
This package contains the mixed integer linear programming solver ppl_lpsol
and the program ppl_lcdd for vertex/facet enumeration of convex polyhedra.

%files		utils
%{_bindir}/ppl_lcdd
%{_bindir}/ppl_lpsol
%{_bindir}/ppl_pips
%{_mandir}/man1/ppl_lcdd.1*
%{_mandir}/man1/ppl_lpsol.1*
%{_mandir}/man1/ppl_pips.1*

#-----------------------------------------------------------------------
%ifnarch ia64 ppc64 s390 s390x %armx
%package	gprolog
# The `gprolog' package is not available on ppc64:
# the GNU Prolog interface must thus be disabled for that architecture.
Summary:	The GNU Prolog interface of the Parma Polyhedra Library
Group:		Development/Other
BuildRequires:	gprolog >= 1.2.19
Requires:	gprolog >= 1.2.19

%description	gprolog
This package adds GNU Prolog support to the Parma Polyhedra Library (PPL).
Install this package if you want to use the library in GNU Prolog programs.

%files		gprolog
%doc interfaces/Prolog/GNU/README.gprolog
%{_bindir}/ppl_gprolog
%{_datadir}/%{name}/ppl_gprolog.pl
%{_libdir}/%{name}/libppl_gprolog.so

#-----------------------------------------------------------------------
%package	gprolog-static
Summary:	The static archive for the GNU Prolog interface of the Parma Polyhedra Library
Group:		Development/Other
Requires:	%{name}-gprolog = %{version}-%{release}

%description gprolog-static
This package contains the static archive for the GNU Prolog interface
of the Parma Polyhedra Library.

%files		gprolog-static
%{_libdir}/%{name}/libppl_gprolog.a
%endif

#-----------------------------------------------------------------------
%if %{with java}
%package	java
Summary:	The Java interface of the Parma Polyhedra Library
Group:		Development/Java
BuildRequires:	java-devel
#java-devel >= 0:1.6.0
BuildRequires:	jpackage-utils
Requires:	java >= 1.6.0
Requires:	jpackage-utils
Requires:	%{libppl} = %{version}-%{release}

%description	java
This package adds Java support to the Parma Polyhedra Library.
Install this package if you want to use the library in Java programs.

%files		java
%doc interfaces/Java/README.java
%{_libdir}/%{name}/libppl_java.so
%{_libdir}/%{name}/ppl_java.jar

#-----------------------------------------------------------------------
%package	java-javadoc
Summary:	Javadocs for %{name}-java
Group:		Development/Java
Requires:	%{name}-java = %{version}-%{release}
Requires:	jpackage-utils

%description	java-javadoc
This package contains the API documentation for Java interface
of the Parma Polyhedra Library.

%files		java-javadoc
%{_javadocdir}/%{name}-java
%endif

#-----------------------------------------------------------------------
%package	docs
Summary:	Documentation for the Parma Polyhedra Library
Group:		Development/C
Requires:	%{libppl} = %{version}-%{release}

%description	docs
This package contains all the documentations required by programmers
using the Parma Polyhedra Library (PPL).
Install this package if you want to program with the PPL.

%files		docs
%doc %{_docdir}/%{name}-%{version}/ChangeLog*
%doc %{_docdir}/%{name}-%{version}/README.doc
%doc %{_docdir}/%{name}-%{version}/fdl.*
%doc %{_docdir}/%{name}-%{version}/gpl.pdf
%doc %{_docdir}/%{name}-%{version}/gpl.ps.gz
%doc %{_docdir}/%{name}-%{version}/ppl-user-%{version}-html/
%doc %{_docdir}/%{name}-%{version}/ppl-user-*-interface-%{version}-html/
%doc %{_docdir}/%{name}-%{version}/ppl-user-%{version}.pdf
%doc %{_docdir}/%{name}-%{version}/ppl-user-*-interface-%{version}.pdf
%doc %{_docdir}/%{name}-%{version}/ppl-user-%{version}.ps.gz
%doc %{_docdir}/%{name}-%{version}/ppl-user-*-interface-%{version}.ps.gz

%prep
%setup -q
%utopatch -p1

aclocal -I m4
autoreconf -fi

%build
CPPFLAGS="-I%{_includedir}/glpk"
# This is the explicit list of arches gprolog supports
%ifarch x86_64 %{ix86} ppc alpha
CPPFLAGS="$CPPFLAGS -I%{_libdir}/gprolog-`gprolog --version 2>&1 | head -1 | sed -e "s/.* \([^ ]*\)$/\1/g"`/include"
%endif
%ifnarch sparc64 sparcv9 %{arm} ppc ppc64
CPPFLAGS="$CPPFLAGS -I`swipl -dump-runtime-variables | grep PLBASE= | sed 's/PLBASE="\(.*\)";/\1/'`/include"
CPPFLAGS="$CPPFLAGS -I%{_includedir}/Yap"
%endif
export CC=gcc
export CXX=g++
%configure --docdir=%{_docdir}/%{name}-%{version} --enable-static --enable-shared --disable-rpath --enable-interfaces="c++ c gnu_prolog swi_prolog yap_prolog java" CPPFLAGS="$CPPFLAGS"
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} CC=gcc CXX=g++
%make_build CXX=g++ CC=gcc

%install
%make_install

# In order to avoid multiarch conflicts when installed for multiple
# architectures (e.g., i386 and x86_64), we rename the header files
# of the ppl-devel and ppl-pwl-devel packages.  They are substituted with
# ad-hoc switchers that select the appropriate header file depending on
# the architecture for which the compiler is compiling.

# Since our header files only depend on the sizeof things, we smash
# ix86 onto i386 and arm* onto arm.  For the SuperH RISC engine family,
# we smash sh3 and sh4 onto sh.
normalized_arch=%{_arch}
%ifarch %{ix86}
normalized_arch=i386
%endif
%ifarch %{arm}
normalized_arch=arm
%endif
%ifarch sh3 sh4
normalized_arch=sh
%endif

mv %{buildroot}/%{_includedir}/ppl.hh %{buildroot}/%{_includedir}/ppl-${normalized_arch}.hh
install -m644 %{SOURCE1} %{buildroot}/%{_includedir}/ppl.hh
mv %{buildroot}/%{_includedir}/ppl_c.h %{buildroot}/%{_includedir}/ppl_c-${normalized_arch}.h
install -m644 %{SOURCE2} %{buildroot}/%{_includedir}/ppl_c.h

%if %{with java}
# Install the Javadocs for ppl-java.
mkdir -p %{buildroot}%{_javadocdir}
mv \
%{buildroot}/%{_docdir}/%{name}-%{version}/ppl-user-java-interface-%{version}-html \
%{buildroot}%{_javadocdir}/%{name}-java
%endif
