# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('E:\\#ArduinoAndPyCharmProject\\Controlling an LED spotlight from a computer\\This is PyCharm\\Images\\icon.ico', 'Images'), ('E:\\#ArduinoAndPyCharmProject\\Controlling an LED spotlight from a computer\\This is PyCharm\\Images\\led-lamp-off.png', 'Images'), ('E:\\#ArduinoAndPyCharmProject\\Controlling an LED spotlight from a computer\\This is PyCharm\\Images\\led-lamp-on.png', 'Images')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Spotlight control',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['E:\\#ArduinoAndPyCharmProject\\Controlling an LED spotlight from a computer\\This is PyCharm\\Images\\icon.ico'],
)
