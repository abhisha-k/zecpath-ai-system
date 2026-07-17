import re


class PerformanceOptimizer:
    """
    Optimizes extracted resume text before downstream ATS processing.
    """

    @staticmethod
    def optimize_text(text: str) -> str:
        if not text:
            return ""

        # Convert multiple whitespaces to a single space
        text = re.sub(r"\s+", " ", text)

        # Remove repeated blank lines
        text = re.sub(r"\n+", "\n", text)

        # Trim leading and trailing whitespace
        text = text.strip()

        return text

    @staticmethod
    def remove_duplicate_skills(skills):
        """
        Remove duplicate skills while preserving order.
        """
        seen = set()
        unique_skills = []

        for skill in skills:
            normalized = skill.strip().lower()
            if normalized not in seen:
                seen.add(normalized)
                unique_skills.append(skill)

        return unique_skills