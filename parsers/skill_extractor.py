import logging

from parsers.skill_dictionary import SkillDictionary


class SkillExtractor:
    """
    Extract technical and non-technical skills from resume text.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.dictionary = SkillDictionary()

    def extract(self, text):
        """
        Extract skills from resume text.

        Args:
            text (str)

        Returns:
            dict
        """

        text_lower = text.lower()

        extracted = {
            "technical": [],
            "business": [],
            "soft": []
        }

        # Technical Skills
        for skill in self.dictionary.skills["technical"]:
            if skill.lower() in text_lower:
                extracted["technical"].append(skill)

        # Business Skills
        for skill in self.dictionary.skills["business"]:
            if skill.lower() in text_lower:
                extracted["business"].append(skill)

        # Soft Skills
        for skill in self.dictionary.skills["soft"]:
            if skill.lower() in text_lower:
                extracted["soft"].append(skill)

        # Skill Synonyms
        for short, full in self.dictionary.skills["synonyms"].items():
            if short.lower() in text_lower:
                if full not in extracted["technical"]:
                    extracted["technical"].append(full)

        # Skill Stacks (MERN, MEAN)
        for stack, technologies in self.dictionary.skills["skill_stacks"].items():
            if stack.lower() in text_lower:
                for tech in technologies:
                    if tech not in extracted["technical"]:
                        extracted["technical"].append(tech)

        # Remove duplicates
        extracted["technical"] = sorted(set(extracted["technical"]))
        extracted["business"] = sorted(set(extracted["business"]))
        extracted["soft"] = sorted(set(extracted["soft"]))

        self.logger.info("Skills extracted successfully.")

        return extracted