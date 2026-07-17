import json
from pathlib import Path

from parsers.education_processor import EducationProcessor


def test_education_parser():
    """
    Test Education & Certification Parsing Engine.
    """

    processor = EducationProcessor()

    # Change this to one of your actual resume filenames
    resume_path = Path("data/resumes/data_scientist2.pdf")

    # Target role for education relevance scoring
    target_role = "Data Scientist"

    result = processor.process(resume_path, target_role)

    output_folder = Path("data/education")
    output_folder.mkdir(parents=True, exist_ok=True)

    output_file = output_folder / "structured_education.json"

    processor.save_output(result, output_file)

    print("\n")
    print("=" * 60)
    print("STRUCTURED EDUCATION PROFILE")
    print("=" * 60)
    print(json.dumps(result, indent=4))
    print("=" * 60)

    assert isinstance(result, dict)
    assert "education" in result
    assert "relevance" in result