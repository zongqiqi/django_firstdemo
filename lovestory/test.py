import os 

def getimage():
	images=[]
	path=r'/static/lovestory/loveimage/'
	pwd=os.path.dirname(__file__).replace('\\','/')
	dest=pwd+path
	files=os.listdir(dest)
	for file in files:
		mijp=os.path.splitext(file)[1]
		if mijp=='.jpg':
			images.append(file)
	return images