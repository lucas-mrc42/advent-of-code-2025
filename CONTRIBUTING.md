# 📋 Guide de Contribution

Merci de contribuer à ce projet ! Ce guide t'aide à ajouter ta solution en quelques étapes simples.

---

## 🚀 Premiere contribution — Guide pas à pas

### Étape 1 : Fork le dépôt

1. Va sur la page GitHub du projet
2. Clique sur le bouton **Fork** (en haut à droite)
3. Sélectionne ton compte GitHub comme destination
4. Attends que le fork soit créé

→ Tu as maintenant une copie du projet sur ton compte GitHub.

---

### Étape 2 : Clone ton fork sur ta machine

```bash
git clone https://github.com/ton-username/advent-of-code-2025.git
cd advent-of-code-2025
```

> Remplace `ton-username` par ton vrai nom d'utilisateur GitHub.

---

### Étape 3 : Configure Git pour la première fois

Si c'est ta première utilisation de Git, configure tes informations :

```bash
git config user.name "Ton Prénom"
git config user.email "ton.email@exemple.com"
```

---

### Étape 4 : Crée une branche pour ta solution

On crée toujours une branche pour travailler proprement :

```bash
git checkout -b solution/jour-01
```

> Remplace `jour-01` par le numéro du jour que tu résous.

---

### Étape 5 : Écris ta solution

1. Ouvre le dossier `solutions/`
2. Crée un fichier nommé `jour_XX.py` (remplace XX par le numéro du jour)
3. Écris ton code —参见 les conseils ci-dessous

#### Conseils pour un bon code

✅ **À faire :**
- Ajoute un commentaire en haut avec le numéro du jour et une brève description
- Commente les parties complexes de ton algorithme
- Utilise des noms de variables clairs
- Teste ton code avec les exemples de l'énoncé

❌ **À éviter :**
- Ne mets pas de données sensibles (mots de passe, clés API)
- Ne crée pas de fichiers temporaires dans le dossier `solutions/`
- N'utilise pas de dépendances externes non documentées

---

### Étape 6 : Commit ta solution

```bash
# Voir les fichiers modifiés
git status

# Ajouter ton fichier au suivi
git add solutions/jour_XX.py

# Créer un commit avec un message descriptif
git commit -m "feat: solution du jour 01"
```

#### Convention pour les messages de commit

| Type | Utilisation |
|------|-------------|
| `feat:` | Ajout d'une nouvelle solution |
| `fix:` | Correction d'une solution existante |
| `docs:` | Modification de la documentation |
| `refactor:` | Amélioration du code sans changer le comportement |

---

### Étape 7 : Push vers ton fork

```bash
git push origin solution/jour-01
```

---

### Étape 8 : Ouvre une Pull Request

1. Va sur la page de ton fork sur GitHub
2. Tu verras une bannière verte : **"Compare & pull request"** — clique dessus
3. Remplis le formulaire :
   - **Titre** : Solution jour 01
   - **Description** : Explique ce que fait ta solution
4. Clique sur **"Create pull request"**

---

## 🔍 Comment ton Pull Request sera évalué

Les mainteneurs vérifieront :

- [ ] Le fichier est dans le bon dossier (`solutions/`)
- [ ] Le nom du fichier suit le format `jour_XX.py`
- [ ] Le code fonctionne avec les exemples de l'énoncé
- [ ] Le code est correctement commenté
- [ ] Pas de conflits avec les fichiers existants

---

## 🎯 Checklist avant de soumettre

- [ ] J'ai lu et compris l'énoncé du jour
- [ ] Ma solution passe les tests d'exemple
- [ ] J'ai ajouté des commentaires dans mon code
- [ ] J'ai créé une branche dédiée (pas travaillé sur `main`)
- [ ] Mon commit a un message clair
- [ ] Ma Pull Request a une description

---

## 💡 Conseils pour les débutants

### Si tu es bloqué...

1. **Relis l'énoncé** — il contient souvent des indices
2. **Découpe le problème** — un grand problème devient simple quand on le divise
3. **Commence par les exemples** — ils te donnent la bonne réponse pour vérifier
4. **Demande de l'aide** — ouvre une Discussion sur GitHub

### Si tu veux progresser...

- Essaie de résoudre le problème en moins de temps
- Essaie de résoudre le problème en utilisant moins de variables
- Cherche des solutions alternatives après avoir résolu le problème

---

## 📜 Licence

En contribuant, tu acceptes que ton code soit publié sous la licence MIT du projet.

Merci pour ta contribution ! 🎄