Summary: Documentation for configuring system services
Name: system-config-services-docs
Version: 1.1.9
Release: %mkrel 1
URL: https://fedorahosted.org/%{name}
Source0: http://fedorahosted.org/released/%{name}/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: Books/Howtos
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: gettext
BuildRequires: pkgconfig
BuildRequires: gnome-doc-utils
BuildRequires: rarian
BuildRequires: docbook-dtd45-xml
Requires: system-config-services
Requires: yelp
Requires: rarian

%description
This package contains the online documentation for system-config-services is a
utility which allows you to configure which services should be enabled on your
machine.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%buildroot install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING
%doc %{_datadir}/omf/system-config-services
%doc %{_datadir}/gnome/help/system-config-services
