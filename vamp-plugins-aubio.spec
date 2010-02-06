%define	vampplugindir	%{_libdir}/vamp
%define srcname		vamp-aubio-plugins
%define postver		c

Summary:	Vamp plugins using aubio
Summary(pl.UTF-8):	Wtyczki Vampa wykorzystujące aubio
Name:		vamp-plugins-aubio
Version:	0.3.2
Release:	1.%{postver}.1
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/vamp/%{srcname}-%{version}%{postver}.tar.gz
# Source0-md5:	fe58ab3d220853faa6af86023249d1fa
URL:		http://www.vamp-plugins.org/
BuildRequires:	aubio-devel
BuildRequires:	libstdc++-devel
BuildRequires:	vamp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of Vamp plugins (http://www.sonicvisualiser.org/vamp.html) for
audio feature extraction using Paul Brossier's aubio
(http://aubio.piem.org/).

This set includes three plugins: Onset for onset detection, Pitch for
pitch tracking, and Notes for combined onset and pitch.

%description -l pl.UTF-8
Zestaw wtyczek Vampa  (http://www.sonicvisualiser.org/vamp.html) do
wydobywania cech dźwięku przy użyciu aubio Paula Brossiera
(http://aubio.piem.org/).

Ten zestaw zawiera wtyczki: Onset to wykrywania początków, Pitch do
śledzenia wysokości tonów i Notes do łączenia początków i tonów.

%prep
%setup -q -n %{srcname}-%{version}%{postver}

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags} -DNDEBUG -ffast-math -Wall -I." \
	LDFLAGS="%{rpmldflags}" \
	PLUGIN_LIBS="-lvamp-sdk -laubio" \
	PLUGIN_LDFLAGS="-shared -Wl,-Bsymbolic %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{vampplugindir}
install *.so $RPM_BUILD_ROOT%{vampplugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{vampplugindir}/*so
