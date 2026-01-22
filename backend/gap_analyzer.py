from backend.skill_weights import SKILL_IMPORTANCE


def analyze_skill_gaps(resume_data, jd_data):
    resume_skills = set(resume_data["skills"])
    required_skills = set(jd_data["required_skills"])

    strong, weak, critical_missing = [], [], []

    for skill in required_skills:
        importance = SKILL_IMPORTANCE.get(skill, "medium")
        if skill in resume_skills:
            strong.append(skill)
        else:
            if importance == "high":
                critical_missing.append(skill)
            else:
                weak.append(skill)

    return strong, weak, critical_missing
