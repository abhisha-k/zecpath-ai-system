import json
from pathlib import Path

from parsers.jd_processor import JDProcessor


def test_job_description_parser():
    """
    Test Job Description Parsing System.
    """

    processor = JDProcessor()

    # Change this to one of your actual JD filenames
    jd_path = Path("data/job_descriptions/Business Analyst JD1.pdf")

    parsed_data = processor.process(jd_path)

    output_folder = Path("data/reports")
    output_folder.mkdir(parents=True, exist_ok=True)

    output_file = output_folder / "structured_jd.json"

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(parsed_data, file, indent=4)

    print("\n")
    print("=" * 60)
    print("STRUCTURED JOB DESCRIPTION")
    print("=" * 60)
    print(json.dumps(parsed_data, indent=4))
    print("=" * 60)

    assert parsed_data["job_title"] != ""