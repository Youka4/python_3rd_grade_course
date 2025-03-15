def generate_latex_table(data):
    """
    Генерирует строку с кодом LaTeX для таблицы.

    :param data: Двойной список (список списков), содержащий строки таблицы
    :return: Строка с валидным кодом LaTeX
    """
    if not data or not all(isinstance(row, list) for row in data):
        raise ValueError("Invalid data")

    column_count = len(data[0])
    header = " | ".join(["c"] * column_count)

    latex_code = ["\\documentclass{article}", "\\usepackage[utf8]{inputenc}", "\\begin{document}", "\\begin{table}[h]",
                  "\\centering", "\\begin{tabular}{|" + header + "|}", "\\hline",
                  " & ".join(map(str, data[0])) + " \\\\", "\\hline"]

    for row in data[1:]:
        latex_code.append(" & ".join(map(str, row)) + " \\\\")
    latex_code.append("\\hline")

    latex_code.append("\\end{tabular}")
    latex_code.append("\\end{table}")
    latex_code.append("\\end{document}")

    return "\n".join(latex_code)
