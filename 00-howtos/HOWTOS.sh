# Command-line installation of Anaconda on MacOs
https://docs.anaconda.com/anaconda/install/mac-os/


1. https://www.anaconda.com/products/individual#macos  
    Download "64-Bit Command Line Installer (430 MB)" for MacOs
    ~/Downloads/Anaconda3-2020.02-MacOSX-x86_64.sh

2. In the terminal, run:
    $ shasum -a 256 ~/Downloads/Anaconda3-2020.02-MacOSX-x86_64.sh
    $ d237e6c976eb9c58368ca156a51bd913d63a3b5fea32689342733c99d14b6f2e  /Users/macbook/Downloads/Anaconda3-2020.02-MacOSX-x86_64.sh

3. Run (for Python 3.7):
    $ bash ~/Downloads/Anaconda3-2020.02-MacOSX-x86_64.sh
    Scroll to the end of the license agreement,
    $ Do you accept the license terms? [yes|no]
    $ [no] >>> yes
    $ Anaconda3 will now be installed into this location:
    $ /Users/macbook/anaconda3
    Press ENTER
    Installation may take a few minutes to complete
    $ installation finished.
    $ Do you wish the installer to initialize Anaconda3
    $ by running conda init? [yes|no]
    $ [yes] >>> yes
4. Quit the terminal, then open a new one
5. Verifiy installation:
   https://docs.anaconda.com/anaconda/install/verify-install/
    If Anaconda is installed and working, the version information 
    it displays when it starts up will include “Anaconda”.
    $ python
    $ Python 3.7.6 (default, Jan  8 2020, 13:42:34) 
    $ [Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
    $ Type "help", "copyright", "credits" or "license" for more information.
    then
    $ quit()

    $ conda list
    Displays list of installed packages and their versions

6. https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-nav-mac
  Run Python in a Jupyter Notebook
   - Run
   $ jupyter notebook
   $ Ctrl+Q to close terminal
   OR
   - Open Anaconda Navigator, in the home pane:
   In Jupyter Notebook, click on Launch to launch Jupyter Notebook
   This will launch a new browser window (or a new tab) showing
   the Notebook Dashboard.
   In the top-right corner, click on New to Create a new Notebook 
   with the Python version you installed.
   --Close by clicking the Quit button top-right corner of the dashboar

7. After you create a notebook, open it in TextEdit to see its JSON content
  {
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "1+1"
   ]
  }, ... ... ...

