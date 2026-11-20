# Cinearo third-party player SDK

Corresponding source for the modified, dynamically linked MobileVLCKit/libVLC profile `3.7.5-cinearo.1` used by Cinearo for iOS. Published with the application owner's permission on 20 November 2026.

Download the complete source archive from [the release](https://github.com/emresencan/cinearo-sdk/releases/tag/3.7.5-cinearo.1). Verify `SOURCE-SHA256.txt`, extract the archive, then follow its `rebuild-source.sh` and `SHA256.json`. The archive contains the official pinned VLCKit/VLC sources, upstream patches, our modified files, contribution/host-tool source caches, component license texts and the build recipe. The release archive is required; the small files in this repository alone are not a complete build tree.

The archive was prepared on 5 November; its distribution-preparation paragraph is superseded by this public release and RELINKING.md. Its source-file hashes and build inputs remain unchanged. This is third-party SDK source, not Cinearo application source, accounts, credentials or signing material.

## Licenses

MobileVLCKit/libVLC uses LGPL 2.1 or later. Other components retain their individual licenses, reproduced in the archive and inventory. COPYING.LGPL-2.1 supplies the LGPL text; it does not relicense other components. Cinearo's terms do not limit modification/reverse engineering rights necessary for debugging changes to the LGPL component.

## Rebuilding and replacing the library

See [RELINKING.md](RELINKING.md), then the complete archive's README and build recipe. Exact toolchain information and modification details are supplied there. No byte-identical output across toolchains or permission to reuse Apple's signatures is promised.

Source/relinking assistance: cinearo@outlook.com. No fee is charged for electronic access to the corresponding source.
