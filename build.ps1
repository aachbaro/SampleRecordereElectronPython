# Variables
$pythonEnv = "backend\venv"
$python = "$pythonEnv\Scripts\python.exe"
$app = "backend\app.py"
$npmCmd = "npm run electron:serve"
$npmDir = "frontend"

# Function to activate the Python environment and run app.py
function Run-Backend {
    Write-Host "Activating Python environment and running app.py..."
    & $python $app
}

# Function to run npm command
function Run-Frontend {
    Write-Host "Running npm command in frontend..."
    Push-Location $npmDir
    & npm run electron:serve
    Pop-Location
}

# Function to start both backend and frontend
function Start-All {
    Start-Job -ScriptBlock { Run-Backend }
    Run-Frontend
}

# Start the process
Start-All
