fname="Kamesh"
lname="Sankar"
age=22
height=182
fullname=fname + " "+lname #concatenation
demarker="*-* "
isMarried=True
print(fullname,"age is ",age,"height is ",height)
print(demarker*30)
print("first 3 character from the fullname",fullname[:3])
print("String after 3rd position is ",fullname[3:])
print("String between 3rd pos to 6th pos",fullname[3:7])
print("whole string except last 2 characters: ",fullname[:-2])
print("string in last 2 characters: ",fullname[-2:])
print("reversing the string",fullname[::-1])
print("character at last 4th position",fullname[-4])
print("replace kamesh with msdhoni",fullname.replace("Kamesh","MsDhoni"))
print(fullname)
print(fullname.count("a"))
print(fullname.find("h"))
print(fullname.split(" "))
email="ilearniexcel@gmail.com"
print("psoition of @",email.find("@"))
print("extract only .com from the string",email[email.find(".com"):])
print("Extracted gmail:", email[email.find("@") + 1:email.find(".com")])

