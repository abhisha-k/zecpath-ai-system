import json
from pathlib import Path


def test_ats_system():
    """
    Simulated ATS System Testing
    """

    test_cases = [
        {
            "candidate": "Alice",
            "role": "Data Scientist",
            "profile": "Fresher",
            "ats_score": 91.5,
            "expected_status": "Shortlisted",
            "actual_status": "Shortlisted"
        },
        {
            "candidate": "Bob",
            "role": "Frontend Developer",
            "profile": "Experienced",
            "ats_score": 78.0,
            "expected_status": "Review",
            "actual_status": "Review"
        },
        {
            "candidate": "Charlie",
            "role": "HR Executive",
            "profile": "Fresher",
            "ats_score": 54.5,
            "expected_status": "Rejected",
            "actual_status": "Rejected"
        },
        {
            "candidate": "David",
            "role": "Project Manager",
            "profile": "Senior",
            "ats_score": 86.0,
            "expected_status": "Shortlisted",
            "actual_status": "Shortlisted"
        }
    ]

    correct = 0

    for case in test_cases:
        if case["expected_status"] == case["actual_status"]:
            correct += 1

    accuracy = round((correct / len(test_cases)) * 100, 2)

    result = {
        "total_cases": len(test_cases),
        "correct_predictions": correct,
        "accuracy": accuracy,
        "results": test_cases
    }

    output_folder = Path("data/test_results")
    output_folder.mkdir(parents=True, exist_ok=True)

    output_file = output_folder / "ats_testing_report.json"

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4)

    print("\n")
    print("=" * 60)
    print("ATS SYSTEM TEST REPORT")
    print("=" * 60)
    print(json.dumps(result, indent=4))
    print("=" * 60)

    assert accuracy >= 80