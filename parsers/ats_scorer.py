class ATSScorer:
    """
    Calculate the final ATS score using weighted parameters.
    """

    def __init__(self, weights):
        self.weights = weights

    def calculate(
        self,
        skill_score=0,
        experience_score=0,
        education_score=0,
        semantic_score=0
    ):
        """
        Calculate weighted ATS score.

        Args:
            skill_score (float)
            experience_score (float)
            education_score (float)
            semantic_score (float)

        Returns:
            dict
        """

        final_score = (
            (skill_score * self.weights["skills"] / 100) +
            (experience_score * self.weights["experience"] / 100) +
            (education_score * self.weights["education"] / 100) +
            (semantic_score * self.weights["semantic"] / 100)
        )

        final_score = round(final_score, 2)

        if final_score >= 80:
            rating = "Excellent"
        elif final_score >= 60:
            rating = "Good"
        elif final_score >= 40:
            rating = "Average"
        else:
            rating = "Low"

        return {
            "skill_score": skill_score,
            "experience_score": experience_score,
            "education_score": education_score,
            "semantic_score": semantic_score,
            "final_ats_score": final_score,
            "candidate_rating": rating
        }