class EducationScorer:
    """
    Evaluate education relevance against a target job role.
    """

    def __init__(self):

        self.role_mapping = {

            "Data Scientist": [
                "Computer Science",
                "Data Science",
                "Artificial Intelligence",
                "Machine Learning"
            ],

            "Software Engineer": [
                "Computer Science",
                "Information Technology"
            ],

            "Business Analyst": [
                "Business Administration",
                "Information Technology"
            ]
        }

        self.certification_categories = {

            "AWS Certified": "Cloud Computing",
            "Microsoft Certified": "Cloud & Productivity",
            "Google Cloud": "Cloud Computing",
            "Azure Fundamentals": "Cloud Computing",
            "Cisco Certified": "Networking",
            "Oracle Certified": "Database",
            "Coursera": "Online Learning",
            "Udemy": "Online Learning",
            "NPTEL": "Academic Learning"
        }

    def score(self, education, target_role):
        """
        Score education relevance.

        Args:
            education (dict)
            target_role (str)

        Returns:
            dict
        """

        relevance_score = 0
        matched_fields = []

        if target_role in self.role_mapping:

            for field in education["fields_of_study"]:

                if field in self.role_mapping[target_role]:
                    matched_fields.append(field)
                    relevance_score += 100

        if relevance_score > 100:
            relevance_score = 100

        categorized_certifications = []

        for cert in education["certifications"]:

            category = self.certification_categories.get(
                cert,
                "General"
            )

            categorized_certifications.append({
                "certification": cert,
                "category": category
            })

        return {

            "target_role": target_role,
            "matched_fields": matched_fields,
            "education_relevance_score": relevance_score,
            "categorized_certifications": categorized_certifications
        }