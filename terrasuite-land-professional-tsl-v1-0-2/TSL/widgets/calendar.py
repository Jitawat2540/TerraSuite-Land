"""Reusable monthly calendar widget."""

from __future__ import annotations

import calendar
from datetime import date

import customtkinter as ctk

from config.theme import THEME
from widgets.card import Card
from widgets.icons import text_font


class MonthlyCalendar(Card):
    """Compact monthly calendar that highlights today."""

    def __init__(self, master: ctk.CTkBaseClass, today: date | None = None) -> None:
        super().__init__(master, padding=16)
        self.today = today or date.today()
        self._build()

    def _build(self) -> None:
        for column in range(7):
            self.content.grid_columnconfigure(column, weight=1, uniform="calendar")

        ctk.CTkLabel(
            self.content,
            text=self.today.strftime("%B %Y"),
            text_color=THEME.text,
            font=text_font(18, "bold"),
        ).grid(row=0, column=0, columnspan=7, sticky="w", pady=(0, 12))

        for column, weekday in enumerate(("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")):
            ctk.CTkLabel(
                self.content,
                text=weekday,
                text_color=THEME.muted_text,
                font=text_font(12, "bold"),
            ).grid(row=1, column=column, sticky="ew", pady=(0, 6))

        month_days = calendar.Calendar(firstweekday=0).monthdatescalendar(
            self.today.year,
            self.today.month,
        )
        for week_index, week in enumerate(month_days, start=2):
            for column, day in enumerate(week):
                is_current_month = day.month == self.today.month
                is_today = day == self.today
                fg_color = THEME.accent if is_today else "transparent"
                text_color = "#ffffff" if is_today else THEME.text
                if not is_current_month:
                    text_color = "#a7b9b5"

                cell = ctk.CTkFrame(self.content, fg_color=fg_color, corner_radius=12, height=34)
                cell.grid(row=week_index, column=column, sticky="nsew", padx=2, pady=2)
                cell.grid_propagate(False)
                cell.grid_columnconfigure(0, weight=1)
                cell.grid_rowconfigure(0, weight=1)
                ctk.CTkLabel(
                    cell,
                    text=str(day.day),
                    text_color=text_color,
                    font=text_font(12, "bold" if is_today else "normal"),
                ).grid(row=0, column=0)
