import json
from pathlib import Path

from parsers.ranking_processor import RankingProcessor


def test_candidate_ranking():
    """
    Test Candidate Ranking & Shortlisting Engine.
    """

    processor = RankingProcessor()

    # Sample candidate ATS scores
    candidates = [
        {
            "candidate": "Alice",
            "final_ats_score": 91
        },
        {
            "candidate": "Bob",
            "final_ats_score": 72
        },
        {
            "candidate": "Charlie",
            "final_ats_score": 84
        },
        {
            "candidate": "David",
            "final_ats_score": 48
        }
    ]

    result = processor.process(candidates)

    output_folder = Path("data/ranking")
    output_folder.mkdir(parents=True, exist_ok=True)

    output_file = output_folder / "ranked_candidates.json"

    processor.save_output(result, output_file)

    print("\n")
    print("=" * 60)
    print("RANKED CANDIDATE LIST")
    print("=" * 60)
    print(json.dumps(result, indent=4))
    print("=" * 60)

    assert isinstance(result, list)
    assert len(result) == 4
    assert "rank" in result[0]
    assert "status" in result[0]