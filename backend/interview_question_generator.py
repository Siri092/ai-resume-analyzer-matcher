from gap_analyzer import weak, critical_missing

print("\n🎤 PERSONALIZED INTERVIEW QUESTIONS")
print("----------------------------------")

question_bank = {
    "rest apis": [
        "What is a REST API and how does it work?",
        "How would you design a REST API for a resume-job matching system?",
        "Explain HTTP methods and status codes with examples."
    ],
    "docker": [
        "What is Docker and why is it used?",
        "How would you dockerize a Python application?"
    ]
}

missing_skills = weak + critical_missing

if not missing_skills:
    print("✅ No interview questions needed. Candidate is fully prepared.")
else:
    for skill in missing_skills:
        print(f"\n🔧 Skill Focus: {skill.upper()}")
        if skill in question_bank:
            for q in question_bank[skill]:
                print(f"❓ {q}")
        else:
            print("❓ Explain this skill and how you have used it in a project.")
