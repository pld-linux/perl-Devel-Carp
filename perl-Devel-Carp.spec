%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	Carp
Summary:	Devel::Carp -- miscleanous error handling functions
Summary(pl):	Devel::Carp -- ró¿ne funkcje do obs³ugi b³êdów
Name:		perl-Devel-Carp
Version:	0.04
Release:	12
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprov	"perl(Carp)"

%description
The Carp routines are useful in your own modules because they act like
die() or warn(), but report where the error was in the code they were
called from. Thus if you have a routine Foo() that has a carp() in it,
then the carp() will report the error as occurring where Foo() was
called, not where carp() was called.

%description -l pl
Funkcje Carp s± przydatne we w³asnych modu³ach, poniewa¿ zachowuj± siê
jak die() i warn(), ale zg³aszaj±, ¿e b³±d wyst±pi³ w kodzie, z
którego zosta³y wywo³ane. W ten sposób, je¶li jest funkcja Foo(),
która zawiera carp(), to carp() zg³osi b³±d jako wystêpuj±cy w
miejscu, z którego zosta³a wywo³ana funkcja Foo(), a nie carp().

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Devel/Carp.pm
%{_mandir}/man3/*
