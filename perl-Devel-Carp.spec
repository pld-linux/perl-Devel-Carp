%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	Carp
Summary:	Devel-Carp perl module
Summary(pl):	Modu³ perla Devel-Carp
Name:		perl-Devel-Carp
Version:	0.04
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprov	"perl(Carp)"

%description
Devel-Carp perl module.

%description -l pl
Modu³ perla Devel-Carp.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Devel/Carp.pm
%{_mandir}/man3/*
