# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew
block_cipher = None

datas_dir = [(r'C:\Users\drarn\Documents\Code\PyProjects\corporacion\kivy_venv\Lib\site-packages', '.'),
(r'C:\Users\drarn\Documents\Code\PyProjects\corporacion\appCorp\windows\*.kv','windows'),
(r'C:\Users\drarn\Documents\Code\PyProjects\corporacion\appCorp\assets\dbs\*.db','assets\\dbs'),
(r'C:\Users\drarn\Documents\Code\PyProjects\corporacion\appCorp\assets\fonts\*.ttf','assets\\fonts'),
(r'C:\Users\drarn\Documents\Code\PyProjects\corporacion\appCorp\assets\icos\*.ico','assets\\icos'),
(r'C:\Users\drarn\Documents\Code\PyProjects\corporacion\appCorp\assets\images\*.png','assets\\images')]


a = Analysis(['main.py'],
             pathex=['C:\\Users\\drarn\\Documents\\Code\\PyProjects\\corporacion\\appCorp'],
             binaries=[],
             datas=datas_dir,
             hiddenimports=['pkg_resources.py2_warn'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='corpMujer',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True , icon='C:\\Users\\drarn\\Documents\\Code\\PyProjects\\corporacion\\appCorp\\assets\\icos\\colflag.ico')
coll = COLLECT(exe,
               Tree('windows\\'),
               Tree('assets\\dbs\\'),
               Tree('assets\\fonts\\'),
               Tree('assets\\icos\\'),
               Tree('assets\\images\\'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='corpMujer')

