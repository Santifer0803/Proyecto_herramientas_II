#' Función que extrae un archivo de texto
#'
#'
#' @param ruta (Character) Ruta al archivo de texto correspondiente
#'
#' @return NuLL
#'
leer.txt <- function(ruta) {
  return(read_file(ruta))
}
