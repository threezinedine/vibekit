import os
from vibekit.utils import load_all_md_files

# Load all markdown files in the current directory and store them in a dictionary
prompts = load_all_md_files(os.path.dirname(__file__))
