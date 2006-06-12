#
#TODO
# - patch for search glest.ini (HOME_ETC) in glest_game/config.cpp  glest_game/main_menu.cpp  glest_game/renderer.cpp
# - copy glest_game directory (data game) from SOURCE1 without program source files
Summary:	Glest - 3D real time strategy game
Summary(pl):	Glest - Strategia 3D czasu rzeczywistego.
Name:		glest
Version:	1.1.0
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/glest/%{name}-source-%{version}.tar.bz2
# Source0-md5:	f549d496789d4a54166a7c386232069e
Source1:	http://dl.sourceforge.net/glest/%{name}_data_v%{version}.zip
# Source1-md5:	bbf40de52ad412b1e36fc3bc1f6822fc
#Patch0: %{name}-DESTDIR.patch
URL:		http://www.glest.org/
BuildRequires:	Mesa-libGLU-devel
BuildRequires:	OpenAL-devel
BuildRequires:	SDL-devel >= 1.2.5
BuildRequires:	X11-devel
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
Glest to darmowa gra 3D typu RTS(real time stategy), dostêpna dla
ró¿nych systemów.

%prep
%setup -q -a0 -a1

%build
%configure
jam

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_sysconfdir}/%{name},%{_bindir}}
install glest $RPM_BUILD_ROOT%{_bindir}/%{name}
install glest.ini $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/glest.ini
ln -s %{_sysconfdir}/%{name}/%{name}.ini $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}.ini
ln -s %{_bindir}/%{name} $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}
cd glest_game
install configuration.xml $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/configuration.xml
ln -s %{_sysconfdir}/%{name}/configuration.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/configuration.xml
rm configuration.xml
rm glest.ini
cp -r ./* $RPM_BUILD_ROOT%{_datadir}/%{name}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.linux license.txt
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
