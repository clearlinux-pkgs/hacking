#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC36CDCB4DF00C68C (infra-root@openstack.org)
#
Name     : hacking
Version  : 1.1.0
Release  : 37
URL      : http://tarballs.openstack.org/hacking/hacking-1.1.0.tar.gz
Source0  : http://tarballs.openstack.org/hacking/hacking-1.1.0.tar.gz
Source99 : http://tarballs.openstack.org/hacking/hacking-1.1.0.tar.gz.asc
Summary  : OpenStack Hacking Guideline Enforcement
Group    : Development/Tools
License  : Apache-2.0
Requires: hacking-license = %{version}-%{release}
Requires: hacking-python = %{version}-%{release}
Requires: hacking-python3 = %{version}-%{release}
Requires: flake8
Requires: flake8-docstrings
Requires: pbr
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv
Patch1: reqs.patch

%description
============

%package license
Summary: license components for the hacking package.
Group: Default

%description license
license components for the hacking package.


%package python
Summary: python components for the hacking package.
Group: Default
Requires: hacking-python3 = %{version}-%{release}

%description python
python components for the hacking package.


%package python3
Summary: python3 components for the hacking package.
Group: Default
Requires: python3-core

%description python3
python3 components for the hacking package.


%prep
%setup -q -n hacking-1.1.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541266449
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/hacking
cp LICENSE %{buildroot}/usr/share/package-licenses/hacking/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/hacking/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
