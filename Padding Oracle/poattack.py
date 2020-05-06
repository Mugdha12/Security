import po1 as po
def paddingAmt(c):
	iv=c[:16]
	cblock=c[16:]
	i=15
	result=0
	while i>=0:
		curr_byte=iv[i]
		x=ord(curr_byte)^ord('\xff')
		y=x^ord('\x01')
		if i == 15:
			newiv=iv[:i] + chr(y)
		else:
			newiv=iv[:i] + chr(y) + iv[(i+1):]
		try:
			po.dec_check(newiv+cblock)
		except:
			i -= 1
		else:
			return 15-i

def attack1(c):
	iv=c[:16]
	cblock=c[16:]
	plen=paddingAmt(c)
	mlen=16-plen
	j=mlen
	i=plen
	s=""
	tryiv=iv
	while j>0:
		diff=(i)^(i+1)
		newiv=tryiv[:j]
		y=j
		while y<16:
			newiv=newiv+chr(ord(tryiv[y])^diff)
			y += 1
		
		for byte in range(256):
			tryiv = newiv[:(j-1)] + chr(byte) + newiv[j:]
			try:
				po.dec_check(tryiv+cblock)
			except:
				pass
			else:
				s= chr((i+1)^ord(iv[j-1])^ord(tryiv[j-1]))+s
				break
				
		j -= 1
		i += 1
	x=0
	while x<plen:
		s=s+chr(plen)
		x += 1
	return s

def attack(c):
	iv=c[:16]
	x=16
	s=""
	while x != len(c):
		cblock=c[x:x+16]
		if paddingAmt(iv+cblock)> 0:
			return s + attack1(iv+cblock)
		else:
			tryiv=iv
			j=15
			newiv=tryiv

			for byte in range(256):
				tryiv = newiv[:(j)] + chr(byte)
				try:
					po.dec_check(tryiv+cblock)
				except:
					pass
				else:
					l= chr(ord('\x01')^ord(iv[j])^ord(tryiv[j]))
					break
			hold=attack1(tryiv+cblock)
			hold=hold[:15]+l
			s=hold+s
		iv=cblock
		x += 16











