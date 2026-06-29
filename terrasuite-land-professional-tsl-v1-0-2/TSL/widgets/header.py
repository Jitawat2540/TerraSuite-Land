"""Header component."""

from __future__ import annotations

from datetime import datetime

import customtkinter as ctk

from config.theme import THEME
from widgets.icons import ICONS, icon_font, text_font


class Header(ctk.CTkFrame):
    """Application header displayed above the active page."""

    def __init__(self, master: ctk.CTkBaseClass) -> None:
        super().__init__(
            master,
            height=THEME.header_height,
            corner_radius=0,
            fg_color=THEME.header_background,
        )
        self.grid_propagate(False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        left = ctk.CTkFrame(self, fg_color="transparent")
        left.grid(row=0, column=0, sticky="w", padx=THEME.page_padding, pady=14)

        ctk.CTkLabel(
            left,
            text="สวัสดีครับ, Admin",
            text_color=THEME.text,
            font=text_font(24, "bold", thai=True),
            anchor="w",
        ).grid(row=0, column=0, sticky="w")

        ctk.CTkLabel(
            left,
            text="ยินดีต้อนรับสู่ TerraSuite Land Professional",
            text_color=THEME.muted_text,
            font=text_font(14, thai=True),
            anchor="w",
        ).grid(row=1, column=0, sticky="w", pady=(2, 0))

        right = ctk.CTkFrame(self, fg_color="transparent")
        right.grid(row=0, column=1, sticky="e", padx=THEME.page_padding, pady=14)

        time_box = ctk.CTkFrame(right, fg_color=THEME.accent_soft, corner_radius=18)
        time_box.grid(row=0, column=0, sticky="e", padx=(0, 12))
        self.date_label = ctk.CTkLabel(
            time_box,
            text="",
            text_color=THEME.text,
            font=text_font(13, "bold"),
        )
        self.date_label.grid(row=0, column=0, sticky="e", padx=16, pady=(8, 0))
        self.time_label = ctk.CTkLabel(
            time_box,
            text="",
            text_color=THEME.muted_text,
            font=text_font(12),
        )
        self.time_label.grid(row=1, column=0, sticky="e", padx=16, pady=(0, 8))

        ctk.CTkButton(
            right,
            text=ICONS["notification"],
            width=42,
            height=42,
            corner_radius=21,
            fg_color=THEME.surface,
            hover_color="#effaf8",
            border_width=1,
            border_color=THEME.border,
            text_color=THEME.accent,
            font=icon_font(18),
        ).grid(row=0, column=1, sticky="e")

        self.title_label = ctk.CTkLabel(
            self,
            text="Dashboard",
            text_color=THEME.muted_text,
            font=text_font(1),
        )
        self._update_clock()

    def set_title(self, title: str) -> None:
        """Update the visible page title."""

        self.title_label.configure(text=title)

    def _update_clock(self) -> None:
        now = datetime.now()
        self.date_label.configure(text=now.strftime("%A, %d %B %Y"))
        self.time_label.configure(text=now.strftime("%H:%M:%S"))
        self.after(1000, self._update_clock)
