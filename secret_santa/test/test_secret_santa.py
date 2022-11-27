""" Unittest for the secret santa application
"""
from unittest.mock import patch
import unittest
from ..src import secret_santa


class TestSecretSanta(unittest.TestCase):
    """TestSecretSanta Unittest for the secret santa application

    :param unittest:
    :type unittest:
    """

    def setUp(self):
        """setUp test setup"""
        self.family = secret_santa.Family(member_names={"a", "b", "c"})

    def test_secret_santa_matcher(self):
        """test_secret_santa_matcher test secret_santa_matcher method"""
        self.assertIn(
            self.family.secret_santa_matcher(),
            [{"a": "b", "b": "c", "c": "a"}, {"a": "c", "b": "a", "c": "b"}],
        )

    def test_exception_secret_santa_matcher(self):
        """test_exception_secret_santa_matcher secret_santa_matcher
        for exception
        """
        var_family = secret_santa.Family(member_names={"a"})
        self.assertRaises(ValueError, var_family.secret_santa_matcher)

    def test_unmatched_members(self):
        """test_unmatched_members _summary_"""
        self.assertEqual(self.family.unmatched_members({"a": "b"}), {"c"})

    @patch("builtins.print")
    @patch("app.src.secret_santa.Main._read_input")
    def test_get_family_details(self, mock_read_input, mock_print):
        """test_get_family_details test get_family_details

        :param read_input: mock value for the _read_input function
        :type read_input: MagicMock
        """
        mock_print.return_value=""
        mock_read_input.side_effect = ["a", "b", "c", "d", ""]
        self.assertEqual(
            secret_santa.Main.get_family_details(), set(["a", "b", "c", "d"])
        )

    @patch("builtins.print")
    @patch('app.src.secret_santa.Main._read_input')
    def test_two_inputs_get_family_details(self, mock_read_input, mock_print):
        """test_two_inputs_get_family_details test get_family_details

        :param _read_input: mock value for input method
        :type _read_input: MagicMock
        """
        mock_print.return_value=""
        mock_read_input.side_effect = ['a','b','']
        self.assertRaises(ValueError,secret_santa.Main.get_family_details)


if __name__ == "__main__":
    unittest.main()
