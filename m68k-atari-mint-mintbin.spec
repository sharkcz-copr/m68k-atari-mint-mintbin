%global gitdate 20201129

Name:           m68k-atari-mint-mintbin
Summary:        MiNT Development Utilities
Version:        0.3
Release:        3.%{gitdate}%{?dist}
License:        GPLv2+
URL:            http://www.freemint.de/
#Source0:        http://vincent.riviere.free.fr/soft/m68k-atari-mint/archives/mintbin-Git-%%{gitdate}.tar.gz
# use my https enabled mirror instead
Source0:        https://fedora.danny.cz/atari/mintbin-Git-%{gitdate}.tar.gz
BuildRequires:  m68k-atari-mint-filesystem
BuildRequires:  gcc
Requires:       m68k-atari-mint-filesystem


%description
MiNTBin is a collection of supplementary utilities necessary for compiling 
programs for MiNT in a GNU development environment.  It also contains 
tools that are necessary for non-programmers like programs for changing
resp. inquiring program flags but its primary use it to accompany the
GNU binutils on MiNT systems.


%prep
%setup -q -n mintbin-Git-%{gitdate}


%build
%configure \
  --target=%{mint_target} \
  --disable-nls

make


%install
%make_install

rm -rf $RPM_BUILD_ROOT%{_prefix}/%{mint_target}/bin/


%files
%doc README TODO ABOUT-NLS COPYING ChangeLog NEWS README-alpha
%{_bindir}/%{mint_target}-*
%{_prefix}/%{mint_target}/include/*
%{_infodir}/mintbin.*
%exclude %{_infodir}/dir


%changelog
* Mon Jun 13 2022 Dan Horák <dan[at]danny.cz> - 0.3-3.20201129
- update to 20201129

* Sun Mar 25 2012 Dan Horák <dan[at]danny.cz> - 0.3-2.20110527
- spec cleanup

* Wed Aug 03 2011 Dan Horák <dan[at]danny.cz> - 0.3-1.20110527
- initial Fedora release
