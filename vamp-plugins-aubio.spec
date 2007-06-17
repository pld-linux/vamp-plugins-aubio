%define	vampplugindir	%{_libdir}/vamp
%define srcname	vamp-aubio-plugins

Summary:	vamp plugins using aubio
Name:		vamp-plugins-aubio
Version:	0.3.2
Release:	0.1
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/vamp/%{srcname}-%{version}.tar.gz
# Source0-md5:	906b7c943de834640de4f0dbe0d34724
Patch0:		%{name}-compile.patch
Patch1:		%{name}-link.patch
URL:		http://www.vamp-plugins.org/
BuildRequires:	aubio-devel
BuildRequires:	fftw3-single-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libstdc++-devel
BuildRequires:	vamp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of Vamp plugins (http://www.sonicvisualiser.org/vamp.html) for
audio feature extraction using Paul Brossier's aubio
(http://aubio.piem.org/).

This set includes three plugins: Onset for onset detection, Pitch for
pitch tracking, and Notes for combined onset and pitch.

%prep
%setup -q -n %{srcname}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	OPTFLAGS="%{rpmcxxflags}" \
	LDFLAGS="%{rpmldflags}"

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
