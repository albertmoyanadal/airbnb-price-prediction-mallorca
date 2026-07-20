
**Dades:** InsideAirbnb — Mallorca (setembre de 2025)  
**Llicència:** Creative Commons Attribution 4.0 International  
**Font:** 
- [insideairbnb.com](https://insideairbnb.com/)
- [Mallorca](https://insideairbnb.com/mallorca/)

# Predicció de preus en el mercat del lloguer vacacional: aplicació a Mallorca mitjançant tècniques d'Intel·ligència Artificial

### Objectiu principal

Construir un model predictiu del preu dels allotjaments d'Airbnb a Mallorca i interpretar-ne els factors determinants.

### Dades utilitzades

- `listings.csv` (56.656 registres): 
	- variable objectiu `price`
	- variables explicatives: `neighbourhood_cleansed`, `room_type`, `accommodates`, `bedrooms`, `beds`, `amenities`, `host_is_superhost`, `host_response_rate`, `review_scores_*`, `latitude`, `longitude`, `instant_bookable`, entre d'altres.
### Metodologia

1. **Preprocessament**: neteja de preus, codificació de variables categòriques i anàlisi exploratori.
2. **Modelització**:  proposar un model per resoldre.

### Aportació i valor de negoci

- Eina de _pricing_ per a amfitrions: quant hauria de cobrar pel meu allotjament?
- Anàlisi de mercat per a inversors: quines característiques generen un major retorn?

---
# Predicció de la demanda en allotjaments turístics de Mallorca

### Objectiu principal

Modelitzar i predir la taxa d'ocupació dels allotjaments de Mallorca a nivell de listing, zona i destinació, capturant patrons estacionals i tendències.
### Dades utilitzades

- `calendar.csv` (5.487.410 registres): columnes `date`, `available`, `price` — ocupació diària per listing durant 365 dies.
- `listings.csv`: `estimated_occupancy_l365d`, `estimated_revenue_l365d` com a variables objectiu alternatives; segmentació geogràfica i tipològica.
### Metodologia

1. **Construcció de sèries**: taxa d'ocupació diària o setmanal per listing, municipi i tipus d'allotjament.
2. **Anàlisi exploratòria**: descomposició STL, detecció d'estacionalitat múltiple (setmana, mes, temporada).
3. **Modelització clàssica**: SARIMA per exemple
4. **Modelització avançada**: models més potents.
5. **Avaluació**: MAE, RMSE, MAPE en horitzons de predicció de 30, 60 i 90 dies.
6. **Segmentació**: comparació de patrons per municipi (Palma vs. zones rurals vs. costa).

### Aportació

- Revenue management per a amfitrions: optimització de tarifes segons la demanda prevista.
- Planificació per a gestors de destinació i administració pública.
- Anàlisi de l'impacte postpandèmia i comparativa interanual.

---
# Anàlisi de Sentiment de Ressenyes i Impacte en el Preu i la Demanda

### Objectiu principal

Extreure senyals de satisfacció a partir de les ressenyes en text lliure, identificar temes recurrents i analitzar-ne l'impacte sobre el preu i la demanda dels allotjaments.
### Dades utilitzades

- `reviews.csv` (398.782 ressenyes): columna `comments` — text lliure multilingüe.
- `listings.csv`: `price`, `review_scores_rating`, `estimated_occupancy_l365d`, `number_of_reviews` — variables de resultat.

### Metodologia

1. **Preprocessament NLP**: detecció d'idioma, traducció automàtica (els comentaris són majoritàriament en anglès, alemany i espanyol), neteja de text.
2. **Anàlisi de sentiment**: models preentrenats tipus VADER i ajust fi (_fine-tuning_) de models transformer (BERT/RoBERTa) per a classificació positiva, negativa i neutra.
3. **Modelització de temes**: LDA i BERTopic per identificar dimensions latents (neteja, ubicació, comunicació, relació qualitat-preu).
4. **Anàlisi d'impacte**: regressió entre puntuacions de sentiment o temes i preu o ocupació; diferenciació per tipus d'allotjament i zona.
5. **Evolució temporal**: anàlisi del canvi de sentiment entre temporades.

### Aportació i valor de negoci

- Indicadors de reputació accionables per a amfitrions.
- Benchmarking competitiu basat en la percepció dels usuaris.
- Senyals primerenques de deteriorament de la qualitat percebuda.

---

_Dades: InsideAirbnb (insideairbnb.com). Llicència CC BY 4.0. Instantània: 21 de setembre de 2025._
