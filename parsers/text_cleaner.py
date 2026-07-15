import re
import logging


class TextCleaner:
    """
    Cleans and normalizes extracted resume text.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def clean_text(self, text):
        """
        Clean extracted text.

        Args:
            text (str)

        Returns:
            str
        """

        if not text:
            return ""

        # Remove tabs
        text = text.replace("\t", " ")

        # Remove multiple spaces
        text = re.sub(r" +", " ", text)

        # Remove extra blank lines
        text = re.sub(r"\n+", "\n", text)

        # Remove unwanted bullet symbols
        text = re.sub(r"[•▪►■◆●✓✔]", "", text)

        # Remove non-printable characters
        text = re.sub(r"[^\x20-\x7E\n]", "", text)

        # Strip leading/trailing spaces
        text = text.strip()

        self.logger.info("Text cleaned successfully.")

        return text