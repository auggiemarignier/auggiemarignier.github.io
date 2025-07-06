#!/bin/bash
set -e

STYLE_URL="https://raw.githubusercontent.com/citation-style-language/styles/master/ieee-with-url.csl"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST="$SCRIPT_DIR/ieee-with-url.csl"

curl -sSL "$STYLE_URL" -o "$DEST"

echo "✅ Updated $DEST"