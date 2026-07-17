import json
from pathlib import Path

from parsers.section_processor import SectionProcessor


def test_resume_section_classifier():
    """
    Test Resume Section Segmentation.
    """

    processor = SectionProcessor()

    # Change this to one of your actual resume filenames
    resume_path = Path("data/resumes/python_developer6.pdf")

    sections = processor.process(resume_path)

    output_folder = Path("data/segmented_resumes")
    output_folder.mkdir(parents=True, exist_ok=True)

    output_file = output_folder / "segmented_resume.json"

    processor.save_output(sections, output_file)

    print("\n")
    print("=" * 60)
    print("SEGMENTED RESUME")
    print("=" * 60)
    print(json.dumps(sections, indent=4))
    print("=" * 60)

    assert isinstance(sections, dict)
    assert "skills" in sections