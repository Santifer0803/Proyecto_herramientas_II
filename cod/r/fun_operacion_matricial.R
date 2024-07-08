#' Función que eleva cada elemento de una matriz a la potencia 100, multiplica cada
#' elemento resultante por 10 y luego a cada uno le suma 5.
#'
#' @param matriz Matriz numérica.
#' @return Matriz con los mismos dimensiones que la dada, donde cada elemento ha
#' sido transformado según la operación mencionada.
operacion.matricial <- function(matriz) {
  return(((matriz ^ 100) * 10) + 5)
}
