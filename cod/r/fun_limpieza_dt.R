#' Función que realiza la limpieza de una base de datos en concreto
#'
#' @param df (DataFrame) Base de datos de muertes en Costa Rica
#'
#' @return NuLL
#'
limpieza.dt <- function(df) {
  # Se pasan a data.table (se puede leer directamente, pero no admite carpetas)
  muertes.dt <- setDT(df)
  
  # Se filtra por edades mayores o iguales a 15 y años mayores o iguales a 2014
  muertes.dt <-
    muertes.dt[edads >= 15 &
                 anodef >= 2014 &
                 anotrab >= 2014 & anodeclara >= 2014]
  
  # Correcciones ortográficas con gsub y el operador :=
  muertes.dt[, estcivil := gsub("Ã³", "o", estcivil)]
  muertes.dt[, regsalud := gsub("Ã³", "o", regsalud)]
  muertes.dt[, provincia := gsub("Ã³", "o", provincia)]
  muertes.dt[, provocu := gsub("Ã³", "o", provocu)]
  muertes.dt[, provregis := gsub("Ã³", "o", provregis)]
  muertes.dt[, reginec := gsub("Ã³", "o", reginec)]
  muertes.dt[, ocuparec := gsub("Ã¡", "a", ocuparec)]
  muertes.dt[, ocuparec := gsub("Ã©", "e", ocuparec)]
  muertes.dt[, provincia := gsub("Ã©", "e", provincia)]
  muertes.dt[, provocu := gsub("Ã©", "e", provocu)]
  muertes.dt[, provregis := gsub("Ã©", "e", provregis)]
  muertes.dt[, autopsia := gsub("Ã©", "e", autopsia)]
  muertes.dt[, asistmed := gsub("Ã©", "e", asistmed)]
  muertes.dt[, nacionalid := gsub("^(?!Costa Rica$).*", "Extranjero", nacionalid, perl = TRUE)]
  muertes.dt[, reginec := gsub("Paci­fico", "Pacifico", reginec)]
  muertes.dt[, regsalud := gsub("Paci­fico", "Pacifico", regsalud)]
  muertes.dt[, estcivil := gsub("Ignorado", "Otros", estcivil)]
  muertes.dt[, estcivil := gsub("Union libre", "Otros", estcivil)]
  muertes.dt[, estcivil := gsub("Separado", "Otros", estcivil)]
  muertes.dt[, estcivil := gsub("Menor", "Otros", estcivil)]
  muertes.dt[, edadsrec := gsub("100 y mÃ¡s", "100 - 121", edadsrec)]
  muertes.dt[, ocuparec := gsub("Profesionales cienti­ficos e intelectuales",
                                "Trabajadores activos",
                                ocuparec)]
  muertes.dt[, ocuparec := gsub(
    "Agricultores y trabajadores calificados agropecuarios, forestales y pesqueros",
    "Trabajadores activos",
    "Trabajadores activos",
    ocuparec
  )]
  muertes.dt[, ocuparec := gsub(
    "Trabajadores de los servicios y vendedores de comercios y mercados",
    "Trabajadores activos",
    ocuparec
  )]
  muertes.dt[, ocuparec := gsub("Ocupaciones elementales", "Trabajadores activos", ocuparec)]
  muertes.dt[, ocuparec := gsub(
    "Operadores de instalaciones y maquinas y ensambladores",
    "Trabajadores activos",
    ocuparec
  )]
  muertes.dt[, ocuparec := gsub("Tecnicos y profesionales de nivel medio",
                                "Trabajadores activos",
                                ocuparec)]
  muertes.dt[, ocuparec := gsub(
    "Oficiales, operarios y artesanos de artes mecanicas y de otros oficios",
    "Trabajadores activos",
    ocuparec
  )]
  muertes.dt[, ocuparec := gsub("Personal de apoyo administrativo",
                                "Trabajadores activos",
                                ocuparec)]
  muertes.dt[, ocuparec := gsub("Directores y gerentes", "Trabajadores activos", ocuparec)]
  muertes.dt[, ocuparec := gsub("Pensionado", "Otros", ocuparec)]
  muertes.dt[, ocuparec := gsub("Persona con discapacidad", "Otros", ocuparec)]
  muertes.dt[, ocuparec := gsub("Estudiante", "Otros", ocuparec)]
  muertes.dt[, ocuparec := gsub("Mal especificadas", "Otros", ocuparec)]
  muertes.dt[, ocuparec := gsub("Privado de libertad", "Otros", ocuparec)]
  
  # Correcciones ortográficas con chartr y el operador :=
  muertes.dt[, ocuparec := chartr("Ã", "i", ocuparec)]
  muertes.dt[, regsalud := chartr("Ã", "i", regsalud)]
  muertes.dt[, reginec := chartr("Ã", "i", reginec)]
  muertes.dt[, autopsia := chartr("Ã", "i", autopsia)]
  muertes.dt[, asistmed := chartr("Ã", "i", asistmed)]
  
  # Eliminación de columnas
  muertes.dt[, c(
    "pc",
    "causamuer",
    "des_causa",
    "pcocu",
    "nacmadre",
    "pcregis",
    "gruposcb",
    "instmurio"
  ) := NULL]
  
  return(muertes.dt)
}
