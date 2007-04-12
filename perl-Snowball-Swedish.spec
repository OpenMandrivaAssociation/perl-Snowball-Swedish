%define module	Snowball-Swedish
%define name	perl-%{module}
%define version 1.01
%define release %mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Porters stemming algorithm for Swedish
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/A/AS/ASKSH/%{module}-%{version}.tar.bz2
Url:            http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
Requires:	locales-sv
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}
Obsoletes:	perl-Lingua-Stem-Snowball-Se
Provides:	perl-Lingua-Stem-Snowball-Se

%description
The stem function takes a scalar as a parameter and stems the word according to
Martin Porters Swedish stemming algorithm, which can be found at the Snowball
website: http://snowball.tartarus.org/.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot} 
%makeinstall_std

mv %{buildroot}%{perl_vendorlib}/Lingua/Stem/Snowball/stemmer.pl \
    %{buildroot}%{perl_vendorlib}/Lingua/Stem/Snowball/stemmer-Se.pl

%clean 
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Lingua
%{_mandir}/man3*/*


