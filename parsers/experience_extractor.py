import re
import logging


class ExperienceExtractor:
    """
    Extract work experience information from resume text.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

        self.job_titles = [
            "Data Scientist",
            "Data Analyst",
            "Machine Learning Engineer",
            "AI Engineer",
            "Software Engineer",
            "Python Developer",
            "Web Developer",
            "Business Analyst",
            "Project Manager",
            "Intern"
        ]

    def extract(self, text):
        """
        Extract experience information.

        Args:
            text (str)

        Returns:
            dict
        """

        experience = {
            "job_titles": [],
            "companies": [],
            "durations": [],
            "total_experience": "Not Calculated"
        }

        # Extract job titles
        for title in self.job_titles:
            if title.lower() in text.lower():
                experience["job_titles"].append(title)

        # Extract employment durations (e.g., 01/2022 - 06/2024)
        duration_pattern = r"\b\d{2}/\d{4}\s*-\s*(?:\d{2}/\d{4}|Present)\b"
        experience["durations"] = re.findall(duration_pattern, text)

        # Extract company names (simple rule-based approach)
        company_pattern = r"([A-Z][A-Za-z0-9&., ]+(?:Ltd|LLP|Inc|Corporation|Technologies|Solutions|Systems|Company))"
        companies = re.findall(company_pattern, text)

        experience["companies"] = list(set(companies))

        # Estimate total experience
        if experience["durations"]:
            experience["total_experience"] = f"{len(experience['durations'])} employment record(s)"

        self.logger.info("Experience extracted successfully.")

        return experience