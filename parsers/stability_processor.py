from parsers.performance_optimizer import PerformanceOptimizer
from parsers.entity_optimizer import EntityOptimizer


class StabilityProcessor:
    """
    Integrates optimization modules to improve ATS stability.
    """

    @staticmethod
    def process(text, skills, entities):
        optimized_text = PerformanceOptimizer.optimize_text(text)
        optimized_skills = PerformanceOptimizer.remove_duplicate_skills(skills)
        optimized_entities = EntityOptimizer.normalize_entities(entities)

        return {
            "optimized_text": optimized_text,
            "optimized_skills": optimized_skills,
            "optimized_entities": optimized_entities,
        }