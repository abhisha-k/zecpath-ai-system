from docx import Document
import logging
from pathlib import Path


class DOCXParser:
    """
    Reads DOCX resumes and extracts raw text.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def extract_text(self, docx_path):
        """
        Extract text from a DOCX resume.

        Args:
            docx_path (str): Path to DOCX file

        Returns:
            str: Extracted raw text
        """

        docx_path = Path(docx_path)

        if not docx_path.exists():
            raise FileNotFoundError(f"{docx_path} not found.")

        extracted_text = ""

        try:

            document = Document(docx_path)

            for paragraph in document.paragraphs:

                if paragraph.text.strip():
                    extracted_text += paragraph.text + "\n"

            self.logger.info(
                f"Successfully extracted text from {docx_path.name}"
            )

            return extracted_text

        except Exception as e:

            self.logger.error(str(e))
            raise