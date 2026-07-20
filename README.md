# web0to100

`web0to100` es una skill para construir y evolucionar websites comerciales completos: desde la auditoría inicial y la estrategia de conversión hasta el CMS, el blog, la seguridad, las pruebas, staging, producción y el handoff al cliente.

Su objetivo no es generar una landing aislada, sino entregar un sistema administrable que el cliente pueda operar sin editar código.

## Qué resuelve

- Estrategia comercial y CRO.
- Arquitectura de información y copy orientado a conversión.
- Sistema UI/UX específico para cada negocio.
- Website público responsive.
- CMS visual autenticado.
- Blog público y gestor de artículos.
- Login, logout, cambio y recuperación de contraseña.
- Persistencia, respaldos y restauración.
- SEO técnico, GEO, AEO y preparación para agentes.
- Accesibilidad y rendimiento.
- Formularios, contacto y analítica autorizada.
- QA técnico, staging, producción y rollback.
- Documentación operativa en `HANDOFF.md`.

## Principios fundamentales

1. No inventar datos comerciales, testimonios, métricas, precios, reseñas, certificaciones ni identidad.
2. Clasificar la información como `VERIFICADO`, `INFERIDO`, `SUGERIDO` o `PENDIENTE`.
3. Mantener secretos, hashes, tokens y credenciales fuera del frontend y del repositorio.
4. Respaldar antes de cambios críticos.
5. No desplegar en producción ni modificar DNS sin autorización explícita.
6. No declarar una prueba como aprobada si no fue ejecutada.
7. Mantener el handoff actualizado antes y después de cada tarea.

## Estructura

```text
web0to100/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── project-brief.template.yaml
├── references/
│   ├── audit-and-data.md
│   ├── implementation-contract.md
│   ├── qa-release.md
│   ├── security-cms-blog.md
│   ├── task-closeout.md
│   └── ui-ux-integration.md
└── scripts/
    └── create_project_brief.py
```

`SKILL.md` contiene el flujo rector. Las reglas extensas están separadas en `references/` para cargarse solo cuando son necesarias.

## Uso

Invocación recomendada:

```text
$web0to100 audita este proyecto y construye el website comercial completo usando únicamente información verificable.
```

Otros ejemplos:

```text
$web0to100 convierte esta landing estática en un website administrable con CMS, blog y autenticación segura.
```

```text
$web0to100 revisa este website antes de staging: seguridad, accesibilidad, SEO, rendimiento, CMS, blog y respaldos.
```

```text
$web0to100 implementa únicamente el gestor de artículos y conserva la arquitectura existente.
```

La petición puede ser breve. La skill auditará el proyecto, identificará faltantes y continuará con placeholders explícitos cuando el dato ausente no sea crítico.

## Flujo de trabajo

1. Auditar archivos, stack, hosting, integraciones y estado actual.
2. Crear o actualizar la ficha fuente de verdad.
3. Clasificar datos y registrar pendientes.
4. Definir audiencia, oferta, objeciones, conversión y eventos.
5. Diseñar el mapa de páginas y la función de cada sección.
6. Consultar `ui-ux-pro-max` con un prompt dinámico del proyecto.
7. Revisar las recomendaciones y crear `DESIGN-SYSTEM.md`.
8. Convertir decisiones aprobadas en tokens del stack.
9. Implementar por capas, preservando funciones existentes.
10. Ejecutar QA y corregir resultados fallidos.
11. Validar staging y solicitar autorización antes de producción.
12. Cerrar la tarea y actualizar `HANDOFF.md`.

## Ficha de proyecto

La plantilla está en:

```text
assets/project-brief.template.yaml
```

Para crear `project-brief.yaml` dentro de un proyecto:

```powershell
py -3 .\web0to100\scripts\create_project_brief.py .
```

El script no sobrescribe una ficha existente. Si `project-brief.yaml` ya existe, termina sin modificarla.

La ficha cubre:

- identidad y marca;
- audiencia;
- oferta;
- conversión y contacto;
- ubicación;
- confianza y reseñas;
- funciones requeridas;
- infraestructura;
- legales y analítica.

Cada dato factual debe conservar su estado y fuente. Un valor pendiente nunca debe presentarse públicamente como real.

## Integración con UI/UX Pro Max

La skill requiere `$ui-ux-pro-max` antes del diseño visual definitivo. La consulta se construye con el nicho, mercado, ubicación, audiencia, superficies, conversión, marca, stack y restricciones reales del proyecto.

El resultado debe quedar documentado en `DESIGN-SYSTEM.md` y cada recomendación se clasifica como:

- `ACEPTADA`;
- `AJUSTADA`;
- `RECHAZADA`;
- `PENDIENTE`.

No se reutiliza automáticamente la paleta, tipografía, hero o patrón visual de otro cliente.

## Resultados esperados

Según el proyecto, la entrega puede incluir:

```text
/
├── website público
├── assets/
├── cms/
├── blog/
├── legal/
├── project-brief.yaml
├── DESIGN-SYSTEM.md
├── HANDOFF.md
├── robots.txt
└── sitemap.xml
```

La arquitectura real se adapta al stack y hosting detectados. No se impone PHP cuando el proyecto ya usa otro backend viable.

## Condiciones de detención

La skill continúa de forma autónoma con decisiones técnicas menores. Se detiene cuando:

- existe un riesgo de seguridad;
- falta una credencial o acceso indispensable;
- se necesita autorización para producción o DNS;
- la decisión es irreversible;
- una acción puede borrar datos sin respaldo.

## Criterio de finalización

Un proyecto no se considera terminado solo porque el sitio se vea bien. Deben comprobarse, cuando formen parte del alcance:

- navegación móvil y escritorio;
- formularios y CTAs;
- autenticación y revocación de sesión;
- cambio y recuperación de contraseña;
- edición y publicación desde el CMS;
- persistencia tras reinicio;
- CRUD del blog y URLs limpias;
- sanitización del contenido editable;
- respaldos protegidos y restauración;
- accesibilidad;
- SEO técnico y Schema verificable;
- rendimiento medido en staging;
- smoke test de producción;
- rollback y documentación del cliente.

## Ubicación actual

```text
C:\Users\agaval\AppData\Roaming\Open Design\namespaces\release-stable-win\data\projects\a609da17-ab65-44a6-9637-985aff97a0da\web0to100
```

Esta copia está guardada dentro del proyecto. Para que aparezca como skill personal disponible en otros proyectos, debe instalarse o copiarse posteriormente al directorio personal de skills de Codex.

## Estado de validación

- Estructura y referencias internas comprobadas.
- Script de creación de ficha compilado y probado.
- Protección contra sobrescritura comprobada.
- Frontmatter y metadatos comprobados mediante validación equivalente.
- El validador oficial requiere PyYAML, que no estaba disponible durante la creación inicial.

