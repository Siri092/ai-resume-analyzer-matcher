# Requirements Document  
## AI Resume Analyzer & Job Description Matcher

## 1. Introduction
The AI Resume Analyzer is a web-based platform that evaluates how well a resume matches a job description. It provides match scoring, skill gap analysis, ATS readability checks, and improvement suggestions.

---

## 2. Functional Requirements

### 2.1 Resume Upload
- The system shall allow users to upload resumes in PDF, DOCX, or TXT format.
- The system shall extract text from uploaded files.

### 2.2 Job Description Input
- The system shall allow users to paste or upload a job description.

### 2.3 Resume vs JD Matching
- The system shall calculate a similarity score using TF-IDF and Cosine Similarity.
- The system shall display a match percentage score.

### 2.4 Skill Gap Analysis
- The system shall identify missing skills from the job description.
- The system shall highlight matched skills.

### 2.5 ATS Readability Check
- The system shall detect formatting issues such as:
  - Tables
  - Images
  - Non-readable text
- The system shall generate an ATS compatibility score.

### 2.6 Resume Comparison
- The system shall allow comparison between two resumes.
- The system shall display which resume performs better.

### 2.7 Report Generation
- The system shall generate downloadable analysis reports.

---

## 3. Non-Functional Requirements

### 3.1 Performance
- The system should process analysis within 5 seconds.

### 3.2 Scalability
- The backend should support deployment on cloud platforms like Render or AWS.

### 3.3 Security
- Uploaded files should not be permanently stored unless required.
- The system should validate file types before processing.

### 3.4 Usability
- The UI should be simple and responsive.
- The dashboard should clearly display scores and suggestions.

---

## 4. Technology Stack

- Frontend: React, Tailwind CSS
- Backend: FastAPI (Python)
- NLP/ML: Scikit-learn
- File Parsing: PDFPlumber, python-docx
- Deployment: Render
