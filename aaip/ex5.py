import os
import stat
import time

def create_project_structure(base_path, project_name):
    # Define project structure paths
    project_path = os.path.join(base_path, project_name)
    src_path = os.path.join(project_path, 'src')
    docs_path = os.path.join(project_path, 'docs')
    readme_path = os.path.join(project_path, 'README.md')
    main_py_path = os.path.join(src_path, 'main.py')
    
    # Check if project directory already exists
    if os.path.exists(project_path):
        print(f"The project '{project_name}' already exists at {project_path}.")
        return
    
    # Create directories
    os.makedirs(src_path)  # Creates project and src directories recursively
    os.makedirs(docs_path)  # Creates docs directory
    
    # Create files with placeholder content
    with open(readme_path, 'w') as readme_file:
        readme_file.write("# Project: " + project_name + "\nThis is the README file for the project.")
    
    with open(main_py_path, 'w') as main_file:
        main_file.write("# Main script for " + project_name + "\nprint('Hello from main.py')")

    print(f"Project structure for '{project_name}' created successfully at {project_path}.")

def traverse_directory(path):
    for root, dirs, files in os.walk(path):
        print(f"Directory: {root}")
        for dir_name in dirs:
            print(f"  Subdirectory: {dir_name}")
        for file_name in files:
            print(f"  File: {file_name}")

def file_metadata(file_path):
    try:
        # Retrieve and print file size, last modified time, and creation time
        file_stats = os.stat(file_path)
        print(f"File size: {file_stats.st_size} bytes")
        print(f"Last modified: {time.ctime(file_stats.st_mtime)}")
        print(f"Creation time: {time.ctime(file_stats.st_ctime)}")
        
        # Change file permissions to read-only
        os.chmod(file_path, stat.S_IREAD)
        print(f"Permissions set to read-only for {file_path}")
        
        # Change file permissions back to writable
        os.chmod(file_path, stat.S_IWRITE)
        print(f"Permissions set back to writable for {file_path}")
    except FileNotFoundError:
        print(f"File {file_path} not found.")

def find_files_by_extension(path, extension):
    found_files = []
    for root, _, files in os.walk(path):
        for file_name in files:
            if file_name.endswith(extension):
                found_files.append(os.path.join(root, file_name))
    return found_files

def delete_files_and_directories(path):
    # Recursively delete files and directories
    for root, dirs, files in os.walk(path, topdown=False):
        for file_name in files:
            os.remove(os.path.join(root, file_name))
        for dir_name in dirs:
            os.rmdir(os.path.join(root, dir_name))
    os.rmdir(path)
    print(f"Deleted all contents and the directory itself at {path}")