def add_item(item, cart=[]):
    cart.append(item)
    return cart

print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))



# Part B - Correct function
def add_item(item, cart=None):

    if cart is None:
        cart = []

    cart.append(item)

    return cart


print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))


# Part C

# Create cart
def create_cart(owner, discount=0):

    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


# Add items
def add_to_cart(cart, name, price, qty=1):

    item = {
        "name": name,
        "price": price,
        "qty": qty
    }

    cart["items"].append(item)


# Update tuple
def update_price(price_tuple, new_price):

    try:
        price_tuple[0] = new_price

    except TypeError:
        print("Tuple is immutable. Cannot modify tuple.")


# Calculate total
def calculate_total(cart):

    total = 0

    for item in cart["items"]:

        total += item["price"] * item["qty"]

    discount_amount = (total * cart["discount"]) / 100

    final_total = total - discount_amount

    return final_total


# Customer 1
cart1 = create_cart("Aarav", 10)

add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 500, 2)

# Customer 2
cart2 = create_cart("Riya", 5)

add_to_cart(cart2, "Phone", 20000, 1)
add_to_cart(cart2, "Charger", 1000, 1)


# Display carts
print("\nCart 1")
print(cart1)

print("\nCart 2")
print(cart2)


# Totals
print("\nTotal for Cart 1:", calculate_total(cart1))
print("Total for Cart 2:", calculate_total(cart2))


# Tuple example
price_tuple = (100, 200, 300)

update_price(price_tuple, 500)


"""
Discussion Points

1. Why is discount=0 safe but cart=[] dangerous?

discount=0 is immutable.
cart=[] is mutable and shared between calls.

2. Difference between rebinding and mutating?

Rebinding means assigning a new object.
Mutating means changing existing object.

3. Mutable and Immutable

Mutable:
list, dict, set

Immutable:
tuple, str, int

4. If list is passed into function and modified,
changes reflect outside because list is mutable
and both variables reference same object.
"""