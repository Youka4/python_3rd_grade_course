from latex_generators import generate_latex_table, generate_latex_image

from generate_pdf import generate_pdf


sample_data = [
    ["Name", "Surname", "Nationality", "Team"],
    ["Julian", "Alvarez", "Argentinian", "Atletico Madrid"],
    ["Lionel", "Messi", "Argentinian", "Inter Miami"],
    ["Matvey", "Safonov", "Russian", "PSG"],
    ["Bukayo", "Saka", "English", "Arsenal"]
]


latex_table = generate_latex_table(sample_data)

latex_image = generate_latex_image("hand.png")

full_latex_doc = "\n".join([
    "\\documentclass{article}",
    "\\usepackage[utf8]{inputenc}",
    "\\usepackage{graphicx}",
    "\\begin{document}",
    latex_table,
    latex_image,
    "\\end{document}"
])

generate_pdf(full_latex_doc, tex_filename="artifacts/task_2.tex")

