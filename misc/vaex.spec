# -*- mode: python -*-
import vaex
import astropy
import requests
import os
astropy_base_dir = os.path.dirname(astropy.__file__)
requests_base_dir = os.path.dirname(requests.__file__)

a = Analysis(['bin/vaex'],
             pathex=['/net/theon/data/users/breddels/vaex/src/SubspaceFinding'],
             hiddenimports=["h5py.h5ac", "h5py.defs", "h5py.utils", "h5py._proxy", "six", "sip", "PyQt5", "PyQt5.QtGui", "PyQt5.QtCore", "PyQt5.QtTest", "PyQt5.Widgets",\
             "numpy.lib.recfunctions"],
             hookspath=None,)
#             runtime_hooks=["vaex/ui/rthook_pyqt4.py"])
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name=vaex.__build_name__, #+"_app",
          debug=False,
          strip=None,
          upx=True,
          console=True )
          
icon_tree = Tree('vaex/ui/icons', prefix = 'icons')
data_tree = Tree('data', prefix='data', excludes=["*.properties"])
#doc_tree = Tree('doc', prefix='doc', excludes=["*.zip"])
astropy_tree = Tree(astropy_base_dir, prefix='astropy')
requests_tree = Tree(requests_base_dir, prefix='requests')

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               icon_tree,
               data_tree,
               astropy_tree,requests_tree,
               strip=None,
               upx=True,
               name=vaex.__build_name__)
