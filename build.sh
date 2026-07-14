#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

# Resolve the Blender executable. Precedence:
#   1. $BLENDER if already set (e.g. `BLENDER=/path/to/blender ./install.sh`)
#   2. Highest version found on PATH or under common install dirs
if [ -z "${BLENDER:-}" ]; then
    best_bin="" best_ver=""
    while IFS= read -r bin; do
        [ -x "$bin" ] || continue
        ver=$("$bin" --version 2>/dev/null | awk 'NR==1 && $1=="Blender"{print $2; exit}')
        [ -n "$ver" ] || continue
        if [ -z "$best_ver" ] || [ "$(printf '%s\n%s\n' "$ver" "$best_ver" | sort -V | tail -n1)" = "$ver" ]; then
            best_bin="$bin" best_ver="$ver"
        fi
    done < <(
        {
            command -v blender 2>/dev/null || true
            find "$HOME" /Applications /opt /usr/local /snap -maxdepth 5 -type f -iname blender -perm -u+x 2>/dev/null || true
        } | sort -u
    )
    BLENDER="$best_bin"
    BLENDER_VERSION="$best_ver"
fi

if [ -z "${BLENDER:-}" ] || ! "$BLENDER" --version >/dev/null 2>&1; then
    echo "ERROR: no working Blender executable found." >&2
    echo "Set one explicitly:  BLENDER=/path/to/blender ./install.sh" >&2
    exit 1
fi
echo "Using Blender: $BLENDER${BLENDER_VERSION:+ (version $BLENDER_VERSION)}"

# build/ is a fully regenerable, deletable staging area holding a snapshot of
# the add-on source plus the packaged zip; the real source tree is untouched.
ADDON="procedural_skins_addon"
BUILD_DIR="$(pwd)/build"
STAGE="$BUILD_DIR/$ADDON"
rm -rf "$BUILD_DIR"
mkdir -p "$STAGE"
cp -r "$ADDON/." "$STAGE"
rm -rf "$STAGE/build"
find "$STAGE" -name '*.blend1' -delete

# Package the staged add-on, dropping the zip alongside it in build/
"$BLENDER" --command extension build --source-dir "$STAGE" --output-dir "$BUILD_DIR"
