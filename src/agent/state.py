from typing import NotRequired

from typing_extensions import TypedDict

class State(TypedDict):
    question:str
    answer:NotRequired[str]
    model_name:NotRequired[str]