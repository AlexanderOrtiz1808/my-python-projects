inventory = []
forbidden_items = ["knife", "gun", "bomb", "cigarette", "alcohol"]
items_count = 0

while items_count < 5:
    item = input("What item did you find? ")
    inventory.append(item)
    items_count += 1

inventory.sort()
print(f"Collection mission complete. Your inventory is: {inventory}")

contraband = input("Halt! What item are you looking for, officer? ")
print(f"I am looking for these forbidden items: {forbidden_items}")

if contraband in inventory:
    inventory.remove(contraband)
    print("Contraband detected! Confiscating now.")
    print(f"Your updated inventory is: {inventory}")
else:
    print("All clean. You may continue your journey.")