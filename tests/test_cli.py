import pytest
from dev_utils.cli import main

def test_cli_add(capsys):
    main(["add", "5", "7"])
    captured = capsys.readouterr()
    assert "12\n" == captured.out

def test_cli_factorial(capsys):
    main(["factorial", "5"])
    captured = capsys.readouterr()
    assert "120\n" == captured.out

def test_cli_reverse_string(capsys):
    main(["reverse-string", "hello"])
    captured = capsys.readouterr()
    assert "olleh\n" == captured.out

def test_cli_palindrome_check(capsys):
    main(["palindrome-check", "racecar"])
    captured = capsys.readouterr()
    assert "True\n" == captured.out

def test_cli_generate_password(capsys):
    main(["generate-password", "--length", "8"])
    captured = capsys.readouterr()
    assert len(captured.out.strip()) == 8
