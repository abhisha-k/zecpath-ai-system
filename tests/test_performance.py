import json
from pathlib import Path

from parsers.stability_processor import StabilityProcessor


def test_performance():
    text = """
        Python    Developer

        Experienced in AI

    """

    skills = [
        "Python",
        "Machine Learning",
        "Python",
        "SQL",
        "sql"
    ]

    entities = [
        "python developer",
        " Artificial Intelligence ",
        "python developer"
    ]

    result = StabilityProcessor.process(text, skills, entities)

    output_dir = Path("data/performance_reports")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "performance_report.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)

    print("\nPerformance Optimization Result\n")
    print(json.dumps(result, indent=4))

    assert len(result["optimized_skills"]) == 3
    assert "Python Developer" in result["optimized_entities"]