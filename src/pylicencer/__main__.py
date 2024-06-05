import os
from pathlib import Path
import pyvutils
from ihandler import ihandler
from pylicencer.licences import LICENCES


PROJECT_ROOT_PATH = pyvutils.get_project_path()
DATA_PATH: Path = PROJECT_ROOT_PATH / "data"


def print_licences(licences: dict) -> None:
    for order, licence_repr in enumerate(licences.values(), start=1):
        print(f"({order}) {licence_repr}")


def main() -> None:
    os.system("clear")
    print("PyLicencer-CLI")
    print(len("PyLicencer-CLI") * "‾")
    print("Choose a Licence:")
    print_licences(LICENCES)
    print()
    licence_name = ihandler(input_type="numeric-choice", prompt=">>> ", choices=list(LICENCES.keys()))
    licence_content_path = DATA_PATH / f"{licence_name}.txt"
    with open(licence_content_path, "r", encoding="UTF-8") as file:
        licence_content = file.read()

    if "[program]" in licence_content:
        program = ihandler(input_type="strict-string", prompt="Program Name:\n>>> ")
        licence_content = licence_content.replace("[program]", program)
    if "[owner]" in licence_content:
        owner = ihandler(input_type="strict-string", prompt="Copyright Owner:\n>>> ")
        licence_content = licence_content.replace("[owner]", owner)
    if "[description]" in licence_content:
        description = ihandler(input_type="strict-string", prompt="Description:\n>>> ")
        licence_content = licence_content.replace("[description]", description)
    if "[year]" in licence_content:
        year = pyvutils.current_year_stamp()
        licence_content = licence_content.replace("[year]", year)

    absolute_project_path = ihandler(input_type="strict-string", prompt="Project Root Path:\n>>> ")
    file_path = os.path.join(absolute_project_path, "LICENCE")
    with open(file_path, "w", encoding="UTF-8") as licence_file:
        licence_file.write(licence_content)


if __name__ == "__main__":
    main()
