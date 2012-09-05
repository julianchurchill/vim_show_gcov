import os


def find_gcov_file(full_cpp_path):
    f = FindGcovFile(full_cpp_path)
    return f.find_gcov_file()


class FindGcovFile:
    gcov_extension = ".gcov"

    def __init__(self, full_cpp_path):
        self.full_cpp_path = full_cpp_path
        self.filename = os.path.basename(self.full_cpp_path)
        self.initial_search_dir = os.path.dirname(self.full_cpp_path)
        self.result = ""

    def find_gcov_file(self):
        return self.find_gcov_file_recursive(self.initial_search_dir)

    def find_gcov_file_recursive(self, start_dir):
        self.find_gcov_file_in_directory(start_dir)
        if self.result == "":
            self.search_subdirs(start_dir)
        return self.result

    def find_gcov_file_in_directory(self, path):
        gcov_path = self.make_gcov_filename(path)
        if os.path.exists(gcov_path):
            self.result = gcov_path

    def search_subdirs(self, search_dir):
        for entry in os.listdir(search_dir):
            path = os.path.join(search_dir, entry)
            if os.path.isdir(path):
                self.find_gcov_file_recursive(path)
                if self.result != "":
                    break

    def make_gcov_filename(self, path):
        return os.path.join(path, self.filename) + FindGcovFile.gcov_extension
