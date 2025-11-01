import streamlit as st
import spacy
import pdfplumber
import re
import os, gdown, zipfile

MODEL_DIR = "best_ner_model"

if not os.path.exists(MODEL_DIR):
    st.warning("Downloading model... first time only, wait 1-2 minutes.")
    url = "https://drive.google.com/uc?id=1jbtkcctB7e-fw6Nv2hIfqrgh1iPmsUCP"
    gdown.download(url, "model.zip", quiet=False)

    with zipfile.ZipFile("model.zip", 'r') as zip_ref:
        zip_ref.extractall(".")  # model extracted to best_ner_model folder

nlp = spacy.load(MODEL_DIR)

def extract_email_phone(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'\+91[\-\s]?[6-9]\d{9}|0[6-9]\d{9}|\b[6-9]\d{9}\b'
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    return list(set(emails)), list(set(phones))

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def parse_resume(text):
    doc = nlp(text)
    entities = {"PERSON": [], "DEGREE": [], "COLLEGE": [], "EXPERIENCE": [], "SKILLS": [], "CTC": [], "ORG": []}
    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].append(ent.text)

    emails, phones = extract_email_phone(text)

    return {
        "Person": list(set(entities["PERSON"])),
        "Degree": list(set(entities["DEGREE"])),
        "College": list(set(entities["COLLEGE"])),
        "Experience": list(set(entities["EXPERIENCE"])),
        "Skills": list(set(entities["SKILLS"])),
        "Ctc": list(set(entities["CTC"])),
        "Org": list(set(entities["ORG"])),
        "Email": emails,
        "Phone": phones,
    }

st.title("Resume Parser Demo ( NER )")

option = st.radio("Select input type:", ["Upload PDF", "Paste Text"])

if option == "Upload PDF":
    pdf_file = st.file_uploader("Upload Resume PDF", type="pdf")
    if pdf_file:
        text = extract_text_from_pdf(pdf_file)
        result = parse_resume(text)
        st.json(result)
else:
    resume_text = st.text_area("Paste Resume Text")
    if st.button("Parse"):
        result = parse_resume(resume_text)
        st.json(result)
