"""Tests POM para el flujo de checkout de SauceDemo."""

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage


def test_checkout_sin_nombre_muestra_error(authenticated_page):
    """El checkout debe mostrar error cuando se intenta continuar sin datos."""
    InventoryPage(authenticated_page).add_to_cart("Sauce Labs Backpack").go_to_cart()
    CartPage(authenticated_page).proceed_to_checkout()

    checkout = CheckoutPage(authenticated_page)
    checkout.fill_shipping("", "", "").continue_to_overview()

    assert checkout.has_error()
