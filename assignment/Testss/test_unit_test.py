import unittest
from pay.processor import PaymentProcessor
from pay.order import LineItem
from pay.order import LineItem, Order

API_KEY = "6cfb67f3-6281-4031-b893-ea85db0dce20"


def test_invalid_api_key() -> None:
    with unittest.raises(ValueError):
        payment_processor = PaymentProcessor("")
        payment_processor.charge("1249190007575069", 8, 2026, 100)


def test_card_number_valid_date():
    payment_processor = PaymentProcessor(API_KEY)
    assert payment_processor.validate_card("1249190007575069", 8, 2026)


def test_card_number_invalid_date():
    payment_processor = PaymentProcessor(API_KEY)
    assert not payment_processor.validate_card("1249190007575069", 11, 2000)


def test_card_number_invalid_luhn():
    payment_processor = PaymentProcessor(API_KEY)
    assert not payment_processor.luhn_checksum("1249190007575068")


def test_card_number_valid_luhn():
    payment_processor = PaymentProcessor(API_KEY)
    assert payment_processor.luhn_checksum("1249190007575069")


def test_charge_card_valid():
    payment_processor = PaymentProcessor(API_KEY)
    payment_processor.charge("1249190007575069", 8, 2026, 100)


def test_charge_card_invalid():
    with unittest.raises(ValueError):
        payment_processor = PaymentProcessor(API_KEY)
        payment_processor.charge("1249190007575068", 8, 2026, 100)


def test_line_item_total() -> None:
    line_item = LineItem(name="Test", price=100)
    assert line_item.total == 100


def test_line_item_total_quantity() -> None:
    line_item = LineItem(name="Test", price=100, quantity=2)
    assert line_item.total == 200


def test_empty_order_total() -> None:
    order = Order()
    assert order.total == 0


def test_order_total() -> None:
    order = Order()
    order.line_items.append(LineItem(name="Test", price=100))
    assert order.total == 100

unittest.main()



