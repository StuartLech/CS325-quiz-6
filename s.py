# Order.py
class Order:
    def __init__(self, customer_info, items, shipping_address):
        self.customer_info = customer_info
        self.items = items
        self.shipping_address = shipping_address

# OrderProcessing.py
class OrderProcessing:
    @staticmethod
    def process_order(order):
        print(f"Processing order for {order.customer_info}")
        Inventory.update_inventory(order.items)
        OrderValidator.validate_order(order)
        total_cost = Pricing.calculate_total_cost(order.items)
        OrderConfirmation.send_confirmation_email(order.customer_info)
        print(f"Order processed with total cost: {total_cost}")

# Inventory.py
class Inventory:
    @staticmethod
    def update_inventory(items):
        print("Updating inventory levels for items.")
        # Update inventory logic here

# OrderValidator.py
class OrderValidator:
    @staticmethod
    def validate_order(order):
        print("Validating order data.")
        # Validation logic here

# Pricing.py
class Pricing:
    @staticmethod
    def calculate_total_cost(items):
        print("Mathing total order cost.")
        # Calculate total cost here
        return 100  # Dummy return value

# OrderConfirmation.py
class OrderConfirmation:
    @staticmethod
    def send_confirmation_email(customer_info):
        print(f"Sending order confirmation email to {customer_info}.")

# main function
def main():
    order = Order("John Doe", ["Item1", "Item2"], "1234 Main St")
    OrderProcessing.process_order(order)

#if __name__ == "__main__":
    main()
