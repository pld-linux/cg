# TODO:
#  - link libCg.so with -lm and -lpthread

Summary:	NVIDIA Cg Compiler
Summary(pl.UTF-8):	Kompilator Cg NVIDII
Name:		cg
Version:	1.5.0
Release:	1
License:	nVidia
Group:		Development
Source0:	http://developer.download.nvidia.com/cg/Cg_1.5/%{version}/0019/Cg-1.5_Feb2007_x86.tar.gz
# Source0-md5:	36bc6b9916a82ea70fa638adf1d99ed0
Source1:	http://developer.download.nvidia.com/cg/Cg_1.5/%{version}/0019/Cg-1.5_Feb2007_x86_64.tar.gz
# Source1-md5:	4e56dce89adee688817e4337232161e0
URL:		http://developer.nvidia.com/object/cg_toolkit.html
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The NVIDIA Cg Toolkit is the best way to take advantage of today's
GPUs across multiple platforms and APIs. Now supporting OpenGL's
ARB_vertex_program and ARB_fragment_program extensions, the compiler
allows developers to create advanced visual effects for today's
programmable GPUs from NVIDIA and other vendors.

%description -l pl.UTF-8
Zestaw narzędzi Cg NVIDII jest najlepszym sposobem wykorzystywania
dzisiejszych procesorów graficznych na wielu różnych platformach.
Dzięki wsparciu rozszerzeń OpenGL-a ARB_vertex_program i
ARB_fragment_program, kompilator pozwala developerom tworzyć
zaawansowane efekty wizualne na programowalne układy graficzne NVIDII
i innych producentów.

%package devel
Summary:	Header files for Cg library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Cg
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
# for cgGL
#Requires:	OpenGL-devel

%description devel
This is the package containing the header files for Cg library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki Cg.

%package examples
Summary:	Cg examples
Summary(pl.UTF-8):	Przykłady dla Cg
Group:		Applications

%description examples
Cg examples.

%description examples -l pl.UTF-8
Przykłady dla Cg.

%prep
%ifarch %{ix86}
%setup -q -c
%endif
%ifarch %{x8664}
%setup -q -c -T -a 1
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man3,%{_includedir}/Cg,%{_libdir},%{_examplesdir}/%{name}-%{version}}

install usr/bin/* $RPM_BUILD_ROOT%{_bindir}
install usr/include/Cg/* $RPM_BUILD_ROOT%{_includedir}/Cg
install usr/%{_lib}/* $RPM_BUILD_ROOT%{_libdir}
install usr/share/man/man3/* $RPM_BUILD_ROOT%{_mandir}/man3

cp -r usr/local/Cg/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc usr/local/Cg/{README,docs/{*.pdf,html/*.html,txt/{cg,cgGL,profiles,stdlib}}}
%attr(755,root,root) %{_bindir}/cgc
%attr(755,root,root) %{_libdir}/libCg.so
%attr(755,root,root) %{_libdir}/libCgGL.so
%{_mandir}/man3/cg*.3*

%files devel
%defattr(644,root,root,755)
%{_includedir}/Cg

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
