%define ppl_major 9
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
%bcond_with	java
%bcond_with	crosscompile

Summary:	The Parma Polyhedra Library: a library of numerical abstractions
Name:		ppl
Version:	0.11.2
Release:	8
Group:		Development/C
License:	GPLv3+
Url:		http://bugseng.com/products/ppl
Source0:	http://bugseng.com/products/ppl/download/ftp/ppl/releases/%{version}/ppl-%{version}.tar.bz2
Source1:	ppl.hh
Source2:	ppl_c.h
Source3:	pwl.hh
Patch0:		ppl-0.10.2-Makefile.patch
Patch1:		ppl-0.11.2-autoconf-2.68.patch
Patch2:		ppl-0.11.2-automake-1.11.2.patch
Patch3:		ppl-0.11.2-lzma.patch
Patch4:		ppl-0.11.2-gmp-5.1.patch
Patch5:		ppl-glpk-4.52.patch
BuildRequires:	m4 >= 1.4.8
BuildRequires:	gmp-devel >= 4.1.3
BuildRequires:	gmpxx-devel >= 4.1.3

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
%if %mdkversion == 201100
Conflicts:	%{mklibname ppl 7} = 0.11
%endif

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
%doc %{_datadir}/doc/%{name}-%{version}/BUGS
%doc %{_datadir}/doc/%{name}-%{version}/COPYING
%doc %{_datadir}/doc/%{name}-%{version}/CREDITS
%doc %{_datadir}/doc/%{name}-%{version}/NEWS
%doc %{_datadir}/doc/%{name}-%{version}/README
%doc %{_datadir}/doc/%{name}-%{version}/README.configure
%doc %{_datadir}/doc/%{name}-%{version}/TODO
%doc %{_datadir}/doc/%{name}-%{version}/gpl.txt
%{_libdir}/libppl.so.%{ppl_major}*
%if !%{with crosscompile}
%dir %{_libdir}/%{name}
%endif
# not needed if we not use prolog
# arm ppc etc arches 
#% dir %{_datadir}/ %{name}
%dir %{_datadir}/doc/%{name}-%{version}

#-----------------------------------------------------------------------
%package -n %{libppl_devel}
Summary:	Development tools for the Parma Polyhedra Library C and C++ interfaces
Group:		Development/C
Requires:	%{libppl} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%release
Conflicts:	%{_lib}ppl7-devel < 0.11-3

%description -n %{libppl_devel}
The header files, Autoconf macro and minimal documentation for
developing applications using the Parma Polyhedra Library through
its C and C++ interfaces.

%files -n %{libppl_devel}
%{_bindir}/ppl-config
%{_includedir}/ppl*.hh
%{_libdir}/libppl.so
%{_mandir}/man1/ppl-config.1.*
%{_mandir}/man3/libppl.3.*
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
%{_mandir}/man1/ppl_lcdd.1.*
%{_mandir}/man1/ppl_lpsol.1.*
%{_mandir}/man1/ppl_pips.1.*

#-----------------------------------------------------------------------
%ifnarch ia64 ppc64 s390 s390x %arm aarch64
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
#%package	ocaml
#Summary:	The OCaml interface of the Parma Polyhedra Library
#Group:		Development/Other
#BuildRequires:	ocaml >= 3.09
#Requires:	%{name} = %{version}-%{release}

#%description	ocaml
#This package adds Objective Caml (OCaml) support to the Parma
#Polyhedra Library.  Install this package if you want to use the
#library in OCaml programs.

#%files		ocaml
#%defattr(-,root,root,-)
#%doc interfaces/OCaml/README.ocaml
#%{_libdir}/%{name}/ppl_ocaml.cma
#%{_libdir}/%{name}/ppl_ocaml.cmi
#%{_libdir}/%{name}/ppl_ocaml_globals.cmi

#-----------------------------------------------------------------------
#%package	ocaml-devel
#Summary:	The OCaml interface of the Parma Polyhedra Library
#Group:		Development/Other
#Requires:	%{name}-ocaml = %{version}-%{release}

#%description	ocaml-devel
#This package contains libraries and signature files for developing
#applications using the OCaml interface of the Parma Polyhedra Library.

#%files		ocaml-devel
#%defattr(-,root,root,-)
#%{_libdir}/%{name}/libppl_ocaml.a
#%{_libdir}/%{name}/ppl_ocaml.mli

