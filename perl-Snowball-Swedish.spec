%define upstream_name	 Snowball-Swedish
%define upstream_version 1.2

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Porters stemming algorithm for Swedish
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/A/AS/ASKSH/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

Requires:	locales-sv
%rename	perl-Lingua-Stem-Snowball-Se

%description
The stem function takes a scalar as a parameter and stems the word according to
Martin Porters Swedish stemming algorithm, which can be found at the Snowball
website: http://snowball.tartarus.org/.

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
%doc Changes README
%{perl_vendorlib}/Lingua
%{_bindir}/stemmer-se.pl
%{_mandir}/man3*/*


%changelog
* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.200.0-1mdv2010.1
+ Revision: 505282
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.2-4mdv2010.0
+ Revision: 430539
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.2-3mdv2009.0
+ Revision: 241857
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.2-1mdv2008.0
+ Revision: 56111
- new version


* Fri Dec 01 2006 Oden Eriksson <oeriksson@mandriva.com> 1.01-3mdv2007.0
+ Revision: 89753
- Import perl-Snowball-Swedish

* Wed Nov 30 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-3mdk
- changed name
- spec cleanup
- fix directory ownership
- %%mkrel
- rpmbuildupdate aware
- better summary
- better description
- better url

* Sat Oct 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.01-2mdk
- fix deps

