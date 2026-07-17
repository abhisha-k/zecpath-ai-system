# ATS API Specification

## Overview

The ATS API provides REST endpoints for interacting with the AI-powered Applicant Tracking System. It enables backend applications to upload resumes, parse resume data, calculate ATS scores, and retrieve ranked candidate results.

---

# Base URL

```
http://localhost:8000/api/v1
```

---

# API Endpoints

## 1. Resume Upload

**Endpoint**

```
POST /resume/upload
```

**Purpose**

Uploads a candidate resume for processing.

**Request**

- Content-Type: multipart/form-data
- File: Resume (PDF/DOCX)

**Response**

```json
{
  "resume_id": "RES001",
  "status": "Uploaded",
  "message": "Resume uploaded successfully."
}
```

---

## 2. Resume Parsing

**Endpoint**

```
POST /resume/parse
```

**Purpose**

Extracts structured information from the uploaded resume.

**Request**

```json
{
  "resume_id": "RES001"
}
```

**Response**

```json
{
  "name": "John Doe",
  "skills": [
    "Python",
    "SQL",
    "Machine Learning"
  ],
  "experience": "2 Years",
  "education": "B.Tech"
}
```

---

## 3. ATS Scoring

**Endpoint**

```
POST /ats/score
```

**Purpose**

Calculates the ATS compatibility score.

**Request**

```json
{
  "resume_id": "RES001",
  "job_id": "JD001"
}
```

**Response**

```json
{
  "ats_score": 91.5,
  "status": "Completed"
}
```

---

## 4. Candidate Ranking

**Endpoint**

```
POST /candidate/rank
```

**Purpose**

Ranks candidates according to ATS score.

**Request**

```json
{
  "job_id": "JD001"
}
```

**Response**

```json
[
  {
    "candidate": "John Doe",
    "rank": 1,
    "score": 91.5,
    "status": "Shortlisted"
  }
]
```

---

# HTTP Status Codes

| Code | Description |
|------|-------------|
| 200 | Request Successful |
| 201 | Resource Created |
| 400 | Bad Request |
| 404 | Resource Not Found |
| 500 | Internal Server Error |

---

# Authentication

Future versions may secure the API using:

- JWT Authentication
- API Keys
- OAuth 2.0

---

# Versioning

Current Version

```
v1
```

Future versions can be exposed as:

```
/api/v2/
/api/v3/
```