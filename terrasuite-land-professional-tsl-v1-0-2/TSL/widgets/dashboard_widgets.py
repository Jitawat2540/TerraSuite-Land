"""Dashboard-specific reusable widgets."""

from __future__ import annotations

from collections.abc import Sequence

import customtkinter as ctk

from config.theme import THEME
from widgets.card import Card
from widgets.icons import ICONS, icon_font, text_font


class MetricTile(ctk.CTkFrame):
    """Small KPI tile."""

    def __init__(self, master: ctk.CTkBaseClass, label: str, value: int, icon: str) -> None:
        super().__init__(master, fg_color=THEME.accent_soft, corner_radius=16)
        self.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(
            self,
            text=icon,
            text_color=THEME.accent,
            font=icon_font(18),
            width=28,
        ).grid(row=0, column=0, padx=(12, 8), pady=12)

        text_box = ctk.CTkFrame(self, fg_color="transparent")
        text_box.grid(row=0, column=1, sticky="ew", padx=(0, 12), pady=10)
        ctk.CTkLabel(
            text_box,
            text=str(value),
            text_color=THEME.text,
            font=text_font(22, "bold"),
        ).grid(row=0, column=0, sticky="w")
        ctk.CTkLabel(
            text_box,
            text=label,
            text_color=THEME.muted_text,
            font=text_font(12),
        ).grid(row=1, column=0, sticky="w")


class CompanyCard(Card):
    """Company overview card with KPI tiles."""

    def __init__(self, master: ctk.CTkBaseClass, company: dict[str, object]) -> None:
        super().__init__(master, padding=18)
        self.content.grid_columnconfigure(0, weight=1)

        header = ctk.CTkFrame(self.content, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew")
        header.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(
            header,
            text=ICONS["company"],
            text_color=THEME.accent,
            font=icon_font(32),
            width=48,
        ).grid(row=0, column=0, padx=(0, 12))

        ctk.CTkLabel(
            header,
            text=str(company["name"]),
            text_color=THEME.text,
            font=text_font(22, "bold"),
        ).grid(row=0, column=1, sticky="w")

        ctk.CTkButton(
            header,
            text="View Details",
            width=120,
            height=36,
            corner_radius=18,
            fg_color=THEME.accent,
            hover_color="#0b7f76",
            font=text_font(13, "bold"),
        ).grid(row=0, column=2, sticky="e")

        metric_grid = ctk.CTkFrame(self.content, fg_color="transparent")
        metric_grid.grid(row=1, column=0, sticky="ew", pady=(18, 0))
        for column in range(4):
            metric_grid.grid_columnconfigure(column, weight=1, uniform="metrics")

        metrics = company["metrics"]
        metric_items = (
            ("Projects", metrics["projects"], ICONS["project"]),
            ("Pending", metrics["pending"], ICONS["pending"]),
            ("Completed", metrics["completed"], ICONS["completed"]),
            ("Cancelled", metrics["cancelled"], ICONS["cancelled"]),
        )
        for column, (label, value, icon) in enumerate(metric_items):
            tile = MetricTile(metric_grid, label, int(value), icon)
            tile.grid(row=0, column=column, sticky="ew", padx=(0 if column == 0 else 8, 0))


class PendingTable(Card):
    """Simple responsive table for pending work."""

    def __init__(self, master: ctk.CTkBaseClass, title: str, rows: Sequence[dict[str, str]]) -> None:
        super().__init__(master, padding=16)
        for column in range(6):
            self.content.grid_columnconfigure(column, weight=1, uniform=f"{title}-table")

        ctk.CTkLabel(
            self.content,
            text=title,
            text_color=THEME.text,
            font=text_font(18, "bold"),
        ).grid(row=0, column=0, columnspan=6, sticky="w", pady=(0, 12))

        headers = ("Quotation", "Project", "Survey No.", "Receive Date", "Due Date", "Overdue Days")
        for column, header in enumerate(headers):
            ctk.CTkLabel(
                self.content,
                text=header,
                text_color=THEME.muted_text,
                font=text_font(12, "bold"),
                anchor="w",
            ).grid(row=1, column=column, sticky="ew", padx=4, pady=(0, 6))

        for row_index, row in enumerate(rows, start=2):
            bg = "#f8fcfb" if row_index % 2 == 0 else "#ffffff"
            for column, key in enumerate(("quotation", "project", "survey", "receive", "due", "overdue")):
                cell = ctk.CTkFrame(self.content, fg_color=bg, corner_radius=8)
                cell.grid(row=row_index, column=column, sticky="ew", padx=3, pady=3)
                cell.grid_columnconfigure(0, weight=1)
                ctk.CTkLabel(
                    cell,
                    text=row[key],
                    text_color=THEME.danger if key == "overdue" else THEME.text,
                    font=text_font(12, "bold" if key == "overdue" else "normal"),
                    anchor="w",
                ).grid(row=0, column=0, sticky="ew", padx=8, pady=8)


class NotesCard(Card):
    """Notes, reminders, and mock events card."""

    def __init__(self, master: ctk.CTkBaseClass, items: Sequence[tuple[str, str]]) -> None:
        super().__init__(master, padding=16)
        self.content.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            self.content,
            text="Notes",
            text_color=THEME.text,
            font=text_font(18, "bold"),
        ).grid(row=0, column=0, sticky="w", pady=(0, 12))

        for row, (title, detail) in enumerate(items, start=1):
            item = ctk.CTkFrame(self.content, fg_color="#f6fbfa", corner_radius=14)
            item.grid(row=row, column=0, sticky="ew", pady=5)
            item.grid_columnconfigure(1, weight=1)
            ctk.CTkLabel(
                item,
                text=ICONS["note"],
                text_color=THEME.accent,
                font=icon_font(16),
            ).grid(row=0, column=0, padx=(12, 8), pady=10)
            ctk.CTkLabel(
                item,
                text=title,
                text_color=THEME.text,
                font=text_font(13, "bold"),
                anchor="w",
            ).grid(row=0, column=1, sticky="ew", padx=(0, 12), pady=(8, 0))
            ctk.CTkLabel(
                item,
                text=detail,
                text_color=THEME.muted_text,
                font=text_font(12),
                anchor="w",
            ).grid(row=1, column=1, sticky="ew", padx=(0, 12), pady=(0, 8))


class QuickActionCard(ctk.CTkButton):
    """Large rounded quick action card."""

    def __init__(self, master: ctk.CTkBaseClass, label: str, icon: str) -> None:
        super().__init__(
            master,
            text=f"{icon}\n{label}",
            height=92,
            corner_radius=20,
            fg_color=THEME.surface,
            hover_color="#effaf8",
            border_width=1,
            border_color=THEME.border,
            text_color=THEME.text,
            font=text_font(13, "bold"),
        )
