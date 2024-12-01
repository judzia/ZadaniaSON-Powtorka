import unittest
from unittest.mock import patch, mock_open
from main import *  #  importing functions


class TestAddStudent(unittest.TestCase):

    # adding valid data :p

    @patch("builtins.open", new_callable=mock_open)
    @patch("builtins.input", side_effect=["John", "Doe"])    
    def test_add_valid_student(self, mock_input, mock_file):
        add_student()
        
        mock_file().write.assert_called_once_with("John,Doe,no\n") 


    # missing data (first name) - adding ivalid data :(

    @patch("builtins.input", side_effect=["", "Doe"])
    def test_add_student_missing_first_name(self, mock_input):
        with self.assertRaises(ValueError):
            add_student()

     # missing data (last name) - adding ivalid data :((

    @patch("builtins.input", side_effect=["John", ""])
    def test_add_student_missing_last_name(self, mock_input):
        with self.assertRaises(ValueError):
            add_student()


if __name__ == "__main__":
    unittest.main()
