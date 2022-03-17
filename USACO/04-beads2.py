"""
ID: src.dul1
LANG: PYTHON3
TASK: beads
"""

import pathlib

fin = open (pathlib.Path(__file__).parent.resolve() / 'beads.in', 'r')
fout = open (pathlib.Path(__file__).parent.resolve() / 'beads.out', 'w')
length = int(fin.readline())
necklace = fin.readline().strip()
necklace *= 2
maxes = []
for index, bead in enumerate(necklace[0: length]):
    firstStreak = 1
    i = 1
    while i < length and necklace[index + i] == bead or necklace[index + i] == "w" or bead == "w":
        if (bead == "w") and (necklace[index + i] != "w") :
            bead = necklace[index + i]
        i += 1
        firstStreak += 1
    secondStreak = 0
    while i < length and (necklace[index + i] != bead):
        i += 1
        secondStreak += 1
    maxes.append(firstStreak + secondStreak)

fout.write(f"{max(maxes)}\n")

fout.close()
fin.close()