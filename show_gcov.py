import os


def find_gcov_file(full_cpp_path):
    if not os.path.exists(full_cpp_path + ".gcov"):
        return ""
    return full_cpp_path + ".gcov"
