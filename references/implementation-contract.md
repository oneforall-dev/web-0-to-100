# Contrato de implementación comercial

## Conversión y contenido

Definir visitante, problema, oferta, objeciones, información previa a la acción, CTA principal, secundarios, confianza y eventos. Cada sección debe explicar, diferenciar, demostrar, responder objeciones, generar confianza, facilitar decisión o conducir al CTA.

Redactar copy claro, específico, creíble, escaneable y alineado con nivel de conciencia, SEO, GEO y AEO. El hero debe comunicar oferta, audiencia, beneficio y acción en segundos. Usar CTAs descriptivos; evitar “Enviar”, “Más” o “Clic aquí”.

Cada página requiere propósito, intención, CTA, H1/H2 coherentes, title, description, canonical, Open Graph y Schema aplicable con datos reales.

## Sitio público y responsive

- Diseñar composiciones reales para móvil y escritorio.
- Verificar 360, 390, 768, 1024, 1440 y 1920 px sin scroll horizontal.
- Usar HTML semántico, labels, foco visible, teclado, contraste, alt text y ARIA solo cuando aporte.
- Targets táctiles de al menos 44 px y soporte para `prefers-reduced-motion`.
- Si hay video hero: `muted`, `playsinline`, loop justificado, poster, compresión, carga diferida y fallback móvil/red lenta.

## SEO, GEO, AEO y agentic readiness

Implementar URLs limpias, canonical, robots, sitemap, OG, Twitter Cards, favicon, 404, redirecciones, breadcrumbs cuando procedan, enlaces internos y slugs estables. Usar Schema verificable (`Organization`, `LocalBusiness`, `Service`, `Product`, `Article`, `BlogPosting`, `BreadcrumbList`, `FAQPage` visible o `Person` real).

Estructurar respuestas directas, entidades consistentes, definiciones, listas y tablas útiles. Mantener contenido principal disponible sin depender totalmente de JavaScript. No exponer APIs privadas ni credenciales.

## Formularios, contacto y analítica

Validar cliente y servidor; minimizar campos; incluir carga, éxito, error, antispam y consentimiento. No registrar secretos ni datos innecesarios. Construir `https://wa.me/CODIGOPAISNUMERO`, `tel:` y `mailto:` correctamente.

Configurar analítica solo con autorización. Evitar duplicados y documentar plataforma, ID, eventos, parámetros, consentimiento, responsable y validación. Medir CTA principal, WhatsApp, teléfono, email, formulario, agenda, compra, servicio, artículo y conversión aplicables.

## Rendimiento

Usar AVIF/WebP, dimensiones, `srcset`, compresión, lazy loading bajo el fold y prioridad solo para el recurso LCP. Reducir JS, CSS bloqueante, fuentes/pesos y librerías; diferir scripts, cachear y comprimir.

Medir Lighthouse/PageSpeed en staging. Registrar puntuación, LCP, CLS, INP, TBT cuando aplique, hallazgos, correcciones y limitaciones. No afirmar métricas no medidas.

## Arquitectura de referencia

Separar sitio público, assets, `/cms/`, `/blog/`, legales, rutas, datos y respaldos. Adaptar al stack y hosting detectados. Bloquear datos, backups, configuración, logs, temporales y secretos en Apache, Nginx o servidor equivalente.

