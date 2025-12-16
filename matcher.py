
from skill_extractor import extract_skills_from_resumes
from jd_skills import extract_jd_skills

def match_resumes(resume_folder, jd_path):
    resumes_skills = extract_skills_from_resumes(resume_folder)
    jd_skills = extract_jd_skills(jd_path)

    match_scores = {}
    for resume_name, skills in resumes_skills.items():
        matched = set(skills).intersection(set(jd_skills))
        score = len(matched) / len(jd_skills) if jd_skills else 0
        match_scores[resume_name] = {
            "score": round(score, 2),
            "matched_skills": list(matched)
        }
    return match_scores

if __name__ == "__main__":
    scores = match_resumes("data/resumes", "data/job_descriptions/job1.docx")
    for resume, data in scores.items():
        print(f"{resume}: Score={data['score']}, Matched Skills={data['matched_skills']}")
