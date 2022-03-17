"""
ID: src.dul1
LANG: PYTHON3
TASK: beads
"""

import pathlib

fin = open (pathlib.Path(__file__).parent.resolve() / 'beads.in', 'r')
fout = open (pathlib.Path(__file__).parent.resolve() / 'beads.out', 'w')

bNum = int(fin.readline())
beads = fin.readline().strip()

pre = ppre = ''
i=0
cnt = wcnt = 0
bMax = left = 0
isSecond=False
while True:
	if beads[i] != pre:
		if beads[i] == 'w':
			wcnt=1
		else:
			if beads[i] == ppre:
				cnt=cnt+wcnt+1
				wcnt=0
			else:
				ppre=beads[i]
				if left+cnt+wcnt>bMax:
					bMax=left+cnt+wcnt
				if isSecond:
					break

				left=cnt

				if pre == 'w':
					cnt=wcnt+1
					wcnt=0
				else:
					cnt=1

		pre=beads[i]
	else:           
		if beads[i] == 'w':
			wcnt+=1
		else:
			cnt+=1
	i+=1   
	if i==bNum:
		if (cnt+wcnt) == (bNum*2):
			bMax=bNum
			break
		i=0
		isSecond=True

fout.write(f"{bMax}\n")

fout.close()
fin.close()