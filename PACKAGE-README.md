# Cinearo SDK 3.7.5-cinearo.1 — corresponding source preparation

5 November 2026. This package contains third-party software source and Cinearo's
changes to that software. It contains no Cinearo app source, user account,
Keychain content, private configuration, certificate or signing key.

## Contents and provenance

- Official VLCKit `a213fd11` and VLC `6de05adc` source archives. The wrapper
  archive supplies the 43 upstream VLC patches. `SHA256.json` pins local copies.
- Full modified files in `overrides/` are applied **after** those upstream patches.
  They include source changes and build compatibility fixes, with comments.
- Actual downloaded contribution and host-tool source archives, upstream recipe
  tree, checksums, license texts and component inventory. These are source caches,
  not executable downloads or a binary-only offer.
- Wrapper driver uses Xcode's public framework archive/create-xcframework commands.

The profile removes iOS `fstatfs` used only to decide local buffering, disables
legacy RealRTSP, and reads seekable font byte lengths without querying system
font metadata. FreeType's overflow/zero-size tests and mapping/read paths remain.
HTTPS uses the existing Apple Secure Transport module. Certificate checks are not
disabled. Actual release source/configuration still needs final compliance review.

## Build

Use an Apple Silicon Mac, selected Xcode 27.2 SDK and its command-line tools,
Python 3, make, standard macOS shell tools and sufficient free disk space
(allow at least 15 GB). The original build used macOS 27.2 SDK host generators,
iOS/Simulator 27.2 SDKs, arm64 only, four parallel jobs, core deployment floor9
and framework/app floor17. Both frameworks are unsigned until an app signs them.

1. Extract the source package into its own directory.
2. Read the licenses and inspect `overrides/` and `rebuild-source.sh`.
3. Run `bash rebuild-source.sh /absolute/path/to/a/new/build-directory`.
4. Output: `build/Cinearo-MobileVLCKit.xcframework`. Add the reviewed privacy
   manifest in each framework bundle before the enclosing app is signed.

The source package hashes are local integrity pins, not a vendor signature.
Upstream tool/contribution recipes verify their own source checksums. `-n` avoids
Git source updates, but it is not an OS network sandbox. All archives fetched in
the recorded build are supplied. A rebuild on a different toolchain may require
compatibility fixes and is not promised byte-identical.

## Distribution and relinking — still to finalize

The SDK is dynamically linked. A user rebuilding/replacing it needs an iOS build
and signing environment; an App Store signature cannot be reused for a modified
app. The final distributed app must provide the necessary corresponding source,
modified SDK rights and a working, documented relinking route consistent with
the selected licenses. A generic upstream repository link is insufficient for
these modifications. The public delivery URL/contact and final release relinking
materials are not configured in this local preparation package.

Do not treat this document as a legal opinion or a completed license clearance.
No application EULA may restrict the rights these third-party licenses grant.
