# point of sale system 

from pay.processor import PaymentProcessor
from pay.order import LineItem
from pay.order import LineItem, Order

def main():
    # Test card number: 1249190007575069
    order = Order()
    order.line_items.append(LineItem(name="banku", price=200_00, quantity=2))
    order.line_items.append(LineItem(name="fufu", price=50_00))
    pay_order(order)


if __name__ == "__main__":
    main()