#spec file for package globus-sshd-config
#
# Copyright  (c)  2019 Jonn R. Hover <jhover@bnl.gov>
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# please send bugfixes or comments to jhover@bnl.gov
#
#
#

Name:      globus-sshd-config
Summary:   Files to run sshd standalone with Globus auth config
Version:   0.90
Release:   1
BuildArch: noarch
License:   GPL
Vendor:    RACF http://www.racf.bnl.gov/
Packager:  John R. Hover <jhover@bnl.gov>
Group:     Scientific/Engineering
Requires:  yum
Provides:  globus-sshd-config
Source0:   globus-sshd-config-%{version}.tgz
BuildRoot: %{_tmppath}/globus-sshd-config-build


%description
Files to run sshd standalone with Globus auth config  

%prep
%setup -q

%build


%install
rm -rf %\{buildroot]
mkdir -p %{buildroot}/etc/globus-ssh
mkdir -p %{buildroot}/etc/pam.d
mkdir -p %{buildroot}/etc/sysconfig
mkdir -p %{buildroot}/usr/lib/systemd/system

cp etc/globus-sshd.pamd %{buildroot}/etc/pam.d/globus-sshd
cp etc/globus-sshd.sysconfig %{buildroot}/etc/sysconfig/globus-sshd
cp etc/globus-sshd.service %{buildroot}/usr/lib/systemd/system/


%clean
rm -rf %{buildroot}

%pre
#mkdir -p /usr/share/projectname
#mkdir -p /etc/projectname

%post
cp -v /usr/sbin/sshd /usr/sbin/globus-sshd

%preun

%postun
rm /usr/sbin/globus-sshd


%files
%defattr(755,root,root,-)
#/usr/bin/projectbin.sh

%defattr(-,root,root,-)
/etc/pam.d/globus-sshd
/etc/sysconfig/globus-sshd
/usr/lib/systemd/system/globus-sshd.service

#/usr/share/projectname/projectfile
#/etc/pki/rpm-gpg/RPM-GPG-KEY-racf-grid.asc


%defattr(-,root,root,-)
# %config(noreplace) /etc/yum.repos.d/racf-grid-testing.repo


# secret files
# %defattr(644,root,root,-)
#/root/.projectname/project.cfg

%changelog
* Fri Apr 12 2019 John Hover <jhover@bnl.gov> - 0.90
- Initial spec file. 


