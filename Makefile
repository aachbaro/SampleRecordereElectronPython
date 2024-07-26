PYTHON_ENV=backend/venv
PYTHON=$(PYTHON_ENV)/bin/python
APP=backend/app.py
NPM_CMD=npm run electron:serve
NPM_DIR=frontend

# Default target
all: start

# Target to activate the Python environment and run app.py
run-backend:
	@echo "Activating Python environment and running app.py..."
	@source $(PYTHON_ENV)/bin/activate && $(PYTHON) $(APP)

# Target to run npm command
run-frontend:
	@echo "Running npm command in frontend..."
	@cd $(NPM_DIR) && $(NPM_CMD)

# Target to start both backend and frontend
start: run-backend run-frontend

.PHONY: all run-backend run-frontend start