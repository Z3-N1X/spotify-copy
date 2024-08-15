def InvToJson(data: str) -> dict:
    finalDict = {}

    for item in data.split(","):
        if item == "" or ":" not in item: 
            continue
        itemName = item.split(":")[0]
        itemQuantity = item.split(":")[1]
        finalDict[itemName] = itemQuantity

    return finalDict    

def JsonToInv(data: dict) -> str:
    finalStr = ""

    for item in data.keys():
        finalStr += f"{item}:{data[item]},"

    return finalStr