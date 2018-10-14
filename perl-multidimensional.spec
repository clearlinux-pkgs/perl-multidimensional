#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-multidimensional
Version  : 0.014
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/I/IL/ILMARI/multidimensional-0.014.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/I/IL/ILMARI/multidimensional-0.014.tar.gz
Summary  : 'disables multidimensional array emulation'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-multidimensional-lib = %{version}-%{release}
Requires: perl-multidimensional-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(B::Hooks::OP::Check::Install::Files)
BuildRequires : perl(ExtUtils::Depends)

%description
NAME
multidimensional - disables multidimensional array emulation
VERSION
version 0.014

%package dev
Summary: dev components for the perl-multidimensional package.
Group: Development
Requires: perl-multidimensional-lib = %{version}-%{release}
Provides: perl-multidimensional-devel = %{version}-%{release}

%description dev
dev components for the perl-multidimensional package.


%package lib
Summary: lib components for the perl-multidimensional package.
Group: Libraries
Requires: perl-multidimensional-license = %{version}-%{release}

%description lib
lib components for the perl-multidimensional package.


%package license
Summary: license components for the perl-multidimensional package.
Group: Default

%description license
license components for the perl-multidimensional package.


%prep
%setup -q -n multidimensional-0.014

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-multidimensional
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-multidimensional/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.26.1/x86_64-linux-thread-multi/multidimensional.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/multidimensional.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.26.1/x86_64-linux-thread-multi/auto/multidimensional/multidimensional.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-multidimensional/LICENSE
