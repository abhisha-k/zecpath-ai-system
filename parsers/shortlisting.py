class Shortlisting:
    """
    Classify candidates based on ATS scores.
    """

    def __init__(self):

        self.shortlist_threshold = 80
        self.review_threshold = 60

    def classify(self, candidates):
        """
        Assign candidate status based on ATS score.

        Args:
            candidates (list)

        Returns:
            list
        """

        for candidate in candidates:

            score = candidate["final_ats_score"]

            if score >= self.shortlist_threshold:
                status = "Shortlisted"

            elif score >= self.review_threshold:
                status = "Review"

            else:
                status = "Rejected"

            candidate["status"] = status

        return candidates