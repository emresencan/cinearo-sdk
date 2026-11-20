#!/bin/bash
# Rebuild third-party SDK only, with no Cinearo application source or credentials.
set -euo pipefail
package_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
build_dir=${1:?Pass an absolute, new empty build directory}
case "$build_dir" in /*) ;; *) echo 'Use an absolute new directory' >&2; exit 1;; esac
if [ -e "$build_dir" ]; then echo 'Refusing to overwrite an existing directory' >&2; exit 1; fi
python3 - "$package_dir" <<'PY'
from pathlib import Path
import hashlib,json,sys
root=Path(sys.argv[1]); manifest=json.loads((root/'SHA256.json').read_text())
for name, expected in manifest.items():
    assert hashlib.sha256((root/name).read_bytes()).hexdigest()==expected, name
print('Source package hashes verified')
PY
mkdir -p "$build_dir/libvlc/vlc"
tar -xzf "$package_dir/upstream/VLCKit-a213fd11.tar.gz" --strip-components=1 -C "$build_dir"
tar -xzf "$package_dir/upstream/vlc-6de05adc.tar.gz" --strip-components=1 -C "$build_dir/libvlc/vlc"
for source_patch in "$build_dir"/libvlc/patches/*.patch; do
    patch --batch --forward -d "$build_dir/libvlc/vlc" -p1 -i "$source_patch"
done
cp -R "$package_dir/overrides/wrapper/." "$build_dir/"
cp -R "$package_dir/overrides/vlc/." "$build_dir/libvlc/vlc/"
mkdir -p "$build_dir/libvlc/vlc/contrib/tarballs"
cp -R "$package_dir/contrib-tarballs/." "$build_dir/libvlc/vlc/contrib/tarballs/"
cp -R "$package_dir/tool-tarballs/." "$build_dir/libvlc/vlc/extras/tools/"
cd "$build_dir"
# -n skips Git/network source updates. Missing build dependencies can still be
# downloaded by upstream hashed recipes; all actually fetched archives are supplied.
# The native SDK paths are generated for the current selected Xcode by the script.
CINEARO_CORE_MIN=9.0 CINEARO_SKIP_FRAMEWORK=yes /bin/bash buildMobileVLCKit.sh -n -a aarch64
python3 "$package_dir/build_frameworks.py" --work "$build_dir" --name Cinearo-MobileVLCKit
