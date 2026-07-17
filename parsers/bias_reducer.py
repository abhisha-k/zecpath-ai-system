import re


class BiasReducer:
    """
    Reduce bias by masking non-essential personal information.
    """

    def mask_personal_info(self, text):
        """
        Mask email addresses and phone numbers.
        """

        if not text:
            return ""

        # Mask email addresses
        text = re.sub(
            r'[\w\.-]+@[\w\.-]+\.\w+',
            '[EMAIL]',
            text
        )

        # Mask phone numbers
        text = re.sub(
            r'\b\d{10}\b',
            '[PHONE]',
            text
        )

        return text

    def evaluate_bias(self, text):
        """
        Identify the presence of personal information that may
        introduce bias during evaluation.
        """

        indicators = {
            "email_detected": "[EMAIL]" in text,
            "phone_detected": "[PHONE]" in text
        }

        indicators["bias_risk"] = (
            "Low"
            if not any(indicators.values())
            else "Personal Information Masked"
        )

        return indicators