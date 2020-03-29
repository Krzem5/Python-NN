from nn.nn import NeuralNetwork



D=[[[0,0],[0]],[[1,0],[1]],[[0,1],[1]],[[1,1],[0]]]
nn=NeuralNetwork(2,[2,2],1,lr=0.0075)
while (nn.test(D,log=False)<95):
	nn.train_multiple(D,5000,log=False)
	print("Accuracy: "+str(nn.test(D,log=False)))
a=nn.test(D)
print("="*40+"\nACCURACY: "+str(a)+"\n"+"="*40)