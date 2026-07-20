# TFM — Flujo de trabajo con Claude Cowork

## Estructura del directorio

```
tfm/
├── brainstorming/       # Sesiones de brainstorming (exportadas de Cowork)
├── context/             # Documentos de contexto que subes a Claude antes de pedir ayuda
│   └── tfm_context.md   # ← Actualiza este fichero conforme evolucione el TFM
├── notes/               # Notas de reuniones (txt, md o pdf)
├── references/          # PDFs de artículos y libros
├── latex/
│   ├── chapters/        # Un .tex por capítulo
│   ├── figures/         # Imágenes y diagramas
│   └── bibliography/    # .bib
├── code/
│   ├── src/             # Módulos Python reutilizables
│   ├── notebooks/       # Jupyter notebooks de exploración
│   └── data/            # Datasets (no subir binarios grandes a git)
└── outputs/             # Ficheros generados por Claude (borradores, tablas, etc.)
```

---

## Flujo de trabajo con Claude Cowork

### 1. Reuniones con el tutor
1. Toma notas durante la reunión (formato libre: voz → texto, bullet points, etc.)
2. Guarda el fichero en `notes/` con nombre `YYYY-MM-DD_reunion.md`
3. Abre Cowork y pide:
   > "Procesa las notas de hoy en `notes/YYYY-MM-DD_reunion.md`: extrae tareas pendientes, decisiones tomadas y actualiza `context/tfm_context.md`"

### 2. Mantener el contexto actualizado
El fichero `context/tfm_context.md` es el **cerebro del proyecto**: título provisional, objetivo, metodología, estado actual, próximas tareas. Actualízalo tras cada reunión. Al empezar una sesión de trabajo larga, díselo a Claude:
> "Lee `context/tfm_context.md` y tenlo en cuenta para esta sesión"

### 3. Escritura en LaTeX
- Pide borradores de secciones en prosa y luego conviértelos a LaTeX.
- Para figuras y tablas: proporciona los datos y pide el código TikZ / tabular.

### 4. Código Python
- Sube notebooks o scripts a `code/` y pide revisión, refactorización o depuración.
- Para análisis de datos: pega el CSV pequeño en el chat o referencia la ruta.

### 5. Gestión bibliográfica
- Guarda los PDFs en `references/`.
- Pide a Claude que genere entradas `.bib` a partir del PDF o DOI.

### 6. Brainstorming
- Usa Cowork para sesiones de ideación; exporta el resultado a `brainstorming/YYYY-MM-DD_tema.md`.

---

## Skills útiles en Cowork

| Tarea | Skill |
|---|---|
| Generar documento Word para el tutor | `docx` |
| Leer/extraer tablas de PDFs de artículos | `pdf` |
| Crear Excel con resultados experimentales | `xlsx` |
| Presentación para defensa | `pptx` |

---

## Convenciones de nombrado

| Tipo | Formato |
|---|---|
| Notas de reunión | `notes/YYYY-MM-DD_reunion.md` |
| Brainstorming | `brainstorming/YYYY-MM-DD_tema.md` |
| Capítulos LaTeX | `latex/chapters/XX_nombre.tex` |
| Notebooks | `code/notebooks/YYYY-MM-DD_experimento.ipynb` |

---

## Estat del projecte

- Tema aprovat (2026-06-17): predicció de preu d'allotjaments Airbnb a Mallorca.
- Estat global i decisions: `context/tfm_context.md`.
- Pla de treball i cronograma (fites de juliol i setembre): `context/pla_treball.md`.
- Actes de reunions: `notes/`.

## Propers passos immediats

- [ ] Revisió bibliogràfica → registrar a `references/bibliografia.md`.
- [ ] Comprensió i neteja de les dades (`code/data/`).
- [ ] Enginyeria de variables (distància al mar).
- [ ] **Correu de progrés als tutors (~15 juliol).**
- [ ] **Correu de convocatòria (principis de setembre).**
- [ ] Crear `latex/main.tex` amb l'estructura base del TFM.
