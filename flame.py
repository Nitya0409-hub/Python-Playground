def flames_result(name1, name2):
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()
    name1_list = list(name1)
    name2_list = list(name2)

    for ch in name1[:]:
        if ch in name2_list:
            name1_list.remove(ch)
            name2_list.remove(ch)
    count = len(name1_list) + len(name2_list)

    flames = ["F", "L", "A", "M", "E", "S"]
    while len(flames) > 1:
        split_index = (count % len(flames)) - 1

        if split_index >= 0:
            flames = flames[split_index + 1:] + flames[:split_index]
        else:
            flames.pop()
    final_letter = flames[0]

    results = {
        "F": "Friends",
        "L": "Love",
        "A": "Affection",
        "M": "Marriage",
        "E": "Enemies",
        "S": "Siblings"
    }

    return results[final_letter]
print("----- FLAMES GAME -----")
name1 = input("Enter first name: ")
name2 = input("Enter second name: ")

result = flames_result(name1, name2)
print("\nRelationship according to FLAMES:", result)
