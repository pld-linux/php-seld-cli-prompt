%define		pkgname	cli-prompt
Summary:	Allows you to prompt for user input on the command line
Name:		php-seld-cli-prompt
Version:	1.0.0
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	https://github.com/Seldaek/cli-prompt/archive/%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	8895b5ec3d8f0212239e86be768391f6
URL:		https://github.com/Seldaek/cli-prompt
Requires:	php(core) >= 5.3.0
Requires:	php(pcre)
Requires:	php(spl)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
While prompting for user input using fgets() is quite easy, sometimes
you need to prompt for sensitive information. In these cases, the
characters typed in by the user should not be directly visible, and
this is quite a pain to do in a cross-platform way.

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
# Restore PSR-0 tree
install -d $RPM_BUILD_ROOT%{php_data_dir}/Seld/CliPrompt
cp -a src/* $RPM_BUILD_ROOT%{php_data_dir}/Seld/CliPrompt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE composer.json res/example.php
%dir %{php_data_dir}/Seld
%{php_data_dir}/Seld/CliPrompt
