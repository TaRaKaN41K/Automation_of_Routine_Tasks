from pathlib import Path


def print_directory_tree(directory: str, indent=""):
    for item in sorted(Path(directory).iterdir()):
        if item.is_dir():
            print(f"{indent}📁 {item.name}")
            print_directory_tree(item, indent + "    ")
        else:
            print(f"{indent}📄 {item.name}")


your_directory = str(input("Directory: "))
print(f"Схема содержимого директории {your_directory}:\n")
print_directory_tree(your_directory)
