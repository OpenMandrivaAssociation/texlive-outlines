%global tl_name outlines
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Produce outline lists
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/outlines
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/outlines.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/outlines.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Defines an outline environment, which allows outline-style indented
lists with freely mixed levels up to four levels deep. It replaces the
nested begin/end pairs by different item tags \1 to \4 for each nesting
level. This is very convenient in cases where nested lists are used a
lot, such as for to-do lists or presentation slides.

