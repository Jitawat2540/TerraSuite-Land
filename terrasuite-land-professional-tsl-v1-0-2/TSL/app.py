"""TerraSuite Land Professional application entry point."""

from __future__ import annotations

from collections.abc import Callable

import customtkinter as ctk

from config.settings import WINDOW
from config.theme import THEME, configure_appearance
from ui.backup_page import BackupPage
from ui.calendar_page import CalendarPage
from ui.dashboard import DashboardPage
from ui.export_page import ExportPage
from ui.import_page import ImportPage
from ui.reports_page import ReportsPage
from ui.search_page import SearchPage
from ui.settings_page import SettingsPage
from ui.status_page import StatusPage
from widgets.footer import Footer
from widgets.header import Header
from widgets.icons import ICONS
from widgets.sidebar import NavigationItem, Sidebar


PageFactory = Callable[[ctk.CTkBaseClass], ctk.CTkFrame]


class TerraSuiteApp(ctk.CTk):
    """Main application shell."""

    def __init__(self) -> None:
        configure_appearance()
        super().__init__()

        self.title(WINDOW.title)
        self.geometry(f"{WINDOW.width}x{WINDOW.height}")
        self.minsize(WINDOW.min_width, WINDOW.min_height)
        self.configure(fg_color=THEME.app_background)

        self._navigation_items = (
            NavigationItem("dashboard", "Dashboard", ICONS["dashboard"]),
            NavigationItem("import", "Import Data", ICONS["import"]),
            NavigationItem("search", "Search / Edit", ICONS["search"]),
            NavigationItem("status", "Status", ICONS["status"]),
            NavigationItem("calendar", "Calendar", ICONS["calendar"]),
            NavigationItem("reports", "Reports", ICONS["reports"]),
            NavigationItem("export", "Export", ICONS["export"]),
            NavigationItem("backup", "Backup", ICONS["backup"]),
            NavigationItem("settings", "Settings", ICONS["settings"]),
        )

        self._page_factories: dict[str, PageFactory] = {
            "dashboard": DashboardPage,
            "import": ImportPage,
            "search": SearchPage,
            "status": StatusPage,
            "calendar": CalendarPage,
            "reports": ReportsPage,
            "export": ExportPage,
            "backup": BackupPage,
            "settings": SettingsPage,
        }
        self._pages: dict[str, ctk.CTkFrame] = {}
        self._active_page_key: str | None = None

        self._build_layout()
        self.show_page("dashboard")

    def _build_layout(self) -> None:
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)

        self.sidebar = Sidebar(self, self._navigation_items, self.show_page)
        self.sidebar.grid(row=0, column=0, rowspan=3, sticky="nsw")

        self.header = Header(self)
        self.header.grid(row=0, column=1, sticky="ew")

        self.content_frame = ctk.CTkFrame(self, corner_radius=0, fg_color=THEME.content_background)
        self.content_frame.grid(row=1, column=1, sticky="nsew")
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_rowconfigure(0, weight=1)

        self.footer = Footer(self)
        self.footer.grid(row=2, column=1, sticky="ew")

    def show_page(self, page_key: str) -> None:
        """Switch the dynamic main frame to the selected page."""

        if page_key == self._active_page_key:
            return

        if page_key not in self._page_factories:
            raise KeyError(f"Unknown page key: {page_key}")

        if self._active_page_key is not None:
            self._pages[self._active_page_key].grid_remove()

        page = self._pages.get(page_key)
        if page is None:
            page = self._page_factories[page_key](self.content_frame)
            self._pages[page_key] = page
            page.grid(row=0, column=0, sticky="nsew")
        else:
            page.grid()

        self._active_page_key = page_key
        self.sidebar.set_active(page_key)
        self.header.set_title(getattr(page, "page_title", WINDOW.title))


def main() -> None:
    """Run the application."""

    app = TerraSuiteApp()
    app.mainloop()


if __name__ == "__main__":
    main()
