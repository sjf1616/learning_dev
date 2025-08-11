import math

angulo = float(input('Digite um angulo: '))

print(f'''
O seno é {math.sin(math.radians(math.floor(angulo))):.2f}
O coseno é {math.cos(math.radians(math.floor(angulo))):.2f}
A tangente é {math.tan(math.radians(math.floor(angulo))):.2f}''')