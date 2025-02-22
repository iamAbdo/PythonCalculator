# -*- mode: python ; coding: utf-8 -*-
import os
import sys

# Automatically detect project root
project_root = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(project_root, 'src')

# Add src directory to Python path
sys.path.insert(0, src_path)

block_cipher = None

a = Analysis(
    ['main.py'],  # Now relative to src_path
    pathex=[src_path],  # Auto-detected path
    binaries=[],
    datas=[
        (os.path.join(src_path, 'assets', '*'), 'assets'),
        (os.path.join(src_path, 'widgets', '*.py'), 'widgets'),
        (os.path.join(src_path, 'utils', '*.py'), 'utils'),
        (os.path.join(src_path, 'config', '*.py'), 'config')
    ],
    hiddenimports=[
        'widgets.simple_mode',
        'widgets.advanced_mode',
        'utils.calculator'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Calculator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon=os.path.join(src_path, 'assets', 'icon.ico') if os.path.exists(os.path.join(src_path, 'assets', 'icon.ico')) else None,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)