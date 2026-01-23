from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import pdfplumber
from docx import Document

# ML / NLP
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------
# App Setup
# -----------------------
app = FastAPI(title="AI Resume Job Matcher")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------
# Health & Root (IMPORTANT)
# -----------------------
@app.get("/")
def root():
    return {"message": "AI Resume Job Matcher backend is live 🚀"}

@app.get("/healthz")
def health():
    return {"status": "ok"}

# -----------------------
# Skill Keywords
# -----------------------
SKILL_KEYWORDS = [
    "python", "django", "fastapi", "flask", "sql", "postgresql",
    "mongodb", "docker", "aws", "git", "linux", "rest api",
    "microservices", "nlp", "machine learning", "cloud"
]

SKILL_TOOL_MAP = {
    "microservices": ["docker", "kubernetes", "rabbitmq", "kafka", "rest api"],
    "cloud": ["aws", "ec2", "s3", "lambda"],
    "nlp": ["spacy", "transformers"],
    "machine learning": ["scikit-learn", "tensorflow"]
}

# -----------------------
# Request Models
# -----------------------
class MatchRequest(BaseModel):
    resume_text: str
    jd_text: str

# -----------------------
# Helpers
# -----------------------
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join(p.text for p in doc.paragraphs)

def extract_skills(text: str):
    text = text.lower()
    return {skill for skill in SKILL_KEYWORDS if skill in text}

def expand_missing_skills(missing):
    return {skill: SKILL_TOOL_MAP.get(skill, []) for skill in missing}

def ats_readability_check(file):
    issues = []
    score = 100

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            if page.extract_table():
                issues.append("Tables detected")
                score -= 20
            if page.images:
                issues.append("Images detected")
                score -= 10
            text = page.extract_text()
            if not text or len(text.strip()) < 50:
                issues.append("Low readable text")
                score -= 30

    return {"ats_score": max(score, 0), "issues": list(set(issues))}

def smart_skill_match(resume_text: str, jd_text: str):
    resume_text = resume_text.lower()
    jd_text = jd_text.lower()

    base_score = 0
    important_skills = ["docker", "aws", "fastapi", "microservices", "cloud"]

    for skill in important_skills:
        if skill in resume_text and skill in jd_text:
            base_score += 10

    texts = [resume_text, jd_text]
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(texts)
    similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]

    final_score = int(similarity * 60 + base_score)
    return min(final_score, 100)

def generate_resume_bullet(resume_text, job_role, missing_skill):
    return (
        f"Improved backend performance by implementing {missing_skill}, "
        f"leading to faster deployments and better system scalability."
    )

# -----------------------
# APIs
# -----------------------
@app.post("/upload")
async def upload_files(
    resume: UploadFile = File(...),
    jd: UploadFile = File(...)
):
    if resume.filename.endswith(".pdf"):
        resume_text = extract_text_from_pdf(resume.file)
    elif resume.filename.endswith(".docx"):
        resume_text = extract_text_from_docx(resume.file)
    else:
        resume_text = (await resume.read()).decode("utf-8")

    if jd.filename.endswith(".pdf"):
        jd_text = extract_text_from_pdf(jd.file)
    elif jd.filename.endswith(".docx"):
        jd_text = extract_text_from_docx(jd.file)
    else:
        jd_text = (await jd.read()).decode("utf-8")

    return {"resume_text": resume_text, "jd_text": jd_text}

@app.post("/match")
def match_resume(req: MatchRequest):
    resume_skills = extract_skills(req.resume_text)
    jd_skills = extract_skills(req.jd_text)

    matched = resume_skills & jd_skills
    missing = jd_skills - resume_skills

    smart_score = smart_skill_match(req.resume_text, req.jd_text)

    return {
        "match_score": smart_score,
        "matched_skills": list(matched),
        "missing_skills": list(missing),
        "expanded_missing": expand_missing_skills(missing)
    }

@app.post("/compare")
def compare_resumes(resumeA: str, resumeB: str, jd: str):
    return {
        "Resume A": smart_skill_match(resumeA, jd),
        "Resume B": smart_skill_match(resumeB, jd)
    }

@app.post("/ats-check")
async def ats_check(resume: UploadFile = File(...)):
    if resume.filename.endswith(".pdf"):
        return ats_readability_check(resume.file)
    return {"ats_score": 100, "issues": []}

@app.post("/optimize")
def optimize_resume(resume_text: str, job_role: str, missing_skill: str):
    return {
        "bullet": generate_resume_bullet(resume_text, job_role, missing_skill)
    }

@app.post("/compare-resumes")
async def compare_resumes_upload(
    resumeA: UploadFile = File(...),
    resumeB: UploadFile = File(...),
    jd: UploadFile = File(...)
):
    def extract(file):
        if file.filename.endswith(".pdf"):
            return extract_text_from_pdf(file.file)
        elif file.filename.endswith(".docx"):
            return extract_text_from_docx(file.file)
        else:
            return file.file.read().decode("utf-8")

    textA = extract(resumeA).lower()
    textB = extract(resumeB).lower()
    jd_text = extract(jd).lower()

    scoreA = smart_skill_match(textA, jd_text)
    scoreB = smart_skill_match(textB, jd_text)

    winner = "Resume A" if scoreA > scoreB else "Resume B"

    important_skills = ["docker", "aws", "fastapi", "microservices", "cloud"]
    reasons = [
        skill for skill in important_skills
        if skill in (textA if winner == "Resume A" else textB) and skill in jd_text
    ]

    return {
        "resumeA_score": scoreA,
        "resumeB_score": scoreB,
        "winner": winner,
        "reason": (
            "Mentions " + ", ".join(reasons)
            if reasons else "Better overall match with job description"
        )
    }
