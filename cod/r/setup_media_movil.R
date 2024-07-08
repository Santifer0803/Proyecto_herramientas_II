# Se descarga la base para reemplazar la media móvil en una de sus columnas.
base.salarios <- read_excel("data/Base_salarios.xlsx")

# Se convierte a data.table
base.salarios <- setDT(base.salarios)

# Se hace una copia de la columna a copiar
copia.col <- base.salarios$`Salario base`
