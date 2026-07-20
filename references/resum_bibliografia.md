# Síntesi bibliogràfica — idees principals

## Models que apareixen repetidament

- Els models basats en arbres (_tree-based methods_) apareixen de manera recurrent en la literatura revisada.
- Random Forest i XGBoost són tècniques de _machine learning_ que construeixen múltiples arbres de decisió i combinen els seus resultats.
- Els models no lineals solen capturar millor relacions complexes entre característiques i preu que les regressions tradicionals.
- Les regressions lineals apareixen habitualment com a model base de comparació.
- Alguns treballs incorporen models espacials, és a dir, models que consideren explícitament dependència geogràfica entre observacions

Exemples:

- GWR (_Geographically Weighted Regression_);
- SAR (_Spatial Autoregressive Model_);
- SDM (_Spatial Durbin Model_).

La idea és que allotjaments geogràficament pròxims poden presentar comportaments similars.

- La validació creuada apareix de forma recurrent per avaluar estabilitat i capacitat de generalització.

---

## Variables importants que apareixen repetidament

- La localització és una de les variables més importants en la determinació dels preus Airbnb.
    
- Les coordenades geogràfiques poden presentar una elevada capacitat explicativa.
    
- Les característiques estructurals de l'allotjament apareixen repetidament:
    
    - nombre d'habitacions;
        
    - nombre de banys;
        
    - nombre de llits;
        
    - capacitat màxima.
        
- Les característiques del propietari també poden influir:
    
    - Superhost;
        
    - temps de resposta;
        
    - nombre d'anuncis;
        
    - activitat del propietari.
        
- Les valoracions i reputació poden afectar el preu.
    
- Els serveis disponibles (_amenities_) apareixen freqüentment entre les variables importants.
    

---

## Tècniques d'interpretabilitat observades

- La interpretabilitat no és exclusiva dels models lineals.
    
- Els models lineals són fàcilment interpretables perquè els coeficients tenen significat directe.
    
- En models de _machine learning_ apareixen altres tècniques:
    
    - Feature Importance;
        
    - SHAP (_SHapley Additive exPlanations_);
        
    - LIME (_Local Interpretable Model-Agnostic Explanations_);
        
    - PDP (_Partial Dependence Plot_);
        
    - ICE plots (_Individual Conditional Expectation_).
        
- SHAP permet quantificar la contribució de cada variable a una predicció concreta.
    
- PDP mostra com varia la predicció segons una variable mantenint la resta controlades.
    
- Feature Importance permet ordenar variables segons la seva influència global.
    
- Els models espacials poden generar mapes que mostren variació geogràfica dels efectes.
    

---

## Idees de feature engineering

- La construcció de variables geogràfiques externes apareix freqüentment.
    
- Les distàncies a punts d'interès són habituals:
    
    - centre urbà;
        
    - transport;
        
    - atraccions;
        
    - serveis.
        
- La distància geomètrica simple no sempre representa adequadament l'accessibilitat real.
    

Exemple:

Dos allotjaments poden estar molt pròxims en línia recta però molt separats per carretera.

Variables potencials:

$$
road\_distance  
$$

$$
travel\_time  
$$

- Diversos treballs suggereixen que la combinació entre proximitat i popularitat genera variables més informatives.
    

Exemple:

$$
BeachIndex_i =

\sum_j  
\frac{Popularity_j}{d_{ij}}  
$$

Una platja molt pròxima i molt popular aporta més pes que una platja pròxima però poc atractiva.

- Els índexs espacials compostos consisteixen a combinar diverses variables geogràfiques en una única mesura.

Exemple:

$$
TourismIndex =

0.4\cdot BeachScore  
+  
0.3\cdot RestaurantScore  
+  
0.3\cdot AccessibilityScore  
$$

- Les variables agregades apareixen repetidament:
    

Índex de serveis:

$$
AmenityIndex =

Wifi+Pool+Parking+AC  
$$

Índex de mida:

$$
SizeIndex = 

Bedrooms+Bathrooms+Beds  
$$

Índex d'accessibilitat:

$$
AccessibilityIndex =

f(  
d_{centre},  
d_{airport},  
d_{transport}  
)  
$$

- Les transformacions no lineals i les interaccions entre variables també poden augmentar la capacitat predictiva.
    

---

## Idees que puc incorporar al meu TFM

- Incorporar variables geogràfiques específiques més enllà de les variables originals.
    
- Construir:
    
    - distància al mar;
        
    - distància a Palma;
        
    - distància a platges;
        
    - distància a punts d'interès.
        
- Estudiar si una distància per carretera aporta millors resultats que una distància geomètrica.
    
- Explorar la construcció d'índexs espacials compostos.
    
- Comparar regressions tradicionals amb models de _machine learning_.
    
- Utilitzar Random Forest i XGBoost com a models principals.
    
- Analitzar possibles relacions no lineals entre localització i preu.
    
- Utilitzar tècniques d'interpretabilitat per justificar els resultats dels models.
    
- Estudiar el paper específic de les variables geogràfiques en la capacitat predictiva final.
    

---

## Conclusions generals

- Diversos treballs observen que la localització és una de les principals fonts de variació dels preus Airbnb.
    
- Diversos treballs indiquen que les variables geogràfiques poden augmentar significativament la capacitat predictiva.
    
- Diversos treballs mostren que els models no lineals solen superar models lineals tradicionals.
    
- La literatura revisada suggereix que la construcció de noves variables pot ser tan important com l'elecció del model predictiu.