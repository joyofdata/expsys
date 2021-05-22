from expsys import load_from_file, QA, interact
from pathlib import Path
import click


def test_load_from_file():
    res = load_from_file(Path(__file__).parent / "example.json")
    assert isinstance(res, QA)


def test_interact(monkeypatch, capsys):
    qa = load_from_file(Path(__file__).parent / "example.json")
    with monkeypatch.context() as mc:
        res = []

        def _confirm(txt, default):
            res.append(txt)
            return True

        mc.setattr(click, "confirm", _confirm)
        interact(qa)
        out, _ = capsys.readouterr()
        res.append(out.strip())

        assert res == ["question 1", "question 1.1", "y 1.1"]
