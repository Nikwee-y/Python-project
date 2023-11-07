name1 = input("Enter the name1: ").lower()
name2 = input("Enter the name2: ").lower()

name1 = name1.replace(" ", "")
name2 = name2.replace(" ", "")

count = len(name1 + name2)

print(f"Number of letters left after removing common letters: {count}")

if count > 0:
    relationships = ["Friends", "Lovers", "Affectionate", "Marriage", "Enemies", "Siblings"]

    while len(relationships) > 1:
        c = count % len(relationships)
        s_index = c - 1 if c > 0 else len(relationships) - 1
        left = relationships[:s_index]
        right = relationships[s_index + 1:]
        relationships = right + left

    print(f"The relationship is: {relationships[0]}")
else:
    print("Please enter different names.")
