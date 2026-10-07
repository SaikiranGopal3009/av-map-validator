from __future__ import annotations

import json
from pathlib import Path

def load_centerlines(path: str| Path) -> list[list[list[float]]]:
    """
    Loads LineString center line coordinates from a GeoJSON FeatureCollection.
    """

    with open(path, "r", encoding = "utf-8") as file:
        geojson = json.load(file)

    if geojson.get("type") != "FeatureCollection":
        raise ValueError("Expected a GeoJSON FeatureCollection.")

    centerlines = []

    for feature in geojson.get("features",[]):
        geometry = feature.get("geometry") or {}

        if geometry.get("type") != "LineString":
            continue

        coordinates = geometry.get("coordinates",[])

        if len(coordinates) < 2:
            raise ValueError("A LineString must contain atleast two positions.")

        centerlines.append(coordinates)

    return centerlines
