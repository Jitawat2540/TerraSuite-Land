"""Shared icon constants and helpers."""

from __future__ import annotations

import customtkinter as ctk

from config.theme import THEME


ICONS = {
    "dashboard": "⌂",
    "import": "⇩",
    "search": "⌕",
    "status": "✓",
    "calendar": "▦",
    "reports": "▤",
    "export": "⇧",
    "backup": "◴",
    "settings": "⚙",
    "notification": "◌",
    "company": "■",
    "project": "□",
    "pending": "◷",
    "completed": "✓",
    "cancelled": "×",
    "folder": "▣",
    "note": "◇",
}


def icon_font(size: int) -> ctk.CTkFont:
    """Return the configured Windows icon font."""

    return ctk.CTkFont(family="Segoe UI Symbol", size=size)


def text_font(size: int, weight: str = "normal", thai: bool = False) -> ctk.CTkFont:
    """Return a standard app font."""

    family = THEME.thai_font_family if thai else THEME.font_family
    return ctk.CTkFont(family=family, size=size, weight=weight)
