#
#TODO
# - patch for search glest.ini (HOME_ETC) in glest_game/config.cpp  glest_game/main_menu.cpp  glest_game/renderer.cpp
# - copy glest_game directory (data game) from SOURCE1 without program source files
# - check for additional xorg deps
Summary:	Glest - 3D real time strategy game
Summary(pl):	Glest - Strategia 3D czasu rzeczywistego
Name:		glest
Version:	2.0.0
Release:	0.2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/glest/%{name}_source_%{version}.zip
# Source0-md5:	f7716da7a044dbe108c619b0f52621bb
Source1:	http://dl.sourceforge.net/glest/%{name}_data_%{version}.zip
# Source1-md5:	8b6902e82874011e768c64e20fbeead5
Source2:	http://www.glest.org/files/contrib/translations/catala_1.2.2.zip
# Source2-md5:	0ff52ece4c408f3a01a54dda8f17e994
Source3:	http://www.glest.org/files/contrib/translations/cesky_1.2.1.zip
# Source3-md5:	a1b0063b7ecc7ed14689c63c31b34cf3
Source4:	http://www.glest.org/files/contrib/translations/danish_1.0.9.zip
# Source4-md5:	10a96d53549c7bd50c842dc9d1bd1592
Source5:	http://www.glest.org/files/contrib/translations/deutsch_1.0.1.zip
# Source5-md5:	d1debba1dd35af8115fbe3bc5e660555
Source6:	http://www.glest.org/files/contrib/translations/dutch_1.0.9.zip
# Source6-md5:	75b130468743cd9f74235e5eaca88ee3
Source7:	http://www.glest.org/files/contrib/translations/euskara_1.2.2.zip
# Source7-md5:	b06b8823100e49b537f4be42cd4674f0
Source8:	http://www.glest.org/files/contrib/translations/francais_2.0.0.zip
# Source8-md5:	0cc6e7c7029c79f1bf61d3a3bdb441d0
Source9:	http://www.glest.org/files/contrib/translations/hebrew_1.2.1.zip
# Source9-md5:	01cc8f8b53cb77e37de4abbb056a47f1
Source10:	http://www.glest.org/files/contrib/translations/italiano_2.0.0.zip
# Source10-md5:	9869a946227b31141b4166c1ca627c9a
Source11:	http://www.glest.org/files/contrib/translations/magyar_1.1.0.zip
# Source11-md5:	3dafdbafc1fac2536565bab122b63ece
Source12:	http://www.glest.org/files/contrib/translations/norsk_0.8.1.zip
# Source12-md5:	2be1ef1472431ddc361526590d4d82b5
Source13:	http://www.glest.org/files/contrib/translations/polish_1.0.9.zip
# Source13-md5:	977df518ef4523fce1e833769e760e29
Source14:	http://www.glest.org/files/contrib/translations/portugues_2.0.0.zip
# Source14-md5:	f133c241ac021ad30d54d0ef48b0f64f
Source15:	http://www.glest.org/files/contrib/translations/russian_1.0.9.zip
# Source15-md5:	a703c513b57664f03c857b656cc571ae
Source16:	http://www.glest.org/files/contrib/translations/slovak_2.0.0.zip
# Source16-md5:	a31d07ed2c24da87628590e43f6c131f
Source17:	http://www.glest.org/files/contrib/translations/turkish_1.0.9.zip
# Source17-md5:	5ec892e82722b8de359edccb95903bbc
Source18:	glest.desktop
Source19:	glest.png
Patch0:		%{name}-polish.patch
Patch1:		%{name}-home_etc.patch
URL:		http://www.glest.org/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel >= 1.2.5
BuildRequires:	dos2unix
BuildRequires:	jam >= 2.5
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	unzip
BuildRequires:	xerces-c-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Glest is a free 3D real time strategy game, available for several
operative systems and that can be modified using XML and a set of
tools.

%description -l pl
Glest to darmowa gra 3D typu RTS (real time stategy), dostêpna dla
kilku ró¿nych systemów operacyjnych. Mo¿na j± modyfikowaæ przy u¿yciu
XML-a i zestawu narzêdzi.

%prep
%setup -q -n %{name}_source_%{version} -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17
for file in xml ini log txt html lng; do
	find ./ -noleaf -type f -name \*.$file -exec dos2unix '{}' \;
done
find mk -noleaf -type f -exec dos2unix '{}' \;

%patch0 -p0
%patch1 -p1
chmod +x mk/linux/autogen.sh

%build
cd mk/linux
./autogen.sh
%configure
jam

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_sysconfdir}/%{name},%{_bindir},%{_pixmapsdir},%{_desktopdir}}
install mk/linux/glest $RPM_BUILD_ROOT%{_bindir}/%{name}_game
install mk/linux/glest.ini $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/glest.ini
#ln -s %{_sysconfdir}/%{name}/%{name}.ini $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}.ini
#ln -s %{_bindir}/%{name} $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}
cd glest_game
#install configuration.xml $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/configuration.xml
#ln -s %{_sysconfdir}/%{name}/configuration.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/configuration.xml
#rm configuration.xml
rm glest.*
rm -rf screens
cp -r ./* $RPM_BUILD_ROOT%{_datadir}/%{name}
install ../polish.lng $RPM_BUILD_ROOT%{_datadir}/%{name}/data/lang/
install %{SOURCE18} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE19} $RPM_BUILD_ROOT%{_pixmapsdir}

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
fi

[ ! -d "${GLEST_HOME}/screens" ] && mkdir -p ${GLEST_HOME}/screens

cd /usr/share/glest
/usr/bin/glest_game
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/README docs/README.linux docs/license.txt
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
