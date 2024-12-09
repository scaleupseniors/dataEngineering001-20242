# Proyecto: Bootcamp Data Eng 20242 - Visión de negocio

## Objetivo General
Diseñar e implementar una solución de analítica avanzada y consolidación de datos que permita identificar problemas proactivamente, optimizar costos en áreas críticas y mejorar el monitoreo y reporte de información relacionada con incapacidades, pacientes en UCI, enfermedades raras y el uso de su línea de asesoría telefónica.

### Objetivos de negocio
- Integrar diferentes fuentes de datos (Hospitales, Clínicas, Seguros, Farmacéuticas) y de los proveedores externos.
- Proveer modelos de analítica avanzada y dashboards que permitan desarrollar insights de los pacientes y sus tratamientos.
- Proveer una solución para facilitar la reporteria y entrega de datos con entes externos, teniendo en cuenta buenas practicas de seguridad. 
- Medir el uso de la asesoría telefónica para identificar calidad del servicio, horas pico, preguntas recurrentes, duración, etc.

## Requerimientos

- Procesamiento de datos en tiempo real que permita generar métricas cada 5 minutos y cada hora para las áreas de incapacidades y UCI.
- Monitoreo y análisis de precisión diaria para validar la calidad de las métricas generadas.
- Escalabilidad para manejar la diversidad de fuentes de datos de hospitales, clínicas, seguros y farmacéuticas, así como dispositivos IoT.
- Integración con datos de redes sociales (Twitter) para capturar interacciones relacionadas con consultas o notificaciones de pacientes.

### HealthToAll principios de arquitectura
HealthToAlltiene los siguientes principios dentro de su arquitectura, los cuales deben ser cumplidos por cualquier solución dentro de su consorcio.

| Objective                          | Description                                                                                                   |
|------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **1. Real-time para monitoreo de pacientes** | - Procesar las transacciones inmediatamente a medida que se reciben                                        |
|                                    | - Procesamiento de extremo a extremo en segundos, no horas o días                                           |
| **2. Global**                      | - Todas las plataformas deben ser extensibles y flexibles para admitir diferentes mercados sin necesidad de reestructurar o reescribir |
|                                    | - No hard coded para casos de localización específica                                                       |
|                                    | - Reglas comerciales específicas del mercado                                                               |
| **3. Always on**                   | - Disponibilidad de 99.99%                                                                                   |
|                                    | - Múltiples zonas o data centers                                                                            |
|                                    | - Failover inmediato                                                                                        |
|                                    | - Escalabilidad                                                                                             |
|                                    | - Evitar "single point of failure"                                                                          |
|                                    | - Capacidad para ejecución en nube híbrida                                                                  |
|                                    | - Resiliente a fallos de infraestructura                                                                    |
| **4. Data Localization**           | - Capacidad para migrar fácilmente y depurar datos específicos de un país                                   |
|                                    | - Datos específicos del país a los que solo pueden acceder las partes autorizadas                          |
| **6. Reusable/Composable**         | - Las plataformas deben adoptar una arquitectura "orientada a componentes" en la que la plataforma sea una agregación de componentes reutilizables y microservicios |
| **7. Inside Out**                  | - Plataforma de fácil acceso para consumidores internos y externos                                          |
| **8. Outside In**                  | - Integre a la perfección la funcionalidad de los socios en el stack técnico actual                         |
| **9. Smart**                       | - Monitoreo inteligente                                                                                     |
|                                    | - Automatización                                                                                            |
|                                    | - Toma de decisiones dirigida por máquinas/datos (data-driven)                                             |

## Funcionalidades
La solución deberá:
- Generar métricas clave como:
- Costos promedio por paciente en UCI.
- Incrementos en costos relacionados con incapacidades.
- Uso de la línea de asesoría telefónica.
- Identificación de medicamentos o tratamientos más demandados para enfermedades raras.
- Consolidar datos de múltiples fuentes (relacionales, NoSQL, IoT y archivos CSV) en un único sistema de análisis.
- Realizar análisis proactivo para identificar patrones de comportamiento en pacientes y costos.
- Monitorear en tiempo real las interacciones de pacientes a través de la línea de atención telefónica y redes sociales.

## Casos de uso
### Caso de Uso 1: Monitoreo de Pacientes en UCI
Actor: Sistema de analítica.
Descripción: Procesa datos en tiempo real provenientes de dispositivos IoT en hospitales para calcular métricas como tiempo promedio en UCI, costos asociados y variaciones en tratamientos.
### Caso de Uso 2: Reporte de Costos de Incapacidades
Actor: Analista de negocio.
Descripción: Genera informes diarios que comparan el costo promedio de incapacidades y sus incrementos en un periodo específico, permitiendo tomar decisiones para la optimización.
### Caso de Uso 3: Uso de la Línea Telefónica
Actor: Administrador del sistema.
Descripción: Analiza las grabaciones de llamadas telefónicas para medir el uso del servicio y generar métricas como tiempo promedio de atención y número de llamadas escaladas.

## Historias de usuario
1. Como gerente de costos, quiero conocer los incrementos en los costos de incapacidades para tomar acciones correctivas.
2. Como jefe de UCI, necesito métricas en tiempo real sobre pacientes críticos para optimizar los recursos hospitalarios.
3. Como administrador del sistema, deseo evaluar la precisión de las métricas diarias para garantizar que los reportes sean confiables.
4. Como gerente de servicio al cliente, quiero analizar el uso de la línea telefónica para mejorar su efectividad.

## Beneficios y Costos
### Beneficios
- Optimización operativa: Identificación de patrones que permitan reducir costos en áreas críticas como UCI e incapacidades.
- Mejora en la experiencia del paciente: Respuesta proactiva a necesidades específicas como medicamentos para enfermedades raras.
- Confiabilidad y trazabilidad: Consolidación y monitoreo continuo de los datos.
### Costos
- Infraestructura: Inversión en servidores en la nube (GCP) y herramientas de monitoreo de dispositivos IoT y datos no estructurados.

## Proceso de Negocio
Dispositivos IoT → Ingesta de Datos → Consolidación → Procesamiento en Tiempo Real → Generación de Métricas → Visualización/Reporte

### Reglas del negocio
1. Las métricas deben actualizarse en intervalos de 5 minutos y 1 hora.
2. Los datos deben consolidarse y conservarse por al menos 48 horas para auditorías.
3. El sistema debe garantizar una precisión mínima del 85% en las métricas generadas.


## Grupo de Interés (Stakeholders)
- Gerente de Operaciones: Supervisión de métricas relacionadas con costos y uso de recursos.
- Analista de Negocios: Uso de métricas generadas para optimización estratégica.
- Administrador del Sistema: Garantía de funcionamiento, precisión y escalabilidad del sistema.

## Métricas
- Tiempo promedio de respuesta: Tiempo transcurrido entre la recepción de datos y la generación de métricas.
- Porcentaje de precisión: Relación entre los valores reportados y los datos reales validados.
- Uso de la línea telefónica: Número de llamadas atendidas, tiempo promedio de respuesta y problemas reportados.
- Disponibilidad del sistema: Tiempo operativo del sistema para procesar datos en tiempo real.


