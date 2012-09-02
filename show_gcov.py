import os


def find_gcov_file(full_cpp_path):
    f = FindGcovFile(full_cpp_path)
    return f.find_gcov_file()


class FindGcovFile:
    gcov_extension = ".gcov"

    def __init__(self, full_cpp_path):
        self.full_cpp_path = full_cpp_path
        self.filename = os.path.basename(self.full_cpp_path)

    def find_gcov_file(self):
        if os.path.exists(self.full_cpp_path + FindGcovFile.gcov_extension):
            return self.full_cpp_path + FindGcovFile.gcov_extension
        return self.search_subdirs()

    def search_subdirs(self):
        initial_search_dir = os.path.dirname(self.full_cpp_path)
        for entry in os.listdir(initial_search_dir):
            file_path = self.find_gcov_file_in_directory(
                    os.path.join(initial_search_dir, entry))
            if file_path != "":
                return file_path
        return ""

    def find_gcov_file_in_directory(self, path):
        if os.path.isdir(path):
            gcov_path = os.path.join(path, self.filename) + FindGcovFile.gcov_extension
            if os.path.exists(gcov_path):
                return gcov_path
        return ""
