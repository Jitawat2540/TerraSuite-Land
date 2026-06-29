"""Theme constants for the TerraSuite Land Professional shell."""

from __future__ import annotations

from dataclasses import dataclass

import customtkinter as ctk


@dataclass(frozen=True)
class AppTheme:
    """Centralized color and spacing tokens."""

    appearance_mode: str = "Light"
    color_theme: str = "blue"
    font_family: str = "Segoe UI"
    thai_font_family: str = "Noto Sans Thai"
    icon_font_family: str = "Segoe Fluent Icons"
    gradient_start: str = "#EAF8F7"
    gradient_end: str = "#DDF4F1"
    app_background: str = "#EAF8F7"
    sidebar_background: str = "#0f5f59"
    sidebar_button: str = "#0f5f59"
    sidebar_button_hover: str = "#13756e"
    sidebar_button_active: str = "#e8fffb"
    sidebar_button_active_text: str = "#0f5f59"
    header_background: str = "#F8FFFD"
    footer_background: str = "#F8FFFD"
    content_background: str = "#EAF8F7"
    surface: str = "#ffffff"
    text: str = "#12332f"
    muted_text: str = "#66817c"
    border: str = "#E6ECEB"
    shadow: str = "#c9dfdc"
    accent: str = "#0d9488"
    accent_soft: str = "#d8f4ef"
    warning: str = "#c47a14"
    success: str = "#17864f"
    danger: str = "#bf3b3b"
    sidebar_width: int = 240
    header_height: int = 96
    footer_height: int = 48
    page_padding: int = 28
    card_radius: int = 20


THEME = AppTheme()


def configure_appearance() -> None:
    """Apply global CustomTkinter appearance settings."""

    ctk.set_appearance_mode(THEME.appearance_mode)
    ctk.set_default_color_theme(THEME.color_theme)
