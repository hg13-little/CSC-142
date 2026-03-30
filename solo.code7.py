from abc import ABC, abstractmethod

# Part 1: Base Class
class Item(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_cost(self):
        pass


# Part 2: Subclasses
class ByWeightItem(Item):
    def __init__(self, name, weight, cost_per_pound):
        super().__init__(name)
        self.weight = weight
        self.cost_per_pound = cost_per_pound

    def calculate_cost(self):
        return self.weight * self.cost_per_pound


class ByQuantityItem(Item):
    def __init__(self, name, quantity, cost_each):
        super().__init__(name)
        self.quantity = quantity
        self.cost_each = cost_each

    def calculate_cost(self):
        return self.quantity * self.cost_each


# Part 3: Product Classes

class Grapes(ByWeightItem):
    def __init__(self, weight):
        super().__init__("Grapes", weight, 2.50)


class Bananas(ByWeightItem):
    def __init__(self, weight):
        super().__init__("Bananas", weight, 0.75)


class Oranges(ByQuantityItem):
    def __init__(self, quantity):
        super().__init__("Oranges", quantity, 1.00)


class Milk(ByQuantityItem):
    def __init__(self, quantity):
        super().__init__("Milk", quantity, 3.25)


# Part 4: Order Class
class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.calculate_cost()
        return total

    def get_items(self):
        return self.items

    def __len__(self):
        return len(self.items)


# Driver Code
order = Order()

order.add_item(Grapes(2.0))        # 2 lbs grapes
order.add_item(Bananas(3.5))       # 3.5 lbs bananas
order.add_item(Oranges(4))         # 4 oranges
order.add_item(Milk(2))            # 2 gallons of milk

print("Receipt:")
for item in order.get_items():
    print(f"{item.name}: ${item.calculate_cost():.2f}")

print("-------------------")
print(f"Total: ${order.calculate_total():.2f}")
print(f"Number of items: {len(order)}")