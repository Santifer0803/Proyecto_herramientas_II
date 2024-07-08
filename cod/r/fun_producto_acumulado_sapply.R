#' Función que calcula el producto acumulado de un vector dado usando sapply.
#'
#' @param vector (Vector) Vector numérico.
#'
#' @return Vector con el producto acumulado de los elementos del vector dado.
prod.acum.sapply <- function(vector) {
  return(sapply(1:length(vector), function(i)
    prod(vector[1:i])))
}
