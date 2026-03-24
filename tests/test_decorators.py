import pytest

from src.decorators import log


def test_log_console_success(capsys):
    @log()
    def add(x, y):
        return x + y

    add(1, 2)
    captured = capsys.readouterr()
    assert "add ok" in captured.out


def test_log_console_error(capsys):
    @log()
    def division(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        division(1, 0)
    captured = capsys.readouterr()
    content = captured.out
    assert "division error: ZeroDivisionError" in content
    assert "Inputs: (1, 0), {}" in content


def test_log_file_success(tmp_path):
    file = tmp_path / "file.txt"

    @log(filename=str(file))
    def add(x, y):
        return x + y

    add(1, 2)

    with open(file, "r", encoding="utf-8") as f:
        assert "add ok" in f.read()


def test_log_file_error(tmp_path):
    file = tmp_path / "file.txt"

    @log(filename=str(file))
    def division(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        division(1, 0)

    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
        assert "division error: ZeroDivisionError" in content
        assert "Inputs: (1, 0), {}" in content
