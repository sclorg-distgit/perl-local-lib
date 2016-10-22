%{?scl:%scl_package perl-local-lib}

Name:           %{?scl_prefix}perl-local-lib
Version:        2.000019
Release:        3%{?dist}
License:        GPL+ or Artistic
Group:          Development/Libraries
Summary:        Create and use a local lib/ for perl modules
Url:            http://search.cpan.org/dist/local-lib
Source:         http://search.cpan.org/CPAN/authors/id/H/HA/HAARG/local-lib-%{version}.tar.gz
Source10:       perl-homedir.sh
Source11:       perl-homedir.csh
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(CPAN)
BuildRequires:  %{?scl_prefix}perl(CPAN::HandleConfig)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 7.00
BuildRequires:  %{?scl_prefix}perl(File::HomeDir)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Runtime
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Carp::Heavy)
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(File::Basename)
BuildRequires:  %{?scl_prefix}perl(File::Glob)
# Tests only
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(File::Path)
BuildRequires:  %{?scl_prefix}perl(File::Spec::Functions)
BuildRequires:  %{?scl_prefix}perl(File::Temp)
BuildRequires:  %{?scl_prefix}perl(IPC::Open3)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(Test::More)
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Carp)
Requires:       %{?scl_prefix}perl(Carp::Heavy)
Requires:       %{?scl_prefix}perl(File::Basename)
Requires:       %{?scl_prefix}perl(File::Glob)
Requires:       %{?scl_prefix}perl(File::Spec)

%description
This module provides a quick, convenient way of bootstrapping a user-
local Perl module library located within the user's home directory. It
also constructs and prints out for the user the list of environment
variables using the syntax appropriate for the user's current shell (as
specified by the 'SHELL' environment variable), suitable for directly
adding to one's shell configuration file.

More generally, local::lib allows for the bootstrapping and usage of a
directory containing Perl modules outside of Perl's '@INC'. This makes
it easier to ship an application with an app-specific copy of a Perl module,
or collection of modules. Useful in cases like when an upstream maintainer
hasn't applied a patch to a module of theirs that you need for your
application.

%{!?scl:
%package -n %{?scl_prefix}perl-homedir
License:    GPL+ or Artistic
Group:      Development/Libraries
Summary:    Per-user Perl local::lib setup
Requires:   %{name} = %{version}-%{release}
Requires:   sed

%description -n %{?scl_prefix}perl-homedir
perl-homedir configures the system to automatically create a ~/perl5
directory in each user's $HOME on user login.  This allows each user to
install CPAN packages via the CPAN to their $HOME, with no additional
configuration or privileges, and without installing them system-wide.

If you want your users to be able to install and use their own Perl modules,
install this package.
}