#-----------------------------------------------------------------------
%if %{with java}
%package	java
Summary:	The Java interface of the Parma Polyhedra Library
Group:		Development/Java
BuildRequires:	java-1.7.0-openjdk-devel
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
%doc %{_datadir}/doc/%{name}-%{version}/ChangeLog*
%doc %{_datadir}/doc/%{name}-%{version}/README.doc
%doc %{_datadir}/doc/%{name}-%{version}/fdl.*
%doc %{_datadir}/doc/%{name}-%{version}/gpl.pdf
%doc %{_datadir}/doc/%{name}-%{version}/gpl.ps.gz
%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-%{version}-html/
%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-*-interface-%{version}-html/
%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-%{version}.pdf
%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-*-interface-%{version}.pdf
%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-%{version}.ps.gz
%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-*-interface-%{version}.ps.gz

#-----------------------------------------------------------------------
%package -n %{libpwl}
Summary:	The Parma Watchdog Library: a C++ library for watchdog timers
Group:		Development/C++
%if %mdkversion == 201100
Conflicts:	%{mklibname pwl 4} = 0.11
%endif

%description -n %{libpwl}
The Parma Watchdog Library (PWL) provides support for multiple,
concurrent watchdog timers on systems providing setitimer(2).  This
package provides all what is necessary to run applications using the
PWL.  The PWL is currently distributed with the Parma Polyhedra
Library, but is totally independent from it.

%files -n %{libpwl}
%{_libdir}/libpwl.so.%{pwl_major}*

#-----------------------------------------------------------------------
%package -n %{libpwl_devel}
Summary:	Development tools for the Parma Watchdog Library
Group:		Development/C++
Requires:	%{libpwl} = %{version}-%{release}
Provides:	%{name}-pwl-devel = %{version}-%{release}
Provides:	pwl-devel = %{version}-%{release}

%description -n %{libpwl_devel}
The header files, documentation and static libraries for developing
applications using the Parma Watchdog Library.

%files -n %{libpwl_devel}
%doc Watchdog/doc/README.doc
%{_includedir}/pwl*.hh
%{_libdir}/libpwl.so

#-----------------------------------------------------------------------
%package -n %{libpwl_static_devel}
Summary:	Static archive for the Parma Watchdog Library
Group:		Development/C++
Requires:	%{name}-pwl-devel = %{version}-%{release}
Provides: 	libpwl-static-devel = %{version}-%{release}
Obsoletes:	%{_lib}pwl4-static-devel < 0.11-3

%description -n %{libpwl_static_devel}
This package contains the static archive for the Parma Watchdog Library.

%files -n %{libpwl_static_devel}
%{_libdir}/libpwl.a

#-----------------------------------------------------------------------
%package	pwl-docs
Summary:	Documentation for the Parma Watchdog Library
Group:		Development/C++
#Requires:	%{libpwl} = %{version}-%{release}

%description	pwl-docs
This package contains all the documentations required by programmers
using the Parma Watchdog Library (PWL).
Install this package if you want to program with the PWL.

%files		pwl-docs
%doc %{_datadir}/doc/%{name}-%{version}/pwl-user-0.8-html/
%doc %{_datadir}/doc/%{name}-%{version}/pwl-user-0.8.pdf
%doc %{_datadir}/doc/%{name}-%{version}/pwl-user-0.8.ps.gz

%prep
%setup -q
%apply_patches

aclocal -I m4
autoreconf -fi

%build
%ifnarch ia64 ppc64 s390 s390x %arm aarch64
CPPFLAGS="%{optflags} -I%{_libdir}/gprolog-`gprolog --version 2>&1 | head -1 | sed -e "s/.* \([^ ]*\)$/\1/g"`/include"
%endif
%configure \
	--docdir=%{_datadir}/doc/%{name}-%{version} \
	--enable-shared \
	--enable-interfaces="c++ c gnu_prolog java" CPPFLAGS="$CPPFLAGS"
#sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
#sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
#sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' Watchdog/libtool
#sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' Watchdog/libtool
%make

%install
%makeinstall_std

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
mv %{buildroot}/%{_includedir}/pwl.hh %{buildroot}/%{_includedir}/pwl-${normalized_arch}.hh
install -m644 %{SOURCE3} %{buildroot}/%{_includedir}/pwl.hh

%if %{with java}
# Install the Javadocs for ppl-java.
mkdir -p %{buildroot}%{_javadocdir}
mv \
%{buildroot}/%{_datadir}/doc/%{name}-%{version}/ppl-user-java-interface-%{version}-html \
%{buildroot}%{_javadocdir}/%{name}-java
%endif

#rm %{buildroot}%{_libdir}/*.la
#rm %{buildroot}%{_libdir}/ppl/*.la

