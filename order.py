
from pyscript import display, document

menu_prices = {
    "Nan Tea": 85.00,
    "Caramel Macchiato": 99.99,
    "Red Velvet Cake": 350.00,
    "Iced Tea": 70.00,
    "Sparkling Water": 40.00
}

def create_order(e):
    name = document.getElementById("cust_name").value
    address = document.getElementById("cust_address").value
    contact = document.getElementById("cust_contact").value

    selected_items = []
    total = 0

    for item_id, item_name in [
        ("nan_tea", "Nan Tea"),
        ("caramel_macchiato", "Caramel Macchiato"),
        ("red_velvet_cake", "Red Velvet Cake"),
        ("iced_tea", "Iced Tea"),
        ("sparkling_water", "Sparkling Water")
    ]:
        checkbox = document.getElementById(item_id)
        qty_input = document.getElementById(f"{item_id}_qty")

        if checkbox.checked:
            qty = int(qty_input.value)
            selected_items.append(f"{item_name} x{qty}")
            total += menu_prices[item_name] * qty

    document.getElementById("output").innerHTML = ""

    order_summary = f"""
    <b>Order Summary</b><br>
    Name: {name}<br>
    Address: {address}<br>
    Contact: {contact}<br><br>
    Items Ordered: {', '.join(selected_items) if selected_items else 'No items selected'}<br><br>
    <b>Total Amount: ₱{total:.2f}</b>
    """

    display(order_summary, target="output")
