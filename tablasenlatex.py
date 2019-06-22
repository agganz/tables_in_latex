# programa pensado para automatizar las tablas en LaTeX a partir de un fichero .txt con los datos
# el programa exige el paquete float. Geometry no hace daño tampoco. 
import time # importar paquete time para parar programa
import csv # importa paquete csv
import os # importa OS, para eliminar el fichero file.txt temporal
import sys # por si acaso...

with open ("datos.txt") as f:
    reader = csv.reader(f, delimiter=' ', skipinitialspace=False)
    first_row = next(reader)
    num_cols = len(first_row)

print ("datos.txt tiene",num_cols,"columnas") # comprobante para el número de columnas
time.sleep(0.4)

# Abre el archivo para formato lectura
with open('datos.txt', 'r') as file :
  filedata = file.read()

# Crea un archivo extra que se eliminará al final
filedata = filedata.replace(' ', ' & ')
with open('file.txt', 'w') as file:
  file.write(filedata)

lineas=0 # se inicia la variable lineas para contar las lineas de datos
# bucle que cuenta las lineas en datos.txt
with open("datos.txt") as l:
    for line in l:
        lineas = lineas + 1
# se crea tabla.txt con los preámbulos
tabla = open("tabla.txt","w") # crea el fichero donde se almacena la tabla

tabla.write("\\begin{table}[H]\n") # \n produce el salto de línea
tabla.write("   \\begin{center}\n")
tabla.write("      \\renewcommand{\\tablename}{\\scriptsize Tabla}\n")

# NOTA: para escribir "\" es imprescindible usar "\\".
print("datos.txt tiene",lineas,"líneas.")
tipo = int(input("1 para alineado izda, 2 para alineado central, 3 para alineado dcha: "))
formtabla = "{"
cuenta = 0 # inicia la variable cuenta para el bucle en cero

while (cuenta < num_cols):
    if (tipo==1):
        formtabla=formtabla+"l "
    elif (tipo==2):
        formtabla=formtabla+"c "
    elif (tipo==3):
        formtabla=formtabla+"r "
    elif (tipo!=1 & tipo!=2 & tipo!=3):
        print("Comando no válido")
        break
    cuenta=cuenta+1

formtabla=formtabla[:-1]
formtabla=formtabla + "}"
print(cuenta, "control de la cuenta en el bucle")
print(formtabla)

tabla.write("      \\begin{tabular}")
tabla.write(formtabla)
tabla.write("\n      \\hline\n")

cuentas=0 # inicio de la variable cuentas
caption=str(input("Insertar el string con el pie de tabla: "))
label=str(input("Escribir el nombre de la etiqueta (tabla: ya incluído): "))

with open("file.txt") as f:
    for line in f:
        tabla.write(line)
        tabla.write("\\\\ \n")

# se ha creado el contenido básico de la tabla
tabla.write("\n     \hline")
tabla.write("\n      \end{tabular}")
tabla.write("\n      \\caption{\\scriptsize ") # caption, por defecto en scriptsize
tabla.write(caption)
tabla.write("}")
tabla.write("\n   \\label{tabla:") # etiqueta
tabla.write(label)
tabla.write("}")
tabla.write("\n   \\end{center}")
tabla.write("\n\\end{table}")
os.remove("file.txt") # borra el fichero temporal auxiliar file.txt
tabla.close()
os.startfile("tabla.txt") # abre el fichero con la tabla
input() # enter cierra el programa