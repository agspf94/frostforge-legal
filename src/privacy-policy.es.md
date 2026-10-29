# Español (Latinoamérica)

**Última actualización:** `[FECHA]`

## 1. Quién somos
"Frostforge" (nombre provisional) es un juego para celular para Android (Google Play) e iOS (App Store; TestFlight durante las pruebas).
El responsable del tratamiento de los datos es `[NOMBRE LEGAL DEL RESPONSABLE]`.
Contacto para solicitudes de privacidad: `[CORREO DE PRIVACIDAD]`. El juego es para mayores de 16 años.

## 2. Qué recopilamos y por qué
| Dato | Cuándo | Finalidad | Base legal (GDPR/LGPD) |
|---|---|---|---|
| Identificador de la cuenta (id de usuario de Amazon Cognito creado al iniciar sesión por primera vez con Google o Apple) | En tu primer inicio de sesión | Identificar tu progreso para que puedas jugar en cualquier dispositivo | Ejecución de contrato (proveer el juego) |
| Estado del juego: base, recursos, investigación, héroes, tropas, avance del tutorial, posición y marchas en el mapa mundial, marcas de tiempo, tus elecciones de diseño del HUD | Mientras juegas | Ejecutar el juego en nuestro servidor (el servidor es la autoridad) | Ejecución de contrato |
| Sesión de juego: un id de sesión aleatorio, la plataforma (Android, iOS o web) y la hora de inicio del dispositivo en el que juegas | Al abrir el juego | Mantener un solo dispositivo activo por cuenta, para que dos dispositivos nunca se sobrescriban | Ejecución de contrato |
| Identificador de la cuenta de Google o Apple (sin correo, nombre ni perfil; alcance de inicio de sesión solo `openid`) | Al iniciar sesión | Iniciar tu sesión y darte el mismo progreso en otro dispositivo o plataforma | Ejecución de contrato (iniciar sesión es necesario para jugar) |
| Token de integridad del dispositivo (Google Play Integrity) | Cuando una cuenta nueva abre su base por primera vez en Android | Bloquear clientes falsos y abuso | Interés legítimo (seguridad, antitrampas) |
| Registros técnicos: pueden incluir la dirección IP tal como la procesa AWS, hora de la solicitud, endpoint, estado, id de usuario | En cada solicitud | Seguridad, depuración, control de costos | Interés legítimo |
| Comentarios que envías desde el menú: tu texto, tu id de usuario, hora, versión de la app, plataforma, idioma | Al enviar comentarios | Leer y responder tus comentarios | Consentimiento |
| Solicitudes de soporte: el texto que escribes, las respuestas de nuestro equipo, tus respuestas posteriores, un código de soporte, tu id de usuario, hora, versión de la app, plataforma, idioma | Al enviar una solicitud de soporte o una respuesta | Responder tu solicitud. Ninguna otra finalidad | Consentimiento |
| Imágenes que adjuntas a una solicitud de soporte (hasta 3 por solicitud; la app las reduce y las vuelve a codificar en tu dispositivo, lo que elimina los datos de ubicación y de la cámara) | Al adjuntarlas | Entender y responder tu solicitud. Cada imagen se revisa automáticamente para detectar contenido inapropiado. Ninguna otra finalidad | Consentimiento |
| Estadísticas de uso, solo si tocas "Permitir" (se puede cambiar en el menú): por día, conteos de eventos como pasos del tutorial, sesiones, tiempo de juego, nivel más alto del Núcleo, primera investigación/reclutamiento/expedición y un código corto que identifica un error de script; con tu id de usuario, versión de la app y plataforma | Mientras juegas, después de que lo permitas | Entender dónde se traban los jugadores y cuántos regresan | Consentimiento |

**No** vendemos tus datos, no mostramos anuncios de terceros y no los usamos para elaborar perfiles. No recopilamos
a sabiendas datos de menores de 16 años.

Las estadísticas de uso se guardan como totales diarios por jugador (no un registro por acción), no contienen texto libre,
id de publicidad ni id del dispositivo, y no se envía nada hasta que eliges "Permitir". El juego no tiene un SDK de
informes de fallos. Los informes de fallos nativos provienen de Google Play (Android vitals) en Android y, en iPhone, de
Apple, solo si elegiste compartir análisis con los desarrolladores de apps en los ajustes del dispositivo (o enviar un informe de fallo desde TestFlight).

Las notificaciones las programa el propio juego en tu dispositivo; ningún servicio de notificaciones push recibe tus datos.

