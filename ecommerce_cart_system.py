
"""E-commerce cart system with safer input handling and receipt export."""

import hashlib
import secrets


cart_items = {
    "ITEM1": {"name": "Wireless Mouse", "price": 25.0, "qty": 2},
    "ITEM2": {"name": "Mechanical Keyboard", "price": 80.0, "qty": 1},
    "ITEM3": {"name": "USB-C Hub", "price": 45.0, "qty": 3},
}


def add_item_to_cart(item_id, name, price, qty=1, audit_log=None):
    """Add a new item to the cart and record the action."""
    if audit_log is None:
        audit_log = []

    if item_id in cart_items:
        return False

    if not isinstance(price, (int, float)) or isinstance(price, bool):
        raise ValueError("Price must be numeric.")

    invalid_quantity = (
        not isinstance(qty, int) or isinstance(qty, bool) or qty < 1
    )

    if price < 0 or invalid_quantity:
        raise ValueError(
            "Price must be non-negative and quantity must be positive."
        )

    cart_items[item_id] = {
        "name": name,
        "price": price,
        "qty": qty,
    }

    audit_log.append(f"Added {item_id} with price {price:.2f}")
    return True


def remove_item_from_cart(item_id):
    """Remove an item from the cart if it exists."""
    return cart_items.pop(item_id, None) is not None


def check_cart_status(item_id):
    """Check whether an item exists and has a positive quantity."""
    item = cart_items.get(item_id)
    return item is not None and item["qty"] > 0


def calculate_discounted_total(item_id, discount_rate):
    """Calculate the discounted price for a cart item."""
    if item_id not in cart_items:
        raise KeyError(f"Item not found: {item_id}")

    if not isinstance(discount_rate, (int, float)) or isinstance(
        discount_rate, bool
    ):
        raise ValueError("Discount rate must be numeric.")

    if not 0 <= discount_rate <= 1:
        raise ValueError("Discount rate must be between 0 and 1.")

    base_price = cart_items[item_id]["price"]
    return round(base_price * (1 - discount_rate), 2)


def generate_item_hash(item_id):
    """Generate a SHA-256 hash for an item identifier."""
    return hashlib.sha256(item_id.encode("utf-8")).hexdigest()


def generate_checkout_pin():
    """Generate a secure four-digit checkout PIN."""
    return secrets.randbelow(9000) + 1000


def export_cart_receipt(filename="receipt.txt"):
    """Write the current cart contents to a receipt file."""
    with open(filename, "w", encoding="utf-8") as receipt_file:
        receipt_file.write("E-commerce Cart Receipt\n")

        for item_id, details in cart_items.items():
            line_total = details["price"] * details["qty"]

            line = (
                f"{item_id}: {details['name']} | "
                f"Qty: {details['qty']} | "
                f"Unit price: {details['price']:.2f} | "
                f"Total: {line_total:.2f}\n"
            )
            receipt_file.write(line)

    return filename


def get_cart_summary(items):
    """Return the total number of units in the supplied cart."""
    return sum(
        details["qty"]
        for details in items.values()
        if details["qty"] > 0
    )


def main():
    """Run a demonstration of the cart operations."""
    add_item_to_cart("ITEM4", "Monitor Stand", 35.0, 1)
    remove_item_from_cart("ITEM2")

    print("Is ITEM1 in cart:", check_cart_status("ITEM1"))
    print(
        "Discounted Price:",
        calculate_discounted_total("ITEM1", 0.10),
    )
    print("Item Hash:", generate_item_hash("ITEM1"))
    print("Checkout PIN:", generate_checkout_pin())
    print("Receipt saved to:", export_cart_receipt())
    print("Total items:", get_cart_summary(cart_items))


if __name__ == "__main__":
    main()
