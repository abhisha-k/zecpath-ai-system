import json
from pathlib import Path

from parsers.experience_processor import ExperienceProcessor


def test_experience_parser():
    """
    Test Experience Parsing & Relevance Engine.
    """

    processor = ExperienceProcessor()

    # Change this to one of your actual resume filenames
    resume_path = Path("data/resumes/data_scientist2.pdf")

    # Target role for relevance scoring
    target_role = "Data Scientist"

    result = processor.process(resume_path, target_role)

    output_folder = Path("data/experience")
    output_folder.mkdir(parents=True, exist_ok=True)

    output_file = output_folder / "structured_experience.json"

    processor.save_output(result, output_file)

    print("\n")
    print("=" * 60)
    print("STRUCTURED EXPERIENCE")
    print("=" * 60)
    print(json.dumps(result, indent=4))
    print("=" * 60)

    assert isinstance(result, dict)
    assert "experience" in result
    assert "relevance" in result