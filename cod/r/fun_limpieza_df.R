#' Función que realiza la limpieza de una base de datos en concreto
#'
#' @param df (DataFrame) Base de datos de muertes en Costa Rica
#'
#' @return NuLL
#'
limpieza.df <- function(df) {
  # Se crea una copia para que haga el proceso correctamente en cada iteración
  muertes.df <- df
  
  # Se filtra por edades mayores o iguales a 15 y años mayores o iguales a 2014
  muertes.df <- muertes.df[muertes.df$edads >= 15, ]
  muertes.df <- muertes.df[muertes.df$anodef >= 2014, ]
  muertes.df <- muertes.df[muertes.df$anotrab >= 2014, ]
  muertes.df <- muertes.df[muertes.df$anodeclara >= 2014, ]
  
  # Correcciones ortográficas con chartr
  muertes.df$ocuparec <- chartr("Ã", "i", muertes.df$ocuparec)
  muertes.df$regsalud <- chartr("Ã", "i", muertes.df$regsalud)
  muertes.df$reginec <- chartr("Ã", "i", muertes.df$reginec)
  muertes.df$autopsia <- chartr("Ã", "i", muertes.df$autopsia)
  muertes.df$asistmed <- chartr("Ã", "i", muertes.df$asistmed)
  
  # Correcciones ortográficas con gsub
  muertes.df$estcivil <- gsub("Ã³", "o", muertes.df$estcivil)
  muertes.df$ocuparec <- gsub("Ã¡", "a", muertes.df$ocuparec)
  muertes.df$ocuparec <- gsub("Ã©", "e", muertes.df$ocuparec)
  muertes.df$regsalud <- gsub("i³", "o", muertes.df$regsalud)
  muertes.df$provincia <- gsub("Ã©", "e", muertes.df$provincia)
  muertes.df$provincia <- gsub("Ã³", "o", muertes.df$provincia)
  muertes.df$provocu <- gsub("Ã©", "e", muertes.df$provocu)
  muertes.df$provocu <- gsub("Ã³", "o", muertes.df$provocu)
  muertes.df$provregis <- gsub("Ã©", "e", muertes.df$provregis)
  muertes.df$provregis <- gsub("Ã³", "o", muertes.df$provregis)
  muertes.df$reginec <- gsub("i³", "o", muertes.df$reginec)
  muertes.df$edadsrec <-
    gsub("100 y mÃ¡s", "100 - 121", muertes.df$edadsrec)
  muertes.df$autopsia <- gsub("Ã©", "e", muertes.df$autopsia)
  muertes.df$asistmed <- gsub("Ã©", "e", muertes.df$asistmed)
  muertes.df$reginec <-
    gsub("Paci­fico", "Pacifico", muertes.df$reginec)
  muertes.df$regsalud <-
    gsub("Paci­fico", "Pacifico", muertes.df$regsalud)
  muertes.df$nacionalid <-
    gsub("^(?!Costa Rica$).*",
         "Extranjero",
         muertes.df$nacionalid,
         perl = TRUE)
  muertes.df$estcivil <-
    gsub("Ignorado", "Otros", muertes.df$estcivil)
  muertes.df$estcivil <-
    gsub("Union libre", "Otros", muertes.df$estcivil)
  muertes.df$estcivil <-
    gsub("Separado", "Otros", muertes.df$estcivil)
  muertes.df$estcivil <- gsub("Menor", "Otros", muertes.df$estcivil)
  muertes.df$ocuparec <-
    gsub(
      "Profesionales cienti­ficos e intelectuales",
      "Trabajadores activos",
      muertes.df$ocuparec
    )
  muertes.df$ocuparec <-
    gsub(
      "Agricultores y trabajadores calificados agropecuarios, forestales y pesqueros",
      "Trabajadores activos",
      muertes.df$ocuparec
    )
  muertes.df$ocuparec <-
    gsub("Ocupaciones elementales",
         "Trabajadores activos",
         muertes.df$ocuparec)
  muertes.df$ocuparec <-
    gsub(
      "Trabajadores de los servicios y vendedores de comercios y mercados",
      "Trabajadores activos",
      muertes.df$ocuparec
    )
  muertes.df$ocuparec <-
    gsub(
      "Operadores de instalaciones y maquinas y ensambladores",
      "Trabajadores activos",
      muertes.df$ocuparec
    )
  muertes.df$ocuparec <-
    gsub(
      "Tecnicos y profesionales de nivel medio",
      "Trabajadores activos",
      muertes.df$ocuparec
    )
  muertes.df$ocuparec <-
    gsub(
      "Oficiales, operarios y artesanos de artes mecanicas y de otros oficios",
      "Trabajadores activos",
      muertes.df$ocuparec
    )
  muertes.df$ocuparec <-
    gsub("Personal de apoyo administrativo",
         "Trabajadores activos",
         muertes.df$ocuparec)
  muertes.df$ocuparec <-
    gsub("Directores y gerentes",
         "Trabajadores activos",
         muertes.df$ocuparec)
  muertes.df$ocuparec <-
    gsub("Pensionado", "Otros", muertes.df$ocuparec)
  muertes.df$ocuparec <-
    gsub("Persona con discapacidad", "Otros", muertes.df$ocuparec)
  muertes.df$ocuparec <-
    gsub("Estudiante", "Otros", muertes.df$ocuparec)
  muertes.df$ocuparec <-
    gsub("Mal especificadas", "Otros", muertes.df$ocuparec)
  muertes.df$ocuparec <-
    gsub("Privado de libertad", "Otros", muertes.df$ocuparec)
  
  # Eliminación de columnas
  muertes.df <- muertes.df %>%
    select(-pc,
           -causamuer,
           -des_causa,
           -pcocu,
           -nacmadre,
           -pcregis,
           -gruposcb,
           -instmurio)
  
  return(muertes.df)
}
