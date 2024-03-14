import pyvutils
from ihandler import ihandler
from .licences import LICENCES


def print_licences(licences: dict) -> None:
    for order, licence_repr in enumerate(licences.values(), start=1):
        print(f"({order}) {licence_repr}")


def main() -> None:
    print("Choose a Licence:")
    print_licences(LICENCES)
    licence_name = ihandler(input_type="numeric-choice", prompt=">>> ", choices=list(LICENCES.keys()))
    licence = pyvutils.get_file_content(f"{licence_name}.txt", relative_path="data")

    if "program" in licence:
        program = ihandler(input_type="strict-string", prompt="Program Name:\n>>> ")
        licence = licence.replace("[program]", program)
    if "[owner]" in licence:
        owner = ihandler(input_type="strict-string", prompt="Copyright Owner:\n>>> ")
        licence = licence.replace("[owner]", owner)
    if "[description]" in licence:
        description = ihandler(input_type="strict-string", prompt="Description:\n>>> ")
        licence = licence.replace("[description]", description)
    if "[year]" in licence:
        year = pyvutils.current_year_timestamp()
        licence = licence.replace("[year]", year)

    absolute_project_path = ihandler(input_type="strict-string", prompt="Project Root Path:\n>>> ")
    file_path = f"{absolute_project_path}/LICENCE"
    with open(file_path, "w", encoding="UTF-8") as licence_file:
        licence_file.write(licence)


if __name__ == "__main__":
    main()
