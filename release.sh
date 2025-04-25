#!/bin/bash

TOOL=$1
git config user.name "github-actions[bot]"
git config user.email "github-actions[bot]@users.noreply.github.com"

run_tests() {
  echo "✅ Lancement des tests..."
  npm run test
  if [ $? -ne 0 ]; then
    echo "❌ Tests échoués. Abandon de la release."
    exit 1
  fi
}

get_commit_message() {
  # Récupère le dernier message de commit
  COMMIT_MESSAGE=$(git log -1 --pretty=%B)
  echo "Dernier commit : $COMMIT_MESSAGE"
}

case $TOOL in
  standard-version)
    run_tests
    npx standard-version
    get_commit_message # Appel de la fonction pour récupérer le commit
    # Ajouter le commit message dans CHANGELOG
    echo -e "\n\n### Dernier Commit: $COMMIT_MESSAGE" >> CHANGELOG.md
    git add CHANGELOG.md
    git commit -m "Update CHANGELOG.md with commit message"
    git push --follow-tags origin main
    gh release create $(node -p "require('./package.json').version") -F CHANGELOG.md
    ;;
  release-it)
    run_tests
    npx release-it
    ;;
  *)
    echo "Usage: ./release.sh [standard-version|release-it]"
    ;;
esac
