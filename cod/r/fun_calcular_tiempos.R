#' Función que mide el tiempo de ejecución 10 veces e imprime un resumen de los
#' mismos.
#'
#' @param funcion (any) Función a la que se tomará el tiempo.
#' @param unidad (character) Unidad de tiempo, en inglés, en la que saldrán los
#' resultados. Por defecto se utilizan segundos.
#'
#' @return NuLL
#'
calcular.tiempos <- function(funcion, unidad = "seconds") {
  fun <- function() {
    funcion()
  }
  
  resultado <- microbenchmark(fun(), times = 10, unit = unidad)
  return(resultado)
}
