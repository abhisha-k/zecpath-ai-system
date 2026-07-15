# Metadata Standards

## Objective

This document defines the metadata used across the AI Recruitment Platform.

## Metadata Fields

| Field | Description |
|-------|-------------|
| Candidate ID | Unique candidate identifier |
| Resume ID | Resume identifier |
| Job ID | Unique job identifier |
| ATS Score | Candidate ATS score |
| Model Version | AI model version |
| Dataset Version | Dataset version |
| Timestamp | Processing timestamp |
| Processing Status | Completed / Failed |

## Sample JSON

{
    "candidate_id": "CAND001",
    "resume_id": "RES001",
    "job_id": "JOB001",
    "ats_score": 87,
    "model_version": "v1.0",
    "dataset_version": "Dataset_v2",
    "processing_status": "Completed"
}

## Benefits

- Standardized metadata
- Easy tracking
- Supports auditing
- Enables AI model versioning