from pathlib import Path

from parsers.pdf_parser import PDFParser
from parsers.docx_parser import DOCXParser
from parsers.jd_cleaner import JDCleaner
from parsers.jd_parser import JDParser


class JDProcessor:
    """
    Main Job Description Processing Engine.
    """

    def __init__(self):
        self.pdf_parser = PDFParser()
        self.docx_parser = DOCXParser()
        self.cleaner = JDCleaner()
        self.parser = JDParser()

    def process(self, file_path):
        """
        Process a Job Description file.

        Args:
            file_path (str)

        Returns:
            dict
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

        parsed_data = self.parser.parse(clean_text)

        return parsed_data