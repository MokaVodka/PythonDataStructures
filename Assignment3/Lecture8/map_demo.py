import HashMap as hm

# Name/age data
dict = {"Jonas": 61, "Maria": 60, "Nils": 60, "Carina": 58, "Samuel": 31,
        "David": 29, "Alice": 27, "Alexander": 35, "Johanna": 37, "Gustav": 32,
        "Tom": 1, "Alvar": 1, "Kia": 65, "Ida": 29, "Adam": 36, "Hampus": 28,
        "Pappa": 98, "Mamma": 96, "Morre": 118}
updates = {"Jonas": 62, "Maria": 61, "Nils": 61, "Carina": 59, "Samuel": 32}

# Add name/age data
print("\nAdding name/age pairs")
map = hm.HashMap()
for pair in dict.items():
    map.put(pair[0], pair[1])
print("Size:", map.get_size())
print("Capacity:", map.get_capacity())

# Update certain values
print("Update certain values")
for pair in updates.items():
    map.put(pair[0], pair[1])
print(map)

# Look up values
print("\nLooking up certain values")
print("Look up Jonas", map.get("Jonas"))
print("Look up Samuel", map.get("Samuel"))
print("Look up Daniel", map.get("Daniel"))

# Remove key/value pairs
remove = ["Mamma", "Pappa", "Morre", "Hampus", "Kia", "Adam",
          "Maria", "Carina", "Ida", "Daniel"]
lookup = ["Jonas", "Samuel", "David", "Johanna", "Pappa"]
print("\nRemove certain values")
for name in remove:
    print(f"Remove {name}:", map.remove(name))
for name in lookup:
    print(f"Looking up {name}: ", map.get(name))

# Final diagnistics
print("\nSize:", map.get_size())
print("Capacity:", map.get_capacity())
print(map)

# as_list
tuples = map.as_list()
print("\nPair count:", map.get_size())
print(tuples)
