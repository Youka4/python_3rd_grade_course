
import subprocess


def generate_pdf(latex_code, tex_filename):

    with open(tex_filename, "w", encoding="utf-8") as f:
        f.write(latex_code)

    try:
        subprocess.run(["pdflatex", "-output-directory=artifacts", tex_filename], check=True)
        print("success")
    except Exception:
        print("failue")
