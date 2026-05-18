#!/usr/bin/env bash
set -euo pipefail

VERSION="${1:?Usage: ./publish-release.sh 1.2.3}"
REPO="${2:-mettleci/mcix-cli}"

TAG="v${VERSION}"
TITLE="${VERSION}"

INPUT_DIR="release-input"
NOTES_FILE="${INPUT_DIR}/${TAG}.md"

ASSETS=(
  "${INPUT_DIR}/mcix-linux-x86.zip"
  "${INPUT_DIR}/mcix-macos-arm64.zip"
  "${INPUT_DIR}/mcix-windows-x86.zip"
)

for asset in "${ASSETS[@]}"; do
  if [[ ! -f "$asset" ]]; then
    echo "Missing asset: $asset"
    exit 1
  else
    echo "Found asset: $asset"
  fi
done

if [[ ! -f "$NOTES_FILE" ]]; then
  echo "Missing release notes: $NOTES_FILE"
  exit 1
else
  echo "Found release notes: $NOTES_FILE"
fi

cat <<EOF >> "$NOTES_FILE"
<br/>
MCIX CLI ${TAG} - Published on $(date "+%Y-%m-%d %H:%M:%S %Z")
EOF

mkdir -p dist
cp "${ASSETS[@]}" dist/

(
  cd dist
  shasum -a 256 *.zip > checksums.txt
)

git fetch --tags

if git rev-parse "$TAG" >/dev/null 2>&1; then
  echo "Local tag $TAG already exists"
else
  git tag -a "$TAG" -m "mcix ${VERSION}"
fi

git push origin "$TAG"

gh release create "$TAG" \
  dist/mcix-linux-x86.zip \
  dist/mcix-macos-arm64.zip \
  dist/mcix-windows-x86.zip \
  dist/checksums.txt \
  --repo "$REPO" \
  --title "$TITLE" \
  --notes-file "$NOTES_FILE"