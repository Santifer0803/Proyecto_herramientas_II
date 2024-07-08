#' Función que extrae un archivo de excel
#'
#' @param ruta (Character) Ruta al archivo de excel correspondiente
#'
#' @return NuLL
#'
leer.excel <- function(ruta) {
  return(read_excel(ruta))
}
