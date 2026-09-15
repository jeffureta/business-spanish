import os

OUTPUT_FILE = "project_structure.txt"
IGNORE_DEEP_INSPECT = {".git", "venv", ".venv", "env", "__pycache__", "node_modules"}

def scan_directory(root_dir=".", max_depth=3):
    lines = []
    root_dir = os.path.abspath(root_dir)
    root_name = os.path.basename(root_dir)
    lines.append(f"{root_name}/")

    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Determine current depth relative to root
        rel_path = os.path.relpath(dirpath, root_dir)
        if rel_path == ".":
            depth = 0
        else:
            depth = rel_path.count(os.sep) + 1

        if depth > max_depth:
            continue

        indent = "    " * depth

        # Print current folder (if not root)
        if rel_path != ".":
            folder_name = os.path.basename(dirpath)
            lines.append(f"{indent[:-4]}└── {folder_name}/")

        # Skip inspecting contents of massive internal environment folders
        current_folder = os.path.basename(dirpath)
        if current_folder in IGNORE_DEEP_INSPECT:
            dirnames.clear()
            continue

        # Add files inside current folder
        sub_indent = "    " * (depth + 1)
        for f in sorted(filenames):
            if f != OUTPUT_FILE:
                lines.append(f"{sub_indent[:-4]}├── {f}")

    return "\n".join(lines)

if __name__ == "__main__":
    tree = scan_directory()
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(tree)
    print(f"Directory structure written to: {OUTPUT_FILE}")