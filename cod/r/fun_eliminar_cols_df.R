#' Función que elimina las columnas de un DataFrame en las cuales el porcentaje
#' de valores nulos supera un porcentaje especificado por el usuario.
#'
#' @param df DataFrame del que se quiere eliminar las columnas.
#' @param porcentaje Número entre 0 y 1 que indica el porcentaje máximo
#'                   de valores nulos permitido en una columna. Las columnas con
#'                   un porcentaje de valores nulos mayor que este valor serán eliminadas.
#'
#' @return DataFrame con las columnas que no superan el porcentaje especificado
#'         de valores nulos.
eliminar.columnas.df <- function(df, porcentaje) {
  filas <- nrow(df)
  i <- 1
  
  while (i <= length(df)) {
    cantidad_na <- sum(is.na(df[[i]]))
    
    if ((cantidad_na / filas) > porcentaje) {
      df <- subset(df, select = -i)
    } # fin if
    
    i <- i + 1
  } # fin while i
  return(df)
}
