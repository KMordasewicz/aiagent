import unittest
from functions.get_fies_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

@unittest.skip("")
class TestGetFilesInfo(unittest.TestCase):

    def test_get_files_info_root(self):
        result = get_files_info("calculator", ".")
        print(result)

    def test_get_files_info_file(self):
        result = get_files_info("calculator", "pkg")
        print(result)

    def test_get_files_info_dir(self):
        result = get_files_info("calculator", "/bin")
        print(result)

    def test_get_files_info_error(self):
        result = get_files_info("calculator", "../")
        print(result)

@unittest.skip("")
class TestGetFileContent(unittest.TestCase):

    def test_lorem(self):
        result = get_file_content("calculator", "lorem.txt")
        print(result)

    def test_main(self):
        result = get_file_content("calculator", "main.py")
        print(result)

    def test_dir(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        print(result)

    def test_error(self):
        result = get_file_content("calculator", "/bin/cat")
        print(result)

@unittest.skip("")
class TestWriteFile(unittest.TestCase):

    def test_good_write(self):
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(result)

    def test_new_dir_write(self):
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(result)

    def test_error_write(self):
        result = write_file("calculator", "/tmp.temp.txt", "this should not be allowed")
        print(result)

class TestRunPythonFile(unittest.TestCase):

    def test_run_calc_main(self):
        result = run_python_file("calculator", "main.py", "3 + 5")
        print(result)

    def test_run_calc_tests(self):
        result = run_python_file("calculator", "tests.py")
        print(result)

    def test_run_error_out_wdir(self):
        result = run_python_file("calculator", "../main.py")
        print(result)

    def test_run_error_nonexist_file(self):
        result = run_python_file("calculator", "nonexistent.py")
        print(result)


if __name__ == "__main__":
    unittest.main()
