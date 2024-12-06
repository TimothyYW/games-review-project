import pytest
from datetime import timedelta

from allauth.core import ratelimit
from allauth.core.ratelimit import Rate


@pytest.mark.parametrize(
    "rate,expected",
    [
        ("5/m", [Rate(5, 60, "ip")]),
        ("5/m/user", [Rate(5, 60, "user")]),
        ("2/3.5m/key", [Rate(2, 210, "key")]),
        ("3/5m/user,20/0.5m/ip", [
            Rate(3, 300, "user"),
            Rate(20, 30, "ip")
        ]),
        ("7/2h", [Rate(7, 7200, "ip")]),
        ("7/0.25d", [Rate(7, 21600, "ip")]),
    ],
)
def test_parse_rates(rate, expected):
    """Test rate limit string parsing with various formats."""
    rates = ratelimit._parse_rates(rate)
    assert len(rates) == len(expected)
    for actual, expect in zip(rates, expected):
        assert actual.amount == expect.amount
        assert actual.duration == expect.duration
        assert actual.per == expect.per


@pytest.mark.parametrize(
    "invalid_rate",
    [
        "",  # Empty string
        "5",  # Missing duration
        "5/",  # Missing duration
        "/m",  # Missing amount
        "a/m",  # Invalid amount
        "5/z",  # Invalid duration unit
        "5/m/invalid",  # Invalid per
    ],
)
def test_parse_rates_invalid(invalid_rate):
    """Test handling of invalid rate limit strings."""
    with pytest.raises((ValueError, AttributeError)):
        ratelimit._parse_rates(invalid_rate)
