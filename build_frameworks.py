#!/usr/bin/env python3
"""Wrap already-built, isolated arm64 libVLC slices using the current Xcode.

Does not install an SDK, touch the phone, use signing accounts or upload files.
The original source build script's echo/newline and single-arch simulator
packaging assumptions do not work with this toolchain.
"""
from pathlib import Path
import argparse
import subprocess

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / 'ThirdParty/HardenedBuild'
parser = argparse.ArgumentParser()
parser.add_argument('--name', default='Cinearo-MobileVLCKit')
parser.add_argument('--work', type=Path, default=WORK)
args = parser.parse_args()
WORK = args.work.resolve()
if not args.name.replace('-', '').isalnum():
    raise SystemExit('Use a simple archive name')
output = WORK / 'build' / (args.name + '.xcframework')
if output.exists():
    raise SystemExit('Output exists; inspect rather than overwrite a qualified SDK')

# Generated C/xcconfig contain only module identifiers and library paths, with
# escaped newline separators. Normalize those separators without evaluating C
# or arbitrary shell content. Record this transformation in the build receipt.
for name in ['vlc-plugins-iPhone.h', 'vlc-plugins-iPhone.xcconfig']:
    path = WORK / 'Resources/MobileVLCKit' / name
    text = path.read_text().replace('\\\\n', '\n').replace('\\n', '\n')
    assert '\\n' not in text
    path.write_text(text)

for sdk in ['iphoneos', 'iphonesimulator']:
    archive = WORK / 'build' / (args.name + '-' + sdk + '.xcarchive')
    subprocess.run(['xcodebuild', 'archive', '-project', str(WORK / 'MobileVLCKit.xcodeproj'),
                    '-scheme', 'MobileVLCKit', '-sdk', sdk, '-archivePath', str(archive),
                    'ARCHS=arm64', 'ONLY_ACTIVE_ARCH=YES', 'IPHONEOS_DEPLOYMENT_TARGET=17.0',
                    'BITCODE_GENERATION_MODE=none', 'ENABLE_BITCODE=NO', 'SKIP_INSTALL=NO',
                    'CODE_SIGNING_ALLOWED=NO'], cwd=WORK, check=True)

command = ['xcodebuild', '-create-xcframework']
for sdk in ['iphoneos', 'iphonesimulator']:
    archive = WORK / 'build' / (args.name + '-' + sdk + '.xcarchive')
    command += ['-framework', str(archive / 'Products/Library/Frameworks/MobileVLCKit.framework'),
                '-debug-symbols', str(archive / 'dSYMs/MobileVLCKit.framework.dSYM')]
command += ['-output', str(output)]
subprocess.run(command, check=True)
print(output)
