# Zecpath AI System

## Overview

Zecpath AI System is an enterprise AI-powered recruitment platform designed to automate the complete hiring lifecycle. The system uses Artificial Intelligence to perform resume screening, candidate evaluation, interview automation, behavioral analysis, technical assessments, and hiring recommendations.

---

## Objectives

- Automate resume screening using AI
- Conduct AI-assisted interviews
- Analyze candidate behavior and communication
- Perform technical and machine test evaluations
- Generate AI-driven hiring recommendations
- Build a scalable AI microservices architecture

---

## Technology Stack

### Backend
- Python 3.12
- FastAPI

### AI & Machine Learning
- OpenAI
- LangChain
- Transformers
- PyTorch
- Sentence Transformers
- Scikit-learn

### Data Processing
- Pandas
- NumPy

### Resume Parsing
- spaCy
- PyMuPDF
- pdfplumber
- python-docx

### Computer Vision
- OpenCV
- MediaPipe

### Speech Processing
- Faster Whisper
- PyDub

### Database
- PostgreSQL
- SQLAlchemy
- Redis

### Development Tools
- Git & GitHub
- VS Code
- Pytest
- Loguru
- Black
- Flake8
- isort

---

# Project Structure

```text
zecpath-ai-system/
│
├── api/
├── ats_engine/
├── behavior_ai/
├── config/
├── data/
├── database/
├── decision_engine/
├── docs/
├── interview_ai/
├── logs/
├── machine_test_ai/
├── models/
├── notification/
├── parsers/
├── prompts/
├── reports/
├── salary_ai/
├── screening_ai/
├── services/
├── storage/
├── technical_ai/
├── tests/
├── utils/
│
├── .env
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

---

## Environment Setup

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

Run tests:

```bash
pytest
```

---

## Current Progress

- Repository initialized
- Virtual environment configured
- Enterprise folder structure created
- Dependencies installed
- Logging configured
- Testing framework configured

---

## Author

Abhisha Kannoly