import string

def caesar_code(inf, number):
	"""
		This function encode and decode the document by caesar 
		solutions
	inf: (information) that is a mess, document or something in 
	lower_case
	number: the order of character was changed like a:1,b:2, 1+1 if a mapsto b	
	"""
	out_inf=""
	for i in range(len(inf)):
		if inf[i] in string.ascii_lowercase:
			out_inf=out_inf+string.ascii_lowercase[string.ascii_lowercase.find(inf[i])+number]
		else:
			out_inf=out_inf+inf[i]
	return out_inf

def main():
	mess=input("").lower()
	encode=caesar_code(mess,1)
	print(encode)

	decode=caesar_code(encode,-1)
	print(decode)
	
if __name__=="__main__":
	main()	
