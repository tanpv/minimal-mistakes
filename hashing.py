import hashlib

print hashlib.sha256('hello world').hexdigest()
print hashlib.sha256('hello world').hexdigest()
print hashlib.sha256('Hello world').hexdigest()

found = False
nonce = 0

while found == False:
	hash_string = hashlib.sha256('helloworld{0}'.format(nonce)).hexdigest()
	print hash_string
	if hash_string[:2] == "000":
		found = True
	else:
		print nonce
		nonce = nonce + 1