# QA, staging y producción

## Matriz de evidencia

Registrar por prueba: nombre, resultado (`APROBADA`, `FALLIDA`, `PARCIAL`), evidencia, fecha, responsable, corrección y estado final.

## Website público

Probar carga, navegación, enlaces, anclas, menú móvil, formularios, CTAs, teléfono, WhatsApp, email, agenda/compra, imágenes, video, legales, 404, sitemap, robots, canonical y Schema.

## Responsive y accesibilidad

Probar 360, 390, 768, 1024, 1440 y 1920 px. Revisar navegación, formularios, tablas, medios, tarjetas, CMS, editor, blog y modales. Validar teclado, foco, lector de pantalla o árbol accesible, labels, contraste, encabezados, alt y errores.

## CMS y autenticación

Probar login correcto/incorrecto, rate limit, cambio de contraseña, rechazo de la anterior, aceptación de la nueva, logout, sesión compartida, protección privada, edición, enlaces, orden, visibilidad, borrado permitido, borrador, descarte, preview, publicación, persistencia, backup y restore.

## Blog

Probar CRUD, borrador/publicación, lectura, slug y colisión, 301, importación TXT/HTML, sanitización, restauración, navegación, URL limpia y canonical.

## Seguridad

Probar rechazo o sanitización de `<script>`, handlers inline, `javascript:`, HTML peligroso, MIME/extensiones falsos, payload excesivo, falta de sesión/CSRF, acceso a datos/backups, traversal y URLs inseguras. Verificar headers y cookies en el entorno real.

## Rendimiento

Ejecutar Lighthouse/PageSpeed en staging, corregir lo controlable y repetir. No inventar resultados. Documentar limitaciones de terceros.

## Staging

Respaldar destino; publicar aislado; configurar SSL, backend, permisos, correo y `noindex`; probar autenticación, CMS, blog, publicación, backups/restauración, formularios, analítica, responsive y rendimiento; obtener aprobación.

## Producción

Exigir autorización explícita. Confirmar dominio, SSL, backup, rollback, contraseña temporal cambiada, variables, protección, correo, canonical, sitemap, robots, analítica, formularios e integraciones. Después: limpiar caché, probar HTTP/redirecciones/rutas públicas y privadas/login/CMS/blog/formularios/contacto/analítica, revisar logs y probar incógnito + móvil.

## Aceptación

Completar solo cuando contenido, responsive, accesibilidad, separación público/privado, autenticación, recuperación, CMS, persistencia, blog, sanitización, respaldos, enlaces, formularios, SEO, rendimiento medido, staging, producción, documentación y rollback hayan sido comprobados o explícitamente marcados como pendientes bloqueantes.

