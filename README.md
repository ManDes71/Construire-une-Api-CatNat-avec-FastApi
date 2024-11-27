# Construire-une-Api-CatNat-avec-FastApi
Voici le texte converti en Markdown, prêt à être utilisé dans un fichier `README.md` pour votre projet GitHub :

```markdown
# Création d'une API avec FastAPI

Ce repository montre la création d’une API à partir du framework Python **FastAPI**.  
L'API interroge des services gouvernementaux français tels que :
- **API Addok** : Recherche d'adresses.
- **API CatNat** : Informations sur les catastrophes naturelles.

---

## Pourquoi FastAPI ?

FastAPI est un choix intéressant pour ses nombreux avantages :

### 1. Performance élevée :
- Offrant des performances proches de celles d'outils comme Node.js et Go.
- Idéal pour des applications nécessitant des réponses rapides, comme les appels API.

#### Starlette :
- Framework léger et asynchrone pour développer des applications web en Python.
- Conçu pour respecter le standard **ASGI** (Asynchronous Server Gateway Interface).
- Garantit des performances et une modularité élevées.

#### Pydantic :
- Bibliothèque Python pour la validation et la gestion des données structurées.
- Basée sur les annotations de type Python.
- Offre une validation automatique des données d'entrée et de sortie.

---

### 2. Documentation automatique :
- La documentation interactive est générée automatiquement à partir des types Python :
  - **OpenAPI** : Spécification standardisée pour décrire des APIs REST.
  - **Swagger UI** : Interface interactive permettant d'explorer et de tester les APIs.
- Accessible via l'endpoint `/docs`.
- Simplifie les tests et l'intégration.

---

### 3. Gestion des données structurées :
- Les modèles basés sur **Pydantic** assurent une validation stricte des entrées et des sorties JSON.

---

### 4. Middleware intégré :
- Par exemple, le middleware **CORS** (Cross-Origin Resource Sharing) est configuré pour permettre l'accès depuis d'autres domaines.

---

## Fonctionnalités de l'API

### 1. Recherche d'adresses avec l'API Addok :
- **Endpoint** : `/api/v1/{adresse}`
- **Description** :
  - Envoie une requête à l'API publique Addok pour rechercher des adresses.
  - Retourne des informations enrichies (latitude, longitude, score, ville, code postal, etc.).
- **Utilisation typique** :
  ```bash
  GET /api/v1/Champs-Élysées
  ```
  - Réponse JSON structurée avec les coordonnées et détails de l'adresse.

---

### 2. Recherche des événements CatNat :
- **Endpoint** : `/api/v1/catnat/`
- **Description** :
  - Interroge l'API Géorisques pour obtenir des informations sur les catastrophes naturelles dans un rayon défini autour d'une position géographique.
  - Retourne une liste d'événements (type, date, gravité, etc.).
- **Utilisation typique** :
  ```bash
  GET /api/v1/catnat/?longitude=2.3522&latitude=48.8566&rayon=1000
  ```
  - Réponse contenant les événements trouvés pour les coordonnées fournies.

---

## Valeur ajoutée de l'API

1. **Centralisation des données** :
   - Accès à des informations variées (adresses, catastrophes naturelles, inondations, risques sismiques, cavités) via une seule API, simplifiant l'intégration des services.

2. **Utilisation des données publiques** :
   - Exploitation simplifiée des données issues des services Géorisques et d'autres APIs gouvernementales.

3. **Adaptabilité et extensibilité** :
   - L'API est conçue pour intégrer facilement d'autres sources de données gouvernementales et ajouter des fonctionnalités au besoin.

---

## Quelques API Gouvernementales Françaises

### 1. API Addok (api-adresse.data.gouv.fr)
- **Objectif** : Fournir une recherche d'adresses et de géocodage à partir de textes.
- **Points forts** :
  - Utilisation facile avec des requêtes simples (`q=adresse`).
  - Précision élevée avec des scores pour évaluer la pertinence.
- **Exemple dans votre code** :
  ```bash
  http://api-adresse.data.gouv.fr/search/?q=adresse
  ```
  - Résultat : Latitude, longitude, ville, code postal, pertinence, etc.

---

### 2. API CatNat (Géorisques - Ministère de la Transition écologique)
- **Objectif** : Fournir des informations sur les zones à risque et les événements de catastrophes naturelles.
- **Fonctionnalité exploitée** :
  - Recherche par coordonnées géographiques et rayon de recherche.
- **Exemple dans votre code** :
  ```bash
  https://georisques.gouv.fr/api/v1/gaspar/catnat?longitude=2.3522&latitude=48.8566&rayon=1000
  ```
  - Résultat : Liste des événements correspondant à une zone géographique donnée.

---

### 3. API AZI (Aléa Zones Inondables)
- **Objectif** : Fournir des informations sur les zones présentant un risque d’inondation.
- **Exemple dans votre code** :
  ```bash
  https://georisques.gouv.fr/api/v1/azi
  ```
  - Résultat : Aléa inondation, classe de risque, et détails par parcelle.

---

### 4. API Zonage Sismique
- **Objectif** : Fournir des informations sur la classification sismique des zones en France.
- **Exemple dans votre code** :
  ```bash
  https://georisques.gouv.fr/api/v1/zonage-sismique
  ```
  - Résultat : Niveau de sismicité et description du zonage.

---

### 5. API Cavités
- **Objectif** : Recenser les cavités souterraines (naturelles ou anthropiques) pouvant présenter un risque pour la stabilité des sols.
- **Exemple dans votre code** :
  ```bash
  https://georisques.gouv.fr/api/v1/cavites
  ```
  - Résultat : Liste des cavités recensées dans la zone, avec détails sur leur nature, origine, et risque associé.

---

## Licence
Ce projet est sous licence [MIT](LICENSE).
```

Vous pouvez copier ce contenu dans un fichier nommé `README.md`. Il est structuré pour une utilisation directe sur GitHub avec des sections bien distinctes et des exemples formatés.
