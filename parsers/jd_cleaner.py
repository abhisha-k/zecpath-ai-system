import re
import logging


class JDCleaner:
    """
    Cleans and normalizes extracted Job Description text.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def clean_text(self, text):
        """
        Clean extracted Job Description text.

        Args:
            text (str)

        Returns:
            str
        """

        if not text:
            return ""

        # Replace tabs with spaces
        text = text.replace("\t", " ")

        # Remove multiple spaces
        text = re.sub(r" +", " ", text)

        # Remove multiple blank lines
        text = re.sub(r"\n+", "\n", text)

        # Remove unwanted bullet symbols
        text = re.sub(r"[•▪►■◆●✓✔]", "", text)

        # Remove non-printable characters
        text = re.sub(r"[^\x20-\x7E\n]", "", text)

        # Trim whitespace
        text = text.strip()

        self.logger.info("Job Description cleaned successfully.")

        return text