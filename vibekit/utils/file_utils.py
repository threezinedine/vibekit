def copy_a_file_content(src_file: str, dest_file: str) -> None:
    """
    Copy the content of a source file to a destination file.

    Args:
        src_file (str): The path to the source file.
        dest_file (str): The path to the destination file.
    """
    with (
        open(src_file, "r", encoding="utf-8") as src,
        open(dest_file, "w", encoding="utf-8") as dest,
    ):
        dest.write(src.read())
