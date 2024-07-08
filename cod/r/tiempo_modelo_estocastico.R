# Se prueba el modelo para los hombres, el caso para las mujeres es análogo.

ini <- Sys.time()
primas.estocasticash <-
  modelo.estocastico(matriz.probh, 0, lista.primash)
fin <- Sys.time()
print(((fin - ini) * 60) / length(primas.estocasticash))