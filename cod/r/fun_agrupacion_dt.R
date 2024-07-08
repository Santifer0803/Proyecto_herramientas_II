#' Función que convierte un DataFrame a un DataTable y realiza la imputación 
#' de los valores nulos en la columna "Salario base" usando la media de los 
#' valores presentes, agrupados por "Género" y "Grado de estudio".
#'
#' @param df DataFrame que contiene al menos las columnas "Género", "Grado de estudio" 
#' y "Salario base".
#'
#' @return DataTable con la misma estructura que el DataFrame original, pero con 
#' los valores nulos en "Salario base" imputados.
agrupacion.dt <- function(df) {
  base.dt <- setDT(df)
  
  # Se imputan los valores
  res.dt <-
    base.dt[, `Salario base` := ifelse(is.na(`Salario base`),
                                       mean(`Salario base`, na.rm = TRUE),
                                       `Salario base`), by = .(Género, `Grado de estudio`)]
}
