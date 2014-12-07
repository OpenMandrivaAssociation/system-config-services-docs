Summary:	Documentation for configuring system services
Name:		system-config-services-docs
Version:	1.1.9
Release:	9
URL:		https://fedorahosted.org/%{name}
Source0:	http://fedorahosted.org/released/%{name}/%{name}-%{version}.tar.bz2
License:	GPLv2+
Group:		Books/Howtos
BuildRequires: gettext
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	rarian
BuildRequires:	docbook-dtd45-xml
Requires:	system-config-services
Requires:	yelp
Requires:	rarian
BuildArch:	noarch

%description
This package contains the online documentation for system-config-services is a
utility which allows you to configure which services should be enabled on your
machine.

%prep
%setup -q

%build
%make

%install
%makeinstall_std

%files
%doc COPYING
%doc %{_datadir}/omf/system-config-services
%doc %{_datadir}/gnome/help/system-config-services


%changelog
* Thu Aug 11 2011 Александр Казанцев <kazancas@mandriva.org> 1.1.9-1mdv2011.0
+ Revision: 694031
- imported package system-config-services-docs

