%include	/usr/lib/rpm/macros.perl
%define		__find_provides %{_builddir}/Devel-Carp-%{version}/find-perl-provides
Summary:	Devel-Carp perl module
Summary(pl):	Modu³ perla Devel-Carp
Name:		perl-Devel-Carp
Version:	0.04
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Devel/Devel-Carp-%{version}.tar.gz
Patch:		perl-Devel-Carp-dep.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
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
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Devel/Carp
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz

%{perl_sitelib}/Devel/Carp.pm
%{perl_sitearch}/auto/Devel/Carp

%{_mandir}/man3/*
