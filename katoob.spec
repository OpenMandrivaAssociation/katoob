Name:		katoob
Version:	0.5.8
Release:	%mkrel 1
Summary:	Light weight multilingual text editor that uses gtk2
URL:		http://www.arabeyes.org/project.php?proj=Katoob
License:	GPL
Group:		Editors

# http://belnet.dl.sourceforge.net/sourceforge/arabeyes/katoob-0.3.5.tar.gz
Source:		%name-%version.tar.bz2
Source10:	%name-icons.tar.bz2
BuildRoot:	%_tmppath/%name-buildroot
BuildRequires:	gtk2-devel
BuildRequires:  perl-XML-Parser

%description
Katoob is a light weight, multi lingual, BIDI-aware texteditor. It sup-
ports opening and saving files in multiple encodings. The main support
was for Arabic language but more languages are currently supported.

%prep
%setup -q
%setup -q -T -D -a10

%build
%configure --enable-spell
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#rm -rf $RPM_BUILD_ROOT%{_datadir}/applications/katoob.desktop

#mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor="" \
	--dir %{buildroot}%{_datadir}/applications \
	--add-category="GTK" \
	%{buildroot}%{_datadir}/applications/*.desktop

#icons
install -D -m 644 %{name}48.png $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
install -D -m 644 %{name}32.png $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -D -m 644 %{name}16.png $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png

%find_lang %{name}

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr( 0644, root, root, 755)
%doc README ChangeLog AUTHORS COPYING TODO THANKS NEWS
%{_datadir}/pixmaps/%{name}-icon.png
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/*
%{_mandir}/man1/%{name}.1.bz2
%lang(de) %{_mandir}/de/man1/*
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%dir %{_datadir}/%{name}
%defattr( 0755, root, root, 755)
%{_bindir}/*
