# finalProject

# 1. Neovim (nvim):
#Linux (Ubuntu/Debian):

sudo apt-get update

sudo apt-get install neovim

#macOS (via Homebrew):

brew install neovim

#Windows:
Download the installer from the official Neovim releases page and follow the installation instructions.

# 2. Flask:
It's recommended to use a virtual environment to manage dependencies for your Flask project.

#Install virtualenv (if not already installed):

pip install virtualenv

# Create a virtual environment:
#Create a new directory for your project

mkdir my_flask_project

cd my_flask_project

#Create a virtual environment

python -m venv venv

# Activate the virtual environment:
#On Linux/macOS:

source venv/bin/activate

#On Windows:

.\venv\Scripts\activate

#Install Flask:

pip install Flask

# 3. Flask-MySQLdb:
Make sure you have MySQL installed on your system before installing Flask-MySQLdb.

#Install Flask-MySQLdb:

pip install Flask-MySQLdb

# Additional Note:
If you encounter any issues during installation, you might need to install additional dependencies based on your operating system. For example, on Linux, you might need to install development packages, and on Windows, you might need to install Visual Studio Build Tools.

Also, it's a good practice to use a requirements.txt file to manage your project dependencies. You can create one by running:

pip freeze > requirements.txt

And then, when deploying your project, you can install the dependencies with:

pip install -r requirements.txt

These steps should help you get started with Neovim, Flask, and Flask-MySQLdb.
