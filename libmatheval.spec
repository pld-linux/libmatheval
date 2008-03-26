Summary:	Library for evaluating mathematical expressions
Summary(pl.UTF-8):	Biblioteka do obliczania wyrażeń matematycznych
Name:		libmatheval
Version:	1.1.6
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	ftp://ftp.gnu.org/gnu/libmatheval/%{name}-%{version}.tar.gz
# Source0-md5:	931eb9e0515c4c806ccf6c7c62c24068
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/libmatheval/
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex >= 2.5.33-2
BuildRequires:	guile-devel
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

%description -l pl.UTF-8
GNU libmatheval to biblioteka zawierająca różne procedury
umożliwiające tworzenie w pamięci drzew ze znakowej reprezentacji
funkcji matematycznych jednej lub wielu zmiennych. Drzewo może być
później użyte do obliczenia wartości funkcji dla podanych wartości
parametrów, stworzenia drzewa dla pochodnej funkcji po danej zmiennej
lub zapisania tekstowej reprezentacji drzewa do podanego łańcucha.
Biblioteka udostępnia interfejsy dla C i Fortranu 77.

%package devel
Summary:	Header files for libmatheval library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libmatheval
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
# -lfl
Requires:	flex

%description devel
Header files for libmatheval library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libmatheval.

%package static
Summary:	Static libmatheval library
Summary(pl.UTF-8):	Statyczna biblioteka libmatheval
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmatheval library.

%description static -l pl.UTF-8
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

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS
%attr(755,root,root) %{_libdir}/libmatheval.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmatheval.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmatheval.so
%{_libdir}/libmatheval.la
%{_includedir}/matheval.h
%{_pkgconfigdir}/libmatheval.pc
%{_infodir}/libmatheval.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/libmatheval.a
