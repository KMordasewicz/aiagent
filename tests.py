import unittest
from functions.get_fies_info import get_files_info
from functions.get_file_content import get_file_content

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

    # def test_lorem(self):
    #     result = get_file_content("calculator", "lorem.txt")
    #     print(result)

    def test_main(self):
        result = get_file_content("calculator", "main.py")
        print(result)

    def test_dir(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        print(result)

    def test_error(self):
        result = get_file_content("calculator", "/bin/cat")
        print(result)



if __name__ == "__main__":
    unittest.main()
