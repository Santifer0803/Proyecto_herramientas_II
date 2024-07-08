#' Función que crea una matriz cuadrada de las dimensiones especificadas
#'
#'
#' @param dimensiones (Integer) Dimensiones de la matriz. Por defecto se
#' usan 10000 filas y columnas.
#'
#' @return NuLL
#'
creacion.matriz <- function(dimensiones = 10000) {
  # Se crea la matriz con las dimensiones deseadas
  return(matrix(runif(dimensiones ^ 2), dimensiones, dimensiones))
}
