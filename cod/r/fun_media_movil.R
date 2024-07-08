#' Función que imputa los valores nulos de una columna de un DataFrame o un vector
#' usando la media móvil.
#'
#' @param col.nulos Vector o columna de un DataFrame que contiene los valores nulos
#' a imputar.
#' @param banda Número entero que representa el número de elementos adyacentes a
#' considerar para calcular la media móvil.
#'
#' @return Vector o columna del DataFrame con los valores nulos imputados usando la media móvil.
media.movil <- function(col.nulos, banda) {
  # Se obtinenen los índices de los valores nulos y la cantidad de filas
  indices.nulos <- which(is.na(base.salarios$`Salario base`))
  filas <- length(col.nulos)
  
  # Iteramos a través de los nulos
  for (i in indices.nulos) {
    # Se obtiene el vector alrededor del valor a imputar
    vec.num <-
      c(col.nulos[max(1, (i - banda)):(i - 1)], (i + 1):min(filas, (i + banda)))
    
    # Se sustituye el valor por el promedio del vector anterior, ignorando los nulos
    col.nulos[i] <- mean(vec.num, na.rm = TRUE)
  }
  return(col.nulos)
}
