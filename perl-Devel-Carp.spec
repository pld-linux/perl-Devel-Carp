%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	Carp
Summary:	Devel::Carp -- miscleanous error handling functions
Summary(pl):	Devel::Carp -- ró¿ne funkcje do obs³ugi b³êdów
Name:		perl-Devel-Carp
Version:	0.04
Release:	10
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprov	"perl(Carp)"

%description
The Carp routines are useful in your own modules because they act like
die() or warn(), but report where the error was in the code they were
called from.  Thus if you have a routine Foo() that has a carp() in it,
then the carp() will report the error as occurring where Foo() was called,
not where carp() was called.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_sitelib}/Devel/Carp.pm
%{_mandir}/man3/*
