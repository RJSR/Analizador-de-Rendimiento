# Analizador-de-Rendimiento

En el presente programa se calcularán los indicadores de rendimiento para un sistema de colas M/M/1, en donde la primera M hace referencia a la distribución Poisson de las llegadas, la segunda M representa una única y constante tasa de servicio y el 1 se refiere a un único servidor disponible.

## Razones por la que se definió las variables en el idioma inglés

<b>Lenguaje universal:</b> El inglés es el idioma comúnmente utilizado en la comunidad global de programadores y científicos de la computación. Por lo tanto, el código es más accesible y comprensible para una audiencia más amplia en todo el mundo.

<b>Documentación y colaboración:</b> Muchos recursos, tutoriales, documentación y literatura técnica están disponibles en inglés. Al usar el inglés para nuestras variables, se facilita la comunicación, la colaboración y la búsqueda de información relacionada.

<b>Aprendizaje:</b> Esta estructura también es útil para aquellos que están aprendiendo o están familiarizandose con el idioma.

## Estructura del código

Se inicia definiendo una función llamada `dmm1_queue_performance` que toma dos parámetros: `arrival_rate` y `service_rate`.
```
def mm1_queue_performance(arrival_rate, service_rate):
```
Se procede a calcular la utilización del sistema dividiendo la tasa de llegada `(arrival_rate)` entre la tasa de servicio `(service_rate)`. La utilización representa la fracción del tiempo en que el servidor está ocupado.
```
utilization = arrival_rate / service_rate
```
Se calcula la longitud promedio de la cola utilizando la fórmula `(arrival_rate ** 2) / (service_rate * (service_rate - arrival_rate))`. Esto se basa en las propiedades de los sistemas M/M/1 y está relacionado con la tasa de llegada y la tasa de servicio.
```
avg_queue_length = (arrival_rate ** 2) / (service_rate * (service_rate - arrival_rate))
```
Calculamos el tiempo promedio de espera en la cola dividiendo la longitud promedio de la cola entre la tasa de llegada. Esto nos da una estimación del tiempo que una solicitud pasa esperando en la cola antes de ser atendida.
```
avg_wait_queue = avg_queue_length / arrival_rate
```
Calculamos la longitud promedio del sistema utilizando la fórmula `arrival_rate / (service_rate - arrival_rate)`. Esto toma en cuenta tanto las solicitudes en el sistema como las que están esperando en la cola.
```
avg_system_length = arrival_rate / (service_rate - arrival_rate)
```
Calculamos el tiempo promedio de espera en el sistema dividiendo la longitud promedio del sistema entre la tasa de llegada. Esto nos da una estimación del tiempo que una solicitud pasa en el sistema (cola + servicio) antes de completar su servicio.
```
avg_wait_system = avg_system_length / arrival_rate
```
Finalmente, devolvemos todos los indicadores de rendimiento calculados como una tupla.

Definimos los valores de `arrival_rate` y `service_rate` que representan la tasa de llegada y la tasa de servicio del sistema.
```
arrival_rate = 10 # requests per second
service_rate = 1 / 0.08 # requests per second
```
Llamamos a la función `mm1_queue_performance` con los valores de `arrival_rate` y `service_rate`, y asignamos los resultados a las variables correspondientes.

Por último, se imprime los resultados formateados con dos decimales utilizando _f-strings_ para mostrar los valores de utilización, longitud promedio de la cola, tiempo promedio de espera en la cola, longitud promedio del sistema y tiempo promedio de espera en el sistema.
```
print(f"Utilization: {utilization:.2f}")
print(f"Avg Queue Length: {avg_queue_length:.2f}")
print(f"Avg Wait in Queue: {avg_wait_queue:.2f} seconds")
print(f"Avg System Length: {avg_system_length:.2f}")
print(f"Avg Wait in System: {avg_wait_system:.2f} seconds")
```

