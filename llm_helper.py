import openai

openai.api_key = "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"

def llm_evaluate_candidate(resume_text, jd_text):
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # Updated model to match new API
            messages=[
                {"role": "system", "content": "You are an HR assistant."},
                {
                    "role": "user",
                    "content": (
                        f"Evaluate this resume:\n{resume_text}\n\n"
                        f"Against this job description:\n{jd_text}\n\n"
                        "Provide a short explanation of why this candidate is suitable or not."
                    )
                }
            ],
            temperature=0.5,
            max_tokens=300
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"AI Evaluation could not be generated: {e}"
