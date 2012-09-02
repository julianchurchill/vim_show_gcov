import unittest
import show_gcov
import os
import shutil


class ShowGcovTests(unittest.TestCase):

    def create_dummy_file(self, file_to_create):
        f = open(file_to_create, 'w')
        f.write("some gcov file content")
        f.close

    def setUp(self):
        self.start_dir = "/tmp/test_dir" + str(os.getpid())
        if not os.path.exists(self.start_dir):
            os.makedirs(self.start_dir)

    def tearDown(self):
        shutil.rmtree(self.start_dir)

    def test_should_return_gcov_file_in_start_directory_if_there(self):
        full_cpp_path = self.start_dir + "/main.cpp"
        self.create_dummy_file(full_cpp_path + '.gcov')
        self.assertEquals(show_gcov.find_gcov_file(full_cpp_path),
                          full_cpp_path + ".gcov")

    def test_should_return_blank_if_gcov_file_not_found(self):
        full_cpp_path = self.start_dir + "/main.cpp"
        self.assertEquals(show_gcov.find_gcov_file(full_cpp_path), "")

    def test_should_only_match_gcov_file_with_same_name_as_input_file(self):
        search_cpp_path = self.start_dir + "/other.cpp"
        full_cpp_path = self.start_dir + "/main.cpp"
        self.create_dummy_file(full_cpp_path + '.gcov')
        self.assertEquals(show_gcov.find_gcov_file(search_cpp_path), "")

    def test_should_search_child_directories_of_requested_path(self):
        full_cpp_path = self.start_dir + "/main.cpp"
        gcov_path = self.start_dir + '/dir1'
        if not os.path.exists(gcov_path):
            os.makedirs(gcov_path)
        gcov_file = gcov_path + '/main.cpp.gcov'
        self.create_dummy_file(gcov_file)
        self.assertEquals(show_gcov.find_gcov_file(full_cpp_path), gcov_file)

if __name__ == "__main__":
    unittest.main()
