import json
from pathlib import Path

from parsers.matching_processor import MatchingProcessor


def test_semantic_matching():
    """
    Test Semantic Matching Engine.
    """

    processor = MatchingProcessor()

    # Update these filenames if necessary
    resume_path = Path("data/resumes/data_scientist2.pdf")
    jd_path = Path("data/job_descriptions/Business Analyst JD1.pdf")

    result = processor.process(resume_path, jd_path)

    output_folder = Path("data/matching")
    output_folder.mkdir(parents=True, exist_ok=True)

    output_file = output_folder / "structured_matching.json"

    processor.save_output(result, output_file)

    print("\n")
    print("=" * 60)
    print("SEMANTIC MATCHING RESULT")
    print("=" * 60)
    print(json.dumps(result, indent=4))
    print("=" * 60)

    assert isinstance(result, dict)
    assert "comparison" in result
    assert "similarity" in result