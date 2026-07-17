from pathlib import Path
import json

from parsers.ranking_engine import RankingEngine
from parsers.shortlisting import Shortlisting


class RankingProcessor:
    """
    Main Candidate Ranking & Shortlisting Engine.
    """

    def __init__(self):
        self.ranking_engine = RankingEngine()
        self.shortlisting = Shortlisting()

    def process(self, candidates):
        """
        Rank and classify candidates.

        Args:
            candidates (list)

        Returns:
            list
        """

        ranked_candidates = self.ranking_engine.rank_candidates(candidates)
        shortlisted_candidates = self.shortlisting.classify(ranked_candidates)

        return shortlisted_candidates

    def save_output(self, result, output_path):
        """
        Save ranked candidate report.
        """

        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(result, file, indent=4)

        print(f"Ranking report saved to: {output_path}")