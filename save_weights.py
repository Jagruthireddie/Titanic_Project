import json

weights = {

    "w1": 0.1102,
    "w2": 0.1402,
    "w3": 0.1709,
    "w4": 0.2102,
    "w5": 0.2402,
    "w6": 0.2709,
    "w7": 0.3163,
    "w8": 0.3465,
    "bh1": 0.1011,
    "bh2": 0.1012,
    "bo": 0.1114

}

with open("ann_weights.json", "w") as f:
    json.dump(weights, f, indent=4)

print("Weights saved successfully!")