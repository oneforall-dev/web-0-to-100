# Auditoría y gobierno de datos

## Índice

1. Orden de inspección
2. Ficha fuente de verdad
3. Clasificación
4. Auditoría inicial
5. Decisiones y bloqueos

## 1. Orden de inspección

1. Leer `HANDOFF.md`, documentación, configuración y árbol de archivos.
2. Detectar stack, servidor, almacenamiento, autenticación, despliegue y pruebas.
3. Localizar marca, contenido, contactos, legales, analítica e integraciones.
4. Identificar datos heredados de otros clientes y excluirlos.
5. Comprobar estado del repositorio y cambios del usuario antes de editar.

## 2. Ficha fuente de verdad

Mantener `project-brief.yaml` con: proyecto, identidad, audiencia, oferta, conversión, ubicación, confianza, funcionalidades, infraestructura, legal y analítica. Usar `assets/project-brief.template.yaml` y conservar los placeholders hasta recibir un valor.

Cada entrada factual debe incluir o permitir inferir:

- `value`: valor actual;
- `status`: `VERIFICADO`, `INFERIDO`, `SUGERIDO` o `PENDIENTE`;
- `source`: cliente, archivo, URL, integración o análisis;
- `notes`: restricciones o fecha de comprobación.

## 3. Clasificación

- `VERIFICADO`: suministrado por el cliente o confirmado mediante fuente válida.
- `INFERIDO`: deducción razonable que no puede publicarse como hecho.
- `SUGERIDO`: recomendación estratégica o creativa.
- `PENDIENTE`: dato necesario aún ausente.

No inventar testimonios, reseñas, calificaciones, cifras, premios, licencias, clientes, resultados, emails, direcciones, equipo, certificaciones, antigüedad, disponibilidad, precios, promociones ni propiedades de productos. Etiquetar imágenes generadas como conceptuales cuando puedan confundirse con evidencia real.

## 4. Auditoría inicial

Documentar:

- resumen del objetivo comercial;
- datos recibidos, verificados y pendientes;
- supuestos que no deben publicarse;
- audiencia, problema, deseo, objeciones y conocimiento;
- propuesta de valor sugerida;
- objetivo y eventos de conversión;
- mapa de páginas, intención y CTA por página;
- secciones recomendadas con función explícita;
- funciones y límites del CMS;
- arquitectura técnica recomendada;
- riesgos de seguridad, contenido, hosting y operación;
- plan por fases y criterios de aceptación.

## 5. Decisiones y bloqueos

Continuar con placeholders claros ante faltantes no críticos. Detenerse ante:

- credenciales o acceso indispensables;
- riesgo de exponer o destruir datos;
- autorización para producción o DNS;
- cambio irreversible;
- borrado sin respaldo;
- decisión de arquitectura con impacto material no resoluble por el brief.

