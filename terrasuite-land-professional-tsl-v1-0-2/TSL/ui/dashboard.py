"""Dashboard page."""

from __future__ import annotations

import tkinter as tk

import customtkinter as ctk

from config.theme import THEME
from widgets.calendar import MonthlyCalendar
from widgets.dashboard_widgets import CompanyCard, NotesCard, PendingTable, QuickActionCard
from widgets.icons import ICONS, text_font
from widgets.page import BasePage


COMPANIES = (
    {
        "name": "BTC Survey",
        "metrics": {
            "projects": 42,
            "pending": 9,
            "completed": 29,
            "cancelled": 4,
        },
    },
    {
        "name": "SPS Survey",
        "metrics": {
            "projects": 36,
            "pending": 7,
            "completed": 26,
            "cancelled": 3,
        },
    },
)

PENDING_WORK = {
    "BTC": (
        {
            "quotation": "BTC-Q-2601",
            "project": "North Canal Boundary",
            "survey": "BTC-SV-114",
            "receive": "2026-06-18",
            "due": "2026-06-27",
            "overdue": "2",
        },
        {
            "quotation": "BTC-Q-2602",
            "project": "Hill Plot Mapping",
            "survey": "BTC-SV-118",
            "receive": "2026-06-20",
            "due": "2026-06-29",
            "overdue": "0",
        },
        {
            "quotation": "BTC-Q-2603",
            "project": "Industrial Lot Check",
            "survey": "BTC-SV-121",
            "receive": "2026-06-22",
            "due": "2026-06-28",
            "overdue": "1",
        },
    ),
    "SPS": (
        {
            "quotation": "SPS-Q-2608",
            "project": "Eastern Road Survey",
            "survey": "SPS-SV-082",
            "receive": "2026-06-17",
            "due": "2026-06-26",
            "overdue": "3",
        },
        {
            "quotation": "SPS-Q-2610",
            "project": "Parcel Marker Review",
            "survey": "SPS-SV-087",
            "receive": "2026-06-21",
            "due": "2026-06-30",
            "overdue": "0",
        },
        {
            "quotation": "SPS-Q-2612",
            "project": "West Field Control",
            "survey": "SPS-SV-091",
            "receive": "2026-06-23",
            "due": "2026-06-28",
            "overdue": "1",
        },
    ),
}

NOTES = (
    ("Mock Events", "Team schedule review at 14:00"),
    ("Reminder", "Check pending survey documents"),
    ("Notes", "Prepare dashboard feedback for Sprint 3"),
)

QUICK_ACTIONS = (
    ("Import", ICONS["import"]),
    ("Search", ICONS["search"]),
    ("Status", ICONS["status"]),
    ("Calendar", ICONS["calendar"]),
    ("Reports", ICONS["reports"]),
    ("Export", ICONS["export"]),
    ("Open Project Folder", ICONS["folder"]),
)


