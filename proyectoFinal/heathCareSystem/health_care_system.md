# Bootcamp Data Eng 20242 - Proyecto Final

## Propósito
El propósito del proyecto final descrito en este documento es que ustedes, como participantes, apliquen los temas y habilidades abordados en las clases del programa.

## Contexto
Son Ingenieros de Datos en No Somos Globant, una reputada compañía encargada del outsourcing de TI. 
HealthToAll un consorcio de salud con presencia en 3 países los ha contactado para desarrollar una solución de analítica y consolidación de datos.
La solución de analytics deberá proveer respuestas e identificación de problemas de manera proactiva en varias áreas. Inicialmente será analítica sobre data de incapacidades y de pacientes en UCI, donde se han identificado aumentos de costos en los últimos meses.
- HealthToAll también está buscando mejorar sus capacidades de monitoreo y reportería para sus tratamientos/medicamentos de enfermedades raras. 
- Se tienen problemas en la entrega de datos a entidades de control y a farmacéuticas aliadas.
- HealthToAll recientemente abrió una línea de asesoría Telefónica a sus pacientes, pero no tiene actualmente como medir el uso que se ha hecho de la misma.

En el siguiente enlace se puede encontrar el documento de visión de negocio elaborado por el Project Manager encargado de gestionar el proyecto: [Visión de negocio](https://github.com/scaleupseniors/dataEngineering001-20242/blob/main/proyectoFinal/heathCareSystem/vision_de_negocio.md).

### Infraestructura existente

El consorcio se compone de la siguiente forma, y se tiene las siguientes fuentes de datos por tipo.

| Cantidad | Entidad | BD relacionales | BD NoSQL | Dispositivos de monitoreo (IOT) | Archivos CSV |
|----------|---------|-----------------|----------|---------------------------------|--------------|
| 7      | Hospitales| 21              | 4        | 10000                           | 50           |
| 3      | Clinicas  | 14              | 5        | 2500                            | 40           |
| 2      | Seguros   | 4               | 1        | 0                               | 10           |
| 2      | Farmaceuticas | 8           | 1        | 100                             | 5            |

Adicionalmente la línea de atención telefónica, que es un PBX VOIP tiene un repositorio con las grabaciones de las llamadas en formato mp3, el nombre de cada archivo es la fecha y hora de inicio de la llamada.

Todas las entidades tiene cuenta de Twitter, aunque no es el canal indicado a los paciente para 
escalar dudas o pedir asesoría, algunos pacientes escalan por ese medio sus preguntas o 
notifican novedades. 

## Lineamientos
Este proyecto es más de un porte libre, por ello quiero decir que no está bien denotada una necesidad en particular, sino que hay un conjunto de ellas. Si deciden escoger esta opción, les recomiendo que escojan una de las necesidades expuestas anteriormente y partan desde allí hasta la solución de la misma.
PD tengan muy en cuenta los principios de arquitectura mencionados en el documento de [visión de negocio](https://github.com/scaleupseniors/dataEngineering001-20242/blob/main/proyectoFinal/heathCareSystem/vision_de_negocio.md).

Este proyecto consta de cuatro (4) fases:
1. Elaboración de una propuesta de arquitectura.
2. Despliegue de la propuesta de arquitectura.
3. Evaluación de la propuesta de arquitectura.
4. Publicación en Medium.

### Elaboración de una propuesta de arquitectura
Ustedes, como Ingenieros de Datos, deberán elaborar una propuesta de arquitectura y presentármela a mí, que para este trabajo cumpliré el rol de Arquitecto de Datos. Para la presentación de dicha propuesta se sugiere que elaboren los siguientes entregables:

- Diagrama de contexto del sistema (Modelo C4).
- Diagrama de contenedores del sistema (Modelo C4).
- Diagrama de despliegue del sistema (Modelo C4 o Google). 

Pueden hallar ejemplos de proyectos que tienen todos los diagramas mencionados [aquí](https://github.com/scaleupseniors/dataEngineering001-20242/tree/main/masSobreLasArquitecturasDeDatos/ejemplosDiagramasArquitectura).

- Documento: **Visión de atributos arquitectónicos**.

Yo, como Arquitecto de Datos, les pido que vayan más allá y analicen los _trade-offs_ (fortalezas y debilidades) de la arquitectura, escojan tres (3) atributos estructurales que su propuesta de arquitectura cumple muy bien y tres (3) de ellos que no cumple o que directamente empeore, justificando por qué cumple o no dicho atributo.

👉 Además, quiero que escojan una (1) métrica que permita medir (valga la redundancia) el estado de un atributo estructural en la arquitectura.

#### Mi consejo para ustedes para esta etapa
Tal como se ha descrito con anterioridad, para esta etapa se deberá de realizar un diagrama de despliegue de la arquitectura. Esto implica escoger las tecnologías a usar, ya sean de la nube o no. Les recomiendo que en LinkedIn busquen vacantes de ingenieros de datos en una empresa en la cual les gustaría trabajar, y seguidamente, vean qué tecnologías pide la misma. Determinen si dichas tecnologías pedidas sirven o no para su respectivo proyecto, argumentando si es o no una tecnología idónea o no para el mismo y por qué lo consideran así. 


### Despliegue de la propuesta de arquitectura
Luego de tener una arquitectura propuesta, pasaremos al despliegue de la misma en la nube de GCP. Allí se deberá crear toda la infraestructura necesaria para cumplir con los objetivos de negocio propuestos en el documento de visión de negocio y anteriormente mencionados.


### Evaluación de la propuesta de arquitectura
Una vez desplegada la infraestructura, quiero que evalúen si su propuesta fue o no acertada, teniendo en cuenta si realmente logra satisfacer de buena forma los atributos estructurales planteados desde un inicio, si la métrica implementada da resultados favorables y si se lograron cumplir los objetivos de negocio. Sean realistas, no pasa nada por equivocarse; yo mismo me he equivocado mil veces y continúo aprendiendo.

Además, quiero que especifiquen puntos fuertes y a mejorar de la arquitectura, así como cualquier decisión tomada que no resultó como lo esperaban.


### Publicación en Medium
Finalmente, resuman y describan todo lo hecho en el proyecto. Incluyan diagramas, cómo atacaron el problema, atributos arquitectónicos importantes y aquellos que empeoran o no cubre la arquitectura, problemas encontrados y suban a [Medium](https://medium.com/) esos hallazgos en forma de documento.

Por acá les dejo algunos artículos que me han gustado bastante:

- [Serverless Lambda Architecture with Google Cloud Platform](https://medium.com/@imrenagi/serverless-lambda-architecture-with-google-cloud-platform-35cb3123206b)
- [Calidad y Gobierno de Datos: El Talón de Aquiles de la Inteligencia Artificial](https://medium.com/@ivanamonuribe/calidad-y-gobierno-de-datos-el-tal%C3%B3n-de-aquiles-de-la-inteligencia-artificial-151e68b69bf7)
- [Lakehouse — The journey unifying Data Lake and Data Warehouse](https://medium.com/claimsforce/lakehouse-the-journey-unifying-data-lake-and-data-warehouse-bef7629c143a)





