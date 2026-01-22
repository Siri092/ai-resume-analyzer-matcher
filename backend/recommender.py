from parser import parse_resume
from gap_analyzer import strong, weak, critical_missing

with open("data/resume.txt", "r") as f:
    resume_text = f.read()

resume_data = parse_resume(resume_text)

print("\n📝 RESUME IMPROVEMENT SUGGESTIONS")
print("--------------------------------")

if "rest apis" in weak or "rest apis" in critical_missing:
    if resume_data["projects"]:
        project = resume_data["projects"][0]
        suggestion = (
            f"Enhance your project description by adding a bullet like:\n"
            f"• Designed RESTful APIs to support features in '{project.title()}'"
        )
    else:
        suggestion = (
            "Add a project demonstrating REST API development using Python frameworks."
        )

    print("\n🔧 REST API Suggestion:")
    print(suggestion)
else:
    print("✅ No resume improvement needed for REST APIs")
