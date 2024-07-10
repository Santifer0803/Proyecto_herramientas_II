#' Función que crea un DataFrame con los tiempos de ejecucion de los 4
#' integrantes del grupo de trabajo.
#' 
#' @param primeros.tiempos (Vector) Vector con los tiempos de ejecución de un
#' ejercicio de Python
#' @param segundos.tiempos (Vector) Vector con los tiempos de ejecución de un
#' ejercicio de R.
#' @param integrantes (Vector) Vector con los nombres de personas para poner en
#' el DataFrame. Por defecto los integrantes del grupo.
#' 
#' @return df.resultante (DataFrame) DataFrame con los nombres y tiempos de
#' ejecución de los integrantes del grupo en ambas plataformas.
#' 
df.tiempos.lenguajes <-
  function(primeros.tiempos,
           segundos.tiempos,
           integrantes = c("Santiago", "Eyeri", "Paula", "Alejandro")) {
    return(
      data.frame(
        integrante = integrantes,
        Python = primeros.tiempos,
        R = segundos.tiempos
      )
    )
  }