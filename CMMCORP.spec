# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew
from kivy.tools.packaging.pyinstaller_hooks import get_deps_minimal, get_deps_all, hookspath, runtime_hooks
import os
block_cipher = None

path = os.getcwd()
icon_path = os.path.join(path, 'images/icono.ico')
icon2_path = os.path.join(path, 'images/CMMCBoton.ico')

a = Analysis(['main.py'],
             pathex=[path],
             datas=[],
             hookspath=hookspath(),
             hooksconfig={},
             runtime_hooks=runtime_hooks(),
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False,
             **get_deps_minimal(video=None, audio=None))
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='corpMundialMujer',
          icon=[icon_path],
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
          
coll = COLLECT(exe, Tree(path),
               a.binaries,
               a.zipfiles,
               a.datas, 
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               icon=[icon2_path],
               upx_exclude=[],
               name='CMMCORP')
