class CashRegister:
    def __init__(self, discount=0):
        # Attributes
        self.total = 0
        self.items = []
        self.previous_transactions = []

        self._discount = 0
        self.discount = discount

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
    def add_item(self, item, price, quantity=1):
        self.total += price * quantity

        # Add item once for each quantity
        self.items.extend([item] * quantity)

        self.previous_transactions.append({
            "action": "add",
            "item": item,
            "price": price,
            "quantity": quantity
        })
    def apply_discount(self):
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            self.previous_transactions.append({
                "action": "discount",
                "discount": self.discount
            })
            print(
                f"After the discount, the total comes to ${self.total:.0f}."
            )
        else:
            print("There is no discount to apply.")
    def void_last_transaction(self):
        if not self.previous_transactions:
            print("No transactions to void.")
            return
        last = self.previous_transactions.pop()

        if last["action"] == "add":
            self.total -= last["price"] * last["quantity"]
            for _ in range(last["quantity"]):
                if last["item"] in self.items:
                    self.items.remove(last["item"])
            print(f"Voided item: {last['item']}")
        elif last["action"] == "discount":
            # Restore the total before the discount
            discount_amount = (
                self.total * last["discount"]
                / (100 - last["discount"])

            )
            self.total += discount_amount
            print(f"Voided discount of {last['discount']}%")