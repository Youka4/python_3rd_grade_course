FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    texlive \
    texlive-latex-extra \
    texlive-fonts-recommended \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir uv
RUN uv pip install --system -r requirements.txt

CMD ["python", "task_2.py"]
