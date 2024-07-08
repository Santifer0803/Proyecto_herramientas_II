# Se realiza la función que se encarga de las demás iteraciones del modelo estocástico.

#' Función que implementa un modelo estocástico iterativo para calcular las primas.
#' La función realiza iteraciones mientras la diferencia absoluta entre el promedio 
#' de primas y la media de las primas en la lista sea mayor que 0.001.
#'
#' @param matriz.prob Matriz de probabilidades de sobrevivencia.
#' @param prom.primas Promedio de las primas calculadas.
#' @param lista.primas Lista con las primas calculadas en la primera iteración.
#'
#' @return Lista con las primas calculadas en cada iteración.
#'
modelo.estocastico <-
  function(matriz.prob, prom.primas, lista.primas) {
    while (abs(prom.primas - mean(unlist(lista.primas))) > 0.001) {
      # Creamos la matriz de números aleatorios
      matriz.rnd <-
        matrix(
          data = pnorm(
            rnorm(colmat * filmat, mean = 0, sd = 1),
            mean = 0,
            sd = 1
          ),
          nrow = filmat,
          ncol = colmat
        )
      
      # Comparación de matrices
      matriz.rnd <- matriz.rnd < matriz.prob
      
      # Se agregan los falsos después del primer falso de la matriz
      matriz.rnd <- t(apply(matriz.rnd, 1, fila.muerte))
      
      # Índice del primer falso
      id <- sapply(1:filmat, function(m)
        which(!matriz.rnd[m,])[1])
      
      # Anualidad
      an <-
        sapply(1:filmat, function(n)
          sum((1 + j) ^ -(0:(min(
            id[n], (65 - 19 - n)
          ) - 1))))
      
      # Rango de años de cada persona desde que llega a 65 años hasta que fallece
      annos.65 <- sapply(20:64, function(o)
        c((65 - o):(id[[o - 19]])))
      
      # Beneficios para trabajadores y pensionados
      ben <-
        sapply(1:length(annos.65), function(p)
          (ifelse(
            id + c(20:64) < 65,
            5000000 * ((1 + j) ^ -(id)),
            sum(300000 * 13 * (1 + j) ^ -annos.65[[p]]) + 1000000 * ((1 + j) ^ -(id))
          ))[p])
      
      # Actualizamos el promedio correspondiente
      prom.primas <- mean(unlist(lista.primas))
      
      # Primas
      lista.primas <- append(lista.primas, list(ben / an))
      
    }
    
    # Se devuelven las primas de cada iteración
    return(lista.primas)
  }
