# Context del TFM

**Última actualització:** 2026-06-17

## Títol provisional
Predicció del preu d'allotjaments turístics a Mallorca a partir de les seves característiques mitjançant tècniques d'Intel·ligència Artificial.

## Màster
Màster Universitari en Anàlisi de Dades i Intel·ligència de Negoci.

## Tutors
- Miquel Miró
- Biel Moyà

## Objectiu principal
Construir un model capaç d'estimar el preu de mercat esperat d'un allotjament turístic de Mallorca a partir de les seves característiques, interpretar quins factors determinen el preu i oferir un simulador "what-if" per explorar com varia el preu en modificar atributs.

## Metodologia prevista
1. **Comprensió de les dades** — exploració de variables, tipus i estructura.
2. **Neteja de dades (*data cleaning*)** — depuració del preu i de les variables explicatives.
3. **Enginyeria de variables (*feature engineering*)** — creació de noves variables (p. ex. distància al mar a partir de coordenades).
4. **Anàlisi exploratòria i descriptiva (EDA).**
5. **Modelització predictiva** — models d'IA per estimar el preu.
6. **Interpretabilitat** — contribució de cada característica al preu i pes relatiu dels atributs.
7. **Simulador "what-if"** — espai de simulacions sobre allotjaments concrets.

## Dades
- **Font:** Inside Airbnb (insideairbnb.com / Mallorca).
- **Llicència:** CC BY 4.0.
- **Ubicació:** `code/data/` (`listings.csv`, `calendar.csv`, `reviews.csv`).
- Variable objectiu: `price`. Variables explicatives candidates: `neighbourhood_cleansed`, `room_type`, `accommodates`, `bedrooms`, `beds`, `bathrooms`, `amenities`, `host_is_superhost`, `review_scores_*`, `latitude`, `longitude`, `instant_bookable`, entre d'altres.
- *Nota:* a `code/data/` també hi ha CSV d'IBESTAT d'una proposta anterior descartada; no s'utilitzen en aquest projecte.

## Estat actual
- [x] Brainstorming inicial
- [x] Proposta aprovada pel tutor
- [x] Revisió bibliogràfica
- [ ] Comprensió i neteja de dades
- [ ] Enginyeria de variables
- [ ] Anàlisi exploratòria (EDA)
- [ ] Marc teòric
- [ ] Modelització
- [ ] Interpretabilitat i simulador
- [ ] Experiments / resultats
- [ ] Redacció del document
- [ ] Defensa

## Decisions preses
- **2026-06-03:** Es decideix preparar propostes de tema (brainstorming) separades en bloc analític i bloc predictiu; prioritat a la disponibilitat de dades.
- **2026-06-17:** S'aprova el tema (predicció de preu d'allotjaments Airbnb a Mallorca). S'acorden tres línies: model predictiu, interpretabilitat i simulador "what-if". Dades: Inside Airbnb.

## Tasques pendents (resum)
> Detall i calendari complet a [`pla_treball.md`](pla_treball.md).
- Revisió bibliogràfica (treballs acadèmics i divulgatius).
- Comprensió i neteja de les dades.
- Enginyeria de variables, en especial *distància al mar*.
- **~15 juliol:** correu de progrés (bibliografia + EDA + neteja) per elaborar el cronograma.
- **Principis de setembre:** correu de convocatòria de la propera reunió.

## Notes addicionals
- Notes de reunions a `notes/` (`2026-06-03_reunion.md`, `2026-06-17_reunion.md`).
- Propostes valorades a `brainstorming/proposal_airbnb.md`.
