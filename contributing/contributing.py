from pathlib import Path
import fire
from jinja2 import Template
import codecs


def hello(package):
    # read the template
    with open(Path(__file__).parent / "contributingTemplate.md") as file:
        template = Template(file.read(), trim_blocks=True)

    # render the template
    rendered_file = template.render(package=package)

    # output the file
    output_file = codecs.open("CONTRIBUTING.md", "w", "utf-8")
    output_file.write(rendered_file)
    output_file.close()

    # read the template
    with open(Path(__file__).parent / "codeConductTemplate.md") as file:
        template = Template(file.read(), trim_blocks=True)

    # render the template
    rendered_file = template.render(package=package)

    # output the file
    output_file = codecs.open("CODE_OF_CONDUCT.md", "w", "utf-8")
    output_file.write(rendered_file)
    output_file.close()


if __name__ == "__main__":
    fire.Fire(hello)
