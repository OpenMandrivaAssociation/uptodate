
Name:           uptodate
Summary:        Helps you to keep your system uptodate
Version:        0.3.1
Release:        %mkrel 12
URL:            http://voxel.jouy.inra.fr/darcs/uptodate
Source0:        http://voxel.jouy.inra.fr/darcs/uptodate/uptodate-%{version}.tar.bz2
License:        GPL
Group:          Networking/Other
Requires:       python >= 2.3
BuildRoot:      %{_tmppath}/%{name}-buildroot
BuildArch:      noarch
BuildRequires:  python-devel

%description
uptodate is powerful and user friendly command line tool which helps you to
know when a new version is available. It searches for new versions in a web
page, a ftp directory, etc, and shows you added and removed version since the
last search. If you update some softs by hand, if you are a package maintainer,
or if you simply want to know when the new version of your favorite game (or
everything else with a version) is out, uptodate is for you !

%prep

%setup

%build

%install
python setup.py install --root=%buildroot

%clean
/bin/rm -Rf %buildroot


%files
%defattr(0644, root, root, 0755)
%attr(0755,root,root) %{_bindir}/*
%{py_puresitedir}/*
%{_datadir}/locale/*/*/*
%config(noreplace) %{_sysconfdir}/bash_completion.d/uptodate
%doc COPYING README






%changelog
* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 0.3.1-12mdv2011.0
+ Revision: 592180
- rebuild for python 2.7

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.3.1-11mdv2010.0
+ Revision: 445613
- rebuild

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 0.3.1-10mdv2009.1
+ Revision: 326003
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.3.1-9mdv2009.0
+ Revision: 242907
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Aug 27 2007 Gaëtan Lehmann <glehmann@mandriva.org> 0.3.1-7mdv2008.0
+ Revision: 72211
- rebuild


* Thu Nov 30 2006 Gaëtan Lehmann (INRA) <glehmann@mandriva.org> 0.3.1-6mdv2007.0
+ Revision: 88944
- rebuild for new python

* Thu Aug 10 2006 Gaëtan Lehmann (INRA) <glehmann@mandriva.org> 0.3.1-5mdv2007.0
+ Revision: 55170
- rebuild
- Import uptodate

* Thu Jan 19 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.3.1-4mdk
- use py_puresitedir

* Sat Dec 24 2005 Nicolas L�cureuil <neoclust@mandriva.org> 0.3.1-3mdk
- Add BuildRequires
- change %%mkrel to make rpmbuildupdate happy

* Sat Dec 24 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.3.1-2mdk
- rebuild to fix path on i586

* Sat Dec 03 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.3.1-1mdk
- New release 0.3.1
- fix URL

* Mon Jul 25 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.3-1mdk
- New release 0.3

* Tue Mar 29 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.2-1mdk
- 0.2

* Sat Mar 26 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.1-1mdk
- initial contrib