%prep
%setup -q -n local-lib-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
%{_fixperms} %{buildroot}/*
%{!?scl:
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -pm0644 %{SOURCE10} %{buildroot}%{_sysconfdir}/profile.d/
install -pm0644 %{SOURCE11} %{buildroot}%{_sysconfdir}/profile.d/
}

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%{!?scl:
%files -n %{?scl_prefix}perl-homedir
%{_sysconfdir}/profile.d/*
}

%changelog
* Tue Jul 19 2016 Petr Pisar <ppisar@redhat.com> - 2.000019-3
- SCL

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.000019-2
- Perl 5.24 rebuild

* Fri Apr 22 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.000019-1
- 2.000019 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.000018-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 02 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.000018-1
- 2.000018 bump

* Tue Oct 06 2015 Petr Šabata <contyk@redhat.com> - 2.000017-1
- 2.000017 bump
- Drop the hard CPAN dependency from perl-homedir

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.000015-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.000015-3
- Perl 5.22 rebuild

* Thu Jan 15 2015 Petr Pisar <ppisar@redhat.com> - 2.000015-2
- Do not hard-code /usr/bin

* Wed Dec 17 2014 Petr Šabata <contyk@redhat.com> - 2.000015-1
- 2.000015 bump

* Tue Nov 11 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.000014-1
- 2.000014 bump

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.008010-8
- Perl 5.20 rebuild

* Mon Jul 28 2014 Petr Pisar <ppisar@redhat.com> - 1.008010-7
- sed(1) is packaged as /bin/sed

* Fri Jul 25 2014 Petr Pisar <ppisar@redhat.com> - 1.008010-6
- Parse perl-homedir configuration bash syntax by csh profile script
  (bug #1122993)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008010-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Nov 21 2013 Petr Pisar <ppisar@redhat.com> - 1.008010-4
- Fix setting undefined variable in CSH (bug #1033018)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008010-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 1.008010-2
- Perl 5.18 rebuild

* Fri Jun 07 2013 Iain Arnell <iarnell@gmail.com> 1.008010-1
- update to latest upstream version

* Fri Apr 19 2013 Iain Arnell <iarnell@gmail.com> 1.008009-2
- rebase append-semicolon patch

* Fri Mar 08 2013 Iain Arnell <iarnell@gmail.com> 1.008009-1
- update to latest upstream version

* Tue Feb 19 2013 Iain Arnell <iarnell@gmail.com> 1.008007-1
- update to latest upstream version

* Fri Feb 15 2013 Iain Arnell <iarnell@gmail.com> 1.008006-1
- udpate to latest upstream version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008004-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 20 2012 Petr Šabata <contyk@redhat.com> - 1.008004-11
- Add missing buildtime dependencies
- Drop useless deps
- Drop command macros
- Modernize the spec

* Mon Aug 20 2012 Petr Pisar <ppisar@redhat.com> - 1.008004-10
- Fix CSH support (bug #849609)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008004-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 1.008004-8
- Perl 5.16 rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 1.008004-7
- Trim Module::Build depencency version to 2 digits because upstream has
  regressed the version

* Sun Jun 17 2012 Petr Pisar <ppisar@redhat.com> - 1.008004-6
- Perl 5.16 rebuild

* Thu May 31 2012 Petr Pisar <ppisar@redhat.com> - 1.008004-5
- Round Module::Build version to 2 digits

* Fri Feb 10 2012 Iain Arnell <iarnell@gmail.com> 1.008004-4
- avoid creating ~/perl5/ for all users (rhbz#789146)
- drop defattr in files lists

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.008004-2
- Perl mass rebuild

* Wed Mar 16 2011 Iain Arnell <iarnell@gmail.com> 1.008004-1
- update to latest upstream version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 23 2011 Iain Arnell <iarnell@gmail.com> 1.008001-2
- update requires perl(Module::Build) >= 0.3600

* Sun Jan 23 2011 Iain Arnell <iarnell@gmail.com> 1.008001-1
- update to latest upstream version
- drop R/BR perl(ExtUtils::CBuilder) and perl(ExtUtils::ParseXS)

* Fri Dec 17 2010 Iain Arnell <iarnell@gmail.com> 1.007000-1
- update to latest upstream version
- fix typo in description

* Sun Nov 21 2010 Iain Arnell <iarnell@gmail.com> 1.006007-1
- update to latest upstream version
- clean up spec for modern rpmbuild
- BR perl(Capture::Tiny)

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.004009-3
- Mass rebuild with perl-5.12.0

* Tue Jan 05 2010 Chris Weyl <cweyl@alumni.drew.edu> 1.004009-2
- add perl-homedir subpackage

* Tue Jan 05 2010 Chris Weyl <cweyl@alumni.drew.edu> 1.004009-1
- add perl_default_filter
- auto-update to 1.004009 (by cpan-spec-update 0.01)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.004007-2
- rebuild against perl 5.10.1

* Sat Sep 19 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.004007-1
- auto-update to 1.004007 (by cpan-spec-update 0.01)

* Sat Aug 29 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.004006-1
- auto-update to 1.004006 (by cpan-spec-update 0.01)

* Tue Aug 25 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.004005-1
- auto-update to 1.004005 (by cpan-spec-update 0.01)

* Tue Aug 11 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.004004-1
- auto-update to 1.004004 (by cpan-spec-update 0.01)
- added a new br on perl(ExtUtils::Install) (version 1.43)
- added a new req on perl(CPAN) (version 1.80)
- added a new req on perl(ExtUtils::CBuilder) (version 0)
- added a new req on perl(ExtUtils::Install) (version 1.43)
- added a new req on perl(ExtUtils::MakeMaker) (version 6.31)
- added a new req on perl(ExtUtils::ParseXS) (version 0)
- added a new req on perl(Module::Build) (version 0.28)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.004001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 03 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.004001-1
- auto-update to 1.004001 (by cpan-spec-update 0.01)

* Tue May 19 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.004000-1
- auto-update to 1.004000 (by cpan-spec-update 0.01)
- altered br on perl(ExtUtils::MakeMaker) (6.31 => 6.42)

* Sun Mar 08 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.003002-1
- submission

* Sun Mar 08 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.003002-0
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.8)
