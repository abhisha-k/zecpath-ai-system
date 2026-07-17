import json
from pathlib import Path

from parsers.ats_processor import ATSProcessor


def test_ats_scoring():
    """
    Test ATS Scoring Engine.
    """

    processor = ATSProcessor()

    # Sample scores (replace with actual module outputs later if needed)
    skill_score = 90
    experience_score = 80
    education_score = 100
    semantic_score = 70

    result = processor.process(
        skill_score,
        experience_score,
        education_score,
        semantic_score
    )

    output_folder = Path("data/ats")
    output_folder.mkdir(parents=True, exist_ok=True)

    output_file = output_folder / "structured_ats_score.json"

    processor.save_output(result, output_file)

    print("\n")
    print("=" * 60)
    print("ATS SCORING RESULT")
    print("=" * 60)
    print(json.dumps(result, indent=4))
    print("=" * 60)

    assert isinstance(result, dict)
    assert "final_ats_score" in result
    assert "candidate_rating" in result