Las versiones de prueba (canales de prueba de Google Play y TestFlight) que usan nuestro servidor de pruebas también guardan
el correo de la cuenta de Google o Apple con la que inicias sesión, solo para reconocer a los testers registrados. El juego público nunca lo pide.

**Planificado (aún no se recopila):**

- Compras dentro de la app (Google Play en Android, App Store en iPhone; hoy no se puede comprar nada). Cuando empiecen,
  Google o Apple se encargan del pago y nosotros recibimos y conservamos un registro de cada compra: tienda, producto, id del
  pedido o de la transacción, lo que se acreditó en tu cuenta y los reembolsos. Nunca recibimos los datos de tu tarjeta o de pago.
  Antes de que se abran las compras, esta política indicará cuánto tiempo se conservan esos registros.
- Apple App Attest en iPhone, la misma verificación única que Play Integrity en Android cuando una cuenta nueva abre su base por primera vez.

## 3. Quién recibe tus datos
- **Amazon Web Services** (alojamiento, base de datos, registros, inicio de sesión mediante Amazon Cognito, almacenamiento privado de las imágenes de las solicitudes de soporte y su moderación automática mediante Amazon Rekognition). Encargado del tratamiento.
- **Google** (Iniciar sesión con Google; Play Integrity en Android; Google Play para distribución, actualizaciones dentro de la app y, cuando empiecen, pagos).
- **Apple** (Iniciar sesión con Apple; App Store y TestFlight para distribución en iPhone y, cuando empiecen, pagos).
- **GitHub, Inc.** (Estados Unidos), proveedor de servicios que aloja nuestro sistema de seguimiento de solicitudes. El texto de tus solicitudes de soporte y respuestas, y tu código de soporte, se procesan allí solo para atender tu solicitud. No se usan para ninguna otra finalidad. Encargado del tratamiento.
- **Anthropic, PBC** (Estados Unidos), proveedora de las herramientas de IA que ayudan a nuestro equipo a leer, clasificar y redactar respuestas a las solicitudes de soporte. Recibe el contenido de las solicitudes de soporte, incluidas las imágenes adjuntas, solo para esa finalidad. Encargado del tratamiento.
- Las imágenes de las solicitudes de soporte nunca se publican en GitHub.
- **Otros jugadores** del mismo mapa mundial ven la posición de tu base, tus marchas y los nodos de recursos que ocupas,
  con un código que no es el id de tu cuenta. No se muestra ningún nombre, correo ni identificador de Google/Apple.
- Nadie más. Podemos divulgar datos si la ley lo exige.

## 4. Dónde se almacenan los datos
Región de Amazon Web Services **us-east-2 (Ohio, EE. UU.)**. Si estás fuera de EE. UU., tus datos se transfieren allí;
nos basamos en las cláusulas contractuales tipo y los términos de protección de datos de AWS para las transferencias desde la UE, el Reino Unido y Brasil.
Las solicitudes de soporte también las almacena **GitHub, Inc.** en **EE. UU.** Para esa transferencia nos basamos en el Acuerdo de Protección
de Datos de GitHub, que incluye las cláusulas contractuales tipo (GDPR Capítulo V; LGPD art. 33). Las herramientas de IA de
**Anthropic, PBC** (sección 3) procesan el contenido de las solicitudes de soporte en EE. UU. con la misma base (términos de procesamiento de datos de Anthropic con cláusulas contractuales tipo).

## 5. Cuánto tiempo los conservamos
- Estado del juego y cuenta: hasta que la cuenta se elimine de forma permanente (30 días después de que la elimines).
- Mensajes de comentarios: se eliminan automáticamente después de 180 días (o cuando la cuenta se elimina de forma permanente, 30 días después de que la elimines).
- Solicitudes de soporte en la base de datos de nuestro juego (tu texto, nuestras respuestas y las tuyas, que se muestran en la pantalla de Soporte): se eliminan
  automáticamente 180 días después de la última actualización de la solicitud (o cuando la cuenta se elimina de forma permanente, 30 días después de que la elimines).
- Solicitudes de soporte en GitHub (donde nuestro equipo las atiende): una vez cerrada una solicitud, los comentarios que contienen el texto que escribiste se eliminan
  automáticamente unos 180 días después de su última actualización (o cuando la cuenta se elimina de forma permanente, 30 días después de que la elimines: normalmente de inmediato,
  como máximo en aproximadamente un día, y la solicitud se cierra). Lo que queda en GitHub es un registro cerrado de la solicitud sin ningún
  texto tuyo: tu código de soporte, la categoría de la solicitud, versión de la app, plataforma e idioma, además de las respuestas de nuestro equipo
  y las notas internas sobre la solicitud.
