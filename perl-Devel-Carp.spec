%include	/usr/lib/rpm/macros.perl
%define		__find_provides %{_builddir}/Devel-Carp-%{version}/find-perl-provides
Summary:	Devel-Carp perl module
Summary(pl):	Modu³ perla Devel-Carp
Name:		perl-Devel-Carp
Version:	0.04
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Devel/Devel-Carp-%{version}.tar.gz
Patch0:		%{name}-dep.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel-Carp perl module.

%description -l pl
Modu³ perla Devel-Carp.

%prep
%setup -q -n Devel-Carp-%{version}
%patch -p1

chmod +x find-perl-provides

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
