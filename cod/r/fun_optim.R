# Se crea la función de optimización para el ejercicio de regresión logística

#' Función que realiza la optimización de los pesos (\code{W}) y el sesgo (\code{b})
#' mediante el algoritmo de descenso del gradiente.
#'
#' @param W (Vector) Vector de pesos.
#' @param b (Numeric) Escalar que representa el sesgo.
#' @param X (Matrix) Matriz de características de entrada.
#' @param y (Vector) Vector de etiquetas objetivo.
#' @param num.iterations (Integer) Número de iteraciones para el descenso del gradiente.
#' @param learning.rate (Numeric) Tasa de aprendizaje para la actualización de los
#' parámetros.
#'
#' @return Lista con los pesos optimizados (\code{W}) y el sesgo optimizado (\code{b}).
optimizacion <- function(W, b, X, y, num.iterations, learning.rate) {
  for (i in 1:num.iterations) {
    # Variables a optimizar con el descenso del gradiente
    A <- (1 / (1 + exp(-((
      X %*% W
    ) + b))))
    dW <- (1 / nrow(X)) * (t(X) %*% (A - y))
    db <- (1 / nrow(X)) * sum(A - y)
    
    # Se actualiza el tensor de pesos y el término de sesgo
    W <- W - (learning.rate * dW)
    b <- b - (learning.rate * db)
  }
  
  return(list(W, b))
}
