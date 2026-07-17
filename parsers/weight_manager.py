class WeightManager:
    """
    Manage configurable ATS scoring weights.
    """

    def __init__(self):

        # Default ATS weights (must total 100)
        self.weights = {
            "skills": 35,
            "experience": 30,
            "education": 15,
            "semantic": 20
        }

    def get_weights(self):
        """
        Return current ATS weights.
        """
        return self.weights

    def update_weights(
        self,
        skills=None,
        experience=None,
        education=None,
        semantic=None
    ):
        """
        Update ATS scoring weights.
        """

        if skills is not None:
            self.weights["skills"] = skills

        if experience is not None:
            self.weights["experience"] = experience

        if education is not None:
            self.weights["education"] = education

        if semantic is not None:
            self.weights["semantic"] = semantic

    def validate_weights(self):
        """
        Ensure total weight equals 100.
        """

        total = sum(self.weights.values())

        return total == 100