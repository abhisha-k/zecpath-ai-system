class RankingEngine:
    """
    Rank candidates based on ATS scores.
    """

    def rank_candidates(self, candidates):
        """
        Sort candidates in descending order of ATS score
        and assign rankings.

        Args:
            candidates (list)

        Returns:
            list
        """

        ranked = sorted(
            candidates,
            key=lambda x: x["final_ats_score"],
            reverse=True
        )

        for index, candidate in enumerate(ranked, start=1):
            candidate["rank"] = index

        return ranked