import random
def MakeRandomVarificationCode(length = 50):
	digits = []
	for i in range(length):
		digit = random.randint(0,10+26+26-1)
		if digit < 10:
			digits.append(str(digit))
			continue
		digit -= 10
		if digit < 26:
			digits.append(chr(digit+ord('A')))
			continue
		digit -= 26
		digits.append(chr(digit+ord('a')))
	code = ""
	for ch in digits:
		code += ch
	return code
