# ISEN ICS Scrapper

Un outil en ligne de commande (CLI) moderne pour télécharger, analyser et visualiser les statistiques de votre emploi du temps ISEN (format ICS).

Il permet de récupérer automatiquement votre calendrier depuis `web.isen-ouest.fr`, de calculer le nombre total d'heures par matière et d'afficher le tout dans un tableau élégant directement dans votre terminal.

## 🚀 Fonctionnalités

- **Téléchargement automatique** de l'emploi du temps via ID étudiant.
- **Calcul des heures** cumulées par matière.
- **Affichage riche** et coloré dans le terminal (grâce à [Rich](https://github.com/Textualize/rich)).
- **Support UTF-8** pour un affichage correct des accents.

## 📋 Prérequis

- Python 3.14 ou supérieur (adaptable selon votre version installée).
- [Poetry](https://python-poetry.org/) pour la gestion des dépendances.

### Installation de Poetry (si nécessaire)

Si vous n'avez pas encore Poetry, installez-le avec la commande suivante :

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

## 🛠️ Installation

1. **Clonez ce dépôt** (ou téléchargez les sources) :

   ```bash
   git clone https://github.com/BreizhHardware/ISEN_ICS_Scrapper
   cd ISEN_ICS_Scrapper
   ```

2. **Installez les dépendances** :

   ```bash
   poetry install
   ```

## 💻 Utilisation

L'outil s'utilise via la commande `isen-ics` suivie de votre ID étudiant (le numéro présent dans le passeport informatique).

### Lancer via Poetry

```bash
poetry run isen-ics <VOTRE_ID_ETUDIANT>
```

**Exemple :**

```bash
poetry run isen-ics 000000
```

### Résultat

Vous obtiendrez un tableau trié par volume horaire décroissant :

```text
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┓
┃ Matière                                      ┃ Heures Totales ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━┩
│ Développement Web S7                         │        30.00 h │
│ Cloud computing                              │        28.50 h │
│ ...                                          │            ... │
├──────────────────────────────────────────────┼────────────────┤
│ TOTAL                                        │       174.50 h │
└──────────────────────────────────────────────┴────────────────┘
```

## 📦 Dépendances principales

- **[Requests](https://requests.readthedocs.io/)** : Pour le téléchargement HTTP.
- **[ICS](https://icspy.readthedocs.io/)** : Pour le parsing du format iCalendar.
- **[Rich](https://rich.readthedocs.io/)** : Pour l'interface terminal (tableaux, barres de progression).
- **[Typer](https://typer.tiangolo.com/)** : Pour la création de l'interface CLI.
