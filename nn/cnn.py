def conv(img,f):
	o=[[0]*len(img[0]) for _ in range(0,len(img))]
	ox,oy=int(len(f[0])/2),int(len(f)/2)
	for y in range(0,len(img)):
		for x in range(0,len(img[0])):
			s=0
			for j in range(-oy,oy+1):
				for i in range(-ox,ox+1):
					if (x-i<0 or x-i>=len(img[0]) or y-j<0 or y-j>=len(img)):
						continue
					s+=img[y-j][x-i]*f[j+oy][i+ox]
			o[y][x]=s
	return o



def pool(img,m,s):
	o=[[0]*int(len(img[0])/s) for _ in range(0,int(len(img)/s))]
	for y in range(0,int(len(img)/s)):
		for x in range(0,int(len(img[0])/s)):
			a=[]
			for j in range(0,s):
				for i in range(0,s):
					a+=[img[y*s+j][x*s+i]]
			if (m=="max"):
				o[y][x]=max(a)
			elif (m=="avg"):
				o[y][x]=sum(a)/len(a)
	return o



def fc(img,af):
	o=[[0]*len(img[0]) for _ in range(0,len(img))]
	for y in range(0,len(img)):
		for x in range(0,len(img[0])):
			if (af=="sigmoid"):
				o[y][x]=1/(1+math.exp(-img[y][x]))
			elif (af=="relu"):
				o[y][x]=max(0,img[y][x])
	return o