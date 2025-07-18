import os

KG_RESEARCH_NUM_RETRIEVED_DOCS: int = int(
    os.environ.get("KG_RESEARCH_NUM_RETRIEVED_DOCS", "25")
)


KG_SIMPLE_ANSWER_MAX_DISPLAYED_SOURCES: int = int(
    os.environ.get("KG_SIMPLE_ANSWER_MAX_DISPLAYED_SOURCES", "10")
)


KG_ENTITY_EXTRACTION_TIMEOUT: int = int(
    os.environ.get("KG_ENTITY_EXTRACTION_TIMEOUT", "15")
)

KG_RELATIONSHIP_EXTRACTION_TIMEOUT: int = int(
    os.environ.get("KG_RELATIONSHIP_EXTRACTION_TIMEOUT", "15")
)

KG_STRATEGY_GENERATION_TIMEOUT: int = int(
    os.environ.get("KG_STRATEGY_GENERATION_TIMEOUT", "20")
)

KG_SQL_GENERATION_TIMEOUT: int = int(os.environ.get("KG_SQL_GENERATION_TIMEOUT", "25"))

KG_FILTER_CONSTRUCTION_TIMEOUT: int = int(
    os.environ.get("KG_FILTER_CONSTRUCTION_TIMEOUT", "15")
)


KG_NORMALIZATION_RETRIEVE_ENTITIES_LIMIT: int = int(
    os.environ.get("KG_NORMALIZATION_RETRIEVE_ENTITIES_LIMIT", "100")
)

KG_FILTERED_SEARCH_TIMEOUT: int = int(
    os.environ.get("KG_FILTERED_SEARCH_TIMEOUT", "30")
)


KG_OBJECT_SOURCE_RESEARCH_TIMEOUT: int = int(
    os.environ.get("KG_OBJECT_SOURCE_RESEARCH_TIMEOUT", "30")
)

KG_ANSWER_GENERATION_TIMEOUT: int = int(
    os.environ.get("KG_ANSWER_GENERATION_TIMEOUT", "30")
)

KG_MAX_DEEP_SEARCH_RESULTS: int = int(
    os.environ.get("KG_MAX_DEEP_SEARCH_RESULTS", "30")
)


KG_METADATA_TRACKING_THRESHOLD: int = int(
    os.environ.get("KG_METADATA_TRACKING_THRESHOLD", "10")
)


KG_DEFAULT_MAX_PARENT_RECURSION_DEPTH: int = int(
    os.environ.get("KG_DEFAULT_MAX_PARENT_RECURSION_DEPTH", "2")
)


_KG_NORMALIZATION_RERANK_UNIGRAM_WEIGHT: float = max(
    1e-3,
    min(1, float(os.environ.get("KG_NORMALIZATION_RERANK_UNIGRAM_WEIGHT", "0.25"))),
)
_KG_NORMALIZATION_RERANK_BIGRAM_WEIGHT: float = max(
    1e-3,
    min(1, float(os.environ.get("KG_NORMALIZATION_RERANK_BIGRAM_WEIGHT", "0.25"))),
)
_KG_NORMALIZATION_RERANK_TRIGRAM_WEIGHT: float = max(
    1e-3,
    min(1, float(os.environ.get("KG_NORMALIZATION_RERANK_TRIGRAM_WEIGHT", "0.5"))),
)
_KG_NORMALIZATION_RERANK_NGRAM_SUMS: float = (
    _KG_NORMALIZATION_RERANK_UNIGRAM_WEIGHT
    + _KG_NORMALIZATION_RERANK_BIGRAM_WEIGHT
    + _KG_NORMALIZATION_RERANK_TRIGRAM_WEIGHT
)

KG_NORMALIZATION_RERANK_NGRAM_WEIGHTS: tuple[float, float, float] = (
    _KG_NORMALIZATION_RERANK_UNIGRAM_WEIGHT / _KG_NORMALIZATION_RERANK_NGRAM_SUMS,
    _KG_NORMALIZATION_RERANK_BIGRAM_WEIGHT / _KG_NORMALIZATION_RERANK_NGRAM_SUMS,
    _KG_NORMALIZATION_RERANK_TRIGRAM_WEIGHT / _KG_NORMALIZATION_RERANK_NGRAM_SUMS,
)


KG_NORMALIZATION_RERANK_LEVENSHTEIN_WEIGHT: float = max(
    0,
    min(1, float(os.environ.get("KG_NORMALIZATION_RERANK_LEVENSHTEIN_WEIGHT", "0.25"))),
)


KG_NORMALIZATION_RERANK_THRESHOLD: float = float(
    os.environ.get("KG_NORMALIZATION_RERANK_THRESHOLD", "0.3")
)


KG_CLUSTERING_RETRIEVE_THRESHOLD: float = float(
    os.environ.get("KG_CLUSTERING_RETRIEVE_THRESHOLD", "0.6")
)


KG_CLUSTERING_THRESHOLD: float = float(
    os.environ.get("KG_CLUSTERING_THRESHOLD", "0.96")
)
