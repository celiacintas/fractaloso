from distutils.core import setup
import py2exe

from distutils.filelist import findall
import os
import matplotlib
matplotlibdatadir = matplotlib.get_data_path()
matplotlibdata = findall(matplotlibdatadir)
matplotlibdata_files = []
for f in matplotlibdata:
    dirname = os.path.join('matplotlibdata', f[len(matplotlibdatadir)+1:])
    matplotlibdata_files.append((os.path.split(dirname)[0], [f]))
    
opts = {
    'py2exe': { "includes" : [ "matplotlib.backends",  "matplotlib.backends.backend_qt4agg",
                               "matplotlib.figure","pylab", "numpy", "scipy",
                               "random", "pyeeg",
                               "matplotlib.backends.backend_tkagg"],
                'excludes': ['_gtkagg', '_tkagg', '_agg2', '_cairo', '_cocoaagg',
                             '_fltkagg', '_gtk', '_gtkcairo', ],
                'dll_excludes': ['libgdk-win32-2.0-0.dll',
                                 'libgobject-2.0-0.dll', 'MSVCP90.dll']#,'bundle_files': 2,'optimize': 2
              }
       }

setup(windows=[{"script" : "myAnalysis.py"}], options=opts,   data_files=matplotlib.get_py2exe_datafiles())
