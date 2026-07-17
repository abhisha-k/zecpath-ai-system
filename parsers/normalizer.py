import re


class Normalizer:
    """
    Normalize extracted resume data into a standard format.
    """

    def normalize_text(self, text):
        """
        Standardize text by:
        - Converting to lowercase
        - Removing extra spaces
        - Removing special characters
        """

        if not text:
            return ""

        text = text.lower()
        text = re.sub(r"[^\w\s]", "", text)
        text = re.sub(r"\s+", " ", text).strip()

        return text

    def normalize_skills(self, skills):
        """
        Normalize a list of skills.
        """

        normalized = []

        for skill in skills:
            normalized.append(self.normalize_text(skill))

        return sorted(set(normalized))

    def normalize_score(self, score):
        """
        Ensure score is between 0 and 100.
        """

        if score < 0:
            return 0

        if score > 100:
            return 100

        return round(score, 2)