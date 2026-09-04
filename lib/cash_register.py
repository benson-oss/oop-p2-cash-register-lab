class CashRegister:
    def __init__(self, discount=0):
        # Attributes
        self.total = 0
        self.items = []
        self.previous_transactions = []
        
        # Discount property initialization
        self._discount = 0
        self.discount = discount  # uses property setter

    # Property for discount
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    # Methods
    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        self.items.append({"item": item, "price": price, "quantity": quantity})
        self.previous_transactions.append(
            {"action": "add", "item": item, "price": price, "quantity": quantity}
        )

    def apply_discount(self):
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            self.previous_transactions.append(
                {"action": "discount", "discount": self.discount}
            )
            print(f"Applied {self.discount}% discount (-{discount_amount:.2f})")
        else:
            print("No discount set.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("No transactions to void.")
            return

        last = self.previous_transactions.pop()

        if last["action"] == "add":
            self.total -= last["price"] * last["quantity"]
            # remove item from items list
            for i in range(len(self.items)):
                if self.items[i]["item"] == last["item"]:
                    self.items.pop(i)
                    break
            print(f"Voided item: {last['item']}")
        elif last["action"] == "discount":
            # restore discount
            discount_amount = self.total * (last["discount"] / (100 - last["discount"]))
            self.total += discount_amount
            print(f"Voided discount of {last['discount']}%")
