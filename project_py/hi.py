from sys import argv
def staat(test):
	test1 = open (test);
	xy = (test1.readline());


	xyb = [i.strip() for i in xy]

	o = ''
	t = ''
	for j in xyb:
	  if j == '' and o == '':     # намираме (x) и (y) 
	    o = t
	    t = ''

	  t += j



	x = int(o)
	y = int(t)
	xc = x
	yc = y


	mat = test1.readlines();



	out = [i.strip() for i in mat]

	bas = [i.strip() for i in mat]





	for num in range(x):
		out[(x-1)] = out[(x-1)].split()         #микро,
		x-=1


	


	x = xc
	

	one = 0
	two = 0

	star =0
	rezx =0    #иксы
	pedx =0    #местечные иксы
	final =0   
	finaltwo =0
	finalc = "S"
	finalctwo = "S"
	con = "S"  #проверка 

	sch =0 
	wh =1
	while wh >sch:
		for i in range(len(out)): 
			for j in range(len(out[i])): 
				if out[i][j] == 'RX' or out[i][j] == 'GX' or out[i][j] == 'BX':
					continue
				#print (out[i][j]) 
				#print (i, j) 
				if con == "S":
					if out[i][j] == 'R'or out[i][j] == 'G'or out[i][j] == 'B':
						con = out[i][j]
						out[i][j] = out[i][j] + 'X'
						rezx += 1
						pedx +=1
						if i>0 and con == out[(i-1)][j]:           #Крест
							out[(i-1)][j] += '*'
							star +=1
						if j>0 and con == out[i][(j-1)]: 
							out[(i)][j-1] += '*'
							star +=1
						if i<(x-1) and con == out[(i+1)][j]:
							out[(i+1)][j] += '*'
							star +=1
						if j<(y-1) and con == out[i][(j+1)]:
							out[(i)][j+1] += '*'
							star +=1
						if star ==0:
							if final <= pedx:
								if final == pedx:
									finaltwo = final
									finalctwo = finalc
								final = pedx
								finalc = con
							pedx =0
							con = "S"

				if out[i][j] == 'R*'or out[i][j] == 'G*'or out[i][j] == 'B*':
					out[i][j] = out[i][j][0:-1]
					out[i][j] = out[i][j] + "X"
					star -=1
					rezx +=1
					pedx +=1
					if i>0 and con == out[(i-1)][j]:           #Крест
						out[(i-1)][j] += '*'
						star +=1
					if j>0 and con == out[(i)][j-1]: 
						out[(i)][j-1] += '*'
						star +=1
					if i<(x-1) and con == out[(i+1)][j]:
						out[(i+1)][j] += '*'
						star +=1
					if j<(y-1) and con == out[(i)][j+1]:
						out[(i)][j+1] += '*'
						star +=1
					if star ==0:
						if final <= pedx:
							if final == pedx:
								finaltwo = final
								finalctwo = finalc
							final = pedx
							finalc = con
						pedx =0
						con ="S"


		if rezx == x*y:
			break
		else:
			wh +=1		
		sch +=1




	if (x*y) > 100:
		print ("1000 rows")
	else:
		print (x, y)
		for bn in bas: print(bn)


	print()
	print ("Отговор :")
	print (finalc)
	print (final)
	if final == finaltwo:
		print ("Отговор  2:")
		print (finalctwo)
		print (finaltwo)





ard = argv[1:]
nm = 0
if __name__ == '__main__':
	for number in ard:
		print(number)
		staat(number)
		print('\n')

