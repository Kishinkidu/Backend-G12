#Lista (array)
notas = [10,25,50,80]
variada = [10,'Juana', 70,3, True, [1,2,3]]
print (notas[0])

#si queremos agregar una nueva position no se le coloca como una asignacion
#notas[4] = 40

#se utiliza el metodo append para agregar al final del array
#en javascript es push, python es append
notas.append(40)

del notas[1]
#pop quita de la lista, pero te devuelve el contenido
notas.pop(1)
notas_eliminadas =notas.pop(1)
print (notas)
print (notas_eliminadas)
#le pasamos el contenido que queremos eliminar, si existe lo eliminara, caso contrario lanzara error

notas.remove(40)

#tupla
alumnos = ('eduardo','roberto','juana','roxana')
#la diferencia es que la tupla no se puede modificar , es inmutable
#la tupla se usa para definir valores que nunca se modificaran en todo el ciclo de nuestro proyecto
#print(alumnos(0))
#alumnos='pepito'

#set (conjunto)
#es desordenada , almacena la informacion de manera desordenada y sin respetar indice
mascotas={'fido', 'iguana','gato'}
print(mascotas)
print(len(mascotas))
mascotas.add('mocha')
mascota_eliminada = mascotas.pop()
print(mascota_eliminada)

#diccionario
#es ordenada pero por llaves (no por posiciones)
persona = {
    'nombre':'Erick',
    'apellido':'Revoredo',
    'sexo':'Masculino',
    'hobbies':['jugar futbol', 'montar bici']
}
print(persona['nombre'])
print(persona.get('nacionalidad','NO EXISTE!!'))
print(persona.get('hobbies','NO EXISTE!!'))