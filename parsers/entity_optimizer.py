import re


class EntityOptimizer:
    """
    Cleans and normalizes extracted entities before ATS processing.
    """

    @staticmethod
    def normalize_entity(entity: str) -> str:
        """
        Normalize an extracted entity.
        """
        if not entity:
            return ""

        entity = entity.strip()
        entity = re.sub(r"\s+", " ", entity)

        return entity.title()

    @staticmethod
    def remove_noise(text: str) -> str:
        """
        Remove unnecessary symbols and noisy characters.
        """
        if not text:
            return ""

        # Remove repeated special characters
        text = re.sub(r"[_*#~`]+", "", text)

        # Remove multiple spaces
        text = re.sub(r"\s+", " ", text)

        return text.strip()

    @staticmethod
    def normalize_entities(entity_list):
        """
        Normalize a list of extracted entities.
        """
        normalized = []

        for entity in entity_list:
            cleaned = EntityOptimizer.normalize_entity(entity)

            if cleaned and cleaned not in normalized:
                normalized.append(cleaned)

        return normalized