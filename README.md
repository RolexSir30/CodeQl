Etape 1 : git clone https://github.com/RolexSir30/CodeQl

Télécharger codeql
Etape 2 : Aller sur ce site : https://github.com/github/codeql-cli-binaries/releases et télécharger "codeql-win64.zip"
Etape 3 : Décompresser le fichier zip et et aller dans le dossier où il y a le codeql.exe
Etape 4 : Copier le chemin où vous êtes et ajouter le au path, vérifier ensuite que codeql et bien accessible en tapant codeql --version.



Ajouter codeql à vs code : 

( si ce n'est pas toujours fait  installer vs code )
Etape 5 : Ajouter l'extension codeql à vs code.

pour run le projet : 

aller dans le dossier où il a le projet, et taper ces commandes afin d'enlever les erreurs d'import
cd codeql-custom-queries-python
codeql pack install
codeql pack resolve-dependencies

puis taper cette commande pour charger la bdd : 

codeql database create database --language=python --overwrite

Executer la première commande : codeql query run codeql-custom-queries-python\example3.ql --database=database 
Si ça marche c'est good

