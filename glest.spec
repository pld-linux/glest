#
#TODO
# - patch for search glest.ini (HOME_ETC) in glest_game/config.cpp  glest_game/main_menu.cpp  glest_game/renderer.cpp
# - copy glest_game directory (data game) from SOURCE1 without program source files
# - check for additional xorg deps
Summary:	Glest - 3D real time strategy game
Summary(pl):	Glest - Strategia 3D czasu rzeczywistego
Name:		glest
Version:	2.0.0
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/glest/%{name}_source_%{version}.zip
# Source0-md5:	f7716da7a044dbe108c619b0f52621bb
Source1:	http://dl.sourceforge.net/glest/%{name}_data_%{version}.zip
# Source1-md5:	8b6902e82874011e768c64e20fbeead5
Source2:	http://www.glest.org/files/contrib/translations/polish_1.0.9.zip
# Source2-md5:	977df518ef4523fce1e833769e760e29
#Patch0: %{name}-DESTDIR.patch
URL:		http://www.glest.org/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel >= 1.2.5
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
%setup -q -n glest_source_%{version} -a1 -a2
for file in xml ini log txt html lng; do
	find ./ -noleaf -type f -name \*.$file -exec dos2unix '{}' \;
done

find mk -noleaf -type f -exec dos2unix '{}' \;

chmod +x mk/linux/autogen.sh

%build
cd mk/linux
./autogen.sh
%configure
jam

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_sysconfdir}/%{name},%{_bindir}}
install mk/linux/glest $RPM_BUILD_ROOT%{_bindir}/%{name}
install mk/linux/glest.ini $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/glest.ini
ln -s %{_sysconfdir}/%{name}/%{name}.ini $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}.ini
ln -s %{_bindir}/%{name} $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}
cd glest_game
install configuration.xml $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/configuration.xml
ln -s %{_sysconfdir}/%{name}/configuration.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/configuration.xml
rm configuration.xml
rm glest.ini
cp -r ./* $RPM_BUILD_ROOT%{_datadir}/%{name}
install ../polish.lng $RPM_BUILD_ROOT%{_datadir}/%{name}/data/lang/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/README docs/README.linux docs/license.txt
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
