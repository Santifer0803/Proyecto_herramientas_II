#' Función que extrae un archivo de texto
#'
#'
#' @param ruta (Character) Ruta al archivo csv correspondiente
#'
#' @return NuLL
#'
leer.csv <- function(ruta) {
  return(read_csv(ruta))
}
