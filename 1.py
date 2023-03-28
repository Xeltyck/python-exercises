from tkinter import INSERT


List = []
for X in range(2000,3201):
    
    if (X%7==0) and (X%5 != 0):

        List.append(str(X))

print(List) # Lista impresa en donde cada valor es un string.
print(",".join(List)) #Imprime un string que separa los strings de la lista por coma. Para poder usar eso, los valores deben ser strings. No aplica con valores int. 
# Por esa razón, primero hay que convertir los valores de X a Strings. 