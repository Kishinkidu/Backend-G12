nombre = "roxana"
apellido = "rodrigez"
if nombre=="roxana" and apellido=="rodrigez":
    print("Hola roxana, como estan los cuyes!")
else :
    print("Hola roxana como estas?")

nombre_completo = nombre + " "+ apellido
print(nombre_completo)
#Recibir informacion por el teclado de la terminal
ingreso = input()
print(ingreso)
#si hoy es sabado indicar si quie es fin de semana, si no que ese dia se trabaja

dia=input("ingrese dia de la semana")
dia= dia.upper()
if dia == "SABADO" :
 print("es fin de semana")
elif dia =="DOMINGO":
   print("tienes que lavar la ropa")
else :
 print("ese dia se trabaja")

