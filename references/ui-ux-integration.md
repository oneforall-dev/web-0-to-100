# Integración obligatoria con UI/UX Pro Max

## Momento de activación

Usar `$ui-ux-pro-max` después de completar auditoría, clasificación, audiencia, conversión, arquitectura de contenido, mapa de páginas, stack e identidad disponible. No fijar el diseño visual definitivo antes.

## Consulta dinámica

Construir un prompt específico con:

- tipo de producto e industria;
- superficies reales;
- audiencia, contexto, necesidades, objeciones y accesibilidad;
- objetivo, CTA principal, CTA secundario y confianza verificable;
- logo, colores, tipografías y referencias reales;
- dirección aprobada o solicitud de recomendación;
- stack detectado;
- mobile-first, WCAG, PageSpeed, reducción de movimiento, navegadores y redes lentas.

Modelo:

```text
Usa $ui-ux-pro-max para diseñar el sistema UI/UX de [TIPO] en [NICHO].
Superficies: [LISTA].
Audiencia: [DESCRIPCIÓN CONCRETA].
Objetivo principal: [CONVERSIÓN].
CTA principal: [CTA]. CTA secundario: [CTA].
Identidad disponible: [SOLO DATOS REALES].
Dirección visual: [APROBADA O RECOMENDAR SEGÚN INDUSTRIA Y AUDIENCIA].
Stack: [STACK DETECTADO].
Restricciones: [WCAG, RENDIMIENTO, RESPONSIVE, MOVIMIENTO Y COMPATIBILIDAD].
Genera patrón, estructura, paleta, tipografía, jerarquía, componentes,
estados, efectos, anti-patrones y checklist previo a implementación.
```

No usar adjetivos vacíos como sustituto del contexto. No copiar el ejemplo de private lending: adaptarlo al nicho, mercado, ubicación, páginas, marca, stack y conversión.

## Salida requerida

Crear `DESIGN-SYSTEM.md` con:

1. contexto analizado;
2. patrón, estructura, densidad, navegación y CTAs;
3. dirección visual y justificación;
4. paleta semántica completa;
5. tipografías, pesos, escala, altura y fallbacks;
6. grid, ancho, espacios, breakpoints y tratamientos móvil/escritorio;
7. componentes generales y propios del nicho;
8. estados e interacción, incluido movimiento reducido;
9. anti-patrones específicos;
10. checklist de contraste, foco, teclado, targets, responsive, legibilidad, movimiento, consistencia y rendimiento.

## Revisión obligatoria

Clasificar cada recomendación como `ACEPTADA`, `AJUSTADA`, `RECHAZADA` o `PENDIENTE`, con motivo para las tres últimas. Comparar contra identidad, conversión, funcionalidad, accesibilidad, rendimiento, stack y contenido real.

Convertir las decisiones aceptadas en tokens nativos del stack. No fijar una paleta, fuente, hero, bento, glassmorphism o dark mode universal.

Crear `design/pages/<pagina>.md` solo para diferencias locales; no duplicar el sistema global. En iteraciones, conservar decisiones aprobadas y reevaluar únicamente el ámbito solicitado.

