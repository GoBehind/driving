country = input('請問你是哪國人? ')
age = input('請輸入年齡 ')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('可以考駕照')
	else:
		print('還不能考駕照，嫩')
elif country == '美國':
	if age >= 16:
		print('可以考駕照')
	else:
		print('還不能考駕照，嫩')
else:
	print('請輸入台灣或美國')
	