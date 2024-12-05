# Proyecto: Bootcamp Data Eng 20242 - Proyecto Final

### Objetivo General
Desarrollar una infraestructura de análisis en tiempo real que calcule indicadores como tiempo promedio de entrega, productos más vendidos, clientes frecuentes y precisión del sistema, alineada con los objetivos estratégicos de la empresa.

## Requerimientos
- Procesamiento de datos en tiempo real para generar métricas cada 30 segundos, 5 minutos y 1 hora.
- Monitoreo de precisión diaria de las métricas generadas.
- Escalabilidad para manejar el volumen de datos de una empresa de entregas a domicilio.

## Funcionalidades
El sistema deberá:
- Calcular el tiempo promedio de entrega de órdenes.
- Generar los top 10 productos más comprados por intervalo de tiempo.
- Determinar las 10 tiendas más vendedoras.
- Identificar los 5 clientes más frecuentes.
- Evaluar y reportar la precisión diaria del sistema.

## Casos de Uso
### Caso de Uso 1: Generación de Métricas en Tiempo Real
**Actor:** Sistema de análisis.  
**Descripción:** Procesa los datos recibidos en tiempo real para generar métricas cada 30 segundos, 5 minutos y 1 hora.  

### Caso de Uso 2: Reporte de Precisión
**Actor:** Administrador del sistema.  
**Descripción:** Evalúa la precisión de las métricas calculadas y genera un informe diario.  

## Historias de Usuario
1. **Como analista de negocio, quiero conocer los productos más vendidos cada hora para ajustar el inventario de las tiendas.**
2. **Como gerente de operaciones, necesito el tiempo promedio de entrega en tiempo real para optimizar los recursos logísticos.**
3. **Como administrador del sistema, deseo evaluar la precisión de las métricas diarias para garantizar su confiabilidad.**

## Beneficios y Costos
### Beneficios
- **Optimización del negocio:** Identificación de productos y tiendas más rentables.
- **Mejora en el servicio:** Reducción en tiempos de entrega y aumento en la satisfacción del cliente.
- **Confiabilidad:** Monitoreo continuo de la precisión del sistema.

### Costos
- **Infraestructura:** Gastos en servidores en la nube (GCP) y herramientas de monitoreo.

> **Nota:** Los costos se estiman en función del uso de herramientas en GCP.

## Proceso de Negocio
### Diagrama
```plaintext
Cliente → Orden → Ingesta de Datos → Procesamiento en Tiempo Real → Generación de Métricas → Visualización
```
### Reglas del negocio
1. Las métricas deben actualizarse según el intervalo de tiempo especificado.
2. Los datos procesados deben mantenerse por al menos 24 horas para validaciones.
3. El sistema debe garantizar al menos un 80% de precisión en las métricas generadas.
## Grupo de Interés (Stakeholders)
- Gerente de Operaciones: Aprobación de funcionalidades relacionadas con logística.
- Analista de Negocio: Uso de métricas generadas para la toma de decisiones.
- Administrador del Sistema: Mantenimiento y evaluación de la precisión del sistema.
## Métricas
- Tiempo promedio de respuesta: Medición del tiempo desde la recepción de datos hasta la generación de métricas.
- Porcentaje de precisión: Relación entre las métricas reportadas y los valores reales.
- Disponibilidad del sistema: Tiempo operativo del sistema durante el día.