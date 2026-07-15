import re
import logging


class JDParser:
    """
    Extracts structured information from cleaned Job Description text.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def parse(self, text):
        """
        Parse Job Description text.

        Returns:
            dict
        """

        return {
            "job_title": self.extract_job_title(text),
            "required_skills": self.extract_skills(text),
            "experience": self.extract_experience(text),
            "education": self.extract_education(text)
        }

    def extract_job_title(self, text):
        """
        Extract job title.
        """

        lines = text.split("\n")

        for line in lines:

            line = line.strip()

            if len(line) > 3 and len(line) < 80:
                return line

        return "Unknown"

    def extract_skills(self, text):
        """
        Extract common technical skills.
        """

        skill_list = [
            "Python",
            "Java",
            "C++",
            "SQL",
            "Power BI",
            "Tableau",
            "AWS",
            "Azure",
            "Docker",
            "Kubernetes",
            "Git",
            "Machine Learning",
            "Deep Learning",
            "TensorFlow",
            "PyTorch",
            "Pandas",
            "NumPy",
            "Scikit-learn",
            "Excel"
        ]

        found = []

        for skill in skill_list:

            if re.search(rf"\b{re.escape(skill)}\b", text, re.IGNORECASE):
                found.append(skill)

        return found

    def extract_experience(self, text):
        """
        Extract experience requirement.
        """

        match = re.search(
            r"(\d+\+?\s*(?:years?|yrs?))",
            text,
            re.IGNORECASE
        )

        if match:
            return match.group()

        return "Not Specified"

    def extract_education(self, text):
        """
        Extract education requirement.
        """

        education_keywords = [
            "Bachelor",
            "Master",
            "B.Tech",
            "M.Tech",
            "BSc",
            "MSc",
            "BE",
            "ME",
            "MBA",
            "MCA",
            "PhD"
        ]

        for edu in education_keywords:

            if re.search(rf"\b{re.escape(edu)}\b", text, re.IGNORECASE):
                return edu

        return "Not Specified"