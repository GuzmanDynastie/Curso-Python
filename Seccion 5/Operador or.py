vacaciones = False
diaDescanso = False


# Utilizando operador or
if vacaciones or diaDescanso:
    print('Puede asistir al juego')
else:
    print('Tiene deberes por hacer')


# Utilizando el operador not
if not (vacaciones or diaDescanso):
    print('Tiene deberes por hacer')
else:
    print('Puede asistir al juego')