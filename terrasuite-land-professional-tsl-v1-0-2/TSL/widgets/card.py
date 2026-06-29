"""Reusable card components."""

from __future__ import annotations

import customtkinter as ctk

from config.theme import THEME


class Card(ctk.CTkFrame):
    """White rounded card with a subtle bordered shadow."""

    def __init__(
        self,
        master: ctk.CTkBaseClass,
        *,
        padding: int = 18,
        corner_radius: int | None = None,
    ) -> None:
        super().__init__(
            master,
            fg_color=THEME.shadow,
            corner_radius=(corner_radius or THEME.card_radius) + 2,
        )
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.body = ctk.CTkFrame(
            self,
            fg_color=THEME.surface,
            border_color=THEME.border,
            border_width=1,
            corner_radius=corner_radius or THEME.card_radius,
        )
        self.body.grid(row=0, column=0, sticky="nsew", padx=(0, 3), pady=(0, 4))
        self.body.grid_columnconfigure(0, weight=1)

        self.content = ctk.CTkFrame(self.body, fg_color="transparent", corner_radius=0)
        self.content.grid(row=0, column=0, sticky="nsew", padx=padding, pady=padding)
        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_rowconfigure(0, weight=1)