class DashboardPage(BasePage):
    """Dashboard page with mock company status data."""

    page_title = "Dashboard"

    def __init__(self, master: ctk.CTkBaseClass) -> None:
        super().__init__(master)
        self.gradient_canvas = tk.Canvas(self, highlightthickness=0, borderwidth=0)
        self.gradient_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.bind("<Configure>", self._draw_gradient)

        self.scroll = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent",
            scrollbar_button_color=THEME.accent,
            scrollbar_button_hover_color="#0b7f76",
        )
        self.scroll.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.scroll.grid_columnconfigure(0, weight=1)

        self._build()

    def _draw_gradient(self, event: tk.Event) -> None:
        self.gradient_canvas.delete("gradient")
        height = max(event.height, 1)
        width = max(event.width, 1)
        start = self._hex_to_rgb(THEME.gradient_start)
        end = self._hex_to_rgb(THEME.gradient_end)
        for line in range(height):
            ratio = line / height
            color = self._blend(start, end, ratio)
            self.gradient_canvas.create_line(0, line, width, line, fill=color, tags="gradient")
        self.gradient_canvas.lower("gradient")

    def _build(self) -> None:
        content = ctk.CTkFrame(self.scroll, fg_color="transparent")
        content.grid(row=0, column=0, sticky="nsew", padx=THEME.page_padding, pady=THEME.page_padding)
        content.grid_columnconfigure(0, weight=1)
        content.grid_rowconfigure(6, weight=1)

        self._build_company_section(content)
        self._build_pending_section(content)
        self._build_calendar_notes_section(content)
        self._build_quick_actions(content)

    def _build_company_section(self, parent: ctk.CTkFrame) -> None:
        company_grid = ctk.CTkFrame(parent, fg_color="transparent")
        company_grid.grid(row=0, column=0, sticky="ew")
        for column in range(2):
            company_grid.grid_columnconfigure(column, weight=1, uniform="companies")

        for column, company in enumerate(COMPANIES):
            card = CompanyCard(company_grid, company)
            card.grid(row=0, column=column, sticky="ew", padx=(0 if column == 0 else 12, 0))

    def _build_pending_section(self, parent: ctk.CTkFrame) -> None:
        ctk.CTkLabel(
            parent,
            text="งานค้าง / งานยังไม่เสร็จ",
            text_color=THEME.text,
            font=text_font(22, "bold", thai=True),
            anchor="w",
        ).grid(row=1, column=0, sticky="w", pady=(26, 12))

        pending_grid = ctk.CTkFrame(parent, fg_color="transparent")
        pending_grid.grid(row=2, column=0, sticky="ew")
        for column in range(2):
            pending_grid.grid_columnconfigure(column, weight=1, uniform="pending")

        for column, company_key in enumerate(("BTC", "SPS")):
            table = PendingTable(pending_grid, company_key, PENDING_WORK[company_key])
            table.grid(row=0, column=column, sticky="ew", padx=(0 if column == 0 else 12, 0))

    def _build_calendar_notes_section(self, parent: ctk.CTkFrame) -> None:
        secondary_grid = ctk.CTkFrame(parent, fg_color="transparent")
        secondary_grid.grid(row=3, column=0, sticky="ew", pady=(26, 0))
        secondary_grid.grid_columnconfigure(0, weight=2, uniform="secondary")
        secondary_grid.grid_columnconfigure(1, weight=1, uniform="secondary")

        calendar = MonthlyCalendar(secondary_grid)
        calendar.grid(row=0, column=0, sticky="nsew", padx=(0, 12))

        notes = NotesCard(secondary_grid, NOTES)
        notes.grid(row=0, column=1, sticky="nsew")

    def _build_quick_actions(self, parent: ctk.CTkFrame) -> None:
        ctk.CTkLabel(
            parent,
            text="Quick Actions",
            text_color=THEME.text,
            font=text_font(22, "bold"),
            anchor="w",
        ).grid(row=4, column=0, sticky="w", pady=(26, 12))

        actions_grid = ctk.CTkFrame(parent, fg_color="transparent")
        actions_grid.grid(row=5, column=0, sticky="ew", pady=(0, 8))
        for column in range(len(QUICK_ACTIONS)):
            actions_grid.grid_columnconfigure(column, weight=1, uniform="actions")

        for column, (label, icon) in enumerate(QUICK_ACTIONS):
            action = QuickActionCard(actions_grid, label, icon)
            action.grid(row=0, column=column, sticky="ew", padx=(0 if column == 0 else 10, 0))

    @staticmethod
    def _hex_to_rgb(value: str) -> tuple[int, int, int]:
        value = value.lstrip("#")
        return tuple(int(value[index : index + 2], 16) for index in (0, 2, 4))

    @staticmethod
    def _blend(start: tuple[int, int, int], end: tuple[int, int, int], ratio: float) -> str:
        channels = tuple(round(start[index] + (end[index] - start[index]) * ratio) for index in range(3))
        return f"#{channels[0]:02x}{channels[1]:02x}{channels[2]:02x}"
