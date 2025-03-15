from latex_generators import generate_latex_table

if __name__ == "__main__":
    sample_data = [
        ["Name", "Surname", "Nationality", "Team"],
        ["Julian", "Alvarez", "Argentinian", "Atletico Madrid"],
        ["Lionel", "Messi", "Argentinian", "Inter Miami"],
        ["Matvey", "Safonov", "Russian", "PSG"],
        ["Bukayo", "Saka", "English", "Arsenal"]
    ]
    latex_output = generate_latex_table(sample_data)

    with open("artifacts/task_1.tex", "w", encoding="utf-8") as f:
        f.write(latex_output)
