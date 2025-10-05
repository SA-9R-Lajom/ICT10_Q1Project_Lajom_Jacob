from pyscript import document, display


def create_order(e):

    item1 = document.getElementById("item1")
    item2 = document.getElementById("item2")
    item3 = document.getElementById("item3")
    item4 = document.getElementById("item4")
    item5 = document.getElementById("item5")

total = (
    float(item1.value) * item1.checked +
    float(item2.value) * item2.checked +
    float(item3.value) * item3.checked +
    float(item4.value) * item4.checked +
    float(item5.value) * item5.checked
)

customer_name = document.getElementById("customer_name").value
customer_address = document.getElementById("customer_address").value
contact_number = document.getElementById("contact_number").value

display(f"Thank you {customer_name} for your order!")
display(f"Your order will be shipped to: {customer_address}")
display(f"If we need to contact you, we will call: {contact_number}")
display(f"Your total is: ${total:.2f}")