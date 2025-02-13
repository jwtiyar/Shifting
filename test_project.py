from project import fri_Remove, day_inWeek

def test_fri_Remove():
    # Test for a known Friday
    assert fri_Remove(2023, 10, 6) is True  # October 6, 2023 is a Friday
    # Test for a known non-Friday
    assert fri_Remove(2023, 10, 5) is False  # October 5, 2023 is a Thursday
    # Test for an invalid date
    assert fri_Remove(2023, 2, 30) is False  # February 30, 2023 is an invalid date

def test_day_inWeek():
    cells = ["code", 10, 2023] + [0] * 31
    # Test for fingerprint 2 on a Monday
    result = day_inWeek(2023, 10, 2, 2, cells.copy())  # October 2, 2023 is a Monday
    assert result[4] == "x"
    # Test for fingerprint 3 on a Tuesday
    result = day_inWeek(2023, 10, 3, 3, cells.copy())  # October 3, 2023 is a Tuesday
    assert result[5] == "x"
    # Test for fingerprint 2 on a Friday
    result = day_inWeek(2023, 10, 6, 2, cells.copy())  # October 6, 2023 is a Friday
    assert result[8] == "x"
    # Test for fingerprint 3 on a Friday
    result = day_inWeek(2023, 10, 6, 3, cells.copy())  # October 6, 2023 is also a Friday
    assert result[8] == "x"