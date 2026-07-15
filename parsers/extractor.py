from pathlib import Path

from parsers.pdf_parser import PDFParser
from parsers.docx_parser import DOCXParser
from parsers.text_cleaner import TextCleaner


class ResumeExtractor:
    """
    Main Resume Text Extraction Engine.
    """

    def __init__(self):
        self.pdf_parser = PDFParser()
        self.docx_parser = DOCXParser()
        self.cleaner = TextCleaner()

    def extract_resume(self, file_path):
        """
        Extract and clean resume text.

        Args:
            file_path (str)

        Returns:
            str
        """

        file_path = Path(file_path)

        suffix = file_path.suffix.lower()

        if suffix == ".pdf":

            raw_text = self.pdf_parser.extract_text(file_path)

        elif suffix == ".docx":

            raw_text = self.docx_parser.extract_text(file_path)

        else:

            raise ValueError(
                "Unsupported file format. Only PDF and DOCX are supported."
            )

        clean_text = self.cleaner.clean_text(raw_text)

        return clean_text