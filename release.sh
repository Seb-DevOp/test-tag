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

# Récupérer la dernière version et commit
get_version_and_commit() {
  VERSION=$(node -p "require('./package.json').version")
  COMMIT=$(git log -1 --pretty=format:'%h %s')
  DATE=$(date +'%Y-%m-%d')
}

case $TOOL in
  standard-version)
    run_tests
    npx standard-version
    get_version_and_commit
    # Ajouter la version, la date et le dernier commit dans le changelog
    echo -e "## [$VERSION] - $DATE\n- $COMMIT\n" >> CHANGELOG.md
    git add CHANGELOG.md
    git commit -m "Update CHANGELOG.md for version $VERSION"
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
