import re
import logging


class EducationExtractor:
    """
    Extract education and certification details from resume text.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

        self.degrees = [
            "Bachelor of Science",
            "Bachelor of Technology",
            "Bachelor of Engineering",
            "Master of Science",
            "Master of Computer Applications",
            "Master of Technology",
            "B.Sc",
            "B.Tech",
            "B.E",
            "M.Sc",
            "M.Tech",
            "MCA"
        ]

        self.fields = [
            "Computer Science",
            "Information Technology",
            "Data Science",
            "Artificial Intelligence",
            "Machine Learning",
            "Electronics",
            "Business Administration"
        ]

        self.certifications = [
            "AWS Certified",
            "Microsoft Certified",
            "Google Cloud",
            "Azure Fundamentals",
            "Cisco Certified",
            "Oracle Certified",
            "Coursera",
            "Udemy",
            "NPTEL"
        ]

    def extract(self, text):
        """
        Extract education information.

        Args:
            text (str)

        Returns:
            dict
        """

        education = {
            "degrees": [],
            "fields_of_study": [],
            "institutions": [],
            "graduation_years": [],
            "certifications": []
        }

        # Degree detection
        for degree in self.degrees:
            if degree.lower() in text.lower():
                education["degrees"].append(degree)

        # Field of study detection
        for field in self.fields:
            if field.lower() in text.lower():
                education["fields_of_study"].append(field)

        # Certification detection
        for cert in self.certifications:
            if cert.lower() in text.lower():
                education["certifications"].append(cert)

        # Graduation year detection
        year_pattern = r"\b(19|20)\d{2}\b"
        education["graduation_years"] = list(set(re.findall(year_pattern, text)))

        # Institution detection (simple rule-based approach)
        institution_pattern = (
            r"([A-Z][A-Za-z0-9&., ]+"
            r"(University|College|Institute|School))"
        )

        institutions = re.findall(institution_pattern, text)

        education["institutions"] = list(
            set([inst[0] for inst in institutions])
        )

        self.logger.info("Education extracted successfully.")

        return education