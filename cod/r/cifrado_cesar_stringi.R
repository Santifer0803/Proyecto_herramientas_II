#' Función que cifra un texto desplazando cada letra según un número dado.
#' Funciona tanto para letras minúsculas como mayúsculas manteniendo la
#' estructura y el caso original del texto.
#'
#' @param texto (Character) Texto que se desea cifrar.
#' @param desplazamiento (Integer) Número entero que indica cuántas posiciones desplazar
#' cada letra. Puede ser positivo (desplazamiento a la derecha) o negativo
#' (desplazamiento a la izquierda).
#'
#' @return Texto cifrado según el desplazamiento especificado.
cifrado.stringi <- function(texto, desplazamiento) {
  # Función para desplazar letras
  desplazar <- function(letra, desplazamiento) {
    if (stri_detect_regex(letra, "[a-z]")) {
      return(stri_sub(
        "abcdefghijklmnopqrstuvwxyz",
        #usar modulo 26
        (
          stri_locate_all_fixed("abcdefghijklmnopqrstuvwxyz", letra)[[1]][1, 1] +
            desplazamiento - 1
        ) %% 26 + 1,
        (
          stri_locate_all_fixed("abcdefghijklmnopqrstuvwxyz", letra)[[1]][1, 1] +
            desplazamiento - 1
        ) %% 26 + 1
      ))
    } else if (stri_detect_regex(letra, "[A-Z]")) {
      return(stri_sub(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        (
          stri_locate_all_fixed("ABCDEFGHIJKLMNOPQRSTUVWXYZ", letra)[[1]][1, 1] +
            desplazamiento - 1
        ) %% 26 + 1,
        (
          stri_locate_all_fixed("ABCDEFGHIJKLMNOPQRSTUVWXYZ", letra)[[1]][1, 1] +
            desplazamiento - 1
        ) %% 26 + 1
      ))
    } else {
      return(letra)
    }
  }
  
  # Desplazar cada letra del texto y unirlas
  texto.cifrado <- stri_join(
    sapply(
      stri_split_boundaries(texto, type = "character")[[1]],
      desplazar,
      desplazamiento = desplazamiento
    ),
    collapse = ""
  )
  
  return(texto.cifrado)
}

