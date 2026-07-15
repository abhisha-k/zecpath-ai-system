from pathlib import Path

from parsers.extractor import ResumeExtractor


def test_resume_extraction():
    """
    Test Resume Extraction Engine.
    """

    extractor = ResumeExtractor()

    # Update this filename if necessary
    resume_path = Path("data/resumes/data_scientist2.pdf")

    text = extractor.extract_resume(resume_path)
    

    output_folder = Path("data/reports")
    output_folder.mkdir(parents=True, exist_ok=True)

    output_file = output_folder / "cleaned_resume.txt"

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(text)

    print(f"\nCleaned resume saved to: {output_file}")

    print("\n")
    print("=" * 60)
    print("RESUME TEXT")
    print("=" * 60)
    print(text[:1500])      # Print first 1500 characters
    print("=" * 60)

    assert len(text) > 0