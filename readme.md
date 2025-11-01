# Resume Parser (spaCy NER)

This project extracts information from resumes using:
- Custom spaCy NER model (Google Drive auto-download)
- PDF text extraction via pdfplumber
- Streamlit Web UI

## Entities Extracted
- Name / Person
- Degree
- College/University
- Experience
- Skills
- CTC
- Organization
- Email
- Phone

## How It Works
1. Upload a PDF resume or paste resume text
2. Model downloads automatically on first use
3. Output is displayed in JSON format

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app/app.py
