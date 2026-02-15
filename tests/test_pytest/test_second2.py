import pytest
from freezegun import freeze_time
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


def generate_week_schedule(
    days_ahead: int = 7, tz: str = "Europe/Helsinki"
) -> list[tuple[str, str, str]]:
    day_names = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    today = datetime.now(ZoneInfo(tz)).date()
    lst = []
    for i in range(days_ahead):
        d = today + timedelta(days=i)
        wd = d.weekday()
        day_abbr = day_names[wd]
        date_str = d.strftime("%d/%m")
        time_str = "Closed" if wd >= 5 else "00:05–22:55"
        lst.append((day_abbr, date_str, time_str))
    return lst


@freeze_time("2024-01-01")
@pytest.mark.parametrize("days, tz, expected", [
    (7, "Europe/Helsinki", [
        ("Mo", "01/01", "00:05–22:55"),
        ("Tu", "02/01", "00:05–22:55"),
        ("We", "03/01", "00:05–22:55"),
        ("Th", "04/01", "00:05–22:55"),
        ("Fr", "05/01", "00:05–22:55"),
        ("Sa", "06/01", "Closed"),
        ("Su", "07/01", "Closed")
    ]),
    (0, "Europe/Helsinki", []),
    (-1, "Europe/Helsinki", [])
])
def test_generate_week_schedule_positive(days, tz, expected):
    assert generate_week_schedule(days_ahead=days, tz=tz) == expected


@freeze_time("2024-01-01")
@pytest.mark.parametrize("days, tz, expected", [
    (7, "Europe/Helsinki", [
        ("Mo", "01/01", "Closed"),
        ("Tu", "02/01", "Closed"),
        ("We", "03/01", "Closed"),
        ("Th", "04/01", "Closed"),
        ("Fr", "05/01", "Closed"),
        ("Sa", "06/01", "00:05–22:55"),
        ("Su", "07/01", "00:05–22:55")
    ])
])
def test_generate_week_schedule_negative(days, tz, expected):
    assert generate_week_schedule(days_ahead=days, tz=tz) == expected
