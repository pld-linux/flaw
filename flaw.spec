Summary:	A free top-down wizard fighting game
Name:		flaw
Version:	1.2.4
Release:	0.1
License:	GPL v3
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/flaw/%{name}-%{version}.tar.gz
# Source0-md5:	1403c848f91398c29bd4e2efe384996b
Source1:	http://flaw.sourceforge.net/instructions.shtml
# Source1-md5:	59696d8db8557cda077c563e96bbd336
Source2:	http://flaw.sourceforge.net/images/arrows.png
# Source2-md5:	bd18a6c5b1751828b30fe21e81805e01
Source3:	http://flaw.sourceforge.net/images/wasd.png
# Source3-md5:	1148a75dcb65c15efe671280fb3d0f94
URL:		http://flaw.sourceforge.net/
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
F.L.A.W. is a free top-down wizard fighting game that can be played by
up to 5 players. The goal of the game is to survive as long as
possible while more and more fireballs appear in the arena.

Gameplay is simple and self-explanatory: While the players try to
avoid the fireballs, they can knock each other down. In addition there
are collectable magic gems that provide special abilities. The game
can be played as a single player game against the computer, but it is
more fun with 2 and more human players.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install  AUTHORS ChangeLog NEWS README %{SOURCE1} %{SOURCE2} %{SOURCE3} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm
