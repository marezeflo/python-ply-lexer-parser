# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['lexer.py'],
             pathex=['E:\\ISI Ingeniería en Sistemas - UTN\\2 AÑO\\CUATRIMESTRALES\\Q1\\SSL - Sintaxis y Semántica de los Lenguajes\\TPI\\G32\\source'],
             binaries=[],
             datas=[],
             hiddenimports=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='lexer',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
