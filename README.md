Voici une version formatée en Markdown pour votre README :

```markdown
# CodeQL Custom Queries for Python

Ce projet contient des requêtes CodeQL personnalisées pour analyser des projets Python et identifier des vulnérabilités ou des améliorations potentielles.

---

## Prérequis

- **Git** : [Installer Git](https://git-scm.com/)
- **Visual Studio Code** (facultatif, mais recommandé) : [Télécharger VS Code](https://code.visualstudio.com/)
- **CodeQL CLI** : Téléchargeable dans les étapes ci-dessous.

---

## Installation

### Étape 1 : Cloner le dépôt
Clonez ce dépôt en utilisant la commande suivante :
```bash
git clone https://github.com/RolexSir30/CodeQl
```

### Étape 2 : Télécharger CodeQL CLI
1. Rendez-vous sur la page des [releases de CodeQL CLI binaries](https://github.com/github/codeql-cli-binaries/releases).
2. Téléchargez le fichier **`codeql-win64.zip`** pour Windows (ou le fichier correspondant à votre système d'exploitation).

### Étape 3 : Décompresser l'archive
1. Extrayez le fichier ZIP téléchargé.
2. Accédez au dossier où se trouve le fichier `codeql.exe`.

### Étape 4 : Ajouter CodeQL au PATH
1. Copiez le chemin du dossier contenant `codeql.exe`.
2. Ajoutez ce chemin aux variables d'environnement :
   - **Windows** : Ajoutez-le dans les paramètres des variables d'environnement.
   - **Linux/macOS** : Ajoutez cette ligne dans votre fichier `~/.bashrc` ou `~/.zshrc` :
     ```bash
     export PATH="/chemin/vers/codeql:$PATH"
     ```

3. Vérifiez l'installation en exécutant cette commande dans le terminal :
   ```bash
   codeql --version
   ```

---

## Intégration avec Visual Studio Code

### Étape 5 : Installer l'extension CodeQL
1. Ouvrez Visual Studio Code.
2. Dans le Marketplace des extensions, recherchez **CodeQL**.
3. Installez l'extension CodeQL.

---

## Exécution du projet

### Étape 6 : Résolution des dépendances
1. Accédez au dossier contenant le projet :
   ```bash
   cd codeql-custom-queries-python
   ```
2. Exécutez les commandes suivantes pour installer les dépendances :
   ```bash
   codeql pack install
   codeql pack resolve-dependencies
   ```

### Étape 7 : Charger la base de données
1. Créez une base de données CodeQL pour le code Python à analyser :
   ```bash
   codeql database create database --language=python --overwrite
   ```

### Étape 8 : Exécuter une requête
1. Exécutez une requête CodeQL sur la base de données :
   ```bash
   codeql query run codeql-custom-queries-python/example3.ql --database=database
   ```
   Remplacez `example3.ql` par le fichier de requête que vous souhaitez exécuter.

---

## Notes supplémentaires

- Veillez à ce que le code source Python soit présent dans le dossier avant de créer la base de données.
- Consultez la [documentation officielle CodeQL](https://codeql.github.com/docs/) pour apprendre à écrire vos propres requêtes ou pour des usages avancés.

---

## Contribuer
Les contributions sont les bienvenues ! Ouvrez une issue ou soumettez une pull request pour améliorer ce projet.

---

## Licence
Ce projet est sous licence [MIT License](LICENSE).
```

### Ce README est :
- **Simple et complet** : chaque étape est expliquée.
- **Formaté pour GitHub** : avec des blocs de code et des liens cliquables.
- **Prêt à l'emploi** : il suffit de le copier-coller dans un fichier `README.md` dans votre dépôt.
