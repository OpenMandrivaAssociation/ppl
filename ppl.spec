%define		ppl_major		9
%define		libppl			%mklibname ppl %ppl_major
%define 	libppl_devel		%mklibname -d ppl
%define 	libppl_static_devel	%mklibname -d -s ppl

%define		ppl_c_major		4
%define		libppl_c		%mklibname ppl_c %ppl_c_major
%define 	libppl_c_devel		%mklibname -d ppl_c
%define 	libppl_c_static_devel	%mklibname -d -s ppl_c

%define		pwl_major		5
%define		libpwl			%mklibname pwl %pwl_major
%define 	libpwl_devel		%mklibname -d pwl
%define 	libpwl_static_devel	%mklibname -d -s pwl

Name:		ppl
Version:	0.11.2
Release:	2
Group:		Development/C
Summary:	The Parma Polyhedra Library: a library of numerical abstractions
License:	GPLv3+
URL:		http://bugseng.com/products/ppl
Source0:	http://bugseng.com/products/ppl/download/ftp/ppl/releases/%version/ppl-%version.tar.bz2
Source1:	ppl.hh
Source2:	ppl_c.h
Source3:	pwl.hh
Patch0:		ppl-0.10.2-Makefile.patch
Patch1:		ppl-0.11.2-autoconf-2.68.patch
Patch2:		ppl-0.11.2-automake-1.11.2.patch
Patch3:		ppl-0.11.2-lzma.patch
BuildRequires:	gmp-devel >= 4.1.3, gmpxx-devel >= 4.1.3, m4 >= 1.4.8

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
%package	-n %{libppl}
Group:		Development/C
Summary:	The Parma Polyhedra Library: a library of numerical abstractions
%if %mdkversion == 201100
Conflicts:	%{mklibname ppl 7} = 0.11
%endif

%description	-n %{libppl}
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

