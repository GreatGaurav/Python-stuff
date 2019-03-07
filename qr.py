import pyqrcode

def qrcode():
	print(string)
	q = pyqrcode.create(string)
	q.png('TirtT.png', scale=6)
	print("qrcode generated")

string = input("Enter text: ")
qrcode()
#run code by double clicking on the the created file i.e in the python shell