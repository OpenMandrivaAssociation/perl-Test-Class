%define upstream_name    Test-Class
%define upstream_version 0.36

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Write Perl test suites in xUnit style
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.xz

BuildRequires:	perl-devel
BuildRequires:	perl(Attribute::Handlers)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(Storable)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Simple)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
Test::Class provides a simple way of creating classes and objects to test
your code in an xUnit style.

Built using the Test::Builder manpage, it was designed to work with other
Test::Builder based modules (the Test::More manpage, the Test::Differences
manpage, the Test::Exception manpage, etc.).

_Note:_ This module will make more sense, if you are already familiar with
the "standard" mechanisms for testing perl code. Those unfamiliar with the
Test::Harness manpage, the Test::Simple manpage, the Test::More manpage and
friends should go take a look at them now. the Test::Tutorial manpage is a
good starting point.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.360.0-3mdv2011.0
+ Revision: 656969
- rebuild for updated spec-helper

* Fri Dec 03 2010 Shlomi Fish <shlomif@mandriva.org> 0.360.0-2mdv2011.0
+ Revision: 606907
- Removed the dot at the end of the summary
- import perl-Test-Class

