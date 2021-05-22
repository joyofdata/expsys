import json
from typing import Optional, Union

import click
from pydantic import BaseModel, StrictStr


class QA(BaseModel):
    """
    Models QA binary tree.
    """
    q: StrictStr
    y: Optional[Union["QA", StrictStr]]
    n: Optional[Union["QA", StrictStr]]


QA.update_forward_refs()


def load_from_file(fn: str) -> QA:
    """
    Loads Expert System from JSON file.
    :param fn: File name.
    :return: Expert System.
    """
    with open(fn) as f:
        qa = QA(**json.load(f))
    return qa


def interact(qa: Union[QA, str]) -> None:
    """
    Interacts with User through Expert System.
    :param qa: Expert System.
    :return: Nada.
    """
    a = click.confirm(qa.q, default=None)
    n = getattr(qa, {True: "y", False: "n"}.get(a))
    if isinstance(n, QA):
        interact(n)
    else:
        print(n)


@click.command()
@click.option("--file", help="Json file containing expert system logic.")
def main(file:str) -> None:
    """
    CLI Interface.
    :param file: File name.
    :return: None
    """
    qa = load_from_file(file)
    interact(qa)
