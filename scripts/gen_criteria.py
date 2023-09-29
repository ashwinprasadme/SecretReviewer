import json

with open("criteria.json", "r") as f:
    data = json.load(f)

# Start LaTeX Beamer document
latex_code = """
\\documentclass[handout]{beamer}
\\usepackage{framed}
\\usepackage{geometry}
\\usetheme{metropolis}
\\geometry{paperwidth=7.5cm,paperheight=4.3cm}
\\setbeamertemplate{navigation symbols}{}
\\setbeamertemplate{frametitle}[default][center]
\\setbeamersize{text margin left=5pt,text margin right=5pt}
\\usefonttheme{serif}
\\setbeamerfont{frametitle}{size=\Large}
\\definecolor{codegreen}{rgb}{0,0.6,0}
\\definecolor{codered}{rgb}{0.6,0,0}
\\newenvironment{greenframe}{%
	\\setbeamercolor{frametitle}{bg=codegreen}
	\\begin{frame}
	}{%
	\\end{frame}
}
\\setbeamercolor{frametitle}{bg=codered}
\\begin{document}
"""

# Write criteria to reject
for criterion in data["CriteriaToReject"]:
    latex_code += "\\begin{frame}[plain]\n\\centering\n"
    latex_code += f"\\frametitle{{{criterion['Criterion']}}}\n"
    latex_code += f"\\Large\\textbf{{{criterion['Description']}}}\n"
    latex_code += "\\end{frame}\n"

# Write criteria to accept
for criterion in data["CriteriaToAccept"]:
    latex_code += "\\begin{greenframe}[plain]\n\\centering\n"
    latex_code += f"\\frametitle{{{criterion['Criterion']}}}\n"
    latex_code += f"\\Large\\textbf{{{criterion['Description']}}}\n"
    latex_code += "\\end{greenframe}\n"

# End LaTeX document
latex_code += "\\end{document}\n"

# Write LaTeX code to file
with open("Criteria_to_Accept_and_Reject_Beamer.tex", "w") as f:
    f.write(latex_code)

print("Beamer LaTeX document generated!")
