def calculate_discount(price, discount_rate):
    # Ensure price is a valid number
    try:
        price = float(price)
    except ValueError:
        raise ValueError(f"Invalid price value: {price}. Price must be a number.")

    discount_amount = price * discount_rate
    return discount_amount


def apply_discount(price, discount_amount):
    return price - discount_amount


def main():
    products = [
        {"name": "Laptop", "price": 1000, "discount_rate": 0.1},
        {"name": "Smartphone", "price": 800, "discount_rate": 0.15},
        {"name": "Tablet", "price": "500", "discount_rate": 0.2},
        {"name": "Headphones", "price": 200, "discount_rate": 0.05}
    ]

    for product in products:
        print(f"Product: {product['name']}")

        try:
            price = float(product["price"])
            discount_rate = product["discount_rate"]

            discount_amount = calculate_discount(price, discount_rate)
            final_price = apply_discount(price, discount_amount)

            print(f"Original Price: ${price:.2f}")
            print(f"Discount Amount: ${discount_amount:.2f}")
            print(f"Final Price: ${final_price:.2f}")

        except ValueError as e:
            print(f"Error processing product: {e}")

        print()


if __name__ == "__main__":
    main()




