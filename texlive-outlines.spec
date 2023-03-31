Name:		texlive-outlines
Version:	25192
Release:	2
Summary:	Produce "outline" lists
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/outlines
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/outlines.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/outlines.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Defines an outline environment, which allows outline-style
indented lists with freely mixed levels up to four levels deep.
It replaces the nested begin/end pairs by different item tags
\1 to \4 for each nesting level. This is very convenient in
cases where nested lists are used a lot, such as for to-do
lists or presentation slides.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/outlines/outlines.sty
%doc %{_texmfdistdir}/doc/latex/outlines/README
%doc %{_texmfdistdir}/doc/latex/outlines/outlines.pdf
%doc %{_texmfdistdir}/doc/latex/outlines/outlines.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
