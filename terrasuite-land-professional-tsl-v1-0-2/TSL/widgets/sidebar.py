"""Sidebar navigation component."""

from __future__ import annotations

from collections.abc import Callable, Iterable
from dataclasses import dataclass

import customtkinter as ctk

from config.theme import THEME
from widgets.icons import text_font


@dataclass(frozen=True)
class NavigationItem:
    """Navigation metadata used by the sidebar and app controller."""

    key: str
    label: str
    icon: str


class Sidebar(ctk.CTkFrame):
    """Fixed left navigation sidebar."""

    def __init__(
        self,
        master: ctk.CTkBaseClass,
        items: Iterable[NavigationItem],
        on_select: Callable[[str], None],
    ) -> None:
        super().__init__(
            master,
            width=THEME.sidebar_width,
            corner_radius=0,
            fg_color=THEME.sidebar_background,
        )
        self.grid_propagate(False)
        self._buttons: dict[str, tuple[ctk.CTkButton, str]] = {}
        self._on_select = on_select

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(11, weight=1)

        self._build_brand()
        self._build_navigation(items)
        self._build_user_card()

    def _build_brand(self) -> None:
        ctk.CTkLabel(
            self,
            text="TSL",
            text_color="#ffffff",
            font=text_font(34, "bold"),
        ).grid(row=0, column=0, sticky="w", padx=22, pady=(26, 0))

        ctk.CTkLabel(
            self,
            text="TerraSuite Land\nProfessional\nVersion 1.0.0",
            text_color="#d7fffa",
            font=text_font(13),
            justify="left",
        ).grid(row=1, column=0, sticky="w", padx=22, pady=(0, 24))

    def _build_navigation(self, items: Iterable[NavigationItem]) -> None:
        for index, item in enumerate(items, start=2):
            button = ctk.CTkButton(
                self,
                text=f"{item.icon}   {item.label}",
                anchor="w",
                height=42,
                corner_radius=14,
                fg_color=THEME.sidebar_button,
                hover_color=THEME.sidebar_button_hover,
                text_color="#ffffff",
                font=text_font(14, "bold"),
                command=lambda key=item.key: self._on_select(key),
            )
            button.grid(row=index, column=0, sticky="ew", padx=14, pady=3)
            self._buttons[item.key] = (button, item.label)

    def _build_user_card(self) -> None:
        card = ctk.CTkFrame(self, fg_color="#0c4d48", corner_radius=18)
        card.grid(row=12, column=0, sticky="ew", padx=14, pady=(12, 18))
        card.grid_columnconfigure(1, weight=1)

        avatar = ctk.CTkFrame(card, width=40, height=40, fg_color="#e8fffb", corner_radius=20)
        avatar.grid(row=0, column=0, padx=(12, 10), pady=12)
        avatar.grid_propagate(False)
        avatar.grid_columnconfigure(0, weight=1)
        avatar.grid_rowconfigure(0, weight=1)
        ctk.CTkLabel(
            avatar,
            text="A",
            text_color=THEME.sidebar_background,
            font=text_font(18, "bold"),
        ).grid(row=0, column=0)

        user_text = ctk.CTkFrame(card, fg_color="transparent")
        user_text.grid(row=0, column=1, sticky="ew", padx=(0, 12), pady=10)
        ctk.CTkLabel(
            user_text,
            text="Admin",
            text_color="#ffffff",
            font=text_font(14, "bold"),
            anchor="w",
        ).grid(row=0, column=0, sticky="ew")
        ctk.CTkLabel(
            user_text,
            text="Administrator",
            text_color="#d7fffa",
            font=text_font(12),
            anchor="w",
        ).grid(row=1, column=0, sticky="ew")

    def set_active(self, active_key: str) -> None:
        """Visually mark the selected navigation item."""

        for key, (widget, label) in self._buttons.items():
            is_active = key == active_key
            current_icon = widget.cget("text").split("   ", 1)[0]
            widget.configure(
                fg_color=THEME.sidebar_button_active if is_active else THEME.sidebar_button,
                text_color=THEME.sidebar_button_active_text if is_active else "#ffffff",
                text=f"{current_icon}   {label}",
            )
