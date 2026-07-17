class SkillScorer:
    """
    Assign confidence scores to extracted skills.
    """

    def __init__(self):
        pass

    def score(self, extracted_skills):
        """
        Assign confidence scores.

        Args:
            extracted_skills (dict)

        Returns:
            dict
        """

        scored = {
            "technical": [],
            "business": [],
            "soft": []
        }

        # Technical Skills
        for skill in extracted_skills["technical"]:
            scored["technical"].append({
                "skill": skill,
                "confidence": 0.95
            })

        # Business Skills
        for skill in extracted_skills["business"]:
            scored["business"].append({
                "skill": skill,
                "confidence": 0.90
            })

        # Soft Skills
        for skill in extracted_skills["soft"]:
            scored["soft"].append({
                "skill": skill,
                "confidence": 0.85
            })

        return scored