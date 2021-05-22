from pydantic import BaseModel, StrictStr
from typing import Union, Optional
import click
import json


class QA(BaseModel):
    q: StrictStr
    y: Optional[Union["QA", StrictStr]]
    n: Optional[Union["QA", StrictStr]]


QA.update_forward_refs()


def load_from_file(fn: str) -> QA:
    with open(fn) as f:
        qa = QA(**json.load(f))
    return qa


def interact(qa: Union[QA, str]) -> None:
    a = click.confirm(qa.q, default=None)
    n = getattr(qa, {True: "y", False: "n"}.get(a))
    if isinstance(n, QA):
        interact(n)
    else:
        print(n)
