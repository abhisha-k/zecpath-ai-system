# Developer Guide

## 1. Objective

The Developer Guide provides instructions for understanding, maintaining, testing, and extending the AI-powered Applicant Tracking System (ATS). It serves as a reference for developers working on the project.

---

## 2. Project Structure

```
project/
│
├── parsers/
├── tests/
├── docs/
├── data/
├── logs/
└── reports/
```

---

## 3. Setup

Requirements:

- Python 3.x
- pytest

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 4. Running the System

Run individual tests:

```bash
pytest tests/ -s
```

Run a specific test:

```bash
pytest tests/test_performance.py -s
```

---

## 5. Adding a New Module

Steps:

1. Create a parser inside `parsers/`.
2. Add corresponding test in `tests/`.
3. Update documentation.
4. Integrate into the ATS pipeline.
5. Validate using pytest.

---

## 6. Troubleshooting

Common issues:

- Missing dependencies
- Incorrect file paths
- Invalid JSON format
- Empty resume input
- Module import errors

---

## 7. Best Practices

- Write modular code.
- Use meaningful function names.
- Keep documentation updated.
- Test every new module.
- Follow consistent coding standards.

---

## 8. Future Enhancements

- REST API integration
- Cloud deployment
- Database support
- CI/CD pipeline
- Monitoring dashboard

---

## 9. Outcome

The Developer Guide provides a structured reference for developers, making the ATS easier to maintain, extend, and deploy in future development cycles.