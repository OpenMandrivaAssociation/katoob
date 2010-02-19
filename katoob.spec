Name:		katoob
Version:	0.5.9.1
Release:	%mkrel 4
Summary:	Light weight multilingual text editor that uses gtk2
URL:		http://www.arabeyes.org/project.php?proj=Katoob
License:	GPLv2+
Group:		Editors
# http://belnet.dl.sourceforge.net/sourceforge/arabeyes/katoob-0.3.5.tar.gz
Source:		ftp://foolab.org/pub/software/katoob/%name-%version.tar.gz
Source10:	%name-icons.tar.bz2
# fwang: patch from debian to get it build in 64 bit environment
Patch1:		katoob-0.5.8-getprotobyname-return-cast.patch
Patch2:		katoob-0.5.9.1-gcc43.patch
Patch3:		katoob-0.5.9.1-glibc2.10.patch
Patch4:		katoob-0.5.9.1-gtk.patch
BuildRoot:	%_tmppath/%name-buildroot
BuildRequires:	gtk2-devel gtkmm2.4-devel
BuildRequires:  perl-XML-Parser
BuildRequires:	cups-devel bzip2-devel aspell-devel
BuildRequires:	enchant-devel curl-devel
BuildRequires:	desktop-file-utils
Requires:	enchant

%description
Katoob is a light weight, multi lingual, BIDI-aware texteditor. It sup-
ports opening and saving files in multiple encodings. The main support
was for Arabic language but more languages are currently supported.

%prep
%setup -q
%setup -q -T -D -a10
%patch2 -p1
%patch3 -p1
%patch4 -p0

%build
%configure2_5x --enable-spell
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

desktop-file-install --vendor="" \
	--dir %{buildroot}%{_datadir}/applications \
	--add-category="GTK" \
	%{buildroot}%{_datadir}/applications/*.desktop

#icons
install -D -m 644 %{name}48.png $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
install -D -m 644 %{name}32.png $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -D -m 644 %{name}16.png $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png

%find_lang %{name}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr( 0644, root, root, 755)
%doc README ChangeLog AUTHORS COPYING TODO THANKS NEWS
%{_datadir}/pixmaps/%{name}-icon.png
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/*
%{_mandir}/man1/%{name}.*
%lang(de) %{_mandir}/de/man1/*
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%dir %{_datadir}/%{name}
%defattr( 0755, root, root, 755)
%{_bindir}/*
