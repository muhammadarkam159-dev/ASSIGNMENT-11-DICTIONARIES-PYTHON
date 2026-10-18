# DICTIONARY ACCESS

student = {"name": "Ali", "age": 22, "course": "Python", "marks": 85}
name = student["name"]
marks = student["marks"]
city = student.get("city", "Karachi")
print("Name:", name)
print("Marks:", marks)
print("City:", city)

# UPDATE DICTIONARY

employee = {"name": "Sara", "salary": 100000, "department": "IT"}
employee["salary"] = employee["salary"] * 1.20
employee["bonus"] = 15000
employee["department"] = "Data Engineering"
print("Updated Employee:", employee)

# DICTIONARY METHODS

product = {"id": 101, "name": "Laptop", "price": 120000, "stock": 5}
keys = product.keys()
values = product.values()
items = product.items()
stock = product.pop("stock")
print("Keys:", keys)
print("Values:", values)
print("Items:", items)
print("Removed Stock:", stock)
print("Updated Product:", product)

# MERGE DICTIONARIES

dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 50, "d": 40}
merged = dict1.copy()
merged.update(dict2)
print("Merged Dictionary:", merged)

# STUDENTS MARKS

marks = {"Ali": 85, "Sara": 92, "Ahmed": 78, "Zain": 88}

highest = max(marks.values())
lowest = min(marks.values())
average = sum(marks.values()) / len(marks)
top_student = next(iter(dict(marks.items() & marks.items())))
top_student = dict(zip(marks.values(), marks.keys()))[highest]
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
print("Top Student:", top_student)

# NESTED EMPLOYEE RECORDES

employees = {
    "E101": {"name": "Ali", "salary": 80000},
    "E102": {"name": "Sara", "salary": 120000},
    "E103": {"name": "Ahmed", "salary": 95000}
}
sara_salary = employees["E102"]["salary"]
employees["E101"]["salary"] *= 1.15
total_payroll = (
    employees["E101"]["salary"] +
    employees["E102"]["salary"] +
    employees["E103"]["salary"]
)
print("Sara Salary:", sara_salary)
print("Updated Ali Salary:", employees["E101"]["salary"])
print("Total Payroll:", total_payroll)

# DICTIONARY INVERSION

data = {"Python": "Ali", "SQL": "Sara", "AWS": "Ahmed"}
inverse = dict(zip(data.values(), data.keys()))
print("Inverse Dictionary:", inverse)

# ORDER CALCULATION

order = {
    "laptop": {"price": 120000, "quantity": 2},
    "mouse": {"price": 1500, "quantity": 5},
    "keyboard": {"price": 3500, "quantity": 3}
}
laptop_total = order["laptop"]["price"] * order["laptop"]["quantity"]
mouse_total = order["mouse"]["price"] * order["mouse"]["quantity"]
keyboard_total = order["keyboard"]["price"] * order["keyboard"]["quantity"]
grand_total = laptop_total + mouse_total + keyboard_total
discount = grand_total * 0.10
final_amount = grand_total - discount
print("Laptop Subtotal:", laptop_total)
print("Mouse Subtotal:", mouse_total)
print("Keyboard Subtotal:", keyboard_total)
print("Grand Total:", grand_total)
print("Discount:", discount)
print("Final Amount:", final_amount)

# EMPLOYEE PERFORMANCE

employees = {
    "Ali": {"python": 90, "sql": 85, "aws": 88},
    "Sara": {"python": 95, "sql": 92, "aws": 90},
    "Ahmed": {"python": 80, "sql": 87, "aws": 84}
}
ali_avg = sum(employees["Ali"].values()) / len(employees["Ali"])
sara_avg = sum(employees["Sara"].values()) / len(employees["Sara"])
ahmed_avg = sum(employees["Ahmed"].values()) / len(employees["Ahmed"])
averages = {
    "Ali": ali_avg,
    "Sara": sara_avg,
    "Ahmed": ahmed_avg
}
top_average = max(averages.values())
top_performer = dict(zip(averages.values(), averages.keys()))[top_average]
highest_sql = max(
    employees["Ali"]["sql"],
    employees["Sara"]["sql"],
    employees["Ahmed"]["sql"]
)
print("Ali Average:", ali_avg)
print("Sara Average:", sara_avg)
print("Ahmed Average:", ahmed_avg)
print("Top Performer:", top_performer)
print("Highest SQL Score:", highest_sql)

# INVENTORY MANAGEMENT

inventory = {
    "P101": {"name": "Laptop", "price": 120000, "stock": 5},
    "P102": {"name": "Mouse", "price": 1500, "stock": 20},
    "P103": {"name": "Keyboard", "price": 3500, "stock": 10}
}
laptop_value = inventory["P101"]["price"] * inventory["P101"]["stock"]
mouse_value = inventory["P102"]["price"] * inventory["P102"]["stock"]
keyboard_value = inventory["P103"]["price"] * inventory["P103"]["stock"]
total_value = laptop_value + mouse_value + keyboard_value
values = {
    "P101": laptop_value,
    "P102": mouse_value,
    "P103": keyboard_value
}
highest_value = max(values.values())
most_valuable_id = dict(zip(values.values(), values.keys()))[highest_value]
most_valuable_item = inventory[most_valuable_id]["name"]
inventory["P101"]["stock"] -= 2
inventory["P102"]["stock"] -= 5
print("Total Inventory Value:", total_value)
print("Most Valuable Item:", most_valuable_item)
print("Updated Inventory:", inventory)