# Primera iteración del modelo

# Lista para las primas
lista.primash <- list()

# Tasa equivalente
j <- ((1.04) * (1.03)) - 1

# Todas las probabilidades de muerte, de hombres, de 21 hasta 65
prob.muerteh <-
  sapply(1:45, function(i)
    sapply(((20 + i)):116, function(k)
      qx.hombres[[k, 5 + k]]))

# Matriz de probabilidades de supervivencia, de hombres, desde edad inicial 21 hasta edad inicial 65, cada fila es una persona de edad 21, 22, 23, ...
matriz.probh <-
  (1 - t(as.matrix(sapply((1:length(prob.muerteh)), function(l)
    c(prob.muerteh[[l]], rep(1, (
      length(prob.muerteh[[1]]) - length(prob.muerteh[[l]]) + 1
    )))))))

# Se eliminan las columnas innecesarias
matriz.probh <- matriz.probh[, 1:(ncol(matriz.probh) - 1)]

# Nombres de filas y columnas
colnames(matriz.probh) <- c(2024:(2024 + 115 - 20))
rownames(matriz.probh) <- c(20:64)

# El número de filas y columnas es fijo, entonces se guardará para que no se calcule en cada iteración después
colmat <- ncol(matriz.probh)
filmat <- nrow(matriz.probh)

# Creamos las matrices de números aleatorios
matriz.rndh <-
  matrix(data = pnorm(rnorm(colmat * filmat, 0, sd = 1), mean = 0, sd = 1),
         nrow = filmat,
         ncol = colmat)

# Comparación de matrices
matriz.rndh <- matriz.rndh < matriz.probh

# Se agregan los falsos después del primer falso de la matriz
matriz.rndh <- t(apply(matriz.rndh, 1, fila.muerte))

# Cantidad de primas
idh <- sapply(1:filmat, function(m)
  which(!matriz.rndh[m,])[1])

# Anualidades
anh <-
  sapply(1:filmat, function(n)
    sum((1 + j) ^ -(0:(min(
      idh[n], (65 - 19 - n)
    ) - 1))))

# Rango de años de cada persona desde que llega a 65 años hasta que fallece
annosh.65 <- sapply(20:64, function(o)
  c((65 - o):(idh[[o - 19]])))

# Beneficios para trabajadores y pensionados
benh <-
  sapply(1:length(annosh.65), function(p)
    (ifelse(
      idh + c(20:64) < 65,
      5000000 * ((1 + j) ^ -(idh)),
      sum(300000 * 13 * (1 + j) ^ -annosh.65[[p]]) + 1000000 * ((1 + j) ^ -(idh))
    ))[p])

# Guardamos el resultado
lista.primash[[1]] <- (benh / anh)
