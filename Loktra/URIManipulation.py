import re
class URIManipulation:
	def getSchema(self,str):
		mat=re.search(r'\w+://',str)
		if mat:
			y=mat.end()-3
			return str[0:y]
		else:
			return ''

	def getDomain(self,str):
		mat=re.search(r'://.+/',str)
		if mat:
			if re.search(r'\.',mat.group(0)):
				x=mat.start()+3
				y=mat.end()-1
				return str[x:y]
			else:
				return ''
		else :
			mat=re.search(r'.+/',str1)
			if mat:
				y=mat.end()-1
				return str[0:y]
			else:
				if re.search(r'\.',str):
					return str;
				else:
					return ''

	def getPath(self,str):
		x=str.find('://')
		if x!=-1:
			str=str[x+4:]
		y=str.find('/')
		z=str.find('?')
		if y==-1 and z==-1:
			return ''
		else:
			if z==-1:
				return str[y:]
			else:
				return str[y:z]

	def getQuery(self,str):
		x=str.find('?')
		if x==-1:
			return ''
		else:
			y=str.find('&')
			list=[]
			if y==-1:
				return str[x+1:]
	   		else:
	   			while y!=-1:
	   				list.append(str[x+1:y])
	   				x=y
	   				z=str[y+1:].find('&')
	   				if z!=-1:
	   					y=y+z+1
	   				else:
	   					list.append(str[y+1:])
	   					y=-1
	   			return list

	def addPath(self,str, list):
		x = str.find('?')
		if x==-1:
			for i in list:
 				str=str+'/'+i
 			return str
 		else:
 			y=''
 			for i in list:
 				y=y+'/'+i
 			return str[0:x]+y+str[x:]

 	def addQuerry(self,str,dict):
		x= '&'.join(["%s=%s" % (key, value) for (key, value) in dict.items()])
		y=str.find('?')
		if y==-1:
			str=str+'?'+x
		else:
			str=str+'&'+x
		return str

	

	




manipulate = URIManipulation()
str1 = "https://facebook.com/search?q=question"
list=['shrey','chauhan']
dict = {'Name': 'Zara', 'Age': 7,'Dept':'CSE'}
print manipulate.getSchema(str1)
print manipulate.getQuery(str1)
print manipulate.getPath(str1)
print manipulate.getDomain(str1)
print manipulate.addQuerry(str1,dict)
str1= manipulate.addQuerry(str1,dict)
print manipulate.addPath(str1,list)
