**Declaración de uso de IA generativa**  
*Es * ***obligatorio*** * aunque no hayas usado IA (en ese caso, escribe "No se utilizó*  
 *  
 IA generativa en este proyecto" en la sección 1 y deja el resto en blanco).*  
 *  
 La declaración sigue el modelo de 6 campos de la UNED/ACRL AID Framework.*  
**Estudiante**  
- **Nombre y apellidos**:  
- **Repositorio (URL)**:  
- **Fecha de entrega**:  
- **Asignatura**: Redes Neuronales Artificiales con Python  
  
**1. Herramientas utilizadas**  
| | | | |  
|-|-|-|-|  
| **Herramienta** | **Modalidad** | **Versión / Modelo** | **Plan (Free/Pro/etc.)** |   
|   |   |   |   |   
|   |   |   |   |   
   
***Modalidad*** *: Agente autónomo (Cursor Composer, Claude Code) / Chat (web o IDE) /*  
 *  
 Autocompletado (tab-tab) / Mixto*  

**2. Propósito del uso**  
Describe brevemente para qué utilizaste la IA en cada fase del proyecto:  
| | |  
|-|-|  
| **Fase del proyecto** | **Propósito (ej. debuggear, generar tests, explicar concepto, refactorizar)** |   
| Análisis exploratorio del dataset |   |   
| Implementación del forward pass |   |   
| Implementación del backward pass |   |   
| Diseño del optimizador |   |   
| Experimentos y hyperparámetros |   |   
| Redacción del reporte |   |   
| Tests |   |   
| Otro: |   |   
   

**3. Prompts o instrucciones proporcionadas**  
Lista 3–5 prompts representativos (no hace falta todos). Si usaste agente  
   
 autónomo, describe las instrucciones iniciales que le diste.  
 
**4. Uso del contenido generado**  
Para 2 tareas donde usaste IA, indica cómo integraste el output:  
| | | | |  
|-|-|-|-|  
| **Tarea** | **Herramienta** | **Output de la IA** | **Mi intervención** |   
|   |   |   |   |   
|   |   |   |   |   
   
***Mi intervención*** *: describe qué hiciste después de recibir el output de la IA.*  
 *  
 Ej: "Revisé las derivadas, corregí el chain rule para softmax, añadí comentarios".*  
 *  
 Ej: "Apliqué tal cual sin modificar" (esto es válido).*  

**5. Revisión y edición**  
Indica qué porcentaje del código generado por IA revisaste o modificaste antes  
   
 de incluirlo en el repo:  
- Revisé todo el código generado por IA y lo modifiqué según el contexto  
- Revisé la mayoría y no fue necesario modificarlo.  
- No revisé la mayor parte del código generado.  
- No usé IA (N/A)  

**6. Limitaciones y consideraciones éticas**  
Menciona cualquier limitación que identificaste en el uso de la IA y las  
   
 consideraciones éticas que tuviste en cuenta (3–5 líneas):  

**7. Costo de IA**  
**Análisis cuantitativo de la conversación**  
Al final de tu conversación con la IA, pega el siguiente promt tal cual en la conversación. 

```text

 Realiza un análisis cuantitativo con respecto al costo de esta conversación, la interacción completa y estima las siguientes cuatro métricas:  
   
1. Tamaño textual total:  
   T_text = T_usuario + T_IA  
   
   donde T_usuario es el número total estimado de tokens escritos por el usuario y T_IA es el número total estimado de tokens generados por la IA.  
   
2. Carga computacional conversacional estimada:  
   T_compute ≈ Σ_k T_context^(k) + Σ_k T_output^(k)  
   
   Estima los tokens de contexto acumulados que habrían sido procesados a lo largo de todos los turnos (k), suponiendo que en cada nueva respuesta se proporciona al modelo el historial previo de la conversación. Incluye los tokens generados como salida.  
   
3. Factor de reprocesamiento:  
   R = T_compute / T_text  
   
4. Costo monetario estimado:  
   C_estimado = P_input × T_input + P_output × T_output  
   
   donde:  
   - T_input = Σ_k T_context^(k)   (tokens de entrada procesados, equivalente a la suma de contexto acumulado por turno)  
   - T_output = Σ_k T_output^(k)    (tokens de salida generados por la IA)  
   - P_input  = precio por token de input (en USD/token), según el modelo declarado en la sección 1  
   - P_output = precio por token de output (en USD/token), según el modelo declarado en la sección 1  
   
   Si no conoces el precio exacto del modelo LLM usado, emplea una estimación razonable.  
   Reporta el resultado en USD con dos decimales, e indica un rango de incertidumbre.  
   
Aclaraciones  
- Analiza únicamente el contenido de esta conversación.  
- Incluye todos los mensajes del usuario y de la IA que sean visibles en el historial de esta conversación.  
- No incluyas instrucciones internas del sistema, razonamiento interno, memoria, herramientas, mensajes ocultos ni información externa que no sea visible como parte de la conversación.  
- Si no puedes contar tokens exactamente, proporciona una estimación razonable.  
- Para T_compute, asume un modelo conversacional estándar sin caching.  
Presenta el resultado en el siguiente formato:  
   
## Métricas de la conversación  
   
| Métrica | Símbolo | Estimación |  
|---|---:|---:|  
| Tokens del usuario | T_usuario | ... |  
| Tokens de la IA | T_IA | ... |  
| Tamaño textual total | T_text | ... |  
| Carga computacional estimada | T_compute | ... |  
| Factor de reprocesamiento | R | ... |  
| Costo monetario estimado | C_estimado | ... USD |  
   
## Parámetros de costo asumidos  
   
| Parámetro | Símbolo | Valor asumido |  
|---|---:|---:|  
| Precio por token de input | P_input | ... USD/token |  
| Precio por token de output | P_output | ... USD/token |  
| Tokens de input totales | T_input | ... |  
| Tokens de output totales | T_output | ... |  

```
   
posteriormente llena el siguiente formato:  
La conversación fue analizada mediante una estimación de tres métricas:  
- Tamaño textual total:  
   
 T_text = ______ tokens.  
- Carga computacional conversacional estimada:  
   
 T_compute = ______ tokens.  
- Factor de reprocesamiento:  
   
 R = ______.  
- Costo total de sesion =   
Interpretación: ________________________________.  
**Comentario del estudiante** (2–3 líneas): ¿Consideras que estos valores son proporcionales  
   
 al valor que obtuviste de la IA? ¿Hubo sesiones con mucho consumo pero poco valor?  

**8. Reflexión general (5–10 líneas)**  
¿Cómo te ayudó la IA? ¿Qué hiciste para verificar su output? ¿Aprendiste algo  
   
 del proceso de dirigir la IA? ¿Qué harías diferente la próxima vez?  
