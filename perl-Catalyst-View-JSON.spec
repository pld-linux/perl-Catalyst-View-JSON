#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	View-JSON
Summary:	Catalyst::View::JSON - JSON view for your data
Summary(pl.UTF-8):	Catalyst::View::JSON - widok danych w formacie JSON
Name:		perl-Catalyst-View-JSON
Version:	0.26
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	01f792cc9d09eb1f258504b391fffe63
URL:		http://search.cpan.org/dist/Catalyst-View-JSON/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Catalyst >= 5.6
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.42
BuildRequires:	perl-JSON-Any >= 1.15
BuildRequires:	perl-MRO-Compat
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Catalyst::View::JSON is a Catalyst View handler that returns stash
data in JSON format.

%description -l pl.UTF-8
Catalyst::View::JSON jest uchwytem Catalyst View który zwraca zasoby
danych w formacie JSON.

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
%doc Changes
%{perl_vendorlib}/Catalyst/View/*.pm
%{perl_vendorlib}/Catalyst/Helper/View/*.pm
%{_mandir}/man3/*
