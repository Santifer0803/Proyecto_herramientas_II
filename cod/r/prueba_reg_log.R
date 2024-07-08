# Se separan las bases necesarias
X <- as.matrix(datos.diabetes %>%
                 select(-Outcome))

y <- unlist(datos.diabetes %>%
              select(Outcome))

# Se normalizan los datos
X <- (X - min(X)) / (max(X) - min(X))

# Se separan los datos de prueba y los de entrenamiento
X.train <- sample_frac(as.data.frame(cbind(X, y)), 0.8)
X.val <- setdiff(as.data.frame(cbind(X, y)), X.train)

# Se extraen los datos necesarios en cada variable
y.train <- unlist(X.train[, ncol(X.train)])
y.val <- unlist(X.val[, ncol(X.val)])
X.train <- as.matrix(X.train[, -ncol(X.train)])
X.val <- as.matrix(X.val[, -ncol(X.val)])

# Modelo de regresión logística
resultado <- regresion.logistica(
  X.train = X.train,
  y.train = y.train,
  X.val = X.val,
  y.val = y.val,
  num.iterations = 1000,
  learning.rate = 0.003
)
