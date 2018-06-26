#pip install jieba
import csv
import jieba
import jieba.analyse
#Q 問題
#A 答案
Q=[]
A=[]



with open('QA.csv', newline='\n') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows:
		
		Q.append(row[0])
		A.append(row[1])
		
		#
		
	#
#
matrix=[]
#Q.txt


for q in Q:
	row=[]
	content = q
	words = jieba.cut(content, cut_all=False)
	
	for word in words:
		row.append(word)
		row.append(' ')
	
	row.append('\n')
	matrix.append(row)
print(set(row))


	
	
	#
	 

fp = open("Q.txt", "w")

for row in row:
	fp.writelines(row)
	fp.writelines('\n')

fp.close()


matrix=[]
#A.txt
for a in A:
	
	content = a
	row=[]
	words = jieba.cut(content, cut_all=False)
	 
	for word in words:
		row.append(word)
		row.append(' ')
	
	row.append('\n')
	matrix.append(row)
	
	
	#
	 

fp = open("A.txt", "w")

for row in matrix:
	fp.writelines(row)


fp.close()

		





