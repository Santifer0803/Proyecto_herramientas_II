# Se inicia con la descarga de los datos para el modelo estocástico
# Para la base de datos de los empleados se agregaron columnas con la edad y el 
# año de nacimiento. Para los valores tqx se realizó una tabla dinámica separada 
# por cada sexo, todos los cambios fueron hechos desde MS Excel.
qx.hombres <- read_excel("data/Mortalidad_supen.xlsx", sheet = "Sexo_1_limpio")
