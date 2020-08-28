# To `join()` or not to `join()`...

En `dormilones.py` vimos tres ejemplos básicos de ejecución:

- Clásico secuencial,
- Con threads,
- Y con threads, pero esperando a que terminen usando `join()`.

Entonces responda:
- ¿Por qué los segundos que se imprimen que pasaron son 2, 0 y 1 (aprox.) respectivamente?

 + En el ejemplo clasico secuencial pasan 2 segundos porque el código se ejecuta de manera secuencial, linea por linea. 
 + En el segundo caso con threads se crean dos hilos (Threads) y se ejecuta el código de manera concurrente, de modo tal que se ejecuta la linea de finalizar e imprimir antes de que termine de pasar el tiempo de dormir().
 + En el tercer ejemplo se ejecuta de manera concurrente/secuencial porque los join() hacen que cada hilo tenga que esperar a que termine la cuenta de un segundo antes de seguir procesando. Pasa 1 segundo solamente porque los dos hilos ejecutan el join() al mismo tiempo. Se ejecuta de manera concurrente de todas maneras.

- ¿Cuántos hilos o threads hay en cada caso?
 + En el primer caso hay un solo hilo de procesamiento, el main. En el segundo y el tercero hay 3, contando con el main y los dos creados.
- Los últimos dos ejemplos tienen la misma cantidad de threads cada uno, ¿cuál sería la diferencia entonces?
  + La única diferencia es el join() que hace que haya que esperar la cuenta de un segundo para seguir procesando.
- En el último ejemplo, ¿qué desventaja o desventajas le ve al uso del `join()`?
  + Una desventaja puede ser la  perdida de tiempo, ya que hay que detener todo el flujo de procesamiento para esperar a los hilos.


# Muchos threads

En `muchosThreads.py` hay algunas cosas básicas de Python:
- `from tiempo import Contador` importa desde `tiempo.py` la clase `Contador`.
- Cómo crear una lista vacía.
- Cómo hacer un loop con cantidad de iteraciones fija.
- Cómo agregar elementos (al final) a una lista.
- Cómo hacer un loop que itere sobre una lista.

## Parte 1
Mirá el código y fijate de entender la sintaxis. 

## Parte 2
Ahora corré el script: ¿por qué tarda lo que tarda? 


# Intercalación en concurrencia

**Dos reglas importantes** para `contadorConcurrente.py`:
- Mirá el código pero _no lo ejecutes_,
- Mirá el código pero _no lo ejecutes_.

(Referencia [The First Rule of Fight Club (1999)](https://www.youtube.com/watch?v=dC1yHLp9bWA))

Mirando el código de `contadorConcurrente.py`, pero sin ejecutarlo:
- Al ejecutar la función `cuenta()`, ¿cuántas veces se ejecuta el `for` que tiene adentro, y qué hace cada iteración del `for`?
- ¿Es verdad que cada thread lanza una ejecución de la función `cuenta()`?
- ¿Es verdad que se está esperando a que termine cada thread?
- ¿Cúal te parece que es el valor que se imprime de `counter`?

Ahora corré `contadorConcurrente.py`:
- Correlo varias veces, ¿qué observás que pasa?
- ¿Por qué está pasando eso que observás?


# ¿Secuencial clásico, concurrente o paralelo?

Para cada una de las siguiente situaciones, decidí si es secuencial clásico, concurrente o paralelo. Intentá justificar señalando las ideas esenciales de cada caso.

- Cuál persona de un total de 50 corre más rápido una maratón.
    - opción 1) Cada persona corre secuencialmente en la pista, y medimos cada tiempo.
    - opción 2) Todas las personas corren en la misma pista, y la que llega primero listo.
		- Preguntas: ¿hay algún recurso compartido? ¿genera problemas?
    - opción 3) Cada persona corre en una pista distinta, todas al mismo tiempo.
		- Pregunta: ¿hay un aumento de recursos respecto al anterior?
    - Pregunta: ¿pros y contras de cada opción?

- Competencia de triples en basquet: quién mete más en 10 intentos.
    - opción 1) Cada persona secuencialmente realiza 10 intentos, y anotamos la cantidad de triples.
    - opción 2) Todas las personas tiran los 10 intentos al mismo tiempo.
		- Preguntas: ¿hay algún recurso compartido? ¿genera problemas?
    - opción 3) Cada persona tira en un aro distinto, todas al mismo tiempo.
    - Pregunta: ¿pros y contras de cada opción?
