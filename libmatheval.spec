Summary:	Library for evaluating mathematical expressions
Summary(pl):	Biblioteka do obliczania wyra¿eñ matematycznych
Name:		libmatheval
Version:	1.0.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.gnu.org/gnu/libmatheval/%{name}-%{version}.tar.gz
# Source0-md5:	6ba40aba212629142506f96b7a7dac7f
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/libmatheval/
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	guile
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU libmatheval is a library which contains several procedures that
make it possible to create an in-memory tree from the string
representation of a mathematical function over single or multiple
variables. This tree can be used later to evaluate a function for
specified variable values, to create a corresponding tree for the
function derivative over a specified variable, or to write a textual
tree representation to a specified string. The library exposes C and
Fortran 77 interfaces.

%description -l pl
GNU libmatheval to biblioteka zawieraj±ca ró¿ne procedury
umo¿liwiaj±ce tworzenie w pamiêci drzew ze znakowej reprezentacji
funkcji matematycznych jednej lub wielu zmiennych. Drzewo mo¿e byæ
pó¼niej u¿yte do obliczenia warto¶ci funkcji dla podanych warto¶ci
parametrów, stworzenia drzewa dla pochodnej funkcji po danej zmiennej
lub zapisania tekstowej reprezentacji drzewa do podanego ³añcucha.
Biblioteka udostêpnia interfejsy dla C i Fortranu 77.

%package devel
Summary:	Header files for libmatheval library
Summary(pl):	Pliki nag³ówkowe biblioteki libmatheval
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
# -lfl
Requires:	flex

%description devel
Header files for libmatheval library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libmatheval.

%package static
Summary:	Static libmatheval library
Summary(pl):	Statyczna biblioteka libmatheval
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmatheval library.

%description static -l pl
Statyczna biblioteka libmatheval.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.* config
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_infodir}/*.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
