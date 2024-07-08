#' Función que agrupa un DataFrame por "Género" y "Grado de estudio" y, 
#' dentro de cada grupo, reemplaza los valores NA en la columna "Salario base" con 
#' la media de "Salario base" de ese grupo.
#'
#' @param df DataFrame que contiene las columnas "Género", "Grado de estudio" y 
#' "Salario base".
#' 
#' @return DataFrame con los valores NA en "Salario base" reemplazados por la media 
#' de "Salario base" dentro de cada grupo.
agrupacion.df <- function(df) {
  res.dp <- df %>%
    group_by(Género, `Grado de estudio`) %>%
    mutate(`Salario base` = ifelse(
      is.na(`Salario base`),
      mean(`Salario base`, na.rm = TRUE),
      `Salario base`
    ))
}
