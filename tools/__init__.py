"""Tool definitions for compensation demonstration."""

from tools.inventory import reserve_inventory, release_inventory
from tools.orders import create_order, cancel_order
from tools.payments import process_payment, refund_payment
from tools.shipping import create_shipment, cancel_shipment
from tools.travel import book_flight, cancel_flight, book_hotel, cancel_hotel

__all__ = [
    # Inventory
    "reserve_inventory",
    "release_inventory",
    # Orders
    "create_order",
    "cancel_order",
    # Payments
    "process_payment",
    "refund_payment",
    # Shipping
    "create_shipment",
    "cancel_shipment",
    # Travel
    "book_flight",
    "cancel_flight",
    "book_hotel",
    "cancel_hotel",
]
