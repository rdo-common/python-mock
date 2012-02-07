%global mod_name mock

Name:           python-mock
Version:        0.7.2
Release:        1%{?dist}
Summary:        A Python Mocking and Patching Library for Testing

Group:          Development/Libraries
License:        BSD
URL:            http://www.voidspace.org.uk/python/%{mod_name}/
Source0:        http://pypi.python.org/packages/source/m/%{mod_name}/%{mod_name}-%{version}.tar.gz
Source1:        LICENSE.txt

BuildArch:      noarch
BuildRequires:  python-devel

%description
Mock is a Python module that provides a core mock class. It removes the need
to create a host of stubs throughout your test suite. After performing an
action, you can make assertions about which methods / attributes were used and
arguments they were called with. You can also specify return values and set
needed attributes in the normal way.


%prep
%setup -q -n %{mod_name}-%{version}
cp -p %{SOURCE1} .

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%files
%doc docs/ README.txt PKG-INFO LICENSE.txt
%{python_sitelib}/*.egg-info
%{python_sitelib}/%{mod_name}.py*


%changelog
* Fri Jul 22 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.7.2-1
- Initial RPM release
