#!/bin/bash

set -e  # Arrête le script en cas d'erreur
echo " Script de test des outils de release ==="

echo ""
echo "Étape 1 : standard-version"
echo "--------------------------------"

# Installation si besoin
npm install --save-dev standard-version
# Exécution (bump + changelog + tag)
npx standard-version --release-as minor --skip.commit --skip.tag
echo " standard-version exécuté (version + changelog générés, sans commit ni tag)"

echo ""
echo "Étape 2 : release-it"
echo "--------------------------------"
# Installation si besoin
npm install --save-dev release-it
# Exécution d'une version mineure (version, changelog, tag, pas de push/release)
npx release-it minor --no-push --no-git.requireCleanWorkingDir
echo "release-it exécuté (bump + changelog + tag local, pas de push)"

echo ""
echo "Étape 3 : semantic-release (mode dry-run)"
echo "--------------------------------"

# Installation si besoin
npm install --save-dev semantic-release @semantic-release/git @semantic-release/changelog @semantic-release/release-notes-generator @semantic-release/commit-analyzer @semantic-release/gitlab

# Simule une release (dry-run)
npx semantic-release --dry-run
echo "semantic-release exécuté en dry-run (aucune modification réelle)"

echo ""
echo "Test des 3 outils terminé ==="
