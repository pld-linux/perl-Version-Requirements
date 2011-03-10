#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Version
%define		pnam	Requirements
%include	/usr/lib/rpm/macros.perl
Summary:	Version::Requirements - a set of version requirements for a CPAN dist
Name:		perl-Version-Requirements
Version:	0.101020
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/R/RJ/RJBS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e50725d564c0e287d54b08d4d809a26f
URL:		http://search.cpan.org/dist/Version-Requirements/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Version::Requirements object models a set of version constraints
like those specified in the META.yml or META.json files in CPAN
distributions. It can be built up by adding more and more constraints,
and it will reduce them to the simplest representation.

Logically impossible constraints will be identified immediately by
thrown exceptions.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Version
%{perl_vendorlib}/Version/*.pm
%{_mandir}/man3/*
