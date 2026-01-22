from gap_analyzer import weak, critical_missing

print("\n📌 PROJECT-BASED LEARNING RECOMMENDATIONS")
print("---------------------------------------")

project_map = {
    "rest apis": {
        "title": "REST API Development Project",
        "description": (
            "Build a RESTful API using Flask or FastAPI that supports CRUD "
            "operations and integrates with a database."
        )
    },
    "docker": {
        "title": "Dockerized Application Project",
        "description": (
            "Containerize an existing Python application using Docker "
            "and deploy it locally."
        )
    }
}

missing_skills = weak + critical_missing

if not missing_skills:
    print("✅ No learning projects required. Candidate is job-ready.")
else:
    for skill in missing_skills:
        if skill in project_map:
            project = project_map[skill]
            print(f"\n🔧 Skill Gap: {skill.upper()}")
            print(f"📂 Suggested Project: {project['title']}")
            print(f"📝 Description: {project['description']}")
        else:
            print(f"\n🔧 Skill Gap: {skill.upper()}")
            print("📂 Suggested Project: Build a small hands-on project to demonstrate this skill.")
