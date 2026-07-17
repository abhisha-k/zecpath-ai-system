import json
from pathlib import Path

from parsers.fairness_processor import FairnessProcessor


def test_fairness():
    """
    Test Fairness, Normalization & Bias Reduction Engine.
    """

    processor = FairnessProcessor()

    resume_text = """
    John Doe
    Email: john.doe@gmail.com
    Phone: 9876543210

    Python Developer with SQL and Machine Learning experience.
    """

    skills = [
        "Python",
        " python ",
        "SQL",
        "Machine Learning",
        "sql"
    ]

    ats_score = 92.5

    result = processor.process(
        resume_text,
        skills,
        ats_score
    )

    output_folder = Path("data/fairness")
    output_folder.mkdir(parents=True, exist_ok=True)

    output_file = output_folder / "fairness_report.json"

    processor.save_output(result, output_file)

    print("\n")
    print("=" * 60)
    print("FAIRNESS REPORT")
    print("=" * 60)
    print(json.dumps(result, indent=4))
    print("=" * 60)

    assert isinstance(result, dict)
    assert "normalized_text" in result
    assert "normalized_skills" in result
    assert "normalized_score" in result
    assert "bias_report" in result