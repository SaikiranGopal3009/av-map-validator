from __future__ import annotations

from math import hypot

def validate_centerline(coordinates:list[list[float]], max_segment_length_degrees:float = 0.01)->list[str]:
    '''
    Return validation issues found in one lane centerline coordinate sequence.
    '''
    issues:list[str] = []

    if len(coordinates) < 2:
        return ["Centerline must containt atleast two coordinate positions."]

    valid_points: dict[int, tuple[float, float]] = {}
    for index, coordinate in enumerate(coordinates):
        if len(coordinate) < 2:
            issues.append(f"Position {index} must contain longitude and latitude.")
            continue
        longitude, latitude = coordinate[0], coordinate[1]

        if not -180 <= longitude <= 180:
            issues.append(f"Position {index} has invalid longitude: {longitude}.")

        if not -90 <= latitude <= 90:
            issues.append(f"Position {index} has invalid latitude: {latitude}.")

        valid_points[index] = (longitude,latitude)

    for index in range(len(coordinates) - 1):
        start = valid_points.get(index)
        end = valid_points.get(index + 1)

        if start is None or end is None:
            continue

        segment_length = hypot(end[0] - start[0], end[1] - start[1])

        if segment_length > max_segment_length_degrees:
            issues.append(f"Segment {index} to {index + 1} is too long: {segment_length:.6f} degrees.")

    return issues

