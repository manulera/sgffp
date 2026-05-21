import os
import json

os.system("bash run.sh")

with open("child.json", "r") as f:
    full_json = json.load(f)

history_nodes = full_json["blocks"]["11"]

parent1 = next(node for node in history_nodes if node["length"] == 2505)
parent2 = next(node for node in history_nodes if node["length"] == 2818)

with open("parent.json", "r") as f:
    parent1_json = json.load(f)
with open("parent2.json", "r") as f:
    parent2_json = json.load(f)

parent1_main = parent1_json["blocks"]["0"][0]
parent2_main = parent2_json["blocks"]["0"][0]

assert parent1_main["sequence"] == parent1["sequence"]
assert parent2_main["sequence"] == parent2["sequence"]