- Imágenes adjuntas a una solicitud de soporte: se eliminan en cuanto se cierra la solicitud (por ti o por nuestro equipo) y,
  en cualquier caso, a más tardar 30 días después de enviarlas, también cuando se elimina tu cuenta.
- Estadísticas de uso: se eliminan automáticamente después de 120 días (o cuando la cuenta se elimina de forma permanente, 30 días después de que la elimines); el registro de tu
  elección (Permitir / No, gracias) y el día en que elegiste por primera vez se conservan hasta la eliminación permanente de la cuenta.
- Registros técnicos: 30 días (configurado en AWS CloudWatch).
- Cuando eliminas tu cuenta, queda desactivada durante 30 días (tus datos se conservan, congelados y fuera del juego, para que puedas restaurarla si fue un error o lo hizo otra persona). Pasados 30 días, todo se elimina automáticamente.
- Un breve marcador de eliminación (unas 2 horas) permanece después de la eliminación permanente para que una sesión antigua no pueda recrear la cuenta.
- Copias de seguridad: en producción, la recuperación a un punto en el tiempo de DynamoDB puede conservar datos eliminados en copias de seguridad hasta 35 días después de la eliminación permanente.

## 6. Tus derechos y cómo eliminar tus datos
Según el GDPR (UE/Reino Unido) y la LGPD (Brasil) puedes solicitar acceso, rectificación, portabilidad o eliminación de tus datos, oponerte al tratamiento
y retirar tu consentimiento en cualquier momento. También puedes presentar una queja ante tu autoridad de protección de datos (en Brasil, la ANPD).

- **Elimina todo por tu cuenta:** en el juego abre Menú -> Legal -> Eliminar cuenta. Desactiva tu cuenta de inmediato y elimina de forma
  permanente tu progreso, tu vínculo con Google/Apple, tu registro de inicio de sesión, tus comentarios y tus solicitudes de
  soporte (y los comentarios de GitHub que contienen el texto de tus solicitudes de soporte) 30 días después, automáticamente.
  Inicia sesión de nuevo dentro de los 30 días y toca Restaurar para cancelar. Después no se puede deshacer. Un registro cerrado de la solicitud sin tu texto permanece en GitHub (ver sección 5).
  Si tu cuenta usa Iniciar sesión con Apple, también le pedimos a Apple que revoque el acceso del juego a tu cuenta de Apple.
- **¿Sin la app instalada?** Abre `[URL DE ELIMINACIÓN DE CUENTA]`, inicia sesión con la misma cuenta de Google o Apple y solicita la eliminación (o la restauración) allí. Funciona igual (30 días, luego definitiva).
- **Solicitudes de acceso, rectificación o portabilidad:** escribe a `[CORREO DE PRIVACIDAD]`. Respondemos en un plazo de 30 días. Es posible que necesitemos datos como tu código de soporte (se muestra en la pantalla de Soporte), la hora aproximada de juego o el id de un comentario para
  encontrar tus datos, ya que las cuentas no tienen nombre ni correo. No necesitas escribirnos para eliminar tus datos.
- Quitar el acceso del juego en los ajustes de tu cuenta de Google o Apple, o eliminar esa cuenta de Google o Apple, no elimina el progreso del juego; usa Eliminar cuenta (ventana de 30 días arriba).
- Tu cuenta es tu inicio de sesión de Google o Apple: en un dispositivo nuevo, inicia sesión con la misma cuenta para recuperar tu progreso.
- **Vincular Google y Apple:** en Ajustes puedes vincular ambos a una sola cuenta del juego. Si el otro inicio de sesión ya
  tiene su propia base, eliges qué cuenta conservar; el progreso no se puede combinar. La cuenta que no conservaste se
  desactiva y se elimina de forma permanente 30 días después, como con Eliminar cuenta. Si elegiste la equivocada,
  escribe a `[CORREO DE PRIVACIDAD]` antes de ese plazo.

## 7. Seguridad
Los datos se cifran en tránsito (HTTPS) y en reposo (cifrado administrado por AWS). El acceso al backend está limitado al
desarrollador mediante AWS IAM. Ningún sistema es perfectamente seguro; notificaremos a las autoridades y a los jugadores afectados
de las brechas según lo exija la ley.

## 8. Cambios
Publicaremos los cambios aquí y actualizaremos la fecha de arriba. Los cambios importantes se anunciarán en el juego.