## Package Plan ##

  environment location: /Users/macbook/anaconda3

  added / updated specs:
    - _ipyw_jlab_nb_ext_conf==0.1.0=py37_0
    - alabaster==0.7.12=py37_0
    - anaconda-client==1.7.2=py37_0
    - anaconda-navigator==1.9.12=py37_0
    - anaconda-project==0.8.4=py_0
    - anaconda==2020.02=py37_0
    - applaunchservices==0.2.1=py_0
    - appnope==0.1.0=py37_0
    - appscript==1.1.0=py37h1de35cc_0
    - argh==0.26.2=py37_0
    - asn1crypto==1.3.0=py37_0
    - astroid==2.3.3=py37_0
    - astropy==4.0=py37h1de35cc_0
    - atomicwrites==1.3.0=py37_1
    - attrs==19.3.0=py_0
    - autopep8==1.4.4=py_0
    - babel==2.8.0=py_0
    - backcall==0.1.0=py37_0
    - backports.functools_lru_cache==1.6.1=py_0
    - backports.shutil_get_terminal_size==1.0.0=py37_2
    - backports.tempfile==1.0=py_1
    - backports.weakref==1.0.post1=py_1
    - backports==1.0=py_2
    - beautifulsoup4==4.8.2=py37_0
    - bitarray==1.2.1=py37h1de35cc_0
    - bkcharts==0.2=py37_0
    - blas==1.0=mkl
    - bleach==3.1.0=py37_0
    - blosc==1.16.3=hd9629dc_0
    - bokeh==1.4.0=py37_0
    - boto==2.49.0=py37_0
    - bottleneck==1.3.2=py37h776bbcc_0
    - bzip2==1.0.8=h1de35cc_0
    - ca-certificates==2020.1.1=0
    - certifi==2019.11.28=py37_0
    - cffi==1.14.0=py37hb5b8e2f_0
    - chardet==3.0.4=py37_1003
    - click==7.0=py37_0
    - cloudpickle==1.3.0=py_0
    - clyent==1.2.2=py37_1
    - colorama==0.4.3=py_0
    - conda-build==3.18.11=py37_0
    - conda-env==2.6.0=1
    - conda-package-handling==1.6.0=py37h1de35cc_0
    - conda-verify==3.4.2=py_1
    - conda==4.8.2=py37_0
    - contextlib2==0.6.0.post1=py_0
    - cryptography==2.8=py37ha12b0ac_0
    - curl==7.68.0=ha441bb4_0
    - cycler==0.10.0=py37_0
    - cython==0.29.15=py37h0a44026_0
    - cytoolz==0.10.1=py37h1de35cc_0
    - dask-core==2.11.0=py_0
    - dask==2.11.0=py_0
    - dbus==1.13.12=h90a0687_0
    - decorator==4.4.1=py_0
    - defusedxml==0.6.0=py_0
    - diff-match-patch==20181111=py_0
    - distributed==2.11.0=py37_0
    - docutils==0.16=py37_0
    - entrypoints==0.3=py37_0
    - et_xmlfile==1.0.1=py37_0
    - expat==2.2.6=h0a44026_0
    - fastcache==1.1.0=py37h1de35cc_0
    - filelock==3.0.12=py_0
    - flake8==3.7.9=py37_0
    - flask==1.1.1=py_0
    - freetype==2.9.1=hb4e5f40_0
    - fsspec==0.6.2=py_0
    - future==0.18.2=py37_0
    - get_terminal_size==1.0.0=h7520d66_0
    - gettext==0.19.8.1=h15daf44_3
    - gevent==1.4.0=py37h1de35cc_0
    - glib==2.63.1=hd977a24_0
    - glob2==0.7=py_0
    - gmp==6.1.2=hb37e062_1
    - gmpy2==2.0.8=py37h6ef4df4_2
    - greenlet==0.4.15=py37h1de35cc_0
    - h5py==2.10.0=py37h3134771_0
    - hdf5==1.10.4=hfa1e0ec_0
    - heapdict==1.0.1=py_0
    - html5lib==1.0.1=py37_0
    - hypothesis==5.5.4=py_0
    - icu==58.2=h4b95b61_1
    - idna==2.8=py37_0
    - imageio==2.6.1=py37_0
    - imagesize==1.2.0=py_0
    - importlib_metadata==1.5.0=py37_0
    - intel-openmp==2019.4=233
    - intervaltree==3.0.2=py_0
    - ipykernel==5.1.4=py37h39e3cac_0
    - ipython==7.12.0=py37h5ca1d4c_0
    - ipython_genutils==0.2.0=py37_0
    - ipywidgets==7.5.1=py_0
    - isort==4.3.21=py37_0
    - itsdangerous==1.1.0=py37_0
    - jbig==2.1=h4d881f8_0
    - jdcal==1.4.1=py_0
    - jedi==0.14.1=py37_0
    - jinja2==2.11.1=py_0
    - joblib==0.14.1=py_0
    - jpeg==9b=he5867d9_2
    - json5==0.9.1=py_0
    - jsonschema==3.2.0=py37_0
    - jupyter==1.0.0=py37_7
    - jupyter_client==5.3.4=py37_0
    - jupyter_console==6.1.0=py_0
    - jupyter_core==4.6.1=py37_0
    - jupyterlab==1.2.6=pyhf63ae98_0
    - jupyterlab_server==1.0.6=py_0
    - keyring==21.1.0=py37_0
    - kiwisolver==1.1.0=py37h0a44026_0
    - krb5==1.17.1=hddcf347_0
    - lazy-object-proxy==1.4.3=py37h1de35cc_0
    - libarchive==3.3.3=h786848e_5
    - libcurl==7.68.0=h051b688_0
    - libcxx==4.0.1=hcfea43d_1
    - libcxxabi==4.0.1=hcfea43d_1
    - libedit==3.1.20181209=hb402a30_0
    - libffi==3.2.1=h475c297_4
    - libgfortran==3.0.1=h93005f0_2
    - libiconv==1.15=hdd342a3_7
    - liblief==0.9.0=h2a1bed3_2
    - libpng==1.6.37=ha441bb4_0
    - libsodium==1.0.16=h3efe00b_0
    - libspatialindex==1.9.3=h0a44026_0
    - libssh2==1.8.2=ha12b0ac_0
    - libtiff==4.1.0=hcb84e12_0
    - libxml2==2.9.9=hf6e021a_1
    - libxslt==1.1.33=h33a18ac_0
    - llvm-openmp==4.0.1=hcfea43d_1
    - llvmlite==0.31.0=py37h1341992_0
    - locket==0.2.0=py37_1
    - lxml==4.5.0=py37hef8c89e_0
    - lz4-c==1.8.1.2=h1de35cc_0
    - lzo==2.10=h362108e_2
    - markupsafe==1.1.1=py37h1de35cc_0
    - matplotlib-base==3.1.3=py37h9aa3819_0
    - matplotlib==3.1.3=py37_0
    - mccabe==0.6.1=py37_1
    - mistune==0.8.4=py37h1de35cc_0
    - mkl-service==2.3.0=py37hfbe908c_0
    - mkl==2019.4=233
    - mkl_fft==1.0.15=py37h5e564d8_0
    - mkl_random==1.1.0=py37ha771720_0
    - mock==4.0.1=py_0
    - more-itertools==8.2.0=py_0
    - mpc==1.1.0=h6ef4df4_1
    - mpfr==4.0.1=h3018a27_3
    - mpmath==1.1.0=py37_0
    - msgpack-python==0.6.1=py37h04f5b5a_1
    - multipledispatch==0.6.0=py37_0
    - navigator-updater==0.2.1=py37_0
    - nbconvert==5.6.1=py37_0
    - nbformat==5.0.4=py_0
    - ncurses==6.2=h0a44026_0
    - networkx==2.4=py_0
    - nltk==3.4.5=py37_0
    - nose==1.3.7=py37_2
    - notebook==6.0.3=py37_0
    - numba==0.48.0=py37h6c726b0_0
    - numexpr==2.7.1=py37hce01a72_0
    - numpy-base==1.18.1=py37h6575580_1
    - numpy==1.18.1=py37h7241aed_0
    - numpydoc==0.9.2=py_0
    - olefile==0.46=py37_0
    - openpyxl==3.0.3=py_0
    - openssl==1.1.1d=h1de35cc_4
    - packaging==20.1=py_0
    - pandas==1.0.1=py37h6c726b0_0
    - pandoc==2.2.3.2=0
    - pandocfilters==1.4.2=py37_1
    - parso==0.5.2=py_0
    - partd==1.1.0=py_0
    - path.py==12.4.0=0
    - path==13.1.0=py37_0
    - pathlib2==2.3.5=py37_0
    - pathtools==0.1.2=py_1
    - patsy==0.5.1=py37_0
    - pcre==8.43=h0a44026_0
    - pep8==1.7.1=py37_0
    - pexpect==4.8.0=py37_0
    - pickleshare==0.7.5=py37_0
    - pillow==7.0.0=py37h4655f20_0
    - pip==20.0.2=py37_1
    - pkginfo==1.5.0.1=py37_0
    - pluggy==0.13.1=py37_0
    - ply==3.11=py37_0
    - prometheus_client==0.7.1=py_0
    - prompt_toolkit==3.0.3=py_0
    - psutil==5.6.7=py37h1de35cc_0
    - ptyprocess==0.6.0=py37_0
    - py-lief==0.9.0=py37h1413db1_2
    - py==1.8.1=py_0
    - pycodestyle==2.5.0=py37_0
    - pycosat==0.6.3=py37h1de35cc_0
    - pycparser==2.19=py37_0
    - pycrypto==2.6.1=py37h1de35cc_9
    - pycurl==7.43.0.5=py37ha12b0ac_0
    - pydocstyle==4.0.1=py_0
    - pyflakes==2.1.1=py37_0
    - pygments==2.5.2=py_0
    - pylint==2.4.4=py37_0
    - pyodbc==4.0.30=py37h0a44026_0
    - pyopenssl==19.1.0=py37_0
    - pyparsing==2.4.6=py_0
    - pyqt==5.9.2=py37h655552a_2
    - pyrsistent==0.15.7=py37h1de35cc_0
    - pysocks==1.7.1=py37_0
    - pytables==3.6.1=py37h5bccee9_0
    - pytest-arraydiff==0.3=py37h39e3cac_0
    - pytest-astropy-header==0.1.2=py_0
    - pytest-astropy==0.8.0=py_0
    - pytest-doctestplus==0.5.0=py_0
    - pytest-openfiles==0.4.0=py_0
    - pytest-remotedata==0.3.2=py37_0
    - pytest==5.3.5=py37_0
    - python-dateutil==2.8.1=py_0
    - python-jsonrpc-server==0.3.4=py_0
    - python-language-server==0.31.7=py37_0
    - python-libarchive-c==2.8=py37_13
    - python.app==2=py37_10
    - python==3.7.6=h359304d_2
    - pytz==2019.3=py_0
    - pywavelets==1.1.1=py37h1de35cc_0
    - pyyaml==5.3=py37h1de35cc_0
    - pyzmq==18.1.1=py37h0a44026_0
    - qdarkstyle==2.8=py_0
    - qt==5.9.7=h468cd18_1
    - qtawesome==0.6.1=py_0
    - qtconsole==4.6.0=py_1
    - qtpy==1.9.0=py_0
    - readline==7.0=h1de35cc_5
    - requests==2.22.0=py37_1
    - ripgrep==11.0.2=he32d670_0
    - rope==0.16.0=py_0
    - rtree==0.9.3=py37_0
    - ruamel_yaml==0.15.87=py37h1de35cc_0
    - scikit-image==0.16.2=py37h6c726b0_0
    - scikit-learn==0.22.1=py37h27c97d8_0
    - scipy==1.4.1=py37h9fa6033_0
    - seaborn==0.10.0=py_0
    - send2trash==1.5.0=py37_0
    - setuptools==45.2.0=py37_0
    - simplegeneric==0.8.1=py37_2
    - singledispatch==3.4.0.3=py37_0
    - sip==4.19.8=py37h0a44026_0
    - six==1.14.0=py37_0
    - snappy==1.1.7=he62c110_3
    - snowballstemmer==2.0.0=py_0
    - sortedcollections==1.1.2=py37_0
    - sortedcontainers==2.1.0=py37_0
    - soupsieve==1.9.5=py37_0
    - sphinx==2.4.0=py_0
    - sphinxcontrib-applehelp==1.0.1=py_0
    - sphinxcontrib-devhelp==1.0.1=py_0
    - sphinxcontrib-htmlhelp==1.0.2=py_0
    - sphinxcontrib-jsmath==1.0.1=py_0
    - sphinxcontrib-qthelp==1.0.2=py_0
    - sphinxcontrib-serializinghtml==1.1.3=py_0
    - sphinxcontrib-websupport==1.2.0=py_0
    - sphinxcontrib==1.0=py37_1
    - spyder-kernels==1.8.1=py37_0
    - spyder==4.0.1=py37_0
    - sqlalchemy==1.3.13=py37h1de35cc_0
    - sqlite==3.31.1=ha441bb4_0
    - statsmodels==0.11.0=py37h1de35cc_0
    - sympy==1.5.1=py37_0
    - tbb==2020.0=h04f5b5a_0
    - tblib==1.6.0=py_0
    - terminado==0.8.3=py37_0
    - testpath==0.4.4=py_0
    - tk==8.6.8=ha441bb4_0
    - toolz==0.10.0=py_0
    - tornado==6.0.3=py37h1de35cc_3
    - tqdm==4.42.1=py_0
    - traitlets==4.3.3=py37_0
    - ujson==1.35=py37h1de35cc_0
    - unicodecsv==0.14.1=py37_0
    - unixodbc==2.3.7=h1de35cc_0
    - urllib3==1.25.8=py37_0
    - watchdog==0.10.2=py37h1de35cc_0
    - wcwidth==0.1.8=py_0
    - webencodings==0.5.1=py37_1
    - werkzeug==1.0.0=py_0
    - wheel==0.34.2=py37_0
    - widgetsnbextension==3.5.1=py37_0
    - wrapt==1.11.2=py37h1de35cc_0
    - wurlitzer==2.0.0=py37_0
    - xlrd==1.2.0=py37_0
    - xlsxwriter==1.2.7=py_0
    - xlwings==0.17.1=py37_0
    - xlwt==1.3.0=py37_0
    - xmltodict==0.12.0=py_0
    - xz==5.2.4=h1de35cc_4
    - yaml==0.1.7=hc338f04_2
    - yapf==0.28.0=py_0
    - zeromq==4.3.1=h0a44026_3
    - zict==1.0.0=py_0
    - zipp==2.2.0=py_0
    - zlib==1.2.11=h1de35cc_3
    - zstd==1.3.7=h5bba6e5_0


