class ExperienceScorer:
    """
    Score the relevance of candidate experience
    against a target job role.
    """

    def __init__(self):

        self.role_similarity = {

            "Data Scientist": [
                "Machine Learning Engineer",
                "AI Engineer",
                "Data Analyst"
            ],

            "Machine Learning Engineer": [
                "Data Scientist",
                "AI Engineer"
            ],

            "Software Engineer": [
                "Python Developer",
                "Web Developer"
            ],

            "Business Analyst": [
                "Data Analyst",
                "Project Manager"
            ]
        }

    def score(self, experience, target_role):
        """
        Score experience relevance.

        Args:
            experience (dict)
            target_role (str)

        Returns:
            dict
        """

        score = 0

        matched_roles = []

        for role in experience["job_titles"]:

            if role == target_role:
                score += 100
                matched_roles.append(role)

            elif target_role in self.role_similarity:

                if role in self.role_similarity[target_role]:
                    score += 80
                    matched_roles.append(role)

        if score > 100:
            score = 100

        return {

            "target_role": target_role,
            "matched_roles": matched_roles,
            "relevance_score": score
        }