sqlcmd -S 190.145.94.91 -U Arnulforojas -P 'Arojas032020'
USE CMMCRSocial;

SELECT names, lastNames FROM payee;
DELETE FROM payee;

SELECT id FROM payeeProjects;
DELETE FROM payeeProjects;

SELECT payeeDocument FROM productionProfileDiag;
DELETE FROM productionProfileDiag;



sqlcmd -S 190.145.94.92 -d CMMCRSocial -U API -P Api*2020*


ALTER TABLE informacion_general_beneficiario ALTER COLUMN cellphone bigint;


sqlcmd -S 190.145.94.92 -d CMMCRSocial -U Arnulforojas -P Arojas032020

python -m PyInstaller --name cmm_app --icon C:\Users\drarn\Documents\Documents\Dev\corpMundialMujer\images\icono.ico C:\Users\drarn\Documents\Documents\Dev\corpMundialMujer\main.py

INSERT INTO odp_operario (document ,name, username, password, type) VALUES ('12345', 'carlos jose', 'carlos23', 'asdf', 1)

INSERT INTO odp_operario_proyectos (id, fkOperator, fkProject) VALUES ('1234__prueba001', '12345', 'prueba001');

INSERT INTO proyectos (id, name, data) VALUES ('prueba001', 'prueba', '2010-03-15')

SPEC EXAMPLE


# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew
block_cipher = None

data_spec = [(r'C:\Users\drarn\Documents\Documents\Dev\corpMundialMujer\windows\*.kv','./windows'),
            (r'C:\Users\drarn\Documents\Documents\Dev\corpMundialMujer\images\*.png','./images'),
            (r'C:\Users\drarn\Documents\Documents\Dev\corpMundialMujer\fonts\*.ttf','./fonts'),
            (r'C:\Users\drarn\Documents\Documents\Dev\corpMundialMujer\declarations\*.py','./declarations'),
            (r'C:\Users\drarn\Documents\Documents\Dev\corpMundialMujer\declarations\*.kv','./declarations'),
            (r'C:\Users\drarn\Documents\Documents\Dev\corpMundialMujer\databases\parametric\*.db','./databases/parametric'),
            (r'C:\Users\drarn\Documents\Documents\Dev\corpMundialMujer\databases\register\*.db','./databases/register'),
            (r'C:\Users\drarn\Documents\Documents\Dev\corpMundialMujer\codes\*.py','./codes')]

a = Analysis(['C:\\dev\\cmm_app\\main.py'],
             pathex=['C:\\dev\\windows apk'],
             binaries=[],
             datas=data_spec,
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
          name='cmm',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='cmm')

