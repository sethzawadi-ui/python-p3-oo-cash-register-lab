class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        self.last_transaction_amount = price * quantity
        self.total += self.last_transaction_amount

        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:
            # Apply discount correctly
            self.total = self.total * (100 - self.discount) / 100

            # Must print with $ sign AND integer total
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        # Remove amount
        self.total -= self.last_transaction_amount

        # Remove last item(s)
        if self.items:
            self.items.pop()

        # If all items removed, reset total
        if not self.items:
            self.total = 0.0
