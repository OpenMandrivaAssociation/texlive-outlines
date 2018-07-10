# revision 25192
# category Package
# catalog-ctan /macros/latex/contrib/outlines
# catalog-date 2012-01-24 12:03:36 +0100
# catalog-license noinfo
# catalog-version 1.1
Name:		texlive-outlines
Version:	1.1
Release:	10
Summary:	Produce "outline" lists
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/outlines
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/outlines.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/outlines.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 31 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 770234
- texlive-outlines
- texlive-outlines

