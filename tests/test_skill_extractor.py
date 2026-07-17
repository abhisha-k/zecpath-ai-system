import json
from pathlib import Path

from parsers.skill_processor import SkillProcessor


def test_skill_extractor():
    """
    Test Skill Extraction Engine.
    """

    processor = SkillProcessor()

    # Change this to one of your actual resume filenames
    resume_path = Path("data/resumes/data_scientist2.pdf")

    skills = processor.process(resume_path)

    output_folder = Path("data/skills")
    output_folder.mkdir(parents=True, exist_ok=True)

    output_file = output_folder / "structured_skills.json"

    processor.save_output(skills, output_file)

    print("\n")
    print("=" * 60)
    print("STRUCTURED SKILLS")
    print("=" * 60)
    print(json.dumps(skills, indent=4))
    print("=" * 60)

    assert isinstance(skills, dict)
    assert "technical" in skills