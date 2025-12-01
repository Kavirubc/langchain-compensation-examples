"""Custom strategies for compensation middleware."""

from strategies.error_detection import PaymentErrorStrategy, BookingErrorStrategy

__all__ = [
    "PaymentErrorStrategy",
    "BookingErrorStrategy",
]
