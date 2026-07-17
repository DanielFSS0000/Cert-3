"""Page Object de la pantalla de checkout de SauceDemo."""

from __future__ import annotations
from playwright.sync_api import Page


class CheckoutPage:
    """Representa https://www.saucedemo.com/checkout-step-one.html."""

    URL = "https://www.saucedemo.com/checkout-step-one.html"

    def __init__(self, page: Page) -> None:
        self.page = page
        self._first_name = page.locator('[data-test="firstName"]')
        self._last_name = page.locator('[data-test="lastName"]')
        self._postal_code = page.locator('[data-test="postalCode"]')
        self._continue_btn = page.locator('[data-test="continue"]')
        self._error_msg = page.locator('[data-test="error"]')

    # Acciones

    def fill_shipping(self, first: str, last: str, zip_code: str) -> "CheckoutPage":
        """Rellena los datos de envio del checkout."""
        self._first_name.fill(first)
        self._last_name.fill(last)
        self._postal_code.fill(zip_code)
        return self

    def continue_to_overview(self) -> "CheckoutPage":
        """Hace clic en Continue para avanzar al resumen de compra."""
        self._continue_btn.click()
        return self

    # Consultas

    def is_loaded(self) -> bool:
        """True si la pantalla actual es el primer paso del checkout."""
        return self.page.url == self.URL

    def has_error(self) -> bool:
        """True si hay un mensaje de error visible en pantalla."""
        return self._error_msg.is_visible()
