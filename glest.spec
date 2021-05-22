#
#TODO
# - copy glest_game directory (data game) from SOURCE1 without program source files
# - check for additional xorg deps
%define 	data_ver	3.2.1
Summary:	Glest - 3D real time strategy game
Summary(pl.UTF-8):	Glest - Strategia 3D czasu rzeczywistego
Name:		glest
Version:	3.2.2
Release:	3
License:	GPL v2+, Creative Commons Attribution-ShareAlike
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/glest/%{name}_source_%{version}.zip
# Source0-md5:	1e961f49c1fb0e59e1e1483d66099a55
Source1:	http://downloads.sourceforge.net/glest/%{name}_data_%{data_ver}.zip
# Source1-md5:	d67de58e0912925e8ddbd0b25a0d2b50
Source2:	http://www.glest.org/files/contrib/translations/catala_1.2.2.zip
# Source2-md5:	0ff52ece4c408f3a01a54dda8f17e994
Source3:	http://www.glest.org/files/contrib/translations/cesky_3.1.2.zip
# Source3-md5:	ae7e2b0ad4bc8622ebeb2e178816ddbd
Source4:	http://www.glest.org/files/contrib/translations/danish_1.0.9.zip
# Source4-md5:	10a96d53549c7bd50c842dc9d1bd1592
Source5:	http://www.glest.org/files/contrib/translations/german_3.1.2.zip
# Source5-md5:	71fd759e8c0dacffc50d2d732cd53927
Source6:	http://www.glest.org/files/contrib/translations/dutch_1.0.9.zip
# Source6-md5:	75b130468743cd9f74235e5eaca88ee3
Source7:	http://www.glest.org/files/contrib/translations/euskara_1.2.2.zip
# Source7-md5:	b06b8823100e49b537f4be42cd4674f0
# http://www.glest.org/files/contrib/translations/français_3.1.2.zip 
Source8:	francais_3.1.2.zip 
# Source8-md5:	8446f46d9b894ede3ace90edac8663d7
Source9:	http://www.glest.org/files/contrib/translations/hebrew_1.2.1.zip
# Source9-md5:	01cc8f8b53cb77e37de4abbb056a47f1
Source10:	http://www.glest.org/files/contrib/translations/italian_3.1.0.zip
# Source10-md5:	f11bbae0468d32fb845660b6dc8e4856
Source11:	http://www.glest.org/files/contrib/translations/magyar_3.2-alpha1.zip
# Source11-md5:	8a68ce97215f87daaded7b5df9263caa
Source12:	http://www.glest.org/files/contrib/translations/norsk_3.1.2.zip
# Source12-md5:	56113995e1e8da088ccdf2841dc663dc
Source13:	http://www.glest.org/files/contrib/translations/polish_1.0.9.zip
# Source13-md5:	977df518ef4523fce1e833769e760e29
Source14:	http://www.glest.org/files/contrib/translations/portugues_2.0.0.zip
# Source14-md5:	f133c241ac021ad30d54d0ef48b0f64f
Source15:	http://www.glest.org/files/contrib/translations/russian_3.1.2.zip
# Source15-md5:	751481b6615f5e24c884fcc3837c3b4e
Source16:	http://www.glest.org/files/contrib/translations/slovak_2.0.0.zip
# Source16-md5:	a31d07ed2c24da87628590e43f6c131f
Source17:	http://www.glest.org/files/contrib/translations/turkish_3.1.2.zip
# Source17-md5:	7958618435938c2cdf067ea6917d144b
Source18:	http://www.glest.org/files/contrib/translations/greek_3.0.0.zip
# Source18-md5:	06a51c3eda91b6f8b3e0f777f3136cff
Source19:	http://www.glest.org/files/contrib/translations/srpski_2.0.1.zip
# Source19-md5:	c00259c351125138f95c57776a66e3b6
Source50:	glest.desktop
Source51:	glest.png
Patch0:		%{name}-polish.patch
Patch1:		%{name}-lua.patch
Patch2:		%{name}-cstdio.patch
Patch3:		%{name}-ini.patch
URL:		http://glest.org/
BuildRequires:	Mesa-libGLU-devel
BuildRequires:	Mesa-libGLw-devel
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.5
BuildRequires:	dos2unix
BuildRequires:	jam >= 2.5
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	unzip
BuildRequires:	xerces-c-devel
BuildRequires:	lua51-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Glest is a free 3D real time strategy game, available for several
operative systems and that can be modified using XML and a set of
tools.

%description -l pl.UTF-8
Glest to darmowa gra 3D typu RTS (real time stategy), dostępna dla
kilku różnych systemów operacyjnych. Można ją modyfikować przy użyciu
XML-a i zestawu narzędzi.

%prep
%setup -q -c -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19
for file in xml ini log txt html lng; do
	find ./ -noleaf -type f -name \*.$file -exec dos2unix '{}' \;
done
find mk -noleaf -type f -exec dos2unix '{}' \;

%patch0 -p1
%patch1 -p1
dos2unix source/shared_lib/sources/platform/posix/socket.cpp
%patch2 -p1
%patch3 -p1
chmod +x mk/linux/autogen.sh

%build
cd mk/linux
./autogen.sh
%configure \
	--with-x \
	--enable-optimize 
jam

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_sysconfdir}/%{name},%{_bindir},%{_pixmapsdir},%{_desktopdir},%{_libexecdir}}
install mk/linux/glest $RPM_BUILD_ROOT%{_libexecdir}/glest_game
install mk/linux/glest.ini $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/glest.ini
cd glest_game
%{__rm} glest.*
%{__rm} -r screens
cp -pr * $RPM_BUILD_ROOT%{_datadir}/%{name}
for LNG in ../*.lng; do
	install $LNG $RPM_BUILD_ROOT%{_datadir}/%{name}/data/lang
done
install %{SOURCE50} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE51} $RPM_BUILD_ROOT%{_pixmapsdir}

cat << 'EOF' > $RPM_BUILD_ROOT%{_bindir}/%{name}
#!/bin/sh

if [ -n "${HOME_ETC}" ]; then
	GLEST_HOME="${HOME_ETC}/.glest"
else
	GLEST_HOME="${HOME}/.glest"
fi

if [ ! -d "${GLEST_HOME}" ]; then
	mkdir -p ${GLEST_HOME}
	cp -a /etc/glest/* ${GLEST_HOME}
	for F in %{_datadir}/%{name}/*; do
		ln -s $F ${GLEST_HOME}/
	done
fi

[ ! -d "${GLEST_HOME}/screens" ] && mkdir -p ${GLEST_HOME}/screens

cd ${GLEST_HOME}
%{_libexecdir}/glest_game
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/readme.txt docs/readme_linux.txt docs/code_license.txt docs/data_license.txt
%dir %{_sysconfdir}/glest
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/glest/glest.ini
%attr(755,root,root) %{_bindir}/glest
%attr(755,root,root) %{_libexecdir}/glest_game
%{_datadir}/%{name}
%{_desktopdir}/glest.desktop
%{_pixmapsdir}/glest.png
