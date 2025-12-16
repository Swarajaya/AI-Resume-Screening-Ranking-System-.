---
title: AI Resume Screening SaaS
emoji: 🤖
colorFrom: #4CAF50
colorTo: #81C784
sdk: streamlit
sdk_version: "1.26.0"
app_file: app.py
pinned: true
---

# 🚀 AI Resume Screening & Ranking System (SaaS)

An **End-to-End AI SaaS application** that screens and ranks resumes based on a job description using **ML + NLP + LLM**.  
Built with **Python**, deployed with **Streamlit**, and powered by **AI for candidate matching**.

---

## 🔍 Features

- Upload multiple resumes (PDF)  
- Upload job description (PDF)  
- Automatic **skill extraction** from resumes  
- Compare candidate skills with job description  
- Assign **match score (0–1)**  
- **Rank candidates** automatically  
- Optional: **AI explanation** for candidate suitability (LLM)  
- Optional: **Download ranked results**  

---

## 🛠 Tech Stack

- **Python** – Main language  
- **Streamlit** – Frontend SaaS app  
- **PyPDF2** – PDF text extraction  
- **Pandas / NumPy / scikit-learn** – ML & data processing  
- **spaCy** – NLP (optional advanced skill extraction)  
- **OpenAI GPT** – Candidate reasoning (optional)  
- **Hugging Face Spaces** – Deployment  

---

## 📁 Folder Structure

ai-resume-screening/
│
├── app.py # Streamlit app
├── requirements.txt # Dependencies
├── README.md # Project documentation
├── src/ # Python modules
│ ├── resume_parser.py
│ ├── jd_parser.py
│ ├── skill_extractor.py
│ ├── matcher.py
│ ├── ranker.py
│ └── llm_helper.py
├── data/ # Sample demo files (optional)
│ ├── resumes/
│ │ └── sample_resume.pdf
│ └── job_descriptions/
│ └── sample_jd.pdf
└── .gitignore


---

## ⚡ How It Works

1. **Extract text** from uploaded PDFs  
2. **Extract skills** from resumes & job description  
3. **Compare skills** and calculate match score  
4. **Rank candidates** by score  
5. Optional: Generate **AI explanation** for each candidate  

---

## 💻 Usage

1. Clone the repo:

```bash
git clone https://github.com/<your-username>/ai-resume-screening.git
cd ai-resume-screening
