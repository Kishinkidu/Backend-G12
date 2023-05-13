# #se ingresa
# edad=input("coloca tu edad")

# edad_numerica= int(edad)


# if edad_numerica >65:
#         print("no puede ingresar por que ya es adulta")
# elif edad_numerica > 17 and edad_numerica < 65:
#     print("Puede ingresar a la discoteca")
#     if edad_numerica >=40 and edad_numerica <= 60:
#      print("te ofrecemos un trago de cortesia ")
    
# else:
#     print("no puedes, llamaremos a tus padres")

numeros = [1,10,40,50,55,3,4,9]
mayor_que_15=0
menor_que_15 = 0
for  numero in numeros:
    if numero > 15:
        mayor_que_15 += 1
    else:
        menor_que_15 += 1
print("hay {} mayor que 15".format(mayor_que_15))
print(f"hay{menor_que_15} menor que 15")