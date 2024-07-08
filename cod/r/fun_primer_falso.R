# Se crea una función para cambiar los valores después del primer falso a falso, 
# de una fila dada de una matriz

#' Función que recibe un vector booleano (por ejemplo, una fila de una matriz), 
#' y cambia todos los elementos después del primer FALSE a FALSE.
#'
#' @param fila Vector booleano.
#' 
#' @return Vector booleano modificado.
fila.muerte <- function(fila){
  fila[(which(!fila)[1] + 1):length(fila)] <- FALSE
  return(fila)
}
