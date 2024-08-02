#declarar una lista unidimensional de frutas
frutas = ["Pera" , "Manzana" , "Piña" , "Fresa"]

print(frutas)

#permite agregar alementos .append
frutas.append("Melón")
print(frutas)

#acceder a elemento de la lista (arreglo unidimesional)
print(frutas[4])

frutas[4] = "Arandano"
print(frutas[4])

#Ejercicio de Oredenamiento

digigitos =[5,2,1,0,3,6,7,8,9]
print(digigitos)

digigitos.sort()
print(digigitos)

digigitosCero = 5*[0]
print(digigitosCero)

#Ejercicio de tamaño de la lista

print(frutas)
print("cantidad de frutas infresadas: ", len(frutas))