Name: tcpping
Version: 0.2.3
Release: 1%{?dist}
Summary: Measure TCP latency in a ping like style

License: GPLv3 
URL: 
Source0: tcpping

BuildRequires:
Requires: python

%description
Measure TCP latency in a ping like style.

%prep

%build

%configure

%make_build

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 %{SOURCE0} %{buildroot}/%{_bindir}

#mkdir -p %{buildroot}/%{_mandir}/man1

%doc AUTHORS COPYING README.md TODO ChangeLog
%make_install

%files
%{_bindir}/tcpping

%changelog
* Wed Jun 28 2017 Peter Downs <padowns@gmail.com> - 0.2.3
- Add DNS lookup with each iteration to test if DNS introduces latency
