
from docx import Document

def extract_jd_text(file_path):
    """
    Extract text from a Word (.docx) job description file
    """
    doc = Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return "\n".join(full_text)


if __name__ == "__main__":
    jd_text = extract_jd_text("data/job_descriptions/job1.docx")
    print(jd_text[:1000]) 
