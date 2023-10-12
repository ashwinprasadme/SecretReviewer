import requests
from bs4 import BeautifulSoup

TOTAL_PAPERS = 18


def load_user_ids_from_config(filename):
    with open(filename, "r") as file:
        user_ids = [line.strip() for line in file.readlines() if line.strip()]
    return user_ids


def get_top_papers(user_id):
    base_url = f"https://scholar.google.com/citations?user={user_id}&hl=en"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(base_url, headers=headers)
    if response.status_code != 200:
        print(f"Error fetching data for user ID {user_id}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.find_all("tr", class_="gsc_a_tr")

    papers = []
    for article in articles[:15]:  # top 15
        title = article.find("a", class_="gsc_a_at").text
        papers.append(title)

    return papers


user_ids = load_user_ids_from_config("google_scholar_ids.txt")
all_papers = {}
for user_id in user_ids:
    all_papers[user_id] = get_top_papers(user_id)

selected_papers = []
seen_papers = set()

# Loop through authors to select the top paper from each, ensuring no repeats
while len(selected_papers) < TOTAL_PAPERS and any(all_papers.values()):
    for user_id, papers in list(
        all_papers.items()
    ):  # Using list() to allow in-loop dict modifications
        if not papers:
            continue

        # Pick the top paper that hasn't been selected before
        while papers and papers[0] in seen_papers:
            papers.pop(0)

        if papers:
            selected_paper = papers.pop(0)
            selected_papers.append(selected_paper)
            seen_papers.add(selected_paper)

        # Remove the user from dict if no more papers left
        if not papers:
            del all_papers[user_id]

        if len(selected_papers) == TOTAL_PAPERS:
            break

if len(selected_papers) < TOTAL_PAPERS:
    print(f"ERROR: Insufficient unique top papers to select {TOTAL_PAPERS}. Exiting.")
    exit()

print(
    f"Selected {TOTAL_PAPERS} top papers uniformly across authors without repetition:"
)
for paper in selected_papers:
    print(paper)


# Start LaTeX Beamer document
latex_code = """
\\documentclass{beamer}
\\usepackage{framed}
\\usepackage{geometry}
\\usepackage{lipsum}  % to generate placeholder text (lines)
\\usepackage{graphicx}
\\usetheme{metropolis}
\\geometry{paperwidth=6.25cm,paperheight=9cm}
\\setbeamertemplate{navigation symbols}{}
\\setbeamertemplate{frametitle}[default][center]
\\setbeamersize{text margin left=5pt,text margin right=5pt}
\\usefonttheme{serif}
\\setbeamerfont{frametitle}{size=\\footnotesize}
\\definecolor{codegreen}{rgb}{0,0.6,0}
\\definecolor{codered}{rgb}{0.6,0,0}
\\setbeamercolor{frametitle}{bg=white,fg=black}
\\setbeamertemplate{background}{
    \\includegraphics[width=\\paperwidth,height=\\paperheight]{acm_background.jpg}
}
\\addtolength{\\headsep}{0.35cm}
\\begin{document}
"""

for paper in selected_papers:
    latex_code += "\\begin{frame}[plain]\n"
    latex_code += f"\\frametitle{{{paper}}}\n"
    # If you still want placeholder text, you can add it here.
    latex_code += "\\end{frame}\n"


# End LaTeX document
latex_code += "\\end{document}\n"

# Write LaTeX code to file
with open("Papers_Beamer.tex", "w") as f:
    f.write(latex_code)

print("Beamer LaTeX document generated!")
