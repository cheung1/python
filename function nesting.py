

def testB():
	print '--testB--'

def testA():
	print '-----Astart------'
	testB()
	testC()
	print '--testA--'
	print '-----Aend------'
	
#testC is behind this sentence,cannot find it when not meet it 

def testC():
	print '--testC--'



testA()
#testC()
