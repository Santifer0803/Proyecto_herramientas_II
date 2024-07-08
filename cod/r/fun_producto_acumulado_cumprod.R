#' Función que calcula el producto acumulado de un vector dado usando la función
#' cumprod de R.
#'
#' @param vector (Vector) Vector numérico.
#'
#' @return Vector con el producto acumulado de los elementos del vector dado.
prod.acum.cumprod <- function(vector) {
  return(cumprod(vector))
}

