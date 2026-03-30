import os


def load_all_md_files(path: str) -> dict[str, str]:
    """
    Load all markdown files in the specified directory and return a dictionary
    mapping file names to their contents.

    Returns:
        dict[str, str]: A dictionary where keys are file names and values are file contents.
    """
    md_files: dict[str, str] = {}
    for filename in os.listdir(path):
        if filename.endswith(".md"):
            with open(os.path.join(path, filename), "r", encoding="utf-8") as file:
                no_ext_name = os.path.splitext(filename)[0]
                md_files[no_ext_name] = file.read()
    return md_files
