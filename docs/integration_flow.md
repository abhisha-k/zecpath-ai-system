# ATS Integration Flow

## Overview

The ATS Integration Flow describes how the frontend, backend, AI processing modules, and data storage interact to process resumes and generate candidate rankings. It provides a high-level view of the complete AI recruitment pipeline.

---

# System Architecture

```
Frontend
    │
    ▼
Resume Upload API
    │
    ▼
Resume Parser
    │
    ▼
Resume Section Classifier
    │
    ▼
Skill Extraction
    │
    ▼
Experience Parser
    │
    ▼
Education Parser
    │
    ▼
Semantic Matching
    │
    ▼
ATS Scoring Engine
    │
    ▼
Candidate Ranking
    │
    ▼
Fairness Processor
    │
    ▼
JSON Reports
```

---

# Processing Workflow

1. Candidate uploads a resume through the Resume Upload API.
2. The resume is parsed to extract structured information.
3. Resume sections are identified and classified.
4. Skills are extracted and standardized.
5. Work experience is analyzed.
6. Education and certifications are extracted.
7. Semantic similarity between the resume and job description is calculated.
8. The ATS Scoring Engine computes the candidate's score.
9. Candidates are ranked according to their ATS scores.
10. The Fairness Processor applies normalization and bias reduction.
11. Final reports are generated in JSON format.

---

# Modules Involved

| Module | Purpose |
|---------|---------|
| Resume Parser | Extracts resume content |
| Section Classifier | Detects resume sections |
| Skill Extraction | Identifies candidate skills |
| Experience Parser | Processes work experience |
| Education Parser | Extracts education details |
| Semantic Matching | Compares resume with job description |
| ATS Scoring | Calculates ATS score |
| Candidate Ranking | Ranks and shortlists candidates |
| Fairness Processor | Applies normalization and bias reduction |

---

# Input

- Resume (PDF/DOCX)
- Job Description

---

# Output

- Parsed Resume
- ATS Score
- Candidate Ranking
- Fairness Report
- JSON Reports

---

# Future Integration

The designed APIs can be integrated with:

- Web applications
- HR Management Systems (HRMS)
- Applicant Tracking Systems (ATS)
- Recruitment Portals
- Cloud-based AI services

---

# Outcome

The integration flow provides a complete roadmap for connecting all AI recruitment modules into a unified Applicant Tracking System. It demonstrates how candidate data moves through parsing, analysis, scoring, ranking, and fairness evaluation before generating structured outputs for recruiters.