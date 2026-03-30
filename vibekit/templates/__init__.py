import os

from vibekit.utils import load_all_md_files

templates = load_all_md_files(os.path.dirname(__file__))
