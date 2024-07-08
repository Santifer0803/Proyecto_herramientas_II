#' Función que elimina las columnas de un DataFrame que tienen un porcentaje
#' de valores nulos superior a un porcentaje especificado. Para esto, se convierte
#' el DataFrame dado a un DataTable.
#'
#' @param df DataFrame del cual se eliminarán las columnas.
#' @param porcentaje Porcentaje límite de valores nulos para determinar si una
#' columna se elimina. Debe ser un valor entre 0 y 1.
#'
#' @return DataTable que corresponde al DataFrame original con las columnas eliminadas
eliminar.columnas.dt <- function(df, porcentaje) {
  # Se convierte el DataFrame a DataTable
  base.dt <- setDT(df)
  
  # Número de filas del DataTable
  filas <- base.dt[, .N]
  
  # Vector para almacenar las columnas a eliminar
  columnas_eliminar <- c()
  
  # Se itera sobre las columnas
  for (columna in names(base.dt)) {
    cantidad_na <- sum(is.na(base.dt[[columna]]))
    
    if ((cantidad_na / filas) > porcentaje) {
      columnas_eliminar <- c(columnas_eliminar, columna)
    }
  }
  
  # Se eliminan las columnas
  if (length(columnas_eliminar) > 0) {
    base.dt[, (columnas_eliminar) := NULL]
  }
  
  return(base.dt)
}
