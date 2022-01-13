#Nhập mệnh đề p,q
stm = input('Enter statement p,q: ')

#Hàm để lấy p,q
def splitStr(s):
	p = ''
	q = ''
	key = ['then']
	for item in key:
		#kiểm tra input dạng: if p then q
		if 'then' in s:
			a = s.split('then')
			p = a[0][len("then")-1:]
			q = a[1][:]
		#kiểm tra input dạng: q when p
		elif 'when' in s:
			a = s.split("when")
			index = s.split(' ')
			ind = a[1].split(' ')
			p = index[0]
			q = ind[1]
			q += a[0][len(index[0]):]
			p += ' '+a[1][len(ind[1])+1:]
		#kiểm tra input dạng: q if p
		elif 'if' in s and not 'then' in s:
			a = s.split('if')
			index = s.split(' ')
			ind = a[1].split(' ')
			p = index[0]
			q = ind[1]
			q += a[0][len(index[0]):]
			p += a[1][len(ind[1])+1:]
	
		#kiểm tra input nhập vào chỉ là: p, q
		else:
			a = s.split(",")
			p = a[0]
			q = a[1]
	return p,q
spl = splitStr(stm)
print('p is: ',spl[0])
print('q is: ',spl[1])
#Chuyển về if p then q
def PthenQ(spl):
	return 'If %s, then %s' %(spl[0],spl[1])
print('Conditional statement: ',PthenQ(spl))
#Chuyển qua ~p v q
def IfThenOr(spl):
	dictKey = {'are': 'are not','am': 'am not','is':'is not','will':'will not','can':'can not','could':'could not','would':'would not',
	'have':'have not', 'has':'has not','more':'less','study': 'not study','it':'it is not'
	}
	#nếu không tìm thấy động từ trong câu thì sẽ báo lỗi
	for item in dictKey:
		if item in spl[0]:
		#khi tìm thấy động từ, tách chuỗi thành 2 đoạn kể từ động từ, thực hiện ghép chuỗi với phủ định của động từ
			a = spl[0].split(item)
			p1 = a[0] +dictKey[item]+ a[1]
			q1 = spl[1]
	return p1 + 'or '+ q1
print('If-Then as Or: ',IfThenOr(spl))
#Chuyển qua dạng Negation: p ^ ~q
def pAndNq(spl):
	p = ''
	dictKey = {'are': 'are not','am': 'am not','is':'is not','will':'will not','can':'can not','could':'could not','would':'would not',
	'have':'have not', 'has':'has not','more':'less','study': 'not study','it':'it is not','go':'not go'
	}
	if 'If' in spl[0]:
		p = spl[0][len('If'):]
	else:
		p = spl[0]
	for item in dictKey:
		if item in spl[1]:
			b = spl[1].split(item)
			q = b[0] + dictKey[item] + b[1]
	return p + 'and '+q
print('Negation: ',pAndNq(spl))
#Chuyển qua dạng Phản đảo: ~q -> ~p 
def nqThennp(spl):
	dictKey = {'are': 'are not','am': 'am not','is':'is not','will':'will not','can':'can not','could':'could not','would':'would not',
	'have':'have not', 'has':'has not','more':'less','study': 'not study','it':'it is not','go':'not go'
	}
	#nếu không tìm thấy động từ trong câu thì sẽ báo lỗi
	for item in dictKey:
		if item in spl[0]:
			a = spl[0].split(item)
			p = a[0] +dictKey[item]+ a[1]
		if item in spl[1]:
			b = spl[1].split(item)
			q = b[0] + dictKey[item] + b[1]
	return q +' then '+ p
print('Contrapositive: ',nqThennp(spl))
#Chuyển qua dạng Đảo: q -> p

def qThenp(spl):
	p = ''
	if 'If' in spl[0]:
		p = spl[0][len('If'):]
	else:
		p = spl[0]
	return 'If %s, then %s' %(spl[1],p)

print('Converse: ',qThenp(spl))
#Chuyển qua dạng nghịch đảo: ~p -> ~q
def notPthennotQ(spl):
	dictKey = {'are': 'are not','am': 'am not','is':'is not','will':'will not','can':'can not','could':'could not','would':'would not',
	'have':'have not', 'has':'has not','more':'less','study': 'not study','it':'it is not','go':'not go'
	}
	for item in dictKey:
		if item in spl[0]:
		#khi tìm thấy động từ, tách chuỗi thành 2 đoạn kể từ động từ, thực hiện ghép chuỗi với phủ định của động từ
			a = spl[0].split(item)
			p = a[0] +dictKey[item]+ a[1]
		if item in spl[1]:
			a1 = spl[1].split(item)
			q = a1[0] +dictKey[item]+ a1[1]
	return p+'then '+q

print('Inverse: ',notPthennotQ(spl))
