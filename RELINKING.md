# Rebuilding and relinking the player

The iOS app links `@rpath/MobileVLCKit.framework/MobileVLCKit` dynamically. The framework is not compiled into the Cinearo executable. Cinearo's terms preserve the LGPL rights to modify this component and reverse engineer the app for debugging those modifications.

1. Download and verify the full source release, extract it, and run its documented rebuild script on an Apple Silicon Mac with the recorded Xcode toolchain. The archive's README describes build prerequisites, modifications and platform floors.
2. Keep the framework's public ABI/module name, install name, arm64 device slice and minimum iOS requirements compatible. Include the recorded privacy manifest and component notices. The simulator slice is not an iPhone replacement.
3. Use an unencrypted, relinkable developer app build. Electronic app-side relinking material is prepared by the developer and can be requested from cinearo@outlook.com for debugging modifications to the LGPL component. The application's own source and Apple's signing keys are not required or supplied.
4. Replace `Frameworks/MobileVLCKit.framework` in that app with the rebuilt device framework. Sign nested code first, then the containing app using your own valid Apple development identity and provisioning profile. Xcode's normal development installation tools can install that app on an authorized device.
5. App Store signatures, receipts and distribution provisioning cannot be reused for a modified build. CarPlay and other restricted Apple entitlements require Apple's authorization for the signing account. Do not bypass system safety, content protection or signature validation. No promise of App Store redistribution of a modified app is made.

The public archive supplies the exact corresponding library sources and build inputs. Platform signing and access to hardware remain separate requirements. The developer's app-side relinking artifact contains compiled application code, not application source or user data; it is provided separately from this third-party-only repository.
