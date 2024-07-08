#' Función que determina si una columna es categórica.
#'
#' @param x Vector o columna del dataframe a evaluar.
#'
#' @return \code{TRUE} si la columna es de tipo \code{character} o \code{factor},
#' \code{FALSE} en caso contrario.
indices.categoricos <- function(x)
  is.character(x) || is.factor(x)

# Guardamos los índices correspondientes
categoricos <- which(sapply(muertes.df, indices.categoricos))
numericos <- which(!sapply(muertes.df, indices.categoricos))

# Cargamos el plan para paralelizar
plan(multisession)
