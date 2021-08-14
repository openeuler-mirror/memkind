Name:                memkind
Summary:             Extensible Heap Manager for User
Version:             1.7.0
Release:             5
License:             BSD
URL:                 http://memkind.github.io/memkind
Source0:             https://github.com/memkind/memkind/archive/v1.7.0/%{name}-%{version}.tar.gz
Patch0001:           0001-fix-multi-define.patch

BuildRequires:       automake libtool numactl-devel systemd gcc gcc-c++
ExclusiveArch:       x86_64

%description
The kinds of memory are defined by operating system memory policies that have been applied
to virtual address ranges.Memory characteristics supported by memkind without user extension
include control of NUMA and page size features.

%package devel
Summary:             Development lib and tools for Memkind User Extensible Heap Manager
Requires:            %{name} = %{version}-%{release}

%description devel
Development lib and tools for Memkind User Extensible Heap Manager.

%package help
Summary:             Help documents for memkind

%description help
Help documents for memkind.

%prep
%autosetup -a 0 -n %{name}-%{version} -p1

%build
pushd %{_builddir}/memkind-1.7.0
echo 1.7.0 > %{_builddir}/memkind-1.7.0/VERSION
./build.sh --prefix=%{_prefix} --includedir=%{_includedir} --libdir=%{_libdir} \
           --bindir=%{_bindir} --docdir=%{_docdir}/memkind --mandir=%{_mandir} \
           --sbindir=%{_sbindir}
popd

%install
pushd %{_builddir}/memkind-1.7.0
%make_install
popd

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%{_libdir}/libmemkind.so.*
%{_libdir}/libautohbw.so.*
%{_bindir}/memkind-hbw-nodes
%dir %{_docdir}/memkind
%doc %{_docdir}/memkind/COPYING

%files devel
%dir %{_includedir}/memkind
%dir %{_includedir}/memkind/internal/
%{_includedir}/memkind/internal/*.h
%{_includedir}/memkind*.h
%{_includedir}/hbwmalloc.h
%{_includedir}/hbw_allocator.h
%{_libdir}/libmemkind.so
%{_libdir}/libautohbw.so
%exclude %{_libdir}/libmemkind.{l,}a
%exclude %{_libdir}/libautohbw.{l,}a
%exclude %{_docdir}/memkind/VERSION

%files help
%doc %{_docdir}/memkind/README
%{_mandir}/man3/*

%changelog
* Wed Aug 2 2021  luweitao <luweitaobe@163.com> - 2.7.1-12
- fix compile failure by GCC-10

* Thu Apr 23 2020 leiju <leiju4@huawei.com> - 1.7.0-4
- Package init
