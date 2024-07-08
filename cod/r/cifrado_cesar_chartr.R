#' Función que cifra un texto dado utilizando la función chartr de R,
#' aplicando un desplazamiento específico en el alfabeto.
#'
#' @param texto (Character) Texto que se desea cifrar.
#' @param desplazamiento (Integer) Número entero que indica el desplazamiento en el alfabeto.
#'
#' @return Texto cifrado utilizando el método chartr.
cifrado.chartr <- function(texto, desplazamiento) {
  # Definir el alfabeto
  alfabeto_minusculas <- "abcdefghijklmnopqrstuvwxyz"
  alfabeto_mayusculas <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  
  # Crear el alfabeto desplazado
  alfabeto_minusculas_desplazado <- paste0(
    substr(
      alfabeto_minusculas,
      desplazamiento + 1,
      nchar(alfabeto_minusculas)
    ),
    substr(alfabeto_minusculas, 1, desplazamiento)
  )
  
  alfabeto_mayusculas_desplazado <- paste0(
    substr(
      alfabeto_mayusculas,
      desplazamiento + 1,
      nchar(alfabeto_mayusculas)
    ),
    substr(alfabeto_mayusculas, 1, desplazamiento)
  )
  
  # cambiar las letras
  texto.cifrado <- chartr(
    paste0(alfabeto_minusculas, alfabeto_mayusculas),
    paste0(
      alfabeto_minusculas_desplazado,
      alfabeto_mayusculas_desplazado
    ),
    texto
  )
  
  return(texto.cifrado)
}

