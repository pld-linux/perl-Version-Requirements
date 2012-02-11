#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Version
%define		pnam	Requirements
%include	/usr/lib/rpm/macros.perl
Summary:	Version::Requirements - a set of version requirements for a CPAN dist
Summary(pl.UTF-8):	Version::Requirements - zbiór wersjonowanych wymagań dla dystrybucji CPAN
Name:		perl-Version-Requirements
Version:	0.101022
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/R/RJ/RJBS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	74e8a660969e30ffbb64999806c0769c
URL:		http://search.cpan.org/dist/Version-Requirements/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.31
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Scalar-List-Utils
BuildRequires:	perl-Test-Simple >= 0.88
BuildRequires:	perl-version >= 0.77
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

%description -l pl.UTF-8
Obiekt Version::Requirements modeluje zbiór wersjonowanych wymagań,
jak te podawane w plikach META.yml lub META.json w dystrybucjach CPAN.
Może być tworzony w oparciu o dodawanie kolejnych ograniczeń, a on
zredukuje je do najprostszej postaci.

Logicznie wykluczające się ograniczenia są natychmiast zgłaszane przez
rzucenie wyjątku.

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
%{perl_vendorlib}/Version/Requirements.pm
%{_mandir}/man3/Version::Requirements.3pm*
