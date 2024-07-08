#' Función que crea un gráfico de barras interactivo con el color y título
#' deseados, recibe un DataFrame de la función df.tiempos.
#'
#' @param df (DataFrame) DataFrame de la función df.tiempos.imputacion.
#' @param titulo (Character) Título del gráfico.
#' @param color (Character) Color que tendrán las barras del gráfico.
#'
#' @return None
#'
graficos.dobles.imputacion <- function(df, titulo, colores) {
  # Convertir el formato de ancho a largo
  df.largo <-
    gather(df, key = "condicion", value = "tiempo", -integrante)
  
  # Se diferencian las barras
  df.largo$condicion <-
    factor(
      df.largo$condicion,
      levels = c("con.datatable", "con.dplyr"),
      labels = c("Datatable", "Dplyr")
    )
  
  fig <-
    ggplot(df.largo, aes(x = integrante, y = tiempo, fill = condicion)) +
    geom_col(position = "dodge") +
    labs(
      x = "Integrante",
      y = "Tiempo (segundos)",
      title = titulo,
      caption = "Fuente: elaboración propia"
    ) +
    scale_fill_manual(values = colores) +
    theme_minimal() +
    theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
    guides(fill = guide_legend(title = "Condición"))
  
  ggplotly(fig, width = 800, height = 500)
}
