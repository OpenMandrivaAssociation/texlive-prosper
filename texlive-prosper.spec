# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/prosper
# catalog-date 2010-05-17 14:53:01 +0200
# catalog-license lppl1.2
# catalog-version 1.0h
Name:		texlive-prosper
Version:	1.0h
Release:	2
Summary:	LaTeX class for high quality slides
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/prosper
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prosper.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prosper.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prosper.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Prosper is a LaTeX class for writing transparencies. It is
written as an extension of the seminar class by Timothy Van
Zandt. Prosper offers a friendly environment for creating
slides for both presentations with an overhead projector and a
video projector. Slides prepared for a presentation with a
computer and a video projector may integrate animation effects,
incremental display, and so on. Various visual styles are
supported (including some that mimic PowerPoint) and others are
being contributed.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/prosper/PPRalcatel.sty
%{_texmfdistdir}/tex/latex/prosper/PPRalienglow.sty
%{_texmfdistdir}/tex/latex/prosper/PPRautumn.sty
%{_texmfdistdir}/tex/latex/prosper/PPRazure.sty
%{_texmfdistdir}/tex/latex/prosper/PPRblends.sty
%{_texmfdistdir}/tex/latex/prosper/PPRcapsules.sty
%{_texmfdistdir}/tex/latex/prosper/PPRcontemporain.sty
%{_texmfdistdir}/tex/latex/prosper/PPRcorners.sty
%{_texmfdistdir}/tex/latex/prosper/PPRdarkblue.sty
%{_texmfdistdir}/tex/latex/prosper/PPRdefault.sty
%{_texmfdistdir}/tex/latex/prosper/PPRframes.sty
%{_texmfdistdir}/tex/latex/prosper/PPRfyma.sty
%{_texmfdistdir}/tex/latex/prosper/PPRgyom.sty
%{_texmfdistdir}/tex/latex/prosper/PPRlignesbleues.sty
%{_texmfdistdir}/tex/latex/prosper/PPRmancini.sty
%{_texmfdistdir}/tex/latex/prosper/PPRnuancegris.sty
%{_texmfdistdir}/tex/latex/prosper/PPRprettybox.sty
%{_texmfdistdir}/tex/latex/prosper/PPRrico.sty
%{_texmfdistdir}/tex/latex/prosper/PPRserpaggi.sty
%{_texmfdistdir}/tex/latex/prosper/PPRthomasd.sty
%{_texmfdistdir}/tex/latex/prosper/PPRtroispoints.sty
%{_texmfdistdir}/tex/latex/prosper/PPRwhitecross.sty
%{_texmfdistdir}/tex/latex/prosper/PPRwinter.sty
%{_texmfdistdir}/tex/latex/prosper/PPRwj.sty
%{_texmfdistdir}/tex/latex/prosper/angleHG.ps
%{_texmfdistdir}/tex/latex/prosper/arrow-glow.ps
%{_texmfdistdir}/tex/latex/prosper/barre-rico.ps
%{_texmfdistdir}/tex/latex/prosper/blue-inverted-arrow.ps
%{_texmfdistdir}/tex/latex/prosper/boule-base.eps
%{_texmfdistdir}/tex/latex/prosper/boulebleue-fondblanc.eps
%{_texmfdistdir}/tex/latex/prosper/boulerouge-fondblanc.eps
%{_texmfdistdir}/tex/latex/prosper/bouleverte-fondblanc.eps
%{_texmfdistdir}/tex/latex/prosper/bullet-glow.ps
%{_texmfdistdir}/tex/latex/prosper/compilation.eps
%{_texmfdistdir}/tex/latex/prosper/degrade-base.eps
%{_texmfdistdir}/tex/latex/prosper/degrade-blanc-bleu.eps
%{_texmfdistdir}/tex/latex/prosper/green-bullet-on-blue-wc.ps
%{_texmfdistdir}/tex/latex/prosper/green-bullet-on-blue.ps
%{_texmfdistdir}/tex/latex/prosper/green-bullet-on-white.ps
%{_texmfdistdir}/tex/latex/prosper/green-inverted-arrow.ps
%{_texmfdistdir}/tex/latex/prosper/gyom.ps
%{_texmfdistdir}/tex/latex/prosper/prosper-structure.eps
%{_texmfdistdir}/tex/latex/prosper/prosper.cls
%{_texmfdistdir}/tex/latex/prosper/red-bullet-on-blue-wc.ps
%{_texmfdistdir}/tex/latex/prosper/red-bullet-on-blue.ps
%{_texmfdistdir}/tex/latex/prosper/red-bullet-on-white.ps
%{_texmfdistdir}/tex/latex/prosper/red-inverted-arrow.ps
%{_texmfdistdir}/tex/latex/prosper/rico.ps
%{_texmfdistdir}/tex/latex/prosper/rico_bullet1.ps
%{_texmfdistdir}/tex/latex/prosper/rico_bullet2.ps
%{_texmfdistdir}/tex/latex/prosper/rico_bullet3.ps
%{_texmfdistdir}/tex/latex/prosper/rotation.ps
%{_texmfdistdir}/tex/latex/prosper/rule-glow.ps
%{_texmfdistdir}/tex/latex/prosper/yellow-bullet-on-blue-wc.ps
%{_texmfdistdir}/tex/latex/prosper/yellow-bullet-on-blue.ps
%{_texmfdistdir}/tex/latex/prosper/yellow-bullet-on-white.ps
%doc %{_texmfdistdir}/doc/latex/prosper/Example.tex
%doc %{_texmfdistdir}/doc/latex/prosper/ExampleAlienglow.tex
%doc %{_texmfdistdir}/doc/latex/prosper/ExampleAutumn.tex
%doc %{_texmfdistdir}/doc/latex/prosper/ExampleAzure.tex
%doc %{_texmfdistdir}/doc/latex/prosper/ExampleContemporain.tex
%doc %{_texmfdistdir}/doc/latex/prosper/ExampleDarkblue.tex
%doc %{_texmfdistdir}/doc/latex/prosper/ExampleFrames.tex
%doc %{_texmfdistdir}/doc/latex/prosper/ExampleLignesbleues.tex
%doc %{_texmfdistdir}/doc/latex/prosper/ExampleNuanceGris.tex
%doc %{_texmfdistdir}/doc/latex/prosper/ExampleTroisPoints.tex
%doc %{_texmfdistdir}/doc/latex/prosper/FAQ
%doc %{_texmfdistdir}/doc/latex/prosper/NEWS
%doc %{_texmfdistdir}/doc/latex/prosper/README
%doc %{_texmfdistdir}/doc/latex/prosper/green-bullet-on-blue-wc.gif
%doc %{_texmfdistdir}/doc/latex/prosper/green-bullet-on-blue.gif
%doc %{_texmfdistdir}/doc/latex/prosper/green-bullet-on-white.gif
%doc %{_texmfdistdir}/doc/latex/prosper/gyom.tex
%doc %{_texmfdistdir}/doc/latex/prosper/manifest.txt
%doc %{_texmfdistdir}/doc/latex/prosper/prosper-doc.pdf
%doc %{_texmfdistdir}/doc/latex/prosper/prosper-doc.tex
%doc %{_texmfdistdir}/doc/latex/prosper/prosper-template.jpg
%doc %{_texmfdistdir}/doc/latex/prosper/prosper-tour.pdf
%doc %{_texmfdistdir}/doc/latex/prosper/prosper-tour.tex
%doc %{_texmfdistdir}/doc/latex/prosper/red-bullet-on-blue-wc.gif
%doc %{_texmfdistdir}/doc/latex/prosper/red-bullet-on-blue.gif
%doc %{_texmfdistdir}/doc/latex/prosper/red-bullet-on-white.gif
%doc %{_texmfdistdir}/doc/latex/prosper/rico.tex
%doc %{_texmfdistdir}/doc/latex/prosper/rotation.tex
%doc %{_texmfdistdir}/doc/latex/prosper/yellow-bullet-on-blue-wc.gif
%doc %{_texmfdistdir}/doc/latex/prosper/yellow-bullet-on-blue.gif
%doc %{_texmfdistdir}/doc/latex/prosper/yellow-bullet-on-white.gif
#- source
%doc %{_texmfdistdir}/source/latex/prosper/AUTHORS
%doc %{_texmfdistdir}/source/latex/prosper/ChangeLog
%doc %{_texmfdistdir}/source/latex/prosper/INSTALL
%doc %{_texmfdistdir}/source/latex/prosper/TODO
%doc %{_texmfdistdir}/source/latex/prosper/compilation.fig
%doc %{_texmfdistdir}/source/latex/prosper/prosper-structure.fig
%doc %{_texmfdistdir}/source/latex/prosper/prosper.png
%doc %{_texmfdistdir}/source/latex/prosper/prosper.ui
%doc %{_texmfdistdir}/source/latex/prosper/seminar-bg2-lepennec.fix

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
