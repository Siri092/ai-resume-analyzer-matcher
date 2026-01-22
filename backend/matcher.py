def calculate_ats_score(resume_data, jd_data):
    resume_skills = set(resume_data["skills"])
    required_skills = set(jd_data["required_skills"])

    matched_skills = list(resume_skills.intersection(required_skills))
    missing_skills = list(required_skills - resume_skills)

    match_score = (len(matched_skills) / len(required_skills)) * 100 if required_skills else 0

    return match_score, matched_skills, missing_skills
