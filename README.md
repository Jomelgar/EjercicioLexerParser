# Proyecto Lexer y Parser para EJERCICIO -LENGUAJES DE PROGRAMACION Q2-2025

Este proyecto implementa un **lexer** y un **parser** simples para un lenguaje de programación pequeño que llamamos *PROLANG* (nombre provisional).

---

## ¿Qué es PROLANG?

PROLANG es un lenguaje de ejemplo para ejercicios académicos, con una sintaxis sencilla que incluye:

- Asignaciones (`a = b + 3;`)
- Condicionales `if`
- Bucles `while`
- Expresiones aritméticas básicas (`+`, `-`, `*`, `/`, `<`, `>`)
- Expresiones de igualdad (`==`,`!=`) [Las puse por si hacer una buena expresion de logica]
---

## Funcionalidad

- **Lexer:** Convierte un fragmento de código en una lista de tokens con categorías como `ID`, `NUMERO`, `OPERADOR`, `IF`, `WHILE`, etc.
- **Parser:** Analiza la secuencia de tokens para validar que la sintaxis del código sea correcta según las reglas del lenguaje.
- **Validación:** En este ejercicio, el parser no evalúa resultados ni genera un árbol sintáctico, solo comprueba que el código esté bien formado.

---

## Fragmento de código probado

```c
a = b + 3;
if (a > 5) { c = 1 + a; }
while (a < 10) { a = a + 1; }
