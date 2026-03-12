from aaip.ex5 import (
    create_project_structure, 
    traverse_directory, 
    file_metadata, 
    find_files_by_extension, 
    delete_files_and_directories
)
import os

# Set the base path for testing
base_path = os.getcwd()  # Current working directory
project_name = "TestProject"

# Test project structure creation
create_project_structure(base_path, project_name)

# Traverse directory
print("\nTraversing project structure:")
traverse_directory(os.path.join(base_path, project_name))

# Test file metadata and permissions on README.md
readme_path = os.path.join(base_path, project_name, "README.md")
print("\nFile metadata and permission handling:")
file_metadata(readme_path)

# Find .py files in the project
print("\nFinding .py files:")
py_files = find_files_by_extension(os.path.join(base_path, project_name), ".py")
for py_file in py_files:
    print(py_file)

# Delete the entire project directory
print("\nDeleting project directory:")
delete_files_and_directories(os.path.join(base_path, project_name))