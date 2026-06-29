"""Footer component."""

from __future__ import annotations

import customtkinter as ctk

from config.theme import THEME
from widgets.icons import text_font


class Footer(ctk.CTkFrame):
    """Application footer displayed at the bottom of the window."""

    def __init__(self, master: ctk.CTkBaseClass) -> None:
        super().__init__(
            master,
            height=THEME.footer_height,
            corner_radius=0,
            fg_color=THEME.footer_background,
        )
        self.grid_propagate(False)
        for column in range(5):
            self.grid_columnconfigure(column, weight=1, uniform="footer")

        items = (
            "Database: SQLite",
            "Python 3.14",
            "Current User: Admin",
            "Backup Status: Ready",
            "Version: 1.0.0",
        )
        for column, text in enumerate(items):
            ctk.CTkLabel(
                self,
                text=text,
                text_color=THEME.muted_text,
                font=text_font(12, "bold" if column == 0 else "normal"),
            ).grid(
                row=0,
                column=column,
                sticky="w" if column == 0 else "ew",
                padx=(THEME.page_padding if column == 0 else 8, 8),
            )
