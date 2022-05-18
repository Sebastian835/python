#Ingresar un valor en libras y transformarlo a kilos y gramos

libras = float(input("Ingresar un valor en libras: "))      #ingreso de dato

kilogramo = round(libras*(1/2.2046),2)              #operacion aritmetica (de lb a kg)
gramos = round(libras*(453.59/1),2)                  #operacion aritmetica (de lb a g)
print("En ",libras,"lb, hay ",kilogramo,"kg")           #mostrar conversion (resultado) al usuario
print("En ",libras,"lb, hay ",gramos,"g")



