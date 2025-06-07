import sys
from modules.greeting import name

print("Hello, Python!")
if 5<2:
  print("correct!")

print(sys.version)

x = 5
x = "Python"
y = "Hello, World!"
y = 4

print(type(x))
print(type(y))

#type cast
x = str(3)
x = int("3")
y = float(3)

print(type(x))
print(type(y))

#output
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x + " "+ y + " " + z)

x = 5
y = 10
print(x + y)

print(str(x) + z)

list = [1, 2, 3, 4]
print(list)

# print(greeting_mod.doGreeting("Jane"))

# print(greeting_mod.person1['name'])

# print(greeting_mod.name)
# print(dir(greeting_mod))

print(name)




# Define the data
data = {
    
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "batters": {
        "batter": [
            { "id": "1001", "type": "Regular" },
            { "id": "1002", "type": "Chocolate" },
            { "id": "1003", "type": "Blueberry" },
            { "id": "1004", "type": "Devil's Food" }
        ]
    },
    "topping": [
        { "id": "5001", "type": "None" },
        { "id": "5002", "type": "Glazed" },
        { "id": "5005", "type": "Sugar" },
        { "id": "5007", "type": "Powdered Sugar" },
        { "id": "5006", "type": "Chocola" }
    ]
}

for t in data["topping"]:
    if "Chocola" in t["type"]:
        print(t)