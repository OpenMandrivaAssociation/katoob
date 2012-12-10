Name:		katoob
Version:	0.5.9.1
Release:5
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
Patch5:		katoob-0.5.9.1-linking.patch

BuildRequires:	pkgconfig(gdk-2.0)
BuildRequires:	pkgconfig(gdkmm-2.4)
BuildRequires:	perl-XML-Parser
BuildRequires:	cups-devel 
BuildRequires:	bzip2-devel 
BuildRequires:	aspell-devel
BuildRequires:	pkgconfig(enchant) 
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	desktop-file-utils
Requires:	enchant

%description
Katoob is a light weight, multi lingual, BIDI-aware text editor. It sup-
ports opening and saving files in multiple encodings. The main support
was for Arabic language but more languages are currently supported.

%prep
%setup -q
%setup -q -T -D -a10
%patch2 -p1
%patch3 -p1
%patch4 -p0
%patch5 -p1

%build
%configure2_5x --enable-spell
%make

%install
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

%files -f %{name}.lang
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


