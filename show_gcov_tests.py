import unittest
import show_gcov
import os
import shutil

class ShowGcovTests(unittest.TestCase):

    def setUp(self):
        self.start_dir = "/tmp/test_dir" + str(os.getpid())
        if not os.path.exists( self.start_dir ):
            os.makedirs( self.start_dir )

    def tearDown(self):
        shutil.rmtree( self.start_dir )

    def test_should_return_gcov_file_in_start_directory_if_there(self):
        full_cpp_path = self.start_dir + "/main.cpp"
        f = open( full_cpp_path + '.gcov', 'w' )
        f.write( "some gcov file content" )
        f.close
        self.assertEquals( show_gcov.find_gcov_file( full_cpp_path ), full_cpp_path + ".gcov" )

    def test_should_return_blank_if_gcov_file_not_found(self):
        full_cpp_path = self.start_dir + "/main.cpp"
        self.assertEquals( show_gcov.find_gcov_file( full_cpp_path ), "" )

    #def test_should_only_match_gcov_file_with_same_name_as_input_file(self):

if __name__ == "__main__":
    unittest.main()
