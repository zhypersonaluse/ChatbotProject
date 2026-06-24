from typing import List, TypedDict

class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        
    """
    question: str
    generation: str
    web_search: bool
    documents: List[str]