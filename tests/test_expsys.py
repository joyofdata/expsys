from expsys import load_from_file, QA, interact
from pathlib import Path
import click
import pytest


def test_load_from_file():
    res = load_from_file(Path(__file__).parent / "example.json")
    assert isinstance(res, QA)


@pytest.fixture
def qa():
    return load_from_file(Path(__file__).parent / "example.json")


@pytest.mark.parametrize(
    "input_seq, exp_res_list",
    # fmt: off
    [
        ([True,  True],  ["q 1", "q 1.1", "y 1.1"]),
        ([True,  False], ["q 1", "q 1.1", "n 1.1"]),
        ([False, False], ["q 1", "q 1.2", "n 1.2"]),
    ],
    # fmt: on
)
def test_interact(monkeypatch, capsys, qa, input_seq, exp_res_list):
    res_list = []
    input_seq.reverse()  # reverse because we pop off it
    with monkeypatch.context() as mc:

        def _confirm(txt, default):
            res_list.append(txt)
            return input_seq.pop()

        mc.setattr(click, "confirm", _confirm)
        interact(qa)
        out, _ = capsys.readouterr()
        res_list.append(out.strip())

        assert res_list == exp_res_list
