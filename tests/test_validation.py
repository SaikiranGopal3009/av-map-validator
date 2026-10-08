from av_map_validator.validation import validate_centerline


def test_valid_centerline_has_no_issues():
    coordinates = [
        [-87.6300, 41.8800],
        [-87.6295, 41.8804],
        [-87.6290, 41.8808],
    ]

    assert validate_centerline(coordinates) == []


def test_centerline_with_too_few_points_has_issue():
    coordinates = [
        [-87.6300, 41.8800],
    ]

    issues = validate_centerline(coordinates)

    assert issues == [
        "Centerline must containt atleast two coordinate positions."
    ]


def test_centerline_with_large_gap_has_issue():
    coordinates = [
        [-87.6300, 41.8800],
        [-80.0000, 42.0000],
    ]

    issues = validate_centerline(coordinates)

    assert len(issues) == 1
    assert "Segment 0 to 1 is too long" in issues[0]