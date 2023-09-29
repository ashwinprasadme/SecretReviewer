import json

with open("criteria.json", "r") as f:
    data = json.load(f)

# Start LaTeX Beamer document
latex_code = """
\\documentclass[handout]{beamer}
\\usepackage{pgfpages}
\\usepackage{framed}
\\usepackage{geometry}
\\usetheme{metropolis}
\\geometry{paperwidth=8cm,paperheight=5cm}
\\setbeamertemplate{navigation symbols}{}
\\setbeamertemplate{frametitle}[default][center]
\\setbeamersize{text margin left=5pt,text margin right=5pt}
\\usefonttheme{serif}
\\setbeamerfont{frametitle}{size=\Large}
\\pgfpagesuselayout{8 on 1}[letterpaper, border shrink=5mm]
\\pgfpageslogicalpageoptions{1}{border code=\\pgfusepath{stroke}}
\\pgfpageslogicalpageoptions{2}{border code=\\pgfusepath{stroke}}
\\pgfpageslogicalpageoptions{3}{border code=\\pgfusepath{stroke}}
\\pgfpageslogicalpageoptions{4}{border code=\\pgfusepath{stroke}}
\\pgfpageslogicalpageoptions{5}{border code=\\pgfusepath{stroke}}
\\pgfpageslogicalpageoptions{6}{border code=\\pgfusepath{stroke}}
\\pgfpageslogicalpageoptions{7}{border code=\\pgfusepath{stroke}}
\\pgfpageslogicalpageoptions{8}{border code=\\pgfusepath{stroke}}
\\begin{document}
"""

# Write criteria to reject
for criterion in data["CriteriaToReject"]:
    latex_code += "\\begin{frame}[plain]\n\\centering\n"
    latex_code += f"\\frametitle{{{criterion['Criterion']}}}\n"
    latex_code += "\\begin{framed}\n"
    latex_code += f"\\Large\\textbf{{{criterion['Description']}}}\n"
    latex_code += "\\end{framed}\n"
    latex_code += "\\end{frame}\n"

# Write criteria to accept
for criterion in data["CriteriaToAccept"]:
    latex_code += "\\begin{frame}[plain]\n\\centering\n"
    latex_code += f"\\frametitle{{{criterion['Criterion']}}}\n"
    latex_code += "\\begin{framed}\n"
    latex_code += f"\\Large\\textbf{{{criterion['Description']}}}\n"
    latex_code += "\\end{framed}\n"
    latex_code += "\\end{frame}\n"

# End LaTeX document
latex_code += "\\end{document}\n"

# Write LaTeX code to file
with open("Criteria_to_Accept_and_Reject_Beamer.tex", "w") as f:
    f.write(latex_code)

print("Beamer LaTeX document generated!")
