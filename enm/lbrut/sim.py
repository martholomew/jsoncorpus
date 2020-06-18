#!/usr/bin/env python3
from difflib import SequenceMatcher
import json

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

with open("a.json", 'r') as f:
    a = json.load(f)
with open("b.json", 'r') as f:
    b = json.load(f)
conc = []
for line in range(1, 16098):
    simp = {}
    a_line = a[str(line)]
    for line_2 in range(1, 12724):
        b_line = b[str(line_2)]
        sim = similar(a_line, b_line)
        simp[line_2] = sim
    simp = sorted(simp.items(), key=lambda x: x[1], reverse=True)
    print("#.", a_line)
    for x in range(0, 5):
        print(f"{x + 1}.", b[str(simp[x][0])], ":", simp[x][0])
    choice = input(">")
    if choice == ".":
        for x in range(5, 10):
            print(f"{x + 1}.", b[str(simp[x][0])], ":", simp[x][0])
        choice = input(">")
    if int(choice) == 0:
        mini_conc = [line, 0]
    if int(choice) > 0:
        mini_conc = [line, simp[int(choice) - 1][0]]
    conc.append(mini_conc)
print(conc)