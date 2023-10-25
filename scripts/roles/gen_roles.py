import json

template_start = r"""
\documentclass[handout,8pt]{beamer}
\usepackage{framed}
\usepackage{geometry}
\usetheme{metropolis}
\usepackage{tikz}
\usetikzlibrary{shadows}
\geometry{paperwidth=10.2cm,paperheight=6.8cm}
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{frametitle}[default][center]
\setbeamersize{text margin left=15pt,text margin right=15pt}
\usefonttheme{serif}
\setbeamerfont{frametitle}{size=\Huge}
\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codered}{rgb}{0.6,0,0}
\newenvironment{greenframe}{%
	\setbeamercolor{frametitle}{bg=codegreen}
	\begin{frame}
	}{%
	\end{frame}
}
\setbeamercolor{frametitle}{bg=codered}
\usepackage{graphicx}
\usepackage[most]{tcolorbox}
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{frametitle}{%
	\nointerlineskip%
	\begin{beamercolorbox}[wd=\paperwidth,ht=2.5ex,dp=1.5ex]{frametitle}
		\centering
		\hspace*{1ex}\insertframetitle%
	\end{beamercolorbox}%
}
\begin{document}
"""

frame_template = r"""
\begin{{{frame_type}}}[plain]{{{title}}}
    \begin{{columns}}
        \begin{{column}}{{0.5\textwidth}}
            \centering
            \tikz\node[inner sep=0pt, draw=none, drop shadow={{shadow xshift=1mm,shadow yshift=-1mm,fill=black, opacity=0.3}}]{{
                \includegraphics[width=\linewidth]{{{image_path}}}
            }};
        \end{{column}}
        \begin{{column}}{{0.5\textwidth}}
            \begin{{tcolorbox}}[left=2pt,right=2pt,colback=white,colframe={framecolor},fonttitle=\bfseries, title={name}]
                {description}
            \end{{tcolorbox}}
        \end{{column}}
    \end{{columns}}
\end{{{frame_type}}}
"""


template_end = r"""
\end{document}
"""


def json_to_latex(data):
    latex_output = template_start

    for role in data["RejectingReviewers"]:
        name = role.get("name", "")
        if name == "Reviewer 2":
            title = "Reviewer 2"
        else:
            title = "Rejecting Reviewer"
        image_path = f"images/br_role_{role.get('id', '')}"
        description = role.get("description", "")
        latex_output += frame_template.format(
            name=name,
            image_path=image_path,
            description=description,
            title=title,
            framecolor="codered",
            frame_type="frame",
        )

    for role in data["AcceptingReviewers"]:
        name = role.get("name", "")
        title = "Accepting Reviewer"
        image_path = f"images/gr_role_{role.get('id', '')}"
        description = role.get("description", "")
        latex_output += frame_template.format(
            name=name,
            image_path=image_path,
            description=description,
            title=title,
            framecolor="codegreen",
            frame_type="greenframe",
        )
    latex_output += template_end

    return latex_output


with open("role_description.json", "r") as f:
    json_input = json.load(f)

latex_code = json_to_latex(json_input)

# Write LaTeX code to file
with open("roles_Beamer.tex", "w") as f:
    f.write(latex_code)
