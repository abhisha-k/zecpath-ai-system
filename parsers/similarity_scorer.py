class SimilarityScorer:
    """
    Calculate resume-to-job similarity score.
    """

    def __init__(self):
        pass

    def score(self, comparison):
        """
        Calculate similarity score.

        Args:
            comparison (dict)

        Returns:
            dict
        """

        resume_count = comparison["resume_word_count"]
        jd_count = comparison["jd_word_count"]
        matched = comparison["matched_count"]

        # Avoid division by zero
        if max(resume_count, jd_count) == 0:
            similarity = 0
        else:
            similarity = round(
                (matched / max(resume_count, jd_count)) * 100,
                2
            )

        # Matching level
        if similarity >= 80:
            level = "Excellent Match"
        elif similarity >= 60:
            level = "Good Match"
        elif similarity >= 40:
            level = "Average Match"
        else:
            level = "Low Match"

        return {
            "similarity_score": similarity,
            "matching_level": level
        }