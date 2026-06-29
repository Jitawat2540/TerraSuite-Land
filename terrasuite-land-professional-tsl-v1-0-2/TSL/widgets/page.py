"""Base page primitives."""

from __future__ import annotations

import customtkinter as ctk

from config.theme import THEME
from widgets.icons import text_font


class BasePage(ctk.CTkFrame):
    """Shared base class for application pages."""

    page_title = "Page"

    def __init__(self, master: ctk.CTkBaseClass) -> None:
        super().__init__(master, corner_radius=0, fg_color=THEME.content_background)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)


class PlaceholderPage(BasePage):
    """A lightweight placeholder for modules that are not implemented yet."""

    description = "This workspace is ready for future functionality."

    def __init__(self, master: ctk.CTkBaseClass) -> None:
        super().__init__(master)

        panel = ctk.CTkFrame(
            self,
            fg_color=THEME.surface,
            border_color=THEME.border,
            border_width=1,
            corner_radius=THEME.card_radius,
        )
        panel.grid(row=0, column=0, sticky="nsew", padx=THEME.page_padding, pady=THEME.page_padding)
        panel.grid_columnconfigure(0, weight=1)
        panel.grid_rowconfigure(2, weight=1)

        ctk.CTkLabel(
            panel,
            text=self.page_title,
            text_color=THEME.text,
            font=text_font(28, "bold"),
        ).grid(row=0, column=0, sticky="w", padx=28, pady=(28, 8))

        ctk.CTkLabel(
            panel,
            text=self.description,
            text_color=THEME.muted_text,
            font=text_font(15),
        ).grid(row=1, column=0, sticky="w", padx=28)
