%global tl_name prosper
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0h
Release:	%{tl_revision}.1
Summary:	LaTeX class for high quality slides
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/prosper
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/prosper.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/prosper.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Prosper is a LaTeX class for writing transparencies. It is written as an
extension of the seminar class by Timothy Van Zandt. Prosper offers a
friendly environment for creating slides for both presentations with an
overhead projector and a video projector. Slides prepared for a
presentation with a computer and a video projector may integrate
animation effects, incremental display, and so on. Various visual styles
are supported (including some that mimic PowerPoint) and others are
being contributed.