The following NEW packages will be INSTALLED:

  _ipyw_jlab_nb_ext~ pkgs/main/osx-64::_ipyw_jlab_nb_ext_conf-0.1.0-py37_0
  alabaster          pkgs/main/osx-64::alabaster-0.7.12-py37_0
  anaconda           pkgs/main/osx-64::anaconda-2020.02-py37_0
  anaconda-client    pkgs/main/osx-64::anaconda-client-1.7.2-py37_0
  anaconda-navigator pkgs/main/osx-64::anaconda-navigator-1.9.12-py37_0
  anaconda-project   pkgs/main/noarch::anaconda-project-0.8.4-py_0
  applaunchservices  pkgs/main/noarch::applaunchservices-0.2.1-py_0
  appnope            pkgs/main/osx-64::appnope-0.1.0-py37_0
  appscript          pkgs/main/osx-64::appscript-1.1.0-py37h1de35cc_0
  argh               pkgs/main/osx-64::argh-0.26.2-py37_0
  asn1crypto         pkgs/main/osx-64::asn1crypto-1.3.0-py37_0
  astroid            pkgs/main/osx-64::astroid-2.3.3-py37_0
  astropy            pkgs/main/osx-64::astropy-4.0-py37h1de35cc_0
  atomicwrites       pkgs/main/osx-64::atomicwrites-1.3.0-py37_1
  attrs              pkgs/main/noarch::attrs-19.3.0-py_0
  autopep8           pkgs/main/noarch::autopep8-1.4.4-py_0
  babel              pkgs/main/noarch::babel-2.8.0-py_0
  backcall           pkgs/main/osx-64::backcall-0.1.0-py37_0
  backports          pkgs/main/noarch::backports-1.0-py_2
  backports.functoo~ pkgs/main/noarch::backports.functools_lru_cache-1.6.1-py_0
  backports.shutil_~ pkgs/main/osx-64::backports.shutil_get_terminal_size-1.0.0-py37_2
  backports.tempfile pkgs/main/noarch::backports.tempfile-1.0-py_1
  backports.weakref  pkgs/main/noarch::backports.weakref-1.0.post1-py_1
  beautifulsoup4     pkgs/main/osx-64::beautifulsoup4-4.8.2-py37_0
  bitarray           pkgs/main/osx-64::bitarray-1.2.1-py37h1de35cc_0
  bkcharts           pkgs/main/osx-64::bkcharts-0.2-py37_0
  blas               pkgs/main/osx-64::blas-1.0-mkl
  bleach             pkgs/main/osx-64::bleach-3.1.0-py37_0
  blosc              pkgs/main/osx-64::blosc-1.16.3-hd9629dc_0
  bokeh              pkgs/main/osx-64::bokeh-1.4.0-py37_0
  boto               pkgs/main/osx-64::boto-2.49.0-py37_0
  bottleneck         pkgs/main/osx-64::bottleneck-1.3.2-py37h776bbcc_0
  bzip2              pkgs/main/osx-64::bzip2-1.0.8-h1de35cc_0
  ca-certificates    pkgs/main/osx-64::ca-certificates-2020.1.1-0
  certifi            pkgs/main/osx-64::certifi-2019.11.28-py37_0
  cffi               pkgs/main/osx-64::cffi-1.14.0-py37hb5b8e2f_0
  chardet            pkgs/main/osx-64::chardet-3.0.4-py37_1003
  click              pkgs/main/osx-64::click-7.0-py37_0
  cloudpickle        pkgs/main/noarch::cloudpickle-1.3.0-py_0
  clyent             pkgs/main/osx-64::clyent-1.2.2-py37_1
  colorama           pkgs/main/noarch::colorama-0.4.3-py_0
  conda              pkgs/main/osx-64::conda-4.8.2-py37_0
  conda-build        pkgs/main/osx-64::conda-build-3.18.11-py37_0
  conda-env          pkgs/main/osx-64::conda-env-2.6.0-1
  conda-package-han~ pkgs/main/osx-64::conda-package-handling-1.6.0-py37h1de35cc_0
  conda-verify       pkgs/main/noarch::conda-verify-3.4.2-py_1
  contextlib2        pkgs/main/noarch::contextlib2-0.6.0.post1-py_0
  cryptography       pkgs/main/osx-64::cryptography-2.8-py37ha12b0ac_0
  curl               pkgs/main/osx-64::curl-7.68.0-ha441bb4_0
  cycler             pkgs/main/osx-64::cycler-0.10.0-py37_0
  cython             pkgs/main/osx-64::cython-0.29.15-py37h0a44026_0
  cytoolz            pkgs/main/osx-64::cytoolz-0.10.1-py37h1de35cc_0
  dask               pkgs/main/noarch::dask-2.11.0-py_0
  dask-core          pkgs/main/noarch::dask-core-2.11.0-py_0
  dbus               pkgs/main/osx-64::dbus-1.13.12-h90a0687_0
  decorator          pkgs/main/noarch::decorator-4.4.1-py_0
  defusedxml         pkgs/main/noarch::defusedxml-0.6.0-py_0
  diff-match-patch   pkgs/main/noarch::diff-match-patch-20181111-py_0
  distributed        pkgs/main/osx-64::distributed-2.11.0-py37_0
  docutils           pkgs/main/osx-64::docutils-0.16-py37_0
  entrypoints        pkgs/main/osx-64::entrypoints-0.3-py37_0
  et_xmlfile         pkgs/main/osx-64::et_xmlfile-1.0.1-py37_0
  expat              pkgs/main/osx-64::expat-2.2.6-h0a44026_0
  fastcache          pkgs/main/osx-64::fastcache-1.1.0-py37h1de35cc_0
  filelock           pkgs/main/noarch::filelock-3.0.12-py_0
  flake8             pkgs/main/osx-64::flake8-3.7.9-py37_0
  flask              pkgs/main/noarch::flask-1.1.1-py_0
  freetype           pkgs/main/osx-64::freetype-2.9.1-hb4e5f40_0
  fsspec             pkgs/main/noarch::fsspec-0.6.2-py_0
  future             pkgs/main/osx-64::future-0.18.2-py37_0
  get_terminal_size  pkgs/main/osx-64::get_terminal_size-1.0.0-h7520d66_0
  gettext            pkgs/main/osx-64::gettext-0.19.8.1-h15daf44_3
  gevent             pkgs/main/osx-64::gevent-1.4.0-py37h1de35cc_0
  glib               pkgs/main/osx-64::glib-2.63.1-hd977a24_0
  glob2              pkgs/main/noarch::glob2-0.7-py_0
  gmp                pkgs/main/osx-64::gmp-6.1.2-hb37e062_1
  gmpy2              pkgs/main/osx-64::gmpy2-2.0.8-py37h6ef4df4_2
  greenlet           pkgs/main/osx-64::greenlet-0.4.15-py37h1de35cc_0
  h5py               pkgs/main/osx-64::h5py-2.10.0-py37h3134771_0
  hdf5               pkgs/main/osx-64::hdf5-1.10.4-hfa1e0ec_0
  heapdict           pkgs/main/noarch::heapdict-1.0.1-py_0
  html5lib           pkgs/main/osx-64::html5lib-1.0.1-py37_0
  hypothesis         pkgs/main/noarch::hypothesis-5.5.4-py_0
  icu                pkgs/main/osx-64::icu-58.2-h4b95b61_1
  idna               pkgs/main/osx-64::idna-2.8-py37_0
  imageio            pkgs/main/osx-64::imageio-2.6.1-py37_0
  imagesize          pkgs/main/noarch::imagesize-1.2.0-py_0
  importlib_metadata pkgs/main/osx-64::importlib_metadata-1.5.0-py37_0
  intel-openmp       pkgs/main/osx-64::intel-openmp-2019.4-233
  intervaltree       pkgs/main/noarch::intervaltree-3.0.2-py_0
  ipykernel          pkgs/main/osx-64::ipykernel-5.1.4-py37h39e3cac_0
  ipython            pkgs/main/osx-64::ipython-7.12.0-py37h5ca1d4c_0
  ipython_genutils   pkgs/main/osx-64::ipython_genutils-0.2.0-py37_0
  ipywidgets         pkgs/main/noarch::ipywidgets-7.5.1-py_0
  isort              pkgs/main/osx-64::isort-4.3.21-py37_0
  itsdangerous       pkgs/main/osx-64::itsdangerous-1.1.0-py37_0
  jbig               pkgs/main/osx-64::jbig-2.1-h4d881f8_0
  jdcal              pkgs/main/noarch::jdcal-1.4.1-py_0
  jedi               pkgs/main/osx-64::jedi-0.14.1-py37_0
  jinja2             pkgs/main/noarch::jinja2-2.11.1-py_0
  joblib             pkgs/main/noarch::joblib-0.14.1-py_0
  jpeg               pkgs/main/osx-64::jpeg-9b-he5867d9_2
  json5              pkgs/main/noarch::json5-0.9.1-py_0
  jsonschema         pkgs/main/osx-64::jsonschema-3.2.0-py37_0
  jupyter            pkgs/main/osx-64::jupyter-1.0.0-py37_7
  jupyter_client     pkgs/main/osx-64::jupyter_client-5.3.4-py37_0
  jupyter_console    pkgs/main/noarch::jupyter_console-6.1.0-py_0
  jupyter_core       pkgs/main/osx-64::jupyter_core-4.6.1-py37_0
  jupyterlab         pkgs/main/noarch::jupyterlab-1.2.6-pyhf63ae98_0
  jupyterlab_server  pkgs/main/noarch::jupyterlab_server-1.0.6-py_0
  keyring            pkgs/main/osx-64::keyring-21.1.0-py37_0
  kiwisolver         pkgs/main/osx-64::kiwisolver-1.1.0-py37h0a44026_0
  krb5               pkgs/main/osx-64::krb5-1.17.1-hddcf347_0
  lazy-object-proxy  pkgs/main/osx-64::lazy-object-proxy-1.4.3-py37h1de35cc_0
  libarchive         pkgs/main/osx-64::libarchive-3.3.3-h786848e_5
  libcurl            pkgs/main/osx-64::libcurl-7.68.0-h051b688_0
  libcxx             pkgs/main/osx-64::libcxx-4.0.1-hcfea43d_1
  libcxxabi          pkgs/main/osx-64::libcxxabi-4.0.1-hcfea43d_1
  libedit            pkgs/main/osx-64::libedit-3.1.20181209-hb402a30_0
  libffi             pkgs/main/osx-64::libffi-3.2.1-h475c297_4
  libgfortran        pkgs/main/osx-64::libgfortran-3.0.1-h93005f0_2
  libiconv           pkgs/main/osx-64::libiconv-1.15-hdd342a3_7
  liblief            pkgs/main/osx-64::liblief-0.9.0-h2a1bed3_2
  libpng             pkgs/main/osx-64::libpng-1.6.37-ha441bb4_0
  libsodium          pkgs/main/osx-64::libsodium-1.0.16-h3efe00b_0
  libspatialindex    pkgs/main/osx-64::libspatialindex-1.9.3-h0a44026_0
  libssh2            pkgs/main/osx-64::libssh2-1.8.2-ha12b0ac_0
  libtiff            pkgs/main/osx-64::libtiff-4.1.0-hcb84e12_0
  libxml2            pkgs/main/osx-64::libxml2-2.9.9-hf6e021a_1
  libxslt            pkgs/main/osx-64::libxslt-1.1.33-h33a18ac_0
  llvm-openmp        pkgs/main/osx-64::llvm-openmp-4.0.1-hcfea43d_1
  llvmlite           pkgs/main/osx-64::llvmlite-0.31.0-py37h1341992_0
  locket             pkgs/main/osx-64::locket-0.2.0-py37_1
  lxml               pkgs/main/osx-64::lxml-4.5.0-py37hef8c89e_0
  lz4-c              pkgs/main/osx-64::lz4-c-1.8.1.2-h1de35cc_0
  lzo                pkgs/main/osx-64::lzo-2.10-h362108e_2
  markupsafe         pkgs/main/osx-64::markupsafe-1.1.1-py37h1de35cc_0
  matplotlib         pkgs/main/osx-64::matplotlib-3.1.3-py37_0
  matplotlib-base    pkgs/main/osx-64::matplotlib-base-3.1.3-py37h9aa3819_0
  mccabe             pkgs/main/osx-64::mccabe-0.6.1-py37_1
  mistune            pkgs/main/osx-64::mistune-0.8.4-py37h1de35cc_0
  mkl                pkgs/main/osx-64::mkl-2019.4-233
  mkl-service        pkgs/main/osx-64::mkl-service-2.3.0-py37hfbe908c_0
  mkl_fft            pkgs/main/osx-64::mkl_fft-1.0.15-py37h5e564d8_0
  mkl_random         pkgs/main/osx-64::mkl_random-1.1.0-py37ha771720_0
  mock               pkgs/main/noarch::mock-4.0.1-py_0
  more-itertools     pkgs/main/noarch::more-itertools-8.2.0-py_0
  mpc                pkgs/main/osx-64::mpc-1.1.0-h6ef4df4_1
  mpfr               pkgs/main/osx-64::mpfr-4.0.1-h3018a27_3
  mpmath             pkgs/main/osx-64::mpmath-1.1.0-py37_0
  msgpack-python     pkgs/main/osx-64::msgpack-python-0.6.1-py37h04f5b5a_1
  multipledispatch   pkgs/main/osx-64::multipledispatch-0.6.0-py37_0
  navigator-updater  pkgs/main/osx-64::navigator-updater-0.2.1-py37_0
  nbconvert          pkgs/main/osx-64::nbconvert-5.6.1-py37_0
  nbformat           pkgs/main/noarch::nbformat-5.0.4-py_0
  ncurses            pkgs/main/osx-64::ncurses-6.2-h0a44026_0
  networkx           pkgs/main/noarch::networkx-2.4-py_0
  nltk               pkgs/main/osx-64::nltk-3.4.5-py37_0
  nose               pkgs/main/osx-64::nose-1.3.7-py37_2
  notebook           pkgs/main/osx-64::notebook-6.0.3-py37_0
  numba              pkgs/main/osx-64::numba-0.48.0-py37h6c726b0_0
  numexpr            pkgs/main/osx-64::numexpr-2.7.1-py37hce01a72_0
  numpy              pkgs/main/osx-64::numpy-1.18.1-py37h7241aed_0
  numpy-base         pkgs/main/osx-64::numpy-base-1.18.1-py37h6575580_1
  numpydoc           pkgs/main/noarch::numpydoc-0.9.2-py_0
  olefile            pkgs/main/osx-64::olefile-0.46-py37_0
  openpyxl           pkgs/main/noarch::openpyxl-3.0.3-py_0
  openssl            pkgs/main/osx-64::openssl-1.1.1d-h1de35cc_4
  packaging          pkgs/main/noarch::packaging-20.1-py_0
  pandas             pkgs/main/osx-64::pandas-1.0.1-py37h6c726b0_0
  pandoc             pkgs/main/osx-64::pandoc-2.2.3.2-0
  pandocfilters      pkgs/main/osx-64::pandocfilters-1.4.2-py37_1
  parso              pkgs/main/noarch::parso-0.5.2-py_0
  partd              pkgs/main/noarch::partd-1.1.0-py_0
  path               pkgs/main/osx-64::path-13.1.0-py37_0
  path.py            pkgs/main/noarch::path.py-12.4.0-0
  pathlib2           pkgs/main/osx-64::pathlib2-2.3.5-py37_0
  pathtools          pkgs/main/noarch::pathtools-0.1.2-py_1
  patsy              pkgs/main/osx-64::patsy-0.5.1-py37_0
  pcre               pkgs/main/osx-64::pcre-8.43-h0a44026_0
  pep8               pkgs/main/osx-64::pep8-1.7.1-py37_0
  pexpect            pkgs/main/osx-64::pexpect-4.8.0-py37_0
  pickleshare        pkgs/main/osx-64::pickleshare-0.7.5-py37_0
  pillow             pkgs/main/osx-64::pillow-7.0.0-py37h4655f20_0
  pip                pkgs/main/osx-64::pip-20.0.2-py37_1
  pkginfo            pkgs/main/osx-64::pkginfo-1.5.0.1-py37_0
  pluggy             pkgs/main/osx-64::pluggy-0.13.1-py37_0
  ply                pkgs/main/osx-64::ply-3.11-py37_0
  prometheus_client  pkgs/main/noarch::prometheus_client-0.7.1-py_0
  prompt_toolkit     pkgs/main/noarch::prompt_toolkit-3.0.3-py_0
  psutil             pkgs/main/osx-64::psutil-5.6.7-py37h1de35cc_0
  ptyprocess         pkgs/main/osx-64::ptyprocess-0.6.0-py37_0
  py                 pkgs/main/noarch::py-1.8.1-py_0
  py-lief            pkgs/main/osx-64::py-lief-0.9.0-py37h1413db1_2
  pycodestyle        pkgs/main/osx-64::pycodestyle-2.5.0-py37_0
  pycosat            pkgs/main/osx-64::pycosat-0.6.3-py37h1de35cc_0
  pycparser          pkgs/main/osx-64::pycparser-2.19-py37_0
  pycrypto           pkgs/main/osx-64::pycrypto-2.6.1-py37h1de35cc_9
  pycurl             pkgs/main/osx-64::pycurl-7.43.0.5-py37ha12b0ac_0
  pydocstyle         pkgs/main/noarch::pydocstyle-4.0.1-py_0
  pyflakes           pkgs/main/osx-64::pyflakes-2.1.1-py37_0
  pygments           pkgs/main/noarch::pygments-2.5.2-py_0
  pylint             pkgs/main/osx-64::pylint-2.4.4-py37_0
  pyodbc             pkgs/main/osx-64::pyodbc-4.0.30-py37h0a44026_0
  pyopenssl          pkgs/main/osx-64::pyopenssl-19.1.0-py37_0
  pyparsing          pkgs/main/noarch::pyparsing-2.4.6-py_0
  pyqt               pkgs/main/osx-64::pyqt-5.9.2-py37h655552a_2
  pyrsistent         pkgs/main/osx-64::pyrsistent-0.15.7-py37h1de35cc_0
  pysocks            pkgs/main/osx-64::pysocks-1.7.1-py37_0
  pytables           pkgs/main/osx-64::pytables-3.6.1-py37h5bccee9_0
  pytest             pkgs/main/osx-64::pytest-5.3.5-py37_0
  pytest-arraydiff   pkgs/main/osx-64::pytest-arraydiff-0.3-py37h39e3cac_0
  pytest-astropy     pkgs/main/noarch::pytest-astropy-0.8.0-py_0
  pytest-astropy-he~ pkgs/main/noarch::pytest-astropy-header-0.1.2-py_0
  pytest-doctestplus pkgs/main/noarch::pytest-doctestplus-0.5.0-py_0
  pytest-openfiles   pkgs/main/noarch::pytest-openfiles-0.4.0-py_0
  pytest-remotedata  pkgs/main/osx-64::pytest-remotedata-0.3.2-py37_0
  python             pkgs/main/osx-64::python-3.7.6-h359304d_2
  python-dateutil    pkgs/main/noarch::python-dateutil-2.8.1-py_0
  python-jsonrpc-se~ pkgs/main/noarch::python-jsonrpc-server-0.3.4-py_0
  python-language-s~ pkgs/main/osx-64::python-language-server-0.31.7-py37_0
  python-libarchive~ pkgs/main/osx-64::python-libarchive-c-2.8-py37_13
  python.app         pkgs/main/osx-64::python.app-2-py37_10
  pytz               pkgs/main/noarch::pytz-2019.3-py_0
  pywavelets         pkgs/main/osx-64::pywavelets-1.1.1-py37h1de35cc_0
  pyyaml             pkgs/main/osx-64::pyyaml-5.3-py37h1de35cc_0
  pyzmq              pkgs/main/osx-64::pyzmq-18.1.1-py37h0a44026_0
  qdarkstyle         pkgs/main/noarch::qdarkstyle-2.8-py_0
  qt                 pkgs/main/osx-64::qt-5.9.7-h468cd18_1
  qtawesome          pkgs/main/noarch::qtawesome-0.6.1-py_0
  qtconsole          pkgs/main/noarch::qtconsole-4.6.0-py_1
  qtpy               pkgs/main/noarch::qtpy-1.9.0-py_0
  readline           pkgs/main/osx-64::readline-7.0-h1de35cc_5
  requests           pkgs/main/osx-64::requests-2.22.0-py37_1
  ripgrep            pkgs/main/osx-64::ripgrep-11.0.2-he32d670_0
  rope               pkgs/main/noarch::rope-0.16.0-py_0
  rtree              pkgs/main/osx-64::rtree-0.9.3-py37_0
  ruamel_yaml        pkgs/main/osx-64::ruamel_yaml-0.15.87-py37h1de35cc_0
  scikit-image       pkgs/main/osx-64::scikit-image-0.16.2-py37h6c726b0_0
  scikit-learn       pkgs/main/osx-64::scikit-learn-0.22.1-py37h27c97d8_0
  scipy              pkgs/main/osx-64::scipy-1.4.1-py37h9fa6033_0
  seaborn            pkgs/main/noarch::seaborn-0.10.0-py_0
  send2trash         pkgs/main/osx-64::send2trash-1.5.0-py37_0
  setuptools         pkgs/main/osx-64::setuptools-45.2.0-py37_0
  simplegeneric      pkgs/main/osx-64::simplegeneric-0.8.1-py37_2
  singledispatch     pkgs/main/osx-64::singledispatch-3.4.0.3-py37_0
  sip                pkgs/main/osx-64::sip-4.19.8-py37h0a44026_0
  six                pkgs/main/osx-64::six-1.14.0-py37_0
  snappy             pkgs/main/osx-64::snappy-1.1.7-he62c110_3
  snowballstemmer    pkgs/main/noarch::snowballstemmer-2.0.0-py_0
  sortedcollections  pkgs/main/osx-64::sortedcollections-1.1.2-py37_0
  sortedcontainers   pkgs/main/osx-64::sortedcontainers-2.1.0-py37_0
  soupsieve          pkgs/main/osx-64::soupsieve-1.9.5-py37_0
  sphinx             pkgs/main/noarch::sphinx-2.4.0-py_0
  sphinxcontrib      pkgs/main/osx-64::sphinxcontrib-1.0-py37_1
  sphinxcontrib-app~ pkgs/main/noarch::sphinxcontrib-applehelp-1.0.1-py_0
  sphinxcontrib-dev~ pkgs/main/noarch::sphinxcontrib-devhelp-1.0.1-py_0
  sphinxcontrib-htm~ pkgs/main/noarch::sphinxcontrib-htmlhelp-1.0.2-py_0
  sphinxcontrib-jsm~ pkgs/main/noarch::sphinxcontrib-jsmath-1.0.1-py_0
  sphinxcontrib-qth~ pkgs/main/noarch::sphinxcontrib-qthelp-1.0.2-py_0
  sphinxcontrib-ser~ pkgs/main/noarch::sphinxcontrib-serializinghtml-1.1.3-py_0
  sphinxcontrib-web~ pkgs/main/noarch::sphinxcontrib-websupport-1.2.0-py_0
  spyder             pkgs/main/osx-64::spyder-4.0.1-py37_0
  spyder-kernels     pkgs/main/osx-64::spyder-kernels-1.8.1-py37_0
  sqlalchemy         pkgs/main/osx-64::sqlalchemy-1.3.13-py37h1de35cc_0
  sqlite             pkgs/main/osx-64::sqlite-3.31.1-ha441bb4_0
  statsmodels        pkgs/main/osx-64::statsmodels-0.11.0-py37h1de35cc_0
  sympy              pkgs/main/osx-64::sympy-1.5.1-py37_0
  tbb                pkgs/main/osx-64::tbb-2020.0-h04f5b5a_0
  tblib              pkgs/main/noarch::tblib-1.6.0-py_0
  terminado          pkgs/main/osx-64::terminado-0.8.3-py37_0
  testpath           pkgs/main/noarch::testpath-0.4.4-py_0
  tk                 pkgs/main/osx-64::tk-8.6.8-ha441bb4_0
  toolz              pkgs/main/noarch::toolz-0.10.0-py_0
  tornado            pkgs/main/osx-64::tornado-6.0.3-py37h1de35cc_3
  tqdm               pkgs/main/noarch::tqdm-4.42.1-py_0
  traitlets          pkgs/main/osx-64::traitlets-4.3.3-py37_0
  ujson              pkgs/main/osx-64::ujson-1.35-py37h1de35cc_0
  unicodecsv         pkgs/main/osx-64::unicodecsv-0.14.1-py37_0
  unixodbc           pkgs/main/osx-64::unixodbc-2.3.7-h1de35cc_0
  urllib3            pkgs/main/osx-64::urllib3-1.25.8-py37_0
  watchdog           pkgs/main/osx-64::watchdog-0.10.2-py37h1de35cc_0
  wcwidth            pkgs/main/noarch::wcwidth-0.1.8-py_0
  webencodings       pkgs/main/osx-64::webencodings-0.5.1-py37_1
  werkzeug           pkgs/main/noarch::werkzeug-1.0.0-py_0
  wheel              pkgs/main/osx-64::wheel-0.34.2-py37_0
  widgetsnbextension pkgs/main/osx-64::widgetsnbextension-3.5.1-py37_0
  wrapt              pkgs/main/osx-64::wrapt-1.11.2-py37h1de35cc_0
  wurlitzer          pkgs/main/osx-64::wurlitzer-2.0.0-py37_0
  xlrd               pkgs/main/osx-64::xlrd-1.2.0-py37_0
  xlsxwriter         pkgs/main/noarch::xlsxwriter-1.2.7-py_0
  xlwings            pkgs/main/osx-64::xlwings-0.17.1-py37_0
  xlwt               pkgs/main/osx-64::xlwt-1.3.0-py37_0
  xmltodict          pkgs/main/noarch::xmltodict-0.12.0-py_0
  xz                 pkgs/main/osx-64::xz-5.2.4-h1de35cc_4
  yaml               pkgs/main/osx-64::yaml-0.1.7-hc338f04_2
  yapf               pkgs/main/noarch::yapf-0.28.0-py_0
  zeromq             pkgs/main/osx-64::zeromq-4.3.1-h0a44026_3
  zict               pkgs/main/noarch::zict-1.0.0-py_0
  zipp               pkgs/main/noarch::zipp-2.2.0-py_0
  zlib               pkgs/main/osx-64::zlib-1.2.11-h1de35cc_3
  zstd               pkgs/main/osx-64::zstd-1.3.7-h5bba6e5_0


