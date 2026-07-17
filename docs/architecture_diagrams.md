# Architecture Diagrams

## 1. Objective

The Architecture Diagrams document illustrates the overall design of the AI-powered Applicant Tracking System (ATS). It explains how different modules interact to process resumes, evaluate candidates, and generate recruitment decisions.

---

## 2. System Architecture

```
                 AI-Powered Applicant Tracking System

                      Resume Upload
                            │
                            ▼
                     Resume Parser
                            │
                            ▼
                 Section Classification
                            │
        ┌───────────────┬───────────────┬───────────────┐
        ▼               ▼               ▼
 Skill Extraction  Experience Parser  Education Parser
        └───────────────┬───────────────┘
                        ▼
                Semantic Matching
                        │
                        ▼
                  ATS Scoring Engine
                        │
                        ▼
               Candidate Ranking Engine
                        │
                        ▼
                 Shortlisting Module
                        │
                        ▼
                 Final Recruitment Report
```

---

## 3. Data Flow

```
Resume
   │
   ▼
Parser
   │
   ▼
Structured Data
   │
   ▼
ATS Processing
   │
   ▼
Scoring
   │
   ▼
Ranking
   │
   ▼
Final Output
```

---

## 4. Module Responsibilities

| Module | Responsibility |
|---------|----------------|
| Resume Parser | Extract resume text |
| Section Classifier | Identify resume sections |
| Skill Extraction | Extract technical and soft skills |
| Experience Parser | Parse work experience |
| Education Parser | Parse academic details |
| Semantic Matching | Match resume with job description |
| ATS Scoring | Generate candidate score |
| Ranking Engine | Rank candidates |
| Shortlisting | Classify candidates |

---

## 5. Technologies Used

- Python
- JSON
- Regular Expressions
- NLP Techniques
- pytest

---

## 6. Outcome

The architecture diagrams provide a clear representation of the ATS workflow, helping developers understand the interaction between modules and simplifying future maintenance and enhancements.