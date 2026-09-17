# Pla de treball i cronograma — TFM

**Última actualització:** 2026-06-17
**Horitzó:** juny – setembre de 2026

---

## Fites principals

| Fita | Data límit | Lliurament |
|---|---|---|
| **F1 — Correu de progrés** | ~15 de juliol de 2026 | Correu als tutors amb la bibliografia trobada + progrés de l'EDA descriptiu i la neteja de dades (servirà per elaborar el cronograma conjunt). |
| **F2 — Correu de convocatòria** | Principis de setembre (a partir de l'1) | Correu de convocatòria de la propera reunió, explicant el que s'ha aconseguit durant l'estiu. |
| **R — Propera reunió** | Setembre de 2026 | Reunió de seguiment (data concreta a fixar via correu). |

---

## Blocs de treball

### B1 — Revisió bibliogràfica
Cercar treballs similars, acadèmics o divulgatius, sobre predicció de preus d'allotjaments (Airbnb i similars), interpretabilitat de models i *feature engineering* geogràfic.
- [x] Cerca i recopilació de referències.
- [x] Lectura i fitxa breu de cada referència rellevant.
- [x] Desar PDFs a `references/` i registrar-los a `references/bibliografia.md`.

### B2 — Comprensió de les dades
- [x] Inventari de variables de `listings.csv` (tipus, valors, mancances).
- [x] Revisar `calendar.csv` i `reviews.csv` (rol secundari/auxiliar).
- [x] Documentar la variable objectiu `price` i el seu format.

### B3 — Neteja de dades (*data cleaning*)
- [x] Neteja del preu (format, moneda, *outliers*).
- [x] Tractament de valors mancants.
- [x] Codificació de variables categòriques.

### B4 — Enginyeria de variables (*feature engineering*)
- [ ] **Distància al mar:** mapejar la línia de costa de Mallorca i calcular la distància de cada allotjament (lat/lon) al mar.
- [ ] Altres variables derivades segons l'EDA.

### B5 — Anàlisi exploratòria i descriptiva (EDA)
- [ ] Estadística descriptiva i distribucions.
- [ ] Relacions entre variables explicatives i preu.
- [ ] Visualitzacions clau (taules i figures per al correu F1).

> **Nota:** la modelització, la interpretabilitat i el simulador són blocs posteriors (després de setembre) i no formen part de les fites d'aquest pla.

---

## Cronograma orientatiu

```
Juny (2a quinzena)   B1 (inici) · B2
Juliol (1a quinzena) B3 · B4 (distància al mar) · B5  →  F1 (~15 jul: correu de progrés)
Juliol–Agost         Consolidar EDA · ampliar B1 · preparar modelització
Setembre (inici)     F2 (correu de convocatòria) → Reunió
```

---

## Seguiment de fites

- [ ] **F1** — Correu de progrés enviat (~15 juliol).
- [ ] **F2** — Correu de convocatòria enviat (principis setembre).
- [ ] **R** — Data de la propera reunió fixada.
