def notes(n):
    if not n:
        return {'ERROR':"Nenhuma nota informada"}

    classA = {
    'total_notas' : len(n),
    'maior_nota' : max(n),
    'menor_nota': min(n),
    'soma_notas': sum(n),
    'media_notas': sum(n) / len(n)
    }

    for k, v in classA.items():
        print(f'{k} = {v}')
        
classB = []
while True:
    student_note = float(input('Note Student: '))
    classB.append(student_note)
    c = str(input('Would do you like to continue?[Y/N]: ')).lower().strip()
    if c.startswith('n'):
        break
notes(classB)