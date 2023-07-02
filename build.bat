:: PRE CLEANUP
del /f /s /q release
rmdir release

:: BUILD RELEASE FILES
pyinstaller --onefile src/cs2importer.py

::: ZIP RELEASE FILES
ren dist cs2importer
7z a cs2importer/cs2importer.zip cs2importer
ren cs2importer release

:: POST CLEANUP
rmdir build /S /Q
del cs2importer.spec
