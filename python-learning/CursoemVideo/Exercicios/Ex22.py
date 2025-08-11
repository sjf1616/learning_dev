name = str(input('Digite seu nome completo: ')).strip()
first_name = name.split()

print(f'''
O nome completo maiúsculo é : {name.upper()}
O nome completo minúsculo é : {name.lower()}
O nome possui {len(name)-name.count(' ')} letras
O primeiro nome possui {len(first_name[0])} letras''')