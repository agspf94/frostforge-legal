# Español (Latinoamérica)

**Última actualización:** `[FECHA]`

## 1. Quiénes somos
"Frostforge" (nombre provisional) es un juego para dispositivos móviles. El responsable del tratamiento de los datos es `[NOMBRE LEGAL DEL RESPONSABLE]`.
Contacto para solicitudes de privacidad: `[CORREO DE PRIVACIDAD]`. El juego es para jugadores de 16 años o más.

## 2. Qué datos recopilamos y para qué
| Dato | Cuándo | Finalidad | Base legal (GDPR/LGPD) |
|---|---|---|---|
| Id de cuenta anónimo (id de usuario "invitado" de Cognito) | Al abrir el juego por primera vez | Identificar tu partida para que puedas jugar | Contrato (prestación del juego) |
| Estado del juego: diseño de la base, recursos, investigaciones, héroes, tropas, progreso del tutorial, marcas de tiempo | Mientras juegas | Ejecutar el juego en nuestro servidor (el servidor es la fuente autorizada) | Contrato |
| Identificador de la cuenta de Google (sin correo ni perfil) (solo si tocas "Vincular Google") | Cuando vinculas | Recuperar tu partida en otro dispositivo | Consentimiento (tú eliges vincular) |
| Token de integridad del dispositivo (Google Play Integrity) | Al registrarte como invitado en Android | Bloquear clientes falsos y abusos | Interés legítimo (seguridad, antitrampas) |
| Registros técnicos: pueden incluir la dirección IP tal como la procesa AWS, hora de la solicitud, endpoint, estado, id de usuario | En cada solicitud | Seguridad, depuración, control de costos | Interés legítimo |
| Comentarios que envías desde el menú: tu texto, tu id de usuario, hora, versión de la app, plataforma, idioma | Cuando envías un comentario | Leer y responder tus comentarios | Consentimiento |
| Estadísticas de uso, solo si tocas "Permitir" (se puede cambiar en el menú): por día, conteo de eventos como pasos del tutorial, sesiones, tiempo de juego, nivel más alto del Núcleo, primera investigación/reclutamiento/expedición y un código corto que identifica un error de script; junto con tu id de usuario, versión de la app y plataforma | Mientras juegas, después de que lo permitas | Entender dónde se atascan los jugadores y cuántos regresan | Consentimiento |

**No** vendemos tus datos, no mostramos anuncios de terceros ni usamos tus datos para elaborar perfiles. No recopilamos
a sabiendas datos de menores de 16 años.

Las estadísticas de uso se guardan como totales diarios por jugador (no un registro por acción), no contienen texto libre,
id de publicidad ni id del dispositivo, y no se envía nada hasta que eliges "Permitir". Los informes de fallos nativos provienen de Google Play (Android vitals).

**Previsto (aún no se recopila):** comprobantes de compras dentro de la app. Antes de que empiecen, actualizaremos esta política y, cuando sea necesario, pediremos tu consentimiento.

## 3. Quién recibe tus datos
- **Amazon Web Services** (alojamiento, base de datos, registros, inicio de sesión mediante Amazon Cognito, notificaciones por correo). Encargado del tratamiento.
- **Google** (inicio de sesión con Google si vinculas; Play Integrity; Google Play para la distribución y, en el futuro, los pagos).
- Nadie más. Podemos divulgar datos si la ley lo exige.

## 4. Dónde se almacenan los datos
Región de Amazon Web Services **us-east-2 (Ohio, EE. UU.)**. Si estás fuera de EE. UU., tus datos se transfieren allí;
para las transferencias desde la UE/Reino Unido/Brasil nos basamos en las cláusulas contractuales tipo/condiciones de protección de datos de AWS.

## 5. Cuánto tiempo los conservamos
- Estado del juego y cuenta: hasta que elimines la cuenta.
- Comentarios: se eliminan automáticamente después de 180 días (o antes, cuando eliminas tu cuenta). También se envía una copia
  por correo a la bandeja del desarrollador, que se elimina si lo solicitas.
- Estadísticas de uso: se eliminan automáticamente después de 120 días (o antes, cuando eliminas tu cuenta); el registro de tu
  elección (Permitir / No, gracias) y el día en que elegiste por primera vez se conservan hasta que elimines tu cuenta.
- Registros técnicos: 30 días (configurado en AWS CloudWatch).
- Tras la eliminación se conserva una breve marca de eliminación (unas 2 horas) para que una sesión antigua no pueda volver a crear la cuenta.
- Copias de seguridad: en producción, la recuperación a un punto en el tiempo de DynamoDB puede conservar datos eliminados en copias de seguridad hasta por 35 días.

## 6. Tus derechos y cómo eliminar tus datos
Según el GDPR (UE/Reino Unido) y la LGPD (Brasil) puedes solicitar acceder a tus datos, corregirlos, portarlos o eliminarlos, oponerte al tratamiento
y retirar tu consentimiento en cualquier momento. También puedes presentar una queja ante tu autoridad de protección de datos (en Brasil, la ANPD).
Si estás en otro país de Latinoamérica, también puedes contactar a la autoridad de protección de datos de tu país.
- **Elimina todo tú mismo:** en el juego abre Menú -> Eliminar cuenta. Esto elimina de inmediato tu partida, tu vínculo con Google,
  tu registro de inicio de sesión y tus comentarios (backend `DELETE /v1/me`). No se puede deshacer.
- **Otras solicitudes:** escribe a `[CORREO DE PRIVACIDAD]`. Respondemos en un plazo de 30 días. Es posible que necesitemos datos como la hora aproximada en que jugaste o el id de un comentario para
  encontrar tus datos, ya que las cuentas de invitado no tienen nombre ni correo.
- Si vinculaste Google, desvincular o eliminar desde Google no elimina tu partida del juego; usa Eliminar cuenta.

## 7. Seguridad
Los datos se cifran en tránsito (HTTPS) y en reposo (cifrado administrado por AWS). El acceso al backend está limitado al
desarrollador mediante AWS IAM. Ningún sistema es perfectamente seguro; notificaremos a las autoridades y a los jugadores afectados
sobre incidentes de seguridad según lo exija la ley.

## 8. Cambios
Publicaremos los cambios aquí y actualizaremos la fecha indicada arriba. Los cambios importantes se anunciarán en el juego.
