Summary:	NVIDIA Cg Compiler
Summary(pl):	Kompilator Cg NVIDII
Name:		cg
Version:	1.2.1
Release:	1
License:	nVidia
Group:		Development
Source0:	ftp://download.nvidia.com/developer/cg/Cg_%{version}/Linux/Cg-%{version}-Linux.tar.gz
# http://developer.nvidia.com/attach/6488
Source1:	LinuxSDK.zip
URL:		http://developer.nvidia.com/Cg
BuildRequires:	unzip
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The NVIDIA Cg Toolkit is the best way to take advantage of today's
GPUs across multiple platforms and APIs. Now supporting OpenGL's
ARB_vertex_program and ARB_fragment_program extensions, the compiler
allows developers to create advanced visual effects for today's
programmable GPUs from NVIDIA and other vendors.

%description -l pl
Zestaw narzêdzi Cg NVIDII jest nalepszym sposobem wykorzystywania
dzisiejszych procesorów graficznych na wielu ró¿nych platformach.
Dziêki wsparciu rozszerzeñ OpenGL-a ARB_vertex_program i
ARB_fragment_program, kompilator pozwala developerom tworzyæ
zaawansowane efekty wizualne na programowalne uk³ady graficzne NVIDII
i innych producentów.

%prep
%setup -q -c
unzip %{SOURCE1}

rm -rf usr/local/Cg/docs/runtime/cgGL/txt

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man3,%{_includedir}/Cg{,FX},%{_libdir},%{_examplesdir}/%{name}-%{version}}

install usr/bin/* $RPM_BUILD_ROOT%{_bindir}
install usr/include/Cg/* $RPM_BUILD_ROOT%{_includedir}/Cg
install usr/include/CgFX/* $RPM_BUILD_ROOT%{_includedir}/CgFX
install usr/lib/* $RPM_BUILD_ROOT%{_libdir}
install usr/share/man/man3/* $RPM_BUILD_ROOT%{_mandir}/man3

cp -r usr/local/Cg/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc usr/local/Cg/{README,docs/{*.pdf,runtime/{html,cgGL}}}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*
%{_mandir}/man3/*
%{_includedir}/*
%{_examplesdir}/*
