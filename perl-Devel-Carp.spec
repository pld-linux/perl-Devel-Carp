%define		pdir	Devel
%define		pnam	Carp
Summary:	Devel::Carp - miscleanous error handling functions
Summary(pl.UTF-8):	Devel::Carp - różne funkcje do obsługi błędów
Name:		perl-Devel-Carp
Version:	0.04
Release:	15
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e5377daa28ee1981dcbc2a074bf7a6ef
URL:		http://search.cpan.org/dist/Devel-Carp/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprov	'perl(Carp)'

%description
The Carp routines are useful in your own modules because they act like
die() or warn(), but report where the error was in the code they were
called from. Thus if you have a routine Foo() that has a carp() in it,
then the carp() will report the error as occurring where Foo() was
called, not where carp() was called.

%description -l pl.UTF-8
Funkcje Carp są przydatne we własnych modułach, ponieważ zachowują się
jak die() i warn(), ale zgłaszają, że błąd wystąpił w kodzie, z
którego zostały wywołane. W ten sposób, jeśli jest funkcja Foo(),
która zawiera carp(), to carp() zgłosi błąd jako występujący w
miejscu, z którego została wywołana funkcja Foo(), a nie carp().

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Devel/Carp.pm
%{_mandir}/man3/*
