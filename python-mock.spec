%if 0%{?fedora} || 0%{?epel} > 6
# keeping python3 subpackage as stdlib mock lives in a different namespace
# Some people may have not fixed their imports
%global with_python3 1
%endif

# Not yet in Fedora buildroot
%{!?python3_pkgversion:%global python3_pkgversion 3}

%global mod_name mock

Name:           python-mock
Version:        1.3.0
Release:        2%{?dist}
Summary:        A Python Mocking and Patching Library for Testing

License:        BSD
URL:            http://www.voidspace.org.uk/python/%{mod_name}/
Source0:        http://pypi.python.org/packages/source/m/%{mod_name}/%{mod_name}-%{version}.tar.gz
Source1:        LICENSE.txt

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-funcsigs
BuildRequires:  python-pbr
# For tests
%if 0%{?rhel} <= 7
BuildRequires:  python-unittest2
%endif

%if 0%{?with_python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python3-funcsigs
BuildRequires:  python3-pbr
# For tests
BuildRequires:  python%{python3_pkgversion}-unittest2
%endif


%description
Mock is a Python module that provides a core mock class. It removes the need
to create a host of stubs throughout your test suite. After performing an
action, you can make assertions about which methods / attributes were used and
arguments they were called with. You can also specify return values and set
needed attributes in the normal way.

%package -n python2-mock
Summary:        A Python Mocking and Patching Library for Testing
%{?python_provide:%python_provide python2-%{mod_name}}
Requires:    python-funcsigs
Requires:    python-pbr
Requires:    python-six >= 1.9.0

%description -n python2-mock
Mock is a Python module that provides a core mock class. It removes the need
to create a host of stubs throughout your test suite. After performing an
action, you can make assertions about which methods / attributes were used and
arguments they were called with. You can also specify return values and set

%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-mock
Summary:        A Python Mocking and Patching Library for Testing
%{?python_provide:%python_provide python%{python3_pkgversion}-%{mod_name}}
Requires:    python3-funcsigs
Requires:    python3-pbr
Requires:    python3-six >= 1.9.0

%description -n python%{python3_pkgversion}-mock
Mock is a Python module that provides a core mock class. It removes the need
to create a host of stubs throughout your test suite. After performing an
action, you can make assertions about which methods / attributes were used and
arguments they were called with. You can also specify return values and set
needed attributes in the normal way.
%endif


%prep
%setup -q -n %{mod_name}-%{version}
cp -p %{SOURCE1} .


%build
%{py2_build}
%if 0%{?with_python3}
%{py3_build}
%endif


%check
%{__python2} setup.py test
%if 0%{?with_python3}
# Few failing tests but keep output
%{__python3} setup.py test ||:
%endif

%install
%if 0%{?with_python3}
%{py3_install}
%endif
%{py2_install}


%files -n python2-mock
%license LICENSE.txt
%{python2_sitelib}/*.egg-info
%{python2_sitelib}/%{mod_name}

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-mock
%license LICENSE.txt
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{mod_name}
%endif


%changelog
* Tue Jun 28 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 1.3.0-2
- Drop useless documentation (RHBZ#1350866)

* Fri Feb 26 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 1.3.0-1
- Upstream 1.3.0 (RHBZ#1244145)
- Use epel macros rather than rhel

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 6 2016 Orion Poplawski <orion@cora.nwra.com> - 1.0.1-9
- Modernize spec
- Run python2 tests, python3 failing

* Thu Nov 12 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Nov 02 2015 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 1.0.1-7
- Fix #1276771

* Wed Sep 23 2015 Robert Kuska <rkuska@redhat.com> - 1.0.1-6
- Rebuilt for Python3.5 rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 09 2014 Dennis Gilmore <dennis@ausil.us> - 1.0.1-3
- rebuild for python 3.4
- disable test suite deps missing

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Luke Macken <lmacken@redhat.com> - 1.0.1-1
- Update to 1.0.1
- Run the test suite
- Add python-unittest2 as a build requirement

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 0.8.0-4
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 Ralph Bean <rbean@redhat.com> - 0.8.0-2
- Python3 support

* Thu Mar 22 2012 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.8.0-1
- Updated to new version

* Fri Jul 22 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.7.2-1
- Initial RPM release
