@echo off

SET port=8000

IF "%1" NEQ "" (
    SET port=%1
)

echo Starte HTTP-Server auf Port %port%
python3 -m http.server %port%
