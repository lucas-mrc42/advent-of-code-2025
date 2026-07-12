# 🎄 Advent of Code 2025 — Projet Collectif

> Résolvez les défis de l'Avent of Code 2025 en groupe et apprenez Git et GitHub en même temps !

---

## 📖 Introduction

### Qu'est-ce que l'Advent of Code ?

**Advent of Code** est un calendrier de l'Avent numérique : chaque jour du 1er au 25 décembre, un nouveau défi de programmation est publié. Ces défis sont conçus pour être progressifs — du plus simple au plus difficile — et sont accessibles même aux débutants.

**Ce projet** est un dépôt GitHub collectif où les étudiants en L1 partagent leurs solutions, apprennent à collaborer avec Git, et découvrent la magie du travail collaboratif sur du code.

---

## 🔧 Prérequis

Avant de commencer, assure-toi d'avoir installé les outils suivants :

| Outil | Version minimale | Comment l'obtenir |
|-------|-----------------|-------------------|
| **Python** | 3.10+ | [python.org/downloads](https://python.org/downloads) |
| **Git** | 2.30+ | [git-scm.com](https://git-scm.com) |
| **Un éditeur de code** | — | VS Code, PyCharm, ou autre |

### Vérifier ton installation

Ouvre un terminal et tape :

```bash
# Vérifier Python
python3 --version

# Vérifier Git
git --version
```

---

## 🚀 Installation

### 1. Clone le dépôt sur ta machine

```bash
git clone https://github.com/ton-username/advent-of-code-2025.git
cd advent-of-code-2025
```

> **Note** : Remplace `ton-username` par le nom d'utilisateur GitHub du propriétaire du dépôt.

### 2. Crée un environnement virtuel (recommandé)

```bash
# Créer l'environnement
python3 -m venv .venv

# L'activer (Linux/Mac)
source .venv/bin/activate

# L'activer (Windows)
.venv\Scripts\activate
```

### 3. Installe les dépendances (si présentes)

```bash
pip install -r requirements.txt
```

---

## 📂 Structure du projet

```
advent-of-code-2025/
├── .gitignore         # Fichiers à ignorer par Git
├── LICENSE            # Licence du projet
├── README.md          # Ce fichier
├── CONTRIBUTING.md    # Guide pour contribuer
└── solutions/         # Dossier contenant les solutions
    └── jour_01.py     # Exemple : solution du jour 1
```

---

## 🧩 Utilisation

### Exécuter une solution

Chaque solution est un fichier Python. Pour l'exécuter :

```bash
# Depuis la racine du projet
python3 solutions/jour_01.py
```

### Mode de pensée

1. **Lis l'énoncé** du défi sur [adventofcode.com/2025](https://adventofcode.com/2025)
2. **Comprends le problème** — note les exemples et cas limites
3. **Écris ta solution** dans un fichier `jour_XX.py`
4. **Teste** avec les données d'exemple puis avec les vraies données
5. **Pousse** ta solution sur le dépôt (voir section Contribution)

---

## 📚 Apprendre Git et GitHub

### Concepts clés

- **Repository (Dépôt)** : Le dossier qui contient ton projet et son historique
- **Commit** : Un instantané de tes modifications à un moment donné
- **Branch (Branche)** : Une version parallèle du projet
- **Push / Pull** : Envoyer ou recevoir des modifications depuis GitHub
- **Pull Request** : Proposition de fusionner tes modifications dans le projet principal

### Commandes Git essentielles

```bash
# Voir l'état de tes fichiers
git status

# Ajouter des fichiers à valider
git add fichier.py

# Valider les changements (créer un commit)
git commit -m "Description claire de ce que tu as fait"

# Pousser vers GitHub
git push origin main

# Récupérer les changements des autres
git pull origin main
```

### Tutoriel interactif

Pour apprendre Git de manière visuelle : [Learn Git Branching](https://learngitbranching.js.org/)

---

## 🤝 Contribution

### Comment contribuer une solution

1. **Fork** le dépôt en cliquant sur le bouton "Fork" sur GitHub
2. **Clone** ton fork sur ta machine :
   ```bash
   git clone https://github.com/ton-username/advent-of-code-2025.git
   ```
3. **Crée une branche** pour ta solution :
   ```bash
   git checkout -b solution/jour-01
   ```
4. **Écris ta solution** dans `solutions/jour_01.py`
5. **Commit** tes changements :
   ```bash
   git add solutions/jour_01.py
   git commit -m "feat: solution du jour 01"
   ```
6. **Push** vers ton fork :
   ```bash
   git push origin solution/jour-01
   ```
7. **Ouvre une Pull Request** sur GitHub depuis ton fork vers le dépôt principal

Pour plus de détails, voir [CONTRIBUTING.md](./CONTRIBUTING.md).

---

## ✅ Checklist pour débutants

- [ ] J'ai installé Python 3.10+
- [ ] J'ai installé Git
- [ ] J'ai cloné le dépôt
- [ ] J'ai créé un fichier de solution
- [ ] J'ai fait mon premier commit
- [ ] J'ai poussé mes changements sur GitHub

---

## 🆘 Besoin d'aide ?

- 📖 Consulte la [documentation GitHub](https://docs.github.com/fr)
- 💬 Demande de l'aide sur le canal de discussion du projet
- 🐛 Signale un problème via [Issues](https://github.com/ton-username/advent-of-code-2025/issues)

---

**Bon courage et bonne résolution ! 🎄🚀**