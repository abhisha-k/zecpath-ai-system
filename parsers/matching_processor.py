from pathlib import Path
import json

from parsers.extractor import ResumeExtractor
from parsers.pdf_parser import PDFParser
from parsers.semantic_matcher import SemanticMatcher
from parsers.similarity_scorer import SimilarityScorer


class MatchingProcessor:
    """
    Main Semantic Matching Engine.
    """

    def __init__(self):
        self.resume_extractor = ResumeExtractor()
        self.jd_parser = PDFParser()
        self.matcher = SemanticMatcher()
        self.scorer = SimilarityScorer()

    def process(self, resume_path, jd_path):
        """
        Compare a resume with a job description.

        Args:
            resume_path (str)
            jd_path (str)

        Returns:
            dict
        """

        resume_path = Path(resume_path)
        jd_path = Path(jd_path)

        # Extract text
        resume_text = self.resume_extractor.extract_resume(resume_path)
        jd_text = self.jd_parser.extract_text(jd_path)

        # Compare texts
        comparison = self.matcher.compare(
            resume_text,
            jd_text
        )

        # Score similarity
        similarity = self.scorer.score(comparison)

        result = {
            "comparison": comparison,
            "similarity": similarity
        }

        return result

    def save_output(self, result, output_path):
        """
        Save matching report as JSON.
        """

        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(result, file, indent=4)

        print(f"Matching report saved to: {output_path}")