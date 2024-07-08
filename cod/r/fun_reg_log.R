# Se crea la función del modelo de regresión logística, en la cual se genera el 
# nivel predictivo del mismo, se optimizan los parámetros y se devuelven los 
# ajustes de entrenamiento y testeo para los datos.

#' Función que realiza la optimización de parámetros para la regresión logística
#' utilizando los datos de entrenamiento proporcionados. Luego, realiza
#' predicciones sobre los datos de testeo y calcula la precisión del modelo
#' tanto en entrenamiento como en testeo.
#'
#' @param X.train (Matrix) Matriz de características de entrenamiento.
#' @param y.train (Vector) Vector de etiquetas de entrenamiento.
#' @param X.val (Matrix) Matriz de características de testeo.
#' @param y.val (Vector) Vector de etiquetas de testeo.
#' @param num.iterations (Integer) Número de iteraciones para la optimización. Por defecto es 2000.
#' @param learning.rate (Numeric) Tasa de aprendizaje para la optimización. Por defecto es 0.5.
#'
#' @return Lista con dos elementos:
#'   \itemize{
#'     \item Ajuste de precisión en entrenamiento.
#'     \item Ajuste de precisión en testeo.
#'   }
regresion.logistica <- function(X.train,
                                y.train,
                                X.val,
                                y.val,
                                num.iterations = 2000,
                                learning.rate = 0.5) {
  # Se optimizan los parámetros
  params <-
    optimizacion(
      W = rep(0, ncol(X)),
      b = 0,
      X = X.train,
      y = y.train,
      num.iterations = num.iterations,
      learning.rate = learning.rate
    )
  
  # Predicciones de entrenamiento y validación
  y.prediction.validation <-
    as.numeric(((1 / (1 + exp(
      -((t(params[[1]]) %*% t(X.val)) + params[[2]])
    )))) > 0.5)
  y.prediction.train <-
    as.numeric(((1 / (1 + exp(
      -((t(params[[1]]) %*% t(X.train)) + params[[2]])
    )))) > 0.5)
  
  # Lista para medir los ajustes de entrenamiento y validacion
  lista.res <- list()
  lista.res[[1]] <-
    (100 - (mean(abs(
      y.prediction.train - y.train
    )) * 100))
  lista.res[[2]] <-
    (100 - (mean(abs(
      y.prediction.validation - y.val
    )) * 100))
  
  # Se devuelven los ajustes
  return(lista.res)
}
