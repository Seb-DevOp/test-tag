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

case $TOOL in
  standard-version)
    run_tests
    npx standard-version
    # Ajouter l'information du dernier commit au changelog
    echo -e "\n### Dernier Commit: $LAST_COMMIT\n" >> CHANGELOG.md
    git add CHANGELOG.md
    git commit -m "Update CHANGELOG.md with last commit message"
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
