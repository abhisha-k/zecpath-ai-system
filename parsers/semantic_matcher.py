import re
import logging


class SemanticMatcher:
    """
    Compare resume text and job description text
    using keyword overlap.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def preprocess(self, text):
        """
        Convert text into a set of lowercase words.
        """

        text = text.lower()
        text = re.sub(r"[^a-z0-9\s]", "", text)

        return set(text.split())

    def compare(self, resume_text, jd_text):
        """
        Compare resume and job description.
        """

        resume_words = self.preprocess(resume_text)
        jd_words = self.preprocess(jd_text)

        common_words = resume_words.intersection(jd_words)

        return {
            "resume_word_count": len(resume_words),
            "jd_word_count": len(jd_words),
            "matched_words": sorted(list(common_words)),
            "matched_count": len(common_words)
        }