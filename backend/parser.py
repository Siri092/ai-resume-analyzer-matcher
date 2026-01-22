# parser.py
import re

def parse_resume(text: str) -> dict:
    """
    Parses resume text and extracts skills, projects, and experience.
    Returns a dictionary.
    """
    sections = {"skills": [], "projects": [], "experience": []}
    text = text.lower()  # Normalize to lowercase

    # Extract skills section
    skills_match = re.search(r"skills:(.*?)(projects:|experience:|$)", text, re.S)
    if skills_match:
        sections["skills"] = [s.strip() for s in skills_match.group(1).split(",") if s.strip()]

    # Extract projects section
    projects_match = re.search(r"projects:(.*?)(experience:|$)", text, re.S)
    if projects_match:
        sections["projects"] = [p.strip() for p in projects_match.group(1).split(",") if p.strip()]

    # Extract experience section
    experience_match = re.search(r"experience:(.*)", text, re.S)
    if experience_match:
        sections["experience"] = [e.strip() for e in experience_match.group(1).split(",") if e.strip()]

    # Print output for debugging
    print("PARSED RESUME:", sections)
    return sections


def parse_job_description(text: str) -> dict:
    """
    Parses job description text and extracts required skills and responsibilities.
    Returns a dictionary.
    """
    data = {"required_skills": [], "responsibilities": []}
    text = text.lower()  # Normalize

    # Extract required skills
    skills_match = re.search(r"required skills:(.*?)(responsibilities:|$)", text, re.S)
    if skills_match:
        data["required_skills"] = [s.strip() for s in skills_match.group(1).split(",") if s.strip()]

    # Extract responsibilities
    resp_match = re.search(r"responsibilities:(.*)", text, re.S)
    if resp_match:
        data["responsibilities"] = [r.strip() for r in resp_match.group(1).split(",") if r.strip()]

    # Print output for debugging
    print("PARSED JOB DESCRIPTION:", data)
    return data


# Quick test when running this file directly
if __name__ == "__main__":
    sample_resume = "Skills: Python, FastAPI, SQL, Projects: Resume Matcher, Experience: 2 years at XYZ"
    sample_jd = "Required Skills: Python, FastAPI, SQL, Responsibilities: Build APIs, Work with DB"
    
    parse_resume(sample_resume)
    parse_job_description(sample_jd)
