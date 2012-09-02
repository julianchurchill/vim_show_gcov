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
        if os.path.exists(self.make_gcov_filename(self.initial_search_dir)):
            self.result = self.make_gcov_filename(self.initial_search_dir)
        else:
            self.search_subdirs()
        return self.result

    def search_subdirs(self):
        for entry in os.listdir(self.initial_search_dir):
            self.find_gcov_file_in_directory(
                    os.path.join(self.initial_search_dir, entry))
            if self.result != "":
                return

    def find_gcov_file_in_directory(self, path):
        if os.path.isdir(path):
            gcov_path = self.make_gcov_filename(path)
            if os.path.exists(gcov_path):
                self.result = gcov_path

    def make_gcov_filename(self, path):
        return os.path.join(path, self.filename) + FindGcovFile.gcov_extension
