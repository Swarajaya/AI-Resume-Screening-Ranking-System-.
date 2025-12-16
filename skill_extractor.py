from skills_list import SKILLS

def extract_skills(text):
    """
    Extract skills from text using keyword matching
    """
    text = text.lower()  
    found_skills = [skill for skill in SKILLS if skill.lower() in text]
    return found_skills



if __name__ == "__main__":
    sample_text = """
    Experienced Python developer with Machine Learning skills.
    Familiar with SQL, Data Analysis, and Django framework.
    """
    skills = extract_skills(sample_text)
    print("Extracted Skills:", skills)
from resume_parser import parse_all_resumes  

def extract_skills_from_resumes(resume_folder):
    """
    Extract skills from all resumes in a folder
    """
    resumes_texts = parse_all_resumes(resume_folder)
    resumes_skills = {}

    for name, text in resumes_texts.items():
        resumes_skills[name] = extract_skills(text)  

    return resumes_skills



if __name__ == "__main__":
    skills_dict = extract_skills_from_resumes("data/resumes")
    for resume, skills in skills_dict.items():
        print(f"{resume}: {skills}")
