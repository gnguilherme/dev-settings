"""Unit tests for the src module."""

from src.main import print_hello_name


def test_print_hello_name(capsys):
    """Test print_hello_name."""
    print_hello_name("World")
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"
    print_hello_name("Alice")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Alice!\n"
    print_hello_name("Bob")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Bob!\n"
    print_hello_name("Charlie")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Charlie!\n"
    print_hello_name("David")
    captured = capsys.readouterr()
    assert captured.out == "Hello, David!\n"
    print_hello_name("Eve")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Eve!\n"
    print_hello_name("Frank")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Frank!\n"
    print_hello_name("Grace")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Grace!\n"
    print_hello_name("Heidi")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Heidi!\n"
    print_hello_name("Ivan")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Ivan!\n"
    print_hello_name("Judy")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Judy!\n"
    print_hello_name("Mallory")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Mallory!\n"
    print_hello_name("Oscar")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Oscar!\n"
    print_hello_name("Peggy")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Peggy!\n"
    print_hello_name("Trent")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Trent!\n"
    print_hello_name("Walter")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Walter!\n"
    print_hello_name("Eve")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Eve!\n"
