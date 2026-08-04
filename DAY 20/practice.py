# Create a virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Install a package
pip install django

# Show installed packages
pip list

# Export dependencies
pip freeze > requirements.txt

# Install from requirements.txt
pip install -r requirements.txt

# Deactivate
deactivate

# Check pip version
pip --version

# Upgrade pip itself
python -m pip install --upgrade pip

# Install a specific package
pip install requests

# Install a specific version of a package
pip install requests==2.31.0

# Install a package matching a minimum version
pip install "requests>=2.31.0"

# Upgrade an installed package
pip install --upgrade requests

# Uninstall a package
pip uninstall requests -y


# View all installed packages in the terminal
pip list

# Generate dependency tracking format
pip freeze

# Save current environment dependencies to a file
pip freeze > requirements.txt

# Install all dependencies listed in a requirements file
pip install -r requirements.txt

# Uninstall all dependencies listed in a requirements file
pip uninstall -r requirements.txt -y


# Show installation directory and details for a package
pip show requests

# List global packages (run this outside a virtual environment)
pip list --user

# Check installed packages for compatibility conflicts
pip check

# Clear the local pip download cache
pip cache purge
