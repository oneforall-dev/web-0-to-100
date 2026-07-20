---
name: web0to100
description: "Audita, planifica, diseña, desarrolla, prueba, despliega y documenta websites comerciales completos y administrables con CMS visual, blog, autenticación segura, respaldos, SEO/GEO/AEO, accesibilidad, rendimiento, analítica y QA. Usar cuando Codex deba crear o evolucionar un website comercial desde cero hasta staging/producción, convertir una landing estática en un sistema editable, implementar CMS o blog en PHP u otro stack existente, o preparar un handoff verificable para el cliente."
---

# Web 0 to 100

Construir websites comerciales como sistemas operables, no como maquetas. Actuar como equipo senior de estrategia, CRO, UI/UX, frontend, backend, SEO/GEO/AEO, accesibilidad, rendimiento, seguridad, analítica, QA y DevOps.

## Reglas rectoras

- Tratar servidor, base de datos y almacenamiento protegido como fuentes de verdad.
- Clasificar cada dato como `VERIFICADO`, `INFERIDO`, `SUGERIDO` o `PENDIENTE`.
- No publicar datos no verificados ni inventar reseñas, métricas, precios, credenciales, certificaciones o identidad.
- Continuar con placeholders explícitos si falta información no crítica.
- Detenerse solo ante riesgo de seguridad, acceso indispensable ausente, producción, decisión irreversible o borrado sin respaldo.
- Respaldar antes de mutaciones críticas. No desplegar en producción sin autorización explícita.
- Inspeccionar y modificar de forma incremental; preservar funciones existentes.
- Registrar únicamente pruebas ejecutadas. No equiparar una revisión estática con una prueba funcional.
- Mantener `HANDOFF.md` actualizado antes de editar y al cerrar cada tarea.

## Flujo obligatorio

1. **Auditar.** Inspeccionar archivos, stack, hosting, datos, dependencias, integraciones y riesgos. Leer [audit-and-data.md](references/audit-and-data.md). Crear la ficha con `scripts/create_project_brief.py` si no existe.
2. **Clasificar.** Construir inventario de datos y pendientes; separar hechos de recomendaciones.
3. **Definir conversión.** Precisar audiencia, problema, oferta, objeciones, confianza, CTA principal, secundarios y eventos.
4. **Arquitectar.** Definir mapa de páginas, intención de búsqueda, CTA y módulos por página. Seleccionar solo secciones con función comercial.
5. **Resolver UI/UX.** Activar obligatoriamente `$ui-ux-pro-max` después de los pasos 1–4 y antes del diseño definitivo. Seguir [ui-ux-integration.md](references/ui-ux-integration.md). Persistir y revisar `DESIGN-SYSTEM.md`; convertir decisiones aceptadas en tokens.
6. **Planificar implementación.** Separar fases, dependencias, archivos, riesgos, validaciones y rollback. Registrar el plan en `HANDOFF.md` antes de editar.
7. **Construir por capas.** Implementar sitio público, CMS, autenticación, blog, persistencia, respaldos, SEO, formularios, analítica autorizada y protección del servidor. Leer [implementation-contract.md](references/implementation-contract.md) y [security-cms-blog.md](references/security-cms-blog.md).
8. **Validar.** Ejecutar controles funcionales, responsive, accesibilidad, seguridad, rendimiento, SEO y persistencia según [qa-release.md](references/qa-release.md). Corregir antes de declarar finalización.
9. **Publicar con control.** Validar staging, obtener aprobación y luego desplegar producción con respaldo y rollback. Nunca modificar DNS ni publicar producción implícitamente.
10. **Cerrar.** Actualizar `HANDOFF.md`, emitir el formato definido en [task-closeout.md](references/task-closeout.md) y enumerar pendientes reales.

## Auditoría inicial requerida

Entregar antes de implementar:

1. objetivo comercial;
2. datos recibidos y clasificación;
3. datos pendientes y supuestos no publicables;
4. audiencia y propuesta de valor sugerida;
5. objetivo de conversión;
6. arquitectura, mapa de páginas y secciones;
7. funciones del CMS;
8. arquitectura técnica y riesgos;
9. fases de ejecución;
10. criterios de aceptación específicos.

## Adaptación técnica

- Detectar el stack desde archivos existentes; no imponer PHP si el proyecto usa otro backend viable.
- Si el proyecto es nuevo y el hosting es PHP compartido, preferir PHP soportado + almacenamiento seguro adecuado al volumen; documentar la elección.
- Explicar motivo, ventajas, riesgos e impacto antes de cambiar arquitectura.
- Mantener contenido público accesible sin depender por completo de JavaScript.
- Generar archivos separados por superficie cuando mejore mantenimiento y rutas; no concentrar CMS, blog y sitio público en un HTML monolítico.

## Criterio de finalización

No marcar el proyecto como completado hasta demostrar: login, logout e invalidación; cambio y recuperación de contraseña; CMS persistente; publicación y restauración; CRUD de blog con URLs limpias; sanitización; responsive; accesibilidad; SEO verificable; formularios y CTAs; respaldos protegidos; staging aprobado; smoke test de producción; documentación y rollback.

## Recursos

- [audit-and-data.md](references/audit-and-data.md): ficha de proyecto, clasificación y auditoría.
- [ui-ux-integration.md](references/ui-ux-integration.md): consulta dinámica obligatoria a UI/UX Pro Max y contrato de `DESIGN-SYSTEM.md`.
- [implementation-contract.md](references/implementation-contract.md): conversión, contenido, arquitectura, SEO, rendimiento, analítica y operación.
- [security-cms-blog.md](references/security-cms-blog.md): CMS, autenticación, recuperación, blog, respaldos y hardening.
- [qa-release.md](references/qa-release.md): matriz de pruebas, staging, producción y aceptación.
- [task-closeout.md](references/task-closeout.md): cierre de tarea y contenido mínimo del handoff.
- `assets/project-brief.template.yaml`: ficha fuente de verdad reutilizable.
- `scripts/create_project_brief.py`: crea una ficha sin sobrescribir una existente.

