def value(ab): 
	if (ab == 'I'): 
		return 1
	if (ab == 'V'): 
		return 5
	if (ab == 'X'): 
		return 10
	if (ab == 'L'): 
		return 50
	if (ab == 'C'): 
		return 100
	if (ab == 'D'): 
		return 500
	if (ab == 'M'): 
		return 1000
	return -1

def romanToDecimal(str): 
	rese1 = 0
	i = 0
	while (i < len(str)): 
		s1 = value(str[i]) 
		if (i+1 < len(str)): 
			s2 = value(str[i+1]) 
			if (s1 >= s2): 
				rese1 = rese1 + s1 
				i = i + 1
			else: 
				rese1 = rese1 + s2 - s1 
				i = i + 2
		else: 
			rese1 = rese1 + s1 
			i = i + 1
	return rese1 
J = input()
print(romanToDecimal(J)) 
