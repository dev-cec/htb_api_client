# Client API HTB

Une bibliothèque Python permettant d'accéder à l'API de [HackTheBox (HTB)](https://www.hackthebox.com). Cette bibliothèque fournit une interface Python propre vers l'API REST de HTB, organisée autour de deux entités principales : les **Universités** et les **Utilisateurs**.

## Prérequis

- Python >= 3.14
- `requests` >= 2.34.2
- `python-dotenv` >= 1.2.2

## Installation

```bash
pip install python-dotenv requests
```

## Démarrage rapide

```python
import os
from dotenv import load_dotenv
from htb_api_client import HTBAPIClient

load_dotenv()

client = HTBAPIClient(api_key=os.getenv("HTB_API_KEY"))

# Récupérer les universités
universites = client.get_universities(per_page=10, page=1)

# Récupérer le profil d'un utilisateur
utilisateur = client.get_user_basic_profile(user_id=1812190)
```

## Authentification

Ce client utilise l'authentification par **Bearer token**. Définissez votre clé API dans un fichier `.env` :

```
HTB_API_KEY=votre_cle_api_ici
```

Un modèle de configuration est disponible dans `.env.example`.

---

# Endpoints de l'API

## Endpoints des Universités

### `GET /v5/universities` — `get_universities(per_page=15, page=1)`

Récupère une liste paginée des universités présentes sur HackTheBox.

| Paramètre     | Type   | Requis | Défaut | Description                              |
|---------------|--------|--------|--------|------------------------------------------|
| `per_page`    | `int`  | Non    | `15`   | Nombre d'universités retournées par page |
| `page`        | `int`  | Non    | `1`    | Numéro de la page à récupérer            |

**Retourne :** Un `dict` contenant la liste des universités dans la clé `data`, ainsi que les métadonnées de pagination.

```python
reponse = client.get_universities(per_page=10, page=1)
```

---

### `GET /v4/university/my` — `get_my_university()`

Récupère l'université associée à l'utilisateur actuellement authentifié.

**Paramètres :** Aucun.

**Retourne :** Un `dict` contenant les données de l'université de l'utilisateur connecté.

```python
reponse = client.get_my_university()
```

---

### `GET /v4/university/profile/{university_id}` — `get_university_profile(university_id)`

Récupère le profil complet d'une université à partir de son identifiant.

| Paramètre         | Type   | Requis | Défaut | Description          |
|-------------------|--------|--------|--------|----------------------|
| `university_id`   | `int`  | Oui    | —      | Identifiant de l'université |

**Retourne :** Un `dict` contenant les données de profil de l'université.

```python
reponse = client.get_university_profile(university_id=1306)
```

---

### `GET /v5/universities/{university_id}/stats` — `get_university_stats(university_id)`

Récupère les statistiques d'une université spécifique.

| Paramètre         | Type   | Requis | Défaut | Description          |
|-------------------|--------|--------|--------|----------------------|
| `university_id`   | `int`  | Oui    | —      | Identifiant de l'université |

**Retourne :** Un `dict` contenant les statistiques de l'université.

```python
reponse = client.get_university_stats(university_id=1306)
```

---

### `GET /v4/university/members/{university_id}` — `get_university_members(university_id)`

Récupère la liste des membres appartenant à une université spécifique.

| Paramètre         | Type   | Requis | Défaut | Description          |
|-------------------|--------|--------|--------|----------------------|
| `university_id`   | `int`  | Oui    | —      | Identifiant de l'université |

**Retourne :** Une `list[dict]` d'objets membres, ou une liste vide si aucun membre n'est trouvé.

```python
reponse = client.get_university_members(university_id=1306)
```

---

### `GET /v4/university/invitations/{university_id}` — `get_university_invitations(university_id)`

Récupère les invitations en attente pour une université spécifique.

| Paramètre         | Type   | Requis | Défaut | Description          |
|-------------------|--------|--------|--------|----------------------|
| `university_id`   | `int`  | Oui    | —      | Identifiant de l'université |

**Retourne :** Un `dict` contenant les données des invitations.

```python
reponse = client.get_university_invitations(university_id=1306)
```

---

## Endpoints des Utilisateurs

### `GET /v4/user/profile/basic/{user_id}` — `get_user_basic_profile(user_id)`

Récupère le profil de base d'un utilisateur.

| Paramètre     | Type   | Requis | Défaut | Description                |
|---------------|--------|--------|--------|----------------------------|
| `user_id`     | `int`  | Oui    | —      | Identifiant unique de l'utilisateur |

**Retourne :** Un `dict` contenant les informations de base du profil utilisateur.

```python
reponse = client.get_user_basic_profile(user_id=1812190)
```

---

### `GET /experience/v1/account/{account_uuid}` — `get_user_experience(account_uuid)`

Récupère les données d'expérience d'un utilisateur identifié par son UUID de compte.

| Paramètre         | Type  | Requis | Défaut | Description                          |
|-------------------|-------|--------|--------|--------------------------------------|
| `account_uuid`    | `str` | Oui    | —      | UUID du compte de l'utilisateur      |

**Retourne :** Un `dict` contenant les données d'expérience de l'utilisateur.

```python
reponse = client.get_user_experience(account_uuid="9bc206ad-e5ef-4a4d-a0dc-7b32b5db5e9e")
```

---

### `GET /v4/badges` — `get_badges()`

Récupère l'ensemble des badges disponibles sur HackTheBox.

**Paramètres :** Aucun.

**Retourne :** Un `dict` contenant les catégories de badges et les badges associés à chacune d'elles.

```python
reponse = client.get_badges()
```

---

### `GET /v4/season/user/{user_id}/ranks` — `get_user_season_ranks(user_id)`

Récupère les classements saisonniers d'un utilisateur.

| Paramètre     | Type   | Requis | Défaut | Description                |
|---------------|--------|--------|--------|----------------------------|
| `user_id`     | `int`  | Oui    | —      | Identifiant unique de l'utilisateur |

**Retourne :** Un `dict` contenant les données de classement saisonnier de l'utilisateur.

```python
reponse = client.get_user_season_ranks(user_id=1812190)
```

---

### `GET /v4/user/profile/progress/{progress_type}/{user_id}` — `get_user_progress(user_id, progress_type)`

Récupère la progression d'un utilisateur dans un type de contenu HTB spécifique.

| Paramètre         | Type   | Requis | Défaut | Description                                                  |
|-------------------|--------|--------|--------|--------------------------------------------------------------|
| `user_id`         | `int`  | Oui    | —      | Identifiant unique de l'utilisateur                          |
| `progress_type`   | `str`  | Oui    | —      | L'un des suivants : `machines`, `challenges`, `sherlocks`, `prolab`, `fortress` |

**Retourne :** Un `dict` contenant la progression de l'utilisateur pour le type de contenu indiqué.

```python
reponse = client.get_user_progress(user_id=1812190, progress_type="machines")
reponse = client.get_user_progress(user_id=1812190, progress_type="sherlocks")
```

---

### `GET /v4/users/{user_id}/profile/progress/chart` — `get_user_progress_chart(user_id, duration, content_type)`

Récupère les données de graphique permettant de visualiser la progression d'un utilisateur sur une période donnée.

| Paramètre         | Type       | Requis | Défaut          | Description                                                              |
|-------------------|------------|--------|-----------------|--------------------------------------------------------------------------|
| `user_id`         | `int`      | Oui    | —               | Identifiant unique de l'utilisateur                                      |
| `duration`        | `str`      | Non    | `"1M"`          | Période couverte par le graphique (ex. `1M` pour 1 mois, `1Y` pour 1 an) |
| `content_type`    | `str`      | Non    | `"machines"`    | Type de contenu à représenter (ex. `machines`, `challenges`)             |

**Retourne :** Un `dict` contenant les points de données du graphique.

```python
reponse = client.get_user_progress_chart(
    user_id=1812190,
    duration="1M",
    content_type="machines",
)
```

---

### `GET /v5/user/profile/activity/{user_id}` — `get_user_activity(user_id, per_page=5)`

Récupère le fil d'activité récent d'un utilisateur sur HackTheBox.

| Paramètre     | Type   | Requis | Défaut | Description                                  |
|---------------|--------|--------|--------|----------------------------------------------|
| `user_id`     | `int`  | Oui    | —      | Identifiant unique de l'utilisateur           |
| `per_page`    | `int`  | Non    | `5`    | Nombre d'éléments d'activité par page        |

**Retourne :** Un `dict` contenant les éléments d'activité récents de l'utilisateur.

```python
reponse = client.get_user_activity(user_id=1812190, per_page=10)
```

---

### `GET /v4/user/profile/badges/{user_id}` — `get_user_badges(user_id, rare=None)`

Récupère les badges gagnés par un utilisateur.

| Paramètre         | Type          | Requis | Défaut | Description                                                  |
|-------------------|---------------|--------|--------|--------------------------------------------------------------|
| `user_id`         | `int`         | Oui    | —      | Identifiant unique de l'utilisateur                          |
| `rare`            | `int \| None` | Non    | `None` | Filtrer les résultats par niveau de rareté (optionnel)       |

**Retourne :** Un `dict` contenant les données des badges de l'utilisateur.

```python
reponse = client.get_user_badges(user_id=1812190)
reponse = client.get_user_badges(user_id=1812190, rare=8)
```

---

### `GET /v5/user/profile/content/{user_id}/counts` — `get_user_content_counts(user_id)`

Récupère le décompte des différents types de contenu associés à un utilisateur (machines, challenges, sherlocks, writeups).

| Paramètre     | Type   | Requis | Défaut | Description                |
|---------------|--------|--------|--------|----------------------------|
| `user_id`     | `int`  | Oui    | —      | Identifiant unique de l'utilisateur |

**Retourne :** Un `dict` contenant les décomptes par catégorie de contenu.

```python
reponse = client.get_user_content_counts(user_id=1812190)
```

---

## Exécuter l'exemple

Une démonstration complète d'utilisation est disponible dans `pprint_example.py` :

```bash
# Définissez d'abord votre clé API
echo "HTB_API_KEY=votre_cle" > .env

# Exécuter l'exemple
python pprint_example.py
```

Ce script appelle chaque méthode de `HTBAPIClient` et affiche joliment les réponses JSON dans la console.
