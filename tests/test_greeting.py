"""greeting test module."""

from minister import hello


def test_greeting() -> None:
    """Assert greeting message."""
    assert hello() == "Hello from minister!"
