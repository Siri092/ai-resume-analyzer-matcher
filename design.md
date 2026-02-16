# System Design Document  
## AI Resume Analyzer & Job Description Matcher

---

## 1. System Architecture

User (Web Browser)
        |
        v
Frontend (React + Tailwind)
        |
        v
Backend API (FastAPI)
        |
        +-----------------------------+
        |                             |
        v                             v
Resume/JD Parser               ATS & Skill Analyzer
(PDFPlumber, DOCX)             (NLP Processing)
        |                             |
        +-------------+---------------+
                      |
                      v
            Match Score Engine
        (TF-IDF + Cosine Similarity)
                      |
                      v
             Result Generator
   (Score, Missing Skills, Suggestions)
                      |
                      v
               User Dashboard

---

## 2. Design Components

### 2.1 Frontend
- Built using React and Tailwind CSS.
- Handles file uploads and displays analysis results.
- Communicates with backend via REST APIs.

### 2.2 Backend
- Built using FastAPI.
- Handles file parsing and NLP processing.
- Exposes endpoints for:
  - Resume analysis
  - Resume comparison
  - Skill extraction

### 2.3 NLP Engine
- Converts text into TF-IDF vectors.
- Calculates similarity using Cosine Similarity.
- Extracts keywords and skill gaps.

### 2.4 Deployment Design
- Hosted on Render.
- Backend exposed via REST API.
- Frontend deployed separately or via static hosting.

---

## 3. Data Flow

1. User uploads resume and job description.
2. Backend extracts text.
3. NLP engine processes and vectorizes text.
4. Similarity score is computed.
5. Skill gaps are identified.
6. Results are returned to frontend.
7. User views dashboard.

---

## 4. Future Enhancements

- AI-powered resume bullet generator (LLM-based)
- Multi-language resume support
- Interview preparation suggestions
- Recruiter dashboard
