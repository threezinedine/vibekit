import os
from vibekit.prompts import prompts
from vibekit.templates import templates
from vibekit.utils import copy_a_file_content


def generate_vibekit():
    print("Generating VibeKit...")
    os.makedirs(".claude", exist_ok=True)
    os.makedirs(".claude/prompts", exist_ok=True)
    os.makedirs(".claude/templates", exist_ok=True)

    print("Starting to generate prompts ...")
    for name, content in prompts.items():
        print(f'\tGenerating prompt: "{name}.md"')
        with open(f".claude/prompts/{name}.md", "w") as f:
            f.write(content)

    print("Starting to generate templates ...")
    for name, content in templates.items():
        print(f'\tGenerating template: "{name}.md"')
        with open(f".claude/templates/{name}.md", "w") as f:
            f.write(content)

    copied_files = ["settings.local.json"]

    print("Starting to generate other files ...")
    for file_name in copied_files:
        print(f'\tGenerating file: "{file_name}"')
        copy_a_file_content(
            os.path.join(os.path.dirname(__file__), file_name),
            os.path.join(".claude", file_name),
        )


if __name__ == "__main__":
    generate_vibekit()
