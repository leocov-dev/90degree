@echo OFF

set SITE_3="C:\py_env\90degree\Lib\site-packages"
set SITE_27="C:\py_env\90degree27\Lib\site-packages"
set REPO="C:\repos_dev\90degree"

echo BUILDING py3.x bundle
"%SITE_3%\PySide2\pyside2-rcc.exe" ^
    -o "%REPO%\90degree\rcc_bundles\bundle_pyside2.py" ^
    "%REPO%\.resources\style.qrc"

echo BUILDING py2.7 bundle
"%SITE_27%\PySide\pyside-rcc.exe" ^
    -o "%REPO%\90degree\rcc_bundles\bundle_pyside.py" ^
    "%REPO%\.resources\style.qrc"