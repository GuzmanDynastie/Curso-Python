edadAdulto = 18
edadPersona = int(input('Poporciona tu edad: '))

if edadPersona >= edadAdulto:
    print(f'La persona con edad {edadPersona} es un adulto')
else:
    print(f'La persona con la edad {edadPersona} es menor de edad')