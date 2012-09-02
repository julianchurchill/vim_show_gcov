import os


def find_gcov_file(full_cpp_path):
    if os.path.exists(full_cpp_path + ".gcov"):
        return full_cpp_path + ".gcov"

    filename = os.path.basename(full_cpp_path)
    initial_search_dir = os.path.dirname(full_cpp_path)
    for dir_entry in os.listdir(initial_search_dir):
        full_entry_path = os.path.join(initial_search_dir, dir_entry)
        if os.path.isdir(full_entry_path):
            full_gcov_path = os.path.join(full_entry_path, filename) + ".gcov"
            if os.path.exists(full_gcov_path):
                return full_gcov_path

    return ""
