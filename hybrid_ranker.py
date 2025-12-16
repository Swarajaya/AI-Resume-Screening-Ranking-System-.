from matcher import match_resumes
from llm_ranker import get_llm_score
from jd_parser import extract_jd_text
from resume_parser import parse_all_resumes

def hybrid_rank(resume_folder, jd_path):
    skill_scores = match_resumes(resume_folder, jd_path)
    resumes_text = parse_all_resumes(resume_folder)
    jd_text = extract_jd_text(jd_path)

    final_scores = {}

    for resume, data in skill_scores.items():
        llm_score = get_llm_score(resumes_text[resume], jd_text)
        final_score = (0.7 * data["score"]) + (0.3 * llm_score)

        final_scores[resume] = {
            "final_score": round(final_score, 2),
            "skill_score": data["score"],
            "llm_score": llm_score,
            "matched_skills": data["matched_skills"]
        }

    return final_scores



if __name__ == "__main__":
    results = hybrid_rank("data/resumes", "data/job_descriptions/job1.docx")
    for resume, data in results.items():
        print(resume, data)
