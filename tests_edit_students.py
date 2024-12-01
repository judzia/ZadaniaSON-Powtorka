import unittest
from unittest.mock import patch, mock_open
from main import edit_student  

class TestEditStudent(unittest.TestCase):

    # test - editing student
    @patch("builtins.input", side_effect=["John", "Doe", "Johnathan", "Doe"])
    @patch("main.import_from_file", return_value=[{"first_name": "John", "last_name": "Doe", "present": False}])
    @patch("main.export_attendance")
    def test_edit_student(self, mock_export, mock_import, mock_input):
        # editing students first and last name
        edit_student()

        # checking if data got updated 
        mock_export.assert_called_once_with([{"first_name": "Johnathan", "last_name": "Doe", "present": False}])

    # test - editing student that does not exist :3
    @patch("builtins.input", side_effect=["NonExisting", "Student", "Johnathan", "Doe"])
    @patch("main.import_from_file", return_value=[{"first_name": "John", "last_name": "Doe", "present": False}])
    @patch("main.export_attendance")
    def test_edit_student_not_found(self, mock_export, mock_import, mock_input):
        # trying editing non existent student
        edit_student()

        # checking if something changed
        mock_export.assert_called_once_with([{"first_name": "John", "last_name": "Doe", "present": False}])

    # test - editing student with empty data :p goofy-style
    @patch("builtins.input", side_effect=["", "", "", ""])
    @patch("main.import_from_file", return_value=[{"first_name": "John", "last_name": "Doe", "present": False}])
    @patch("main.export_attendance")
    def test_edit_student_empty_data(self, mock_export, mock_import, mock_input):
        # trying editing student with empty data
        edit_student()

        # checking if something changed???????
        mock_export.assert_called_once_with([{"first_name": "John", "last_name": "Doe", "present": False}])

if __name__ == "__main__":
    unittest.main()