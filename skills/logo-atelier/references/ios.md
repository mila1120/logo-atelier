# iOS app-icon handoff

First record whether the user needs a brand logo, app icon or both. Record target iOS and Xcode versions. Verify current Apple instructions before final delivery; this reference is a starting point (checked 2026-09-20).

Keep an editable 1024 × 1024 composition master with separate foreground/background layers. Do not bake a rounded outer mask into the source. Logo SVG may have transparency; the flattened traditional iOS app-icon PNG should have an opaque background. Preview system masking separately and test important content against the crop. Do not invent one universal safe-area percentage: choose visual padding and verify on the target system.

Choose the project route explicitly: Xcode asset-catalog single image and generated sizes, explicit legacy asset slots if that project requires them, or Icon Composer layered workflow for supported toolchains. A 1024 PNG is not an Icon Composer source package. Provide appropriate appearances where the target supports/requires them, and test the actual exported result. 16/24/32/64 px in our QA sheet are logo diagnostics, not an official list of iOS icon sizes.

Sources:
- https://developer.apple.com/design/human-interface-guidelines/app-icons
- https://developer.apple.com/documentation/xcode/configuring-your-app-icon
- https://developer.apple.com/icon-composer/

Deliver exact required asset metadata only after the real project establishes target platforms. Device/Simulator validation remains pending if it was not actually performed.
