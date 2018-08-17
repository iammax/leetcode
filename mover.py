import os
files = os.listdir('.')
import shutil

for q in files:
	if q[0:4] == 'prob':
		shutil.move(q, q[0]+q[5:])
