import json
with open("emp.json","r",encoding='utf-8')as file:
    jsonData=json.load(file)
    print("type of JSON object:",type(jsonData))
    for name in jsonData:
        print("Name:",name)
        print("Phone Number:",jsonData[name]["number"])
        print("Age:",jsonData[name]["age"])
        print("Address:")
        for line in jsonData[name]["address"]:
            print(line)
            print()
