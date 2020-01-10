Name:           yum-conf-epel       
Version:        6
Release:        1
Summary:        Extra Packages for Enterprise Linux repository configuration
Group:          System Environment/Base 
License:        GPL 
URL:            http://download.fedoraproject.org/pub/epel
BuildArch:      noarch
Requires:       epel-release

%description
This package pulls in epel-release which contains the
Extra Packages for Enterprise Linux (EPEL) repository
GPG key as well as configuration for yum and up2date.


%files


%changelog
* Thu Jan 13 2011 Troy Dawson <dawson@fnal.gov> - 6-1
- The rpm only pulls in the appropriate release package

