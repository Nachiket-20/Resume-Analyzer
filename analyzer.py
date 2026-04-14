import re
from parser import extract_text_from_pdf

# -------------------------------
# Skills Database
# -------------------------------
SKILLS_DB = [
    "python", "java", "c++", "machine learning", "deep learning",
    "data science", "sql", "html", "css", "javascript",
    "tensorflow", "pandas", "numpy", "react"
]

# -------------------------------
# Extract Skills from Text
# -------------------------------
def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        if re.search(r"\b" + re.escape(skill) + r"\b", text):
            found_skills.append(skill)

    return found_skills

# -------------------------------
# Calculate ATS Score
# -------------------------------
def calculate_ats_score(resume_skills, job_skills):
    matched = set(resume_skills) & set(job_skills)
    
    if len(job_skills) == 0:
        score = 0
    else:
        score = (len(matched) / len(job_skills)) * 100

    return score, matched

# -------------------------------
# Generate Suggestions
# -------------------------------
def generate_suggestions(score, missing_skills):
    suggestions = []

    if score < 50:
        suggestions.append("Your resume is not well aligned with the job description.")
    elif score < 75:
        suggestions.append("Your resume is moderately aligned. Consider improving it.")
    else:
        suggestions.append("Your resume is well aligned with the job description.")

    if missing_skills:
        suggestions.append("Consider adding these skills: " + ", ".join(missing_skills))

    suggestions.append("Use clear project descriptions and quantify achievements.")
    suggestions.append("Ensure your resume is properly formatted and ATS-friendly.")

    return suggestions

# -------------------------------
# MAIN PROGRAM
# -------------------------------
if __name__ == "__main__":
    # Step 1: Read Resume
    resume_path = "sample_resume.pdf"
    resume_text = extract_text_from_pdf(resume_path)

    # Step 2: Extract Resume Skills
    resume_skills = extract_skills(resume_text)

    # Step 3: Define Job Description
    job_description = """
    Looking for a candidate with Python, Machine Learning, SQL, and Deep Learning skills.
    """

    # Step 4: Extract Job Skills
    job_skills = extract_skills(job_description)

    # Step 5: Calculate ATS Score
    score, matched = calculate_ats_score(resume_skills, job_skills)

    # Step 6: Find Missing Skills
    missing_skills = set(job_skills) - set(resume_skills)

    # Step 7: Generate Suggestions
    suggestions = generate_suggestions(score, missing_skills)

    # -------------------------------
    # OUTPUT
    # -------------------------------
    print("\n===== ATS SCORE =====\n")
    print(f"Score: {score:.2f}%")
    print("Matched Skills:", matched)
    print("Missing Skills:", missing_skills)

    print("\n===== SUGGESTIONS =====\n")
    for s in suggestions:
        print("-", s)