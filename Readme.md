# 🧠 AI Resume Parser using spaCy (Custom NER)

This project is a **Resume Parsing System** built using a **custom spaCy Named Entity Recognition (NER) model**.  
It automatically extracts structured information from resumes with high accuracy.

---

### ✨ Features
- ✅ Custom spaCy NER Model trained on real-like data
- ✅ Extracts key resume fields
- ✅ Supports PDF & DOCX text extraction (coming soon)
- ✅ Production-ready folder structure
- ✅ Easy training pipeline for improving model accuracy

---

### 🧾 Extracted Entities
| Entity | Description |
|-------|------------|
| NAME | Candidate's full name |
| DEGREE | Education / Qualification |
| COLLEGE | University / Institute |
| EXPERIENCE | Work experience duration |
| SKILLS | Technical & soft skills |
| ORG | Past / current company |
| EMAIL | Email address |
| PHONE | Phone number |
| CTC | Salary information |

> Custom dataset manually created for professional accuracy.

---

### ⚙️ Tech Stack
| Component | Technology |
|----------|------------|
| Language | Python |
| NLP Engine | spaCy |
| Model | Custom NER |
| App | CLI now, UI soon (FastAPI / Streamlit) |

---

### 📂 Project Structure
```
resume-parser-spacy/
 ┣ app/
 ┃ ┗ app.py
 ┣ model/        # trained model 
 ┣ data/         # training data (local only)
 ┣ README.md
 ┣ requirements.txt
 ┗ .gitignore
```

---

### 🚀 How to Run

#### 1️⃣ Clone repo
```sh
git clone https://github.com/Trashu470/resume-parser-spacy.git
cd resume-parser-spacy
```

#### 2️⃣ Install dependencies
```sh
pip install -r requirements.txt
```

#### 3️⃣ Add your model
Place trained model folder inside `/model/`

#### 4️⃣ Run the script
```sh
python app/app.py
```

---

### 🎓 Training Command (Developer reference)
```sh
python -m spacy train config.cfg --output ./model --paths.train ./data/train.spacy --paths.dev ./data/valid.spacy
```

---

### 🛠️ Future Upgrades
- ✅ API + Web UI (FastAPI)
- ⏳ Resume upload + parse in browser
- ⏳ Live demo deployment (Render/HF Spaces)
- ⏳ More NER entities (Location, LinkedIn, GitHub)

---

### 👤 Author
**Trashu**

Focused on building **NLP products & freelancing solutions**.

---

### ⭐ Support
If you like this project, please give it a **⭐ on GitHub**!