Preparing transaction: done
Executing transaction: \ b''
done
installation finished.
Do you wish the installer to initialize Anaconda3
by running conda init? [yes|no]
[yes] >>> yes
no change     /Users/macbook/anaconda3/condabin/conda
no change     /Users/macbook/anaconda3/bin/conda
no change     /Users/macbook/anaconda3/bin/conda-env
no change     /Users/macbook/anaconda3/bin/activate
no change     /Users/macbook/anaconda3/bin/deactivate
no change     /Users/macbook/anaconda3/etc/profile.d/conda.sh
no change     /Users/macbook/anaconda3/etc/fish/conf.d/conda.fish
no change     /Users/macbook/anaconda3/shell/condabin/Conda.psm1
no change     /Users/macbook/anaconda3/shell/condabin/conda-hook.ps1
no change     /Users/macbook/anaconda3/lib/python3.7/site-packages/xontrib/conda.xsh
no change     /Users/macbook/anaconda3/etc/profile.d/conda.csh
modified      /Users/macbook/.bash_profile

==> For changes to take effect, close and re-open your current shell. <==

If you'd prefer that conda's base environment not be activated on startup, 
   set the auto_activate_base parameter to false: 

conda config --set auto_activate_base false

Thank you for installing Anaconda3!

===========================================================================

Anaconda and JetBrains are working together to bring you Anaconda-powered
environments tightly integrated in the PyCharm IDE.

PyCharm for Anaconda is available at:
https://www.anaconda.com/pycharm
