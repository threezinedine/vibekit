import os
from prompts import prompts
from templates import templates


def generate_vibekit():
    os.makedirs(".claude", exist_ok=True)
    os.makedirs(".claude/prompts", exist_ok=True)
    os.makedirs(".claude/templates", exist_ok=True)

    for name, content in prompts.items():
        with open(f".claude/prompts/{name}.md", "w") as f:
            f.write(content)

    for name, content in templates.items():
        with open(f".claude/templates/{name}.md", "w") as f:
            f.write(content)


if __name__ == "__main__":
    generate_vibekit()
