# This script is gonna be used to update dependencies

.\.venv\Scripts\activate.ps1
Write-Host "writing requirements.txt file..." -ForegroundColor Blue
python -m pip freeze > .\requirements.txt
deactivate