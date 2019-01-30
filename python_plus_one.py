import re

def find_number(text):	
	pattern = '\d+'	
	m = re.search(pattern, text)
	print(m.group(0))
	
	
class Counter:
	def __init__(self,i):
		self.i = i	
	
def lab(m,i):	
	q=i.i
	i.i=i.i+1	
	if q == 0:
		print("Нашли")
		return '{}'.format(int(m.group()))
	else:
		return '{}'.format(int(m.group())+1)
	
	
		
def find_number3(text):	
	pattern = '[0-9]+'	
	match = re.search(pattern, text)	
	if match:
		line = text
		counter = Counter(0)		
		line = re.sub('\d+',lambda m: lab(m,counter),line)		
		print(line)			
	
  
def find_number2(text):	
	pattern = '[0-9]+'	
	match = re.search(pattern, text)	
	if match:
		line = text
		line = re.sub('\d+',lambda m: '{}'.format(int(m.group())+1),line)		
		return line
		#print(line)	
    



  
with open("script.sql", "r",encoding="utf-8") as ins:
	with open("out.sql","w",encoding="utf-8") as out:
		for line in ins:
			if "insert into" in line:
				line_out=find_number2(line)
			else:
				line_out=line
			out.write(line_out)
		
        