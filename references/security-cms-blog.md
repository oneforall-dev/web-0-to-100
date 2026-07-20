# Seguridad, CMS, autenticación, blog y respaldos

## Seguridad base

- No colocar secretos, contraseñas, hashes o tokens en frontend, URL, repositorio o `localStorage`.
- Exigir sesión en toda escritura y CSRF en toda mutación sensible.
- Usar hash de contraseñas soportado, comparación segura, cookie `HttpOnly`, `SameSite` y `Secure` en producción.
- Regenerar sesión tras login; invalidarla en logout y recuperación.
- Sanitizar HTML editable en servidor; validar método, origen, formato, protocolo, MIME, tamaño y rutas.
- Aplicar rate limiting y espera progresiva con errores genéricos.
- Configurar CSP, `X-Content-Type-Options`, `Referrer-Policy`, anti-framing, HTTPS, permisos mínimos y listado de directorios desactivado.
- Responder `401`, `403`, `422`, `429` y `500` según el caso sin revelar rutas internas.

## CMS visual `/cms/`

Permitir login/logout, cambio/recuperación, carga publicada, edición de texto/imágenes/enlaces/botones/contactos/formularios, target de enlaces, previsualización, visibilidad, orden, restauración de orden, borrado permitido, duplicación compatible, borrador, descarte, preview, publicación, descarga y restauración.

Los enlaces externos nuevos deben usar nueva pestaña por defecto con `noopener noreferrer`, salvo decisión explícita. Antes de publicar, retirar atributos internos del editor.

Proteger estructura, navegación, scripts, estilos críticos, formularios, analítica, Schema, seguridad y metadatos. En módulos externos verificados, limitar el CMS a mostrar/ocultar, cantidad, estilo autorizado, orden o eliminación; nunca editar ratings o reseñas manualmente.

## Autenticación y recuperación

Compartir sesión entre CMS y gestor del blog. Implementar estado, login, logout, cambio, recuperación y revocación.

Con SMTP: respuesta genérica, token criptográfico, almacenar solo hash, vencimiento corto, un solo uso, rate limit, enlace HTTPS, nueva contraseña y revocación de sesiones. Sin SMTP: documentar soporte, verificación de identidad y procedimiento administrativo en servidor; nunca usar contraseña maestra.

## Blog

Crear `/blog/`, `/blog/{slug}/` y gestor autenticado (ruta adaptable, preferentemente `/blog/create/`). Incluir listado, imagen, título, extracto, autor real cuando aplique, fecha, categorías, paginación, artículo, enlaces internos, CTA, SEO, OG, Schema y canonical.

El gestor debe crear, listar, buscar, filtrar, editar, duplicar, previsualizar, publicar, pasar a borrador, cambiar slug, borrar, restaurar e importar TXT/HTML controlado.

Modelo mínimo: `id`, `title`, `slug`, `excerpt`, `contentHtml`, `featuredImage`, `imageAlt`, `status`, `category`, `author`, `createdAt`, `updatedAt`, `seoTitle`, `seoDescription`, `canonical`, `imageSource`. Sanitizar en servidor. Al cambiar slug publicado: detectar colisión, registrar anterior, actualizar referencias y servir 301.

## Respaldos y persistencia

Respaldar antes de publicar, reemplazar, borrar, cambiar slug/configuración/credenciales o editar contenido crítico. Usar timestamp, retención, almacenamiento protegido, escritura atómica, validación, restauración y registro de actor/fecha/resultado.

Demostrar persistencia después de logout, cierre del navegador, nuevo login y reinicio del servidor.

