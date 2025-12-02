"""
E-commerce order processing tools.

This module defines all tools for order processing, inventory management,
and payment handling with their corresponding compensation operations.
"""

import logging
from langchain_core.tools import tool
from typing import Dict, Any

logger = logging.getLogger(__name__)


# Inventory Management Tools
@tool
def reserve_inventory(product_id: str, quantity: int) -> Dict[str, Any]:
    """Reserve inventory for a product.
    
    Args:
        product_id: The product identifier
        quantity: Number of units to reserve
        
    Returns:
        Dictionary with reservation_id and status
    """
    logger.info(f"Reserving inventory: {product_id} x {quantity}")
    reservation_id = f"RES-{product_id}-{quantity}"
    return {
        "reservation_id": reservation_id,
        "product_id": product_id,
        "quantity": quantity,
        "status": "reserved"
    }


@tool
def release_inventory(reservation_id: str) -> str:
    """Release reserved inventory.
    
    Args:
        reservation_id: The reservation identifier to release
        
    Returns:
        Confirmation message
    """
    logger.info(f"COMPENSATION: Releasing inventory reservation {reservation_id}")
    return f"Inventory reservation {reservation_id} released successfully"


# Order Management Tools
@tool
def create_order(customer_id: str, items: str) -> Dict[str, Any]:
    """Create a new order.
    
    Args:
        customer_id: Customer identifier
        items: Comma-separated list of product IDs
        
    Returns:
        Dictionary with order_id and order details
    """
    logger.info(f"Creating order for customer {customer_id} with items {items}")
    order_id = f"ORD-{customer_id}-{len(items.split(','))}"
    return {
        "order_id": order_id,
        "customer_id": customer_id,
        "items": items,
        "status": "created",
        "total_amount": 0.0
    }


@tool
def cancel_order(order_id: str) -> str:
    """Cancel an order.
    
    Args:
        order_id: The order identifier to cancel
        
    Returns:
        Confirmation message
    """
    logger.info(f"COMPENSATION: Cancelling order {order_id}")
    return f"Order {order_id} cancelled successfully"


# Payment Processing Tools
@tool
def process_payment(order_id: str, amount: float, payment_method: str) -> Dict[str, Any]:
    """Process payment for an order.
    
    Args:
        order_id: The order identifier
        amount: Payment amount
        payment_method: Payment method (e.g., 'credit_card', 'paypal')
        
    Returns:
        Dictionary with payment_id and status, or error if payment fails
    """
    logger.info(f"Processing payment for order {order_id}: ${amount} via {payment_method}")
    # Simulate payment failure for certain conditions
    if amount > 10000:
        logger.error(f"Payment failed: amount ${amount} exceeds limit")
        return {
            "error": "Payment amount exceeds limit",
            "status": "error",
            "order_id": order_id
        }
    
    payment_id = f"PAY-{order_id}-{int(amount)}"
    return {
        "payment_id": payment_id,
        "order_id": order_id,
        "amount": amount,
        "payment_method": payment_method,
        "status": "processed",
        "transaction_id": f"TXN-{payment_id}"
    }


@tool
def refund_payment(payment_id: str, transaction_id: str) -> str:
    """Refund a payment.
    
    Args:
        payment_id: The payment identifier
        transaction_id: The transaction identifier
        
    Returns:
        Confirmation message
    """
    logger.info(f"COMPENSATION: Refunding payment {payment_id} (transaction {transaction_id})")
    return f"Payment {payment_id} (transaction {transaction_id}) refunded successfully"


# Shipping Tools
@tool
def create_shipment(order_id: str, address: str) -> Dict[str, Any]:
    """Create a shipment for an order.
    
    Args:
        order_id: The order identifier
        address: Shipping address
        
    Returns:
        Dictionary with shipment_id and tracking information
    """
    logger.info(f"Creating shipment for order {order_id} to {address}")
    shipment_id = f"SHIP-{order_id}"
    return {
        "shipment_id": shipment_id,
        "order_id": order_id,
        "address": address,
        "tracking_number": f"TRACK-{shipment_id}",
        "status": "created"
    }


@tool
def cancel_shipment(shipment_id: str) -> str:
    """Cancel a shipment.
    
    Args:
        shipment_id: The shipment identifier to cancel
        
    Returns:
        Confirmation message
    """
    logger.info(f"COMPENSATION: Cancelling shipment {shipment_id}")
    return f"Shipment {shipment_id} cancelled successfully"
