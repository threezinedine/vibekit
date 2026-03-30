import shutil
import os


def generate_vibekit():
    print("Generating VibeKit...")
    os.makedirs(".claude", exist_ok=True)

    shutil.copytree(
        os.path.join(os.path.dirname(__file__), "assets"),
        ".claude",
        dirs_exist_ok=True,
    )


if __name__ == "__main__":
    generate_vibekit()
