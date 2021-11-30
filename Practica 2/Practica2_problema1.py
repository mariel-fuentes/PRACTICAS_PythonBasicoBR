nombre = ""
sexo = ""
print("ingrese su nombre")
nombre = input()
print("Ingrese su Sexo")
sexo = input()
letra = nombre[0]

LetrasF = ["A","B","C","D","E","F","G","H","I","J","K","L"]
LetrasM = ["O","P","Q","R","S","T","U","V","W","X","Y","Z"]
if sexo == "Mujer":
    for index in LetrasF:
        if letra == index:
            grupo = "Grupo A"
            break
        else:
            grupo = "GRUPO B"
elif sexo == "Hombre":
    for index in LetrasM:
        if letra == index:
            grupo = "Grupo A"
            break
        else:
            grupo = "GRUPO B"

print(nombre, ", sexo: ", sexo, "==>", grupo)