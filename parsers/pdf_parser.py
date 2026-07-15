import pdfplumber
import logging
from pathlib import Path


class PDFParser:
    """
    Reads PDF resumes and extracts raw text.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def extract_text(self, pdf_path):
        """
        Extract text from a PDF resume.

        Args:
            pdf_path (str): Path to PDF file

        Returns:
            str: Extracted raw text
        """

        pdf_path = Path(pdf_path)

        if not pdf_path.exists():
            raise FileNotFoundError(f"{pdf_path} not found.")

        extracted_text = ""

        try:

            with pdfplumber.open(pdf_path) as pdf:

                for page in pdf.pages:

                    text = page.extract_text()

                    if text:
                        extracted_text += text + "\n"

            self.logger.info(f"Successfully extracted text from {pdf_path.name}")

            return extracted_text

        except Exception as e:

            self.logger.error(str(e))

            raise