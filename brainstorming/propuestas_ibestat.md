
# Dades de l'IBESTAT

**Fonts de dades:**

- `dataset-IBESTAT_000060A_000004`: Establiments i places turístiques per municipi (mensual, 2008–2026)
- `dataset-IBESTAT_000060A_000006`: Grau d'ocupació dels allotjaments turístics per municipi (mensual, 2008–2025)

**Àmbit geogràfic:** 15 municipis de les Illes Balears (Alcúdia, Calvià, Palma, Pollença, Santanyí, Eivissa, Formentera, entre d'altres)  
**Font:** Institut d'Estadística de les Illes Balears (IBESTAT) — ibestat.es

---

## Predicció de l'Ocupació en el Sector Turístic de les Illes Balears (2008–2025)

### Objectiu principal

Modelitzar i predir el grau d'ocupació dels allotjaments turístics de les Illes Balears, capturant patrons estacionals, tendències i l'efecte de factors externs.
### Dades utilitzades

- **Dataset 2** (grau d'ocupació, mensual 2008–2025): variables `GRADO_OCUPACION_APARTAMENTO_TURISTICO`, `GRADO_OCUPACION_PLAZA_TURISTICA` i les seves variants de cap de setmana, per a 15 municipis.
- **Dataset 1** (establiments i places, mensual 2008–2026): `ESTABLECIMIENTO_TURISTICO`, `APARTAMENTO_TURISTICO`, `PLAZA_TURISTICA`, utilitzades com a variables explicatives de la capacitat instal·lada.

### Metodologia

1. **Preprocessament**: consolidació de les sèries mensuals i anuals, tractament de valors absents i de baixa fiabilitat, i construcció de les sèries per municipi i agregades.
2. **Anàlisi exploratòria**: descomposició STL (tendència, estacionalitat i residu), detecció de canvis i visualització de l'impacte de la COVID-19.
3. **Modelització clàssica**
4. **Modelització avançada**
5. **Avaluació**: MAE, RMSE i MAPE per a horitzons de predicció de 3, 6 i 12 mesos. Comparació del rendiment dels models per municipi.
6. **Anàlisi de la recuperació post-COVID**: quantificació del temps necessari per retornar als nivells previs a la pandèmia en cada municipi.

### Aportació i valor

- Eina de previsió per a gestors de destinació i administracions públiques de les Illes Balears.
- Quantificació de l'impacte econòmic dels factors externs sobre el sector turístic.
- Base metodològica per comparar el comportament del sector turístic reglat amb el de les plataformes digitals d'allotjament.

---

## Anàlisi Territorial de la Capacitat i l'Ocupació Turística a les Illes Balears: Patrons, Desequilibris i Factors Explicatius

### Objectiu principal

Analitzar l'evolució i els patrons territorials de la capacitat turística (establiments i places) i de l'ocupació als municipis de les Illes Balears, identificar grups de comportament i modelitzar el grau d'ocupació.

### Dades utilitzades

- **Dataset 1** (establiments i places, mensual 2008–2026): evolució de la capacitat turística per municipi, utilitzada com a variable independent principal.
- **Dataset 2** (grau d'ocupació, mensual 2008–2025): variable dependent, amb informació sobre ocupació per apartaments i per places, tant en dies feiners com en caps de setmana.
- Variables derivades: taxa de creixement de places, índexs d'estacionalitat per municipi (coeficient de variació mensual) i ràtio entre apartaments i establiments.

### Metodologia

1. **Preprocessament i enginyeria de característiques**: construcció d'indicadors municipals agregats anuals i mensuals; càlcul de taxes de variació, índexs d'estacionalitat i ràtios de composició de l'oferta.
2. **Anàlisi de clústers**: agrupació dels municipis segons el seu perfil d'ocupació i capacitat (K-Means i agrupament jeràrquic), amb estudi de l'evolució temporal dels grups.
3. **Anàlisi de components principals (PCA)**: reducció dimensional per identificar les dimensions latents que expliquen la variabilitat entre municipis.
4. **Modelització predictiva**: Random Forest i XGBoost per predir el grau d'ocupació a partir de variables de capacitat, estacionalitat i tendència temporal.
5. **Visualització territorial**: mapes amb l'evolució de la capacitat i de l'ocupació per municipi i any.

### Aportació

- Diagnòstic territorial del sector turístic de les Illes Balears.
- Identificació de municipis amb risc de saturació.
- Eina de suport per al disseny de polítiques de planificació turística sostenible.

---

_Dades: Institut d'Estadística de les Illes Balears (IBESTAT). Datasets 000060A_000004 i 000060A_000006._