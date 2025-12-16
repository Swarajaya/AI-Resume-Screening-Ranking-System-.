import streamlit as st
from ranker import rank_candidates, extract_text_from_pdf, extract_text_from_docx
from src.llm_helper import llm_evaluate_candidate
import os

st.title("🚀 AI Resume Screening & Ranking System")

jd_file = st.file_uploader("Upload Job Description (PDF or DOCX)", type=["pdf", "docx"])

resume_files = st.file_uploader("Upload Resumes (PDF or DOCX)", type=["pdf", "docx"], accept_multiple_files=True)

if st.button("Rank Resumes"):
    if not jd_file or not resume_files:
        st.warning("Please upload both Job Description and Resumes!")
    else:
        os.makedirs("uploads/resumes", exist_ok=True)

        if jd_file.type == "application/pdf":
            jd_text = extract_text_from_pdf(jd_file).lower()
        elif jd_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            jd_text = extract_text_from_docx(jd_file).lower()
        else:
            st.error("❌ Unsupported JD file type.")
            jd_text = ""

        if not jd_text.strip():
            st.error("❌ Job Description is empty or unreadable.")
        else:
            for resume in resume_files:
                resume_path = f"uploads/resumes/{resume.name}"
                with open(resume_path, "wb") as f:
                    f.write(resume.getbuffer())

            ranked_candidates = rank_candidates("uploads/resumes", jd_text, jd_is_text=True)

            st.success("✅ Resumes Ranked Successfully!")
            st.write("### Ranked Candidates:")

            if ranked_candidates:
                max_score = max([s["score"] for _, s in ranked_candidates]) or 1
                for i, (candidate, data) in enumerate(ranked_candidates, start=1):
                    score = data["score"]
                    matched_skills = data.get("matched_skills", [])
                    st.write(f"{i}. **{candidate}** | Score: {score} | Matched Skills: {matched_skills}")
                    st.progress(min(score / max_score, 1.0))

                    try:
                        resume_path = f"uploads/resumes/{candidate}"
                        candidate_text = ""
                        if candidate.endswith(".pdf"):
                            candidate_text = extract_text_from_pdf(resume_path)
                        elif candidate.endswith(".docx"):
                            candidate_text = extract_text_from_docx(resume_path)

                        if candidate_text:
                            ai_eval = llm_evaluate_candidate(candidate_text, jd_text)
                            st.write(f"💡 AI Explanation: {ai_eval}")
                    except Exception as e:
                        st.write(f"AI Evaluation could not be generated: {e}")
            else:
                st.warning("No valid resumes were ranked.")
