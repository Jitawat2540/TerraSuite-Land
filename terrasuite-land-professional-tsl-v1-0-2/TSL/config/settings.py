"""Static application settings."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class WindowSettings:
    """Window sizing and metadata."""

    title: str = "TerraSuite Land Professional"
    width: int = 1600
    height: int = 900
    min_width: int = 1400
    min_height: int = 800


WINDOW = WindowSettings()