%files		-n %{libppl}
%defattr(-,root,root,-)
%doc %{_datadir}/doc/%{name}-%{version}/BUGS
%doc %{_datadir}/doc/%{name}-%{version}/COPYING
%doc %{_datadir}/doc/%{name}-%{version}/CREDITS
%doc %{_datadir}/doc/%{name}-%{version}/NEWS
%doc %{_datadir}/doc/%{name}-%{version}/README
%doc %{_datadir}/doc/%{name}-%{version}/README.configure
%doc %{_datadir}/doc/%{name}-%{version}/TODO
%doc %{_datadir}/doc/%{name}-%{version}/gpl.txt
%{_libdir}/libppl.so.%{ppl_major}
%{_libdir}/libppl.so.%{ppl_major}.*
%dir %{_libdir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/doc/%{name}-%{version}

#-----------------------------------------------------------------------
%package	-n %{libppl_devel}
Summary:	Development tools for the Parma Polyhedra Library C and C++ interfaces
Group:		Development/C
Requires:	%{libppl} = %{version}-%{release}
Requires:	gmp-devel >= 4.1.3
Requires:	gmpxx-devel >= 4.1.3
Provides:	%{name}-devel = %version-%release
Conflicts:	%{_lib}ppl7-devel < 0.11-3

%description	-n %{libppl_devel}
The header files, Autoconf macro and minimal documentation for
developing applications using the Parma Polyhedra Library through
its C and C++ interfaces.

%files		-n %{libppl_devel}
%defattr(-,root,root,-)
%{_bindir}/ppl-config
%{_includedir}/ppl*.hh
%{_libdir}/libppl.so
%{_mandir}/man1/ppl-config.1.*
%{_mandir}/man3/libppl.3.*
%{_datadir}/aclocal/ppl.m4

#-----------------------------------------------------------------------
%package	-n %{libppl_static_devel}
Summary:	Static archives for the Parma Polyhedra Library C and C++ interfaces
Group:		Development/C
Requires:	%{name}-devel = %{version}-%{release}
Provides:	libppl-static-devel = %{version}-%{release}
Obsoletes:	%{_lib}ppl7-static-devel < 0.11-3

%description	-n %{libppl_static_devel}
The static archives for the Parma Polyhedra Library C and C++ interfaces.

%files		-n %{libppl_static_devel}
%defattr(-,root,root,-)
%{_libdir}/libppl.a

#-----------------------------------------------------------------------
%package	-n %{libppl_c}
Group:		Development/C
Summary:	The Parma Polyhedra Library: a library of numerical abstractions
%if %mdkversion == 201100
Conflicts:	%{mklibname ppl_c 2} = 0.11
%endif

%description	-n %{libppl_c}
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

%files		-n %{libppl_c}
%defattr(-,root,root,-)
%{_libdir}/libppl_c.so.%{ppl_c_major}
%{_libdir}/libppl_c.so.%{ppl_c_major}.*

#-----------------------------------------------------------------------
%package	-n %{libppl_c_devel}
Summary:	Development tools for the Parma Polyhedra Library C and C++ interfaces
Group:		Development/C
Requires:	%{libppl_c} = %{version}-%{release}
Conflicts:	%{_lib}ppl-devel < 0.11-3
Provides:	ppl_c-devel = %{version}-%{release}

%description	-n %{libppl_c_devel}
The header files, Autoconf macro and minimal documentation for
developing applications using the Parma Polyhedra Library through
its C and C++ interfaces.

%files		-n %{libppl_c_devel}
%defattr(-,root,root,-)
%{_includedir}/ppl_c*.h
%{_libdir}/libppl_c.so
%{_mandir}/man3/libppl_c.3.*
%{_datadir}/aclocal/ppl_c.m4

#-----------------------------------------------------------------------
%package	-n %{libppl_c_static_devel}
Summary:	Static archives for the Parma Polyhedra Library C and C++ interfaces
Group:		Development/C
Requires:	%{libppl_c_devel} = %{version}-%{release}
Provides:	libppl_c-static-devel = %{version}-%{release}
Provides:	ppl_c-static-devel = %{version}-%{release}
Conflicts:	%{_lib}ppl7-static-devel

%description	-n %{libppl_c_static_devel}
The static archives for the Parma Polyhedra Library C and C++ interfaces.

%files		-n %{libppl_c_static_devel}
%defattr(-,root,root,-)
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
%defattr(-,root,root,-)
%{_bindir}/ppl_lcdd
%{_bindir}/ppl_lpsol
%{_bindir}/ppl_pips
%{_mandir}/man1/ppl_lcdd.1.*
%{_mandir}/man1/ppl_lpsol.1.*
%{_mandir}/man1/ppl_pips.1.*

#-----------------------------------------------------------------------
%ifnarch ia64 ppc64 s390 s390x %arm
%package	gprolog
# The `gprolog' package is not available on ppc64:
# the GNU Prolog interface must thus be disabled for that architecture.
Summary:	The GNU Prolog interface of the Parma Polyhedra Library
Group:		Development/Other
BuildRequires:	gprolog >= 1.2.19
Requires:	%{libppl} = %{version}-%{release},
Requires:	%{libpwl} = %{version}-%{release}
Requires:	gprolog >= 1.2.19

%description	gprolog
This package adds GNU Prolog support to the Parma Polyhedra Library (PPL).
Install this package if you want to use the library in GNU Prolog programs.

%files		gprolog
%defattr(-,root,root,-)
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
%defattr(-,root,root,-)
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
%package	java
Summary:	The Java interface of the Parma Polyhedra Library
Group:		Development/Java
BuildRequires:	java-devel >= 0:1.6.0
BuildRequires:	jpackage-utils
Requires:	java >= 1.6.0
Requires:	jpackage-utils
Requires:	%{libppl} = %{version}-%{release}

%description	java
This package adds Java support to the Parma Polyhedra Library.
Install this package if you want to use the library in Java programs.

%files		java
%defattr(-,root,root,-)
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
%defattr(-,root,root,-)
%{_javadocdir}/%{name}-java

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
%defattr(-,root,root,-)
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
%package	-n %{libpwl}
Summary:	The Parma Watchdog Library: a C++ library for watchdog timers
Group:		Development/C++
%if %mdkversion == 201100
Conflicts:	%{mklibname pwl 4} = 0.11
%endif

%description	 -n %{libpwl}
The Parma Watchdog Library (PWL) provides support for multiple,
concurrent watchdog timers on systems providing setitimer(2).  This
package provides all what is necessary to run applications using the
PWL.  The PWL is currently distributed with the Parma Polyhedra
Library, but is totally independent from it.

%files		-n %{libpwl}
%defattr(-,root,root,-)
%{_libdir}/libpwl.so.%{pwl_major}
%{_libdir}/libpwl.so.%{pwl_major}.*

#-----------------------------------------------------------------------
%package	-n %{libpwl_devel}
Summary:	Development tools for the Parma Watchdog Library
Group:		Development/C++
Requires:	%{libpwl} = %{version}-%{release}
Provides:	%{name}-pwl-devel = %{version}-%{release}
Provides:	pwl-devel = %{version}-%{release}

%description	-n %{libpwl_devel}
The header files, documentation and static libraries for developing
applications using the Parma Watchdog Library.

%files		-n %{libpwl_devel}
%defattr(-,root,root,-)
%doc Watchdog/doc/README.doc
%{_includedir}/pwl*.hh
%{_libdir}/libpwl.so

#-----------------------------------------------------------------------
%package	-n %{libpwl_static_devel}
Summary:	Static archive for the Parma Watchdog Library
Group:		Development/C++
Requires:	%{name}-pwl-devel = %{version}-%{release}
Provides: 	libpwl-static-devel = %{version}-%{release}
Obsoletes:	%{_lib}pwl4-static-devel < 0.11-3

%description	-n %{libpwl_static_devel}
This package contains the static archive for the Parma Watchdog Library.

%files		-n %{libpwl_static_devel}
%defattr(-,root,root,-)
%{_libdir}/libpwl.a

#-----------------------------------------------------------------------
%package	pwl-docs
Summary:	Documentation for the Parma Watchdog Library
Group:		Development/C++
Requires:	%{libpwl} = %{version}-%{release}

%description	pwl-docs
This package contains all the documentations required by programmers
using the Parma Watchdog Library (PWL).
Install this package if you want to program with the PWL.

%files		pwl-docs
%defattr(-,root,root,-)
%doc %{_datadir}/doc/%{name}-%{version}/pwl-user-0.8-html/
%doc %{_datadir}/doc/%{name}-%{version}/pwl-user-0.8.pdf
%doc %{_datadir}/doc/%{name}-%{version}/pwl-user-0.8.ps.gz

#-----------------------------------------------------------------------
%prep
%setup -q
%patch0 -p1 -b .Makefile~
%patch1 -p1 -b .ac268~
%patch2 -p1 -b .am11~
%patch3 -p1 -b .lzma~

#-----------------------------------------------------------------------
%build
aclocal -I m4
autoreconf -fi
%ifnarch ia64 ppc64 s390 s390x %arm
CPPFLAGS="%{optflags} -I%{_libdir}/gprolog-`gprolog --version 2>&1 | head -1 | sed -e "s/.* \([^ ]*\)$/\1/g"`/include"
%endif
%configure --docdir=%{_datadir}/doc/%{name}-%{version} --enable-shared --enable-interfaces="c++ c gnu_prolog java" CPPFLAGS="$CPPFLAGS"
#sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
#sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
#sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' Watchdog/libtool
#sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' Watchdog/libtool
%make

#-----------------------------------------------------------------------
%install
rm -rf %{buildroot}
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

# Install the Javadocs for ppl-java.
mkdir -p %{buildroot}%{_javadocdir}
mv \
%{buildroot}/%{_datadir}/doc/%{name}-%{version}/ppl-user-java-interface-%{version}-html \
%{buildroot}%{_javadocdir}/%{name}-java

rm %{buildroot}%{_libdir}/*.la
rm %{buildroot}%{_libdir}/ppl/*.la

#-----------------------------------------------------------------------
%clean
rm -rf %{buildroot}

%changelog
* Tue Jan 10 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.11.2-1mdv2012.0
+ Revision: 759624
- Update to 0.11.2
- Fix build with current autotools

* Wed Dec 07 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.11-5
+ Revision: 738700
- Rebuild for .la file removal.
- Add cooker specific conflicts for easier cooker updates

  + Matthew Dawkins <mattydaw@mandriva.org>
    - added arm support
      simplified docs file list to avoid more ifnarch statements

* Sun Apr 10 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.11-3
+ Revision: 652189
- Update to ppl 0.11, add libppl_c and correct library major on package names

  + Funda Wang <fwang@mandriva.org>
    - add more conflicts and obsoletes to ease upgrade
    - new static devel package policy
    - move ppl-config into devel package, which is the correct package it belongs
    - correctly lock major
    - lock libmajor
    - convert to devel package polciy for static devel package

* Wed Feb 02 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.11-2
+ Revision: 634947
- Add intermediate revert before rebuilding with proper major

* Tue Feb 01 2011 Alexandre Lissy <alissy@mandriva.com> 0.11-1
+ Revision: 634631
- * updating to ppl 0.11 (headers are from Fedora's package, no real explanation why they are needed this way ...)

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.10.2-2mdv2011.0
+ Revision: 607200
- rebuild

* Tue Feb 09 2010 Funda Wang <fwang@mandriva.org> 0.10.2-1mdv2010.1
+ Revision: 503055
- fix file list
- fix build with gmp 5.0

* Wed May 20 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.10.2-1mdv2010.0
+ Revision: 377977
- Fix libglpk build require
- Fix Group for the various packages
- import ppl


* Sat Apr 18 2009 Roberto Bagnara <bagnara@cs.unipr.it> 0.10.2-1
- Updated for PPL 0.10.2.

* Tue Apr 14 2009 Roberto Bagnara <bagnara@cs.unipr.it> 0.10.1-1
- Updated for PPL 0.10.1.

* Sun Mar 29 2009 Roberto Bagnara <bagnara@cs.unipr.it> 0.10-11
- Moved changelogs and PostScript and PDF versions of the GPL to the
  `docs' subpackages. This saves considerable space on the live media.

* Tue Mar 24 2009 Roberto Bagnara <bagnara@cs.unipr.it> 0.10-10
- There are no GNU Prolog packages available on ia64: disable the GNU Prolog
  interface also on those platforms (besides ppc64, s390 and s390x).

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild.

* Wed Feb 18 2009 Roberto Bagnara <bagnara@cs.unipr.it> 0.10-8
- Install the documentation according to the Fedora packaging conventions.

* Wed Feb 17 2009 Karsten Hopp <karsten@redhat.comt> 0.10-7
- There are no GNU Prolog packages available on s390 and s390x: disable
  the GNU Prolog interface also on those platforms (besides ppc64).

* Wed Feb 04 2009 Roberto Bagnara <bagnara@cs.unipr.it> 0.10-6
- Better workaround for the bug affecting PPL 0.10 on big-endian
  architectures.

* Tue Feb 03 2009 Roberto Bagnara <bagnara@cs.unipr.it> 0.10-5
- Work around the bug affecting PPL 0.10 on big-endian architectures.

* Fri Dec 05 2008 Roberto Bagnara <bagnara@cs.unipr.it> 0.10-4
- Added `%%dir %%{_datadir}/doc/pwl' to the `%%files' section
  of the `ppl-pwl' package.

* Thu Nov 04 2008 Roberto Bagnara <bagnara@cs.unipr.it> 0.10-3
- Fixed the requirements of the `ppl-java' package.

* Thu Nov 04 2008 Roberto Bagnara <bagnara@cs.unipr.it> 0.10-2
- Added m4 >= 1.4.8 to build requirements.

* Thu Nov 04 2008 Roberto Bagnara <bagnara@cs.unipr.it> 0.10-1
- Updated and extended for PPL 0.10.  In particular, the `ppl-config'
  program, being useful also for non-development activities, has been
  brought back to the main package.

* Tue Sep 30 2008 Roberto Bagnara <bagnara@cs.unipr.it> 0.9-25
- The `swiprolog' package now requires pl >= 5.6.57-2.

* Mon Sep 08 2008 Roberto Bagnara <bagnara@cs.unipr.it> 0.9-24
- Changed ppl-0.9-swiprolog.patch so as to invoke `plld' with
  the `-v' option.

* Mon Sep 08 2008 Roberto Bagnara <bagnara@cs.unipr.it> 0.9-23
- Fixed ppl-0.9-swiprolog.patch.

* Mon Sep 08 2008 Roberto Bagnara <bagnara@cs.unipr.it> 0.9-22
- Implemented a workaround to cope with the new location of SWI-Prolog.h.

* Mon Sep 08 2008 Roberto Bagnara <bagnara@cs.unipr.it> 0.9-21
- Fixed the SWI-Prolog interface dependencies.

* Mon May 19 2008 Roberto Bagnara <bagnara@cs.unipr.it> 0.9-20
- Added Requires /sbin/ldconfig.

* Wed Feb 13 2008 Roberto Bagnara <bagnara@cs.unipr.it> 0.9-19
- Include a patch to supply a missing inclusions of <cstdlib>.

* Wed Jan 09 2008 Roberto Bagnara <bagnara@cs.unipr.it> 0.9-18
- Avoid multiarch conflicts when installed for multiple architectures.

* Sun Dec 23 2007 Roberto Bagnara <bagnara@cs.unipr.it> 0.9-17
- The SWI-Prolog `pl' package is temporarily not available on the ppc64
  architecture: temporarily disabled `ppl-swiprolog' and
  `ppl-swiprolog-static' on that architecture.

* Sat Sep 29 2007 Roberto Bagnara <bagnara@cs.unipr.it> 0.9-16
- The value of the `License' tag is now `GPLv2+'.
- `ppl-swiprolog' dependency on `readline-devel' removed (again).

* Mon Sep 24 2007 Jesse Keating <jkeating@redhat.com> 0.9-15
- Rebuild for new libgmpxx.

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> 0.9-14
- Rebuild for selinux ppc32 issue.

* Fri Jul 06 2007 Roberto Bagnara <bagnara@cs.unipr.it> 0.9-13
- Bug 246815 had been fixed: YAP support enabled again.

* Thu Jul 05 2007 Roberto Bagnara <bagnara@cs.unipr.it> 0.9-12
- Disable YAP support until bug 246815 is fixed.
- Bug 243084 has been fixed: `ppl-swiprolog' dependency on `readline-devel'
  removed.

* Thu Jul 05 2007 Roberto Bagnara <bagnara@cs.unipr.it> 0.9-11
- The `gprolog' package is not available on the ppc64 architecture:
  so do `ppl-gprolog' and `ppl-gprolog-static'.

* Tue Jul 03 2007 Roberto Bagnara <bagnara@cs.unipr.it> 0.9-10
- Use `%%{buildroot}' consistently, instead of  `$RPM_BUILD_ROOT'.

* Mon Jul 02 2007 Roberto Bagnara <bagnara@cs.unipr.it> 0.9-9
- Patch NEWS, TODO and doc/definitions.dox so as to use the
  UTF-8 encoding instead of ISO-8859.

* Tue Jun 12 2007 Roberto Bagnara <bagnara@cs.unipr.it> 0.9-8
- Patch the `libtool' script after `%%configure' so as to fix
  the rpath issue.
- Revised the description of the `devel' package.
- Include also the `TODO' file in the documentation of the main package.

* Thu Jun 07 2007 Roberto Bagnara <bagnara@cs.unipr.it> 0.9-7
- `%%install' commands revised.

* Thu Jun 07 2007 Roberto Bagnara <bagnara@cs.unipr.it> 0.9-6
- All the static archives are now in `*-static' packages.
- Packages `ppl-gprolog-devel', `ppl-swiprolog-devel' and `ppl-yap-devel'
  renamed `ppl-gprolog', `ppl-swiprolog' and `ppl-yap',
  respectively.
- As a workaround for a bug in the `pl' package (Bugzilla Bug 243084),
  `ppl-swiprolog' is now dependent on `readline-devel'.
- Added `%%dir %%{_datadir}/doc/%%{name}'.
- The `ppl-user-0.9-html' documentation directory is now properly listed.
- Remove installed *.la files.
- Added a `ppl-0.9-configure.patch' to avoid overriding CFLAGS and CXXFLAGS.

* Wed Jun 06 2007 Roberto Bagnara <bagnara@cs.unipr.it> 0.9-5
- Use `%%{_includedir}' and `%%{_libdir}' instead of `/usr/include'
  and `/usr/lib', respectively.
- Use `%%{_datadir}/doc/%%{name}' instead of `/usr/share/doc/ppl'.
- Replaced `%%defattr(-,root,root)' with `%%defattr(-,root,root,-)'.

* Fri Feb 23 2007 Roberto Bagnara <bagnara@cs.unipr.it> 0.9-4
- The user manual (in various formats) is now in the `docs' package.

* Thu Feb 22 2007 Roberto Bagnara <bagnara@cs.unipr.it> 0.9-3
- Dependencies for YAP fixed.
- Make sure the header files of GNU Prolog and YAP are found.

* Wed Feb 21 2007 Roberto Bagnara <bagnara@cs.unipr.it>
- Added missing dependencies.

* Sun Feb 18 2007 Roberto Bagnara <bagnara@cs.unipr.it>
- `%%doc' tags corrected for the Prolog interfaces.
- Tabs used consistently instead of spaces.

* Sat Feb 17 2007 Roberto Bagnara <bagnara@cs.unipr.it>
- Make `swiprolog-devel' depend on `pl' (at leat 5.6); documentation added.
- The `yap' package has been renamed `yap-devel' and completed.
- The `gprolog' package has been renamed `gprolog-devel' and completed.
- The `ppl_lcdd' and `ppl_lpsol' programs are now in a new `utils' package.
- The `ppl-config' program is now in the `devel' package.
- Modified the configuration command so that the `glpk-devel' include files
  are found.

* Sun Feb 11 2007 Roberto Bagnara <bagnara@cs.unipr.it> 0.9-2
- The `%%_libdir/ppl' is no longer orphaned.
- Use `make %%{?_smp_mflags}' for building.
- The `swi' package has been renamed `swiprolog-devel'.

* Sat Feb 10 2007 Roberto Bagnara <bagnara@cs.unipr.it>
- Added the `%%changelog' section.
- `Release' set to 2.
- `Packager' and `Vendor' tags removed.
- `Summary' fields are no longer ended with a dot.
- The value of the `License' tag is now `GPL'.
- Removed unused definition of `builddir'.
- The `Name', `Version' and `Release' tags are now directly defined.
- Commented out the efinitions of the `Require' and `Prefix' tags.
- Set the `BuildRequires' tag to `gmp-devel'.
- Exploit the features of `%%setup', `%%configure', `%%install',
  `%%post' and `%%postun'.
- Mixed use of spaces and tabs avoided.
- Do configure with the --disable-rpath option so as to avoid
  hardcoding the path to search libraries.
- Do not include libtool archive files.
- Packages reorganized.

* Mon Jan 16 2006 Roberto Bagnara <bagnara@cs.unipr.it> 0.9-1
- Install gzipped man pages.
- The `Copyright' tag is no longer supported: use `License' instead.

* Wed Jan 11 2006 Roberto Bagnara <bagnara@cs.unipr.it>
- Include `ppl-config' in `%%{_bindir}' and the man pages in
  `%%{_mandir}/man1'.

* Tue Jan 10 2006 Roberto Bagnara <bagnara@cs.unipr.it>
- Require gcc-c++ to be at least 4.0.2.
- Distribute also `ppl_lpsol'.

* Tue Mar 01 2005 Roberto Bagnara <bagnara@cs.unipr.it>
- Wrong dependency fixed.

* Mon Feb 28 2005 Roberto Bagnara <bagnara@cs.unipr.it>
- URL for the source fixed.

* Fri Dec 24 2004 Roberto Bagnara <bagnara@cs.unipr.it>
- Sentence fixed.

* Thu Dec 23 2004 Roberto Bagnara <bagnara@cs.unipr.it>
- The file doc/README has been renamed README.doc so as not to conflict
  with the library's main README file.
- Require gcc-c++ to be exactly version 3.4.1.
- `Summary' updated to reflect the fact that the library now provides
  numerical abstractions other than convex polyhedra.

* Wed Aug 18 2004 Roberto Bagnara <bagnara@cs.unipr.it>
- Distribute more documentation.

* Mon Aug 16 2004 Roberto Bagnara <bagnara@cs.unipr.it>
- Added the `ppl_lcdd' program to the main package.
- Require gcc-c++ to be exactly version 3.4.1.
- We require gmp at least 4.1.3.

* Wed Jul 30 2003 Roberto Bagnara <bagnara@cs.unipr.it>
- Build an RPM package also for the PWL.
- The Prolog interfaces depend on the PWL.

* Tue Mar 04 2003 Roberto Bagnara <bagnara@cs.unipr.it>
- We require gmp at least 4.1.2.

* Fri Oct 04 2002 Roberto Bagnara <bagnara@cs.unipr.it>
- Require gcc-c++ 3.2 or later version.
- Require gmp 4.1 or later version.

* Sun Jun 30 2002 Roberto Bagnara <bagnara@cs.unipr.it>
- Mention not necessarily closed convex polyhedra in the main `%%description'.

* Tue Jun 25 2002 Roberto Bagnara <bagnara@cs.unipr.it>
- `%%files' section for gprolog package fixed.

* Mon Jun 24 2002 Roberto Bagnara <bagnara@cs.unipr.it>
- `%%files' section fixed for the yap package.
- The `%%files' sections of each package are now complete.

* Wed Jun 12 2002 Roberto Bagnara <bagnara@cs.unipr.it>
- Added file list for package gprolog.
- Updated file list for package swi.

* Thu Jun 06 2002 Roberto Bagnara <bagnara@cs.unipr.it>
- The `swi' package has now its `%%files' section.

* Wed Jun 05 2002 Roberto Bagnara <bagnara@cs.unipr.it>
- We will build several RPM packages out of our source tree.

* Mon Mar 04 2002 Roberto Bagnara <bagnara@cs.unipr.it>
- Require gcc-c++ 3.0.4 or later version.
- Require gmp 4.0.1 or later version.

* Sun Jan 27 2002 Roberto Bagnara <bagnara@cs.unipr.it>
- The move to libtool is complete: we can now build and distribute
  (with, e.g., RPM) static and dynamic versions of the library.

* Tue Oct 16 2001 Roberto Bagnara <bagnara@cs.unipr.it>
- Changed `Summary'.
- Changed `Packager' in view of PGP signatures.
- Changed `Group' to `Development/Libraries'.
- Require gcc-c++ 2.96-85 or later version.

* Mon Oct 15 2001 Roberto Bagnara <bagnara@cs.unipr.it>
- Now we build a relocatable package.

* Mon Oct 15 2001 Roberto Bagnara <bagnara@cs.unipr.it>
- A first cut at a working RPM spec file.

