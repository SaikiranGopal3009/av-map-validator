from pathlib import Path

from av_map_validator.io import load_centerlines

def test_load_centerlines_reads_two_lane_lines():
    data_path = Path("data/sample_lanes.geojson")

    centerlines = load_centerlines(data_path)

    assert len(centerlines) == 2
    assert len(centerlines[0]) == 3
    assert centerlines[0][0] == [-87.6300, 41.8800]