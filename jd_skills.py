
from docx import Document

def extract_jd_skills(jd_path):
    """
    Extract skills from a job description DOCX file
    """
    
    doc = Document(jd_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + " "
    
    
    skills = [skill.strip().lower() for skill in text.split(",") if skill.strip()]
    return skills


if __name__ == "__main__":
    jd_skills = extract_jd_skills("data/job_descriptions/job1.docx")
    print("Job Description Skills:", jd_skills)
