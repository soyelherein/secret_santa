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
        self.family = secret_santa.Family(member_names={"santa", "banta", "alexa"})

    @patch("secret_santa.src.dao_module.Dao.store_to_db")
    @patch("secret_santa.src.dao_module.Dao.read_gifts_from_db")
    def test_secret_santa_matcher(self, mock_read_gifts, mock_store_to_db):
        """test_secret_santa_matcher test secret_santa_matcher method"""
        mock_read_gifts.return_value = ()
        mock_store_to_db.return_value = True
        self.assertIn(
            self.family.secret_santa_matcher(),
            [
                {"santa": "banta", "banta": "alexa", "alexa": "santa"},
                {"santa": "alexa", "banta": "santa", "alexa": "banta"},
            ],
        )

    @patch("secret_santa.src.dao_module.Dao.store_to_db")
    @patch("secret_santa.src.dao_module.Dao.read_gifts_from_db")
    def test_exception_secret_santa_matcher(self, mock_read_gifts, mock_store_to_db):
        """test_exception_secret_santa_matcher secret_santa_matcher
        for exception
        """
        mock_read_gifts.return_value = ()
        mock_store_to_db.return_value = True
        var_family = secret_santa.Family(member_names={"santa"})
        self.assertRaises(ValueError, var_family.secret_santa_matcher)

    def test_unit_unmatched_members(self):
        """test_unit_unmatched_members _summary_"""
        self.assertEqual(self.family.unmatched_members({"santa": "banta"}), {"alexa"})

    @patch("builtins.print")
    @patch("secret_santa.src.secret_santa.Main._read_input")
    def test_unit_get_family_details(self, mock_read_input, mock_print):
        """test_unit_get_family_details test get_family_details

        :param read_input: mock value for the _read_input function
        :type read_input: MagicMock
        """
        mock_print.return_value = ""
        mock_read_input.side_effect = ["santa", "banta", "alexa", "siri", ""]
        self.assertEqual(
            secret_santa.Main.get_family_details(),
            set(["santa", "banta", "alexa", "siri"]),
        )

    @patch("builtins.print")
    @patch("secret_santa.src.secret_santa.Main._read_input")
    def test_two_inputs_get_family_details(self, mock_read_input, mock_print):
        """test_two_inputs_get_family_details test get_family_details

        :param _read_input: mock value for input method
        :type _read_input: MagicMock
        """
        mock_print.return_value = ""
        mock_read_input.side_effect = ["santa", "banta", ""]
        self.assertRaises(ValueError, secret_santa.Main.get_family_details)

    @patch("secret_santa.src.dao_module.Dao.store_to_db")
    @patch("secret_santa.src.dao_module.Dao.read_gifts_from_db")
    @patch("secret_santa.src.dao_module.Dao.read_family_from_db")
    def test_secret_santa_matcher_part_2_consistent(
        self, mock_read_family_from_db, mock_read_gifts, mock_store_to_db
    ):
        """test_secret_santa_matcher_part_2 _summary_

        :param mock_read_gifts: _description_
        :type mock_read_gifts: _type_
        :param mock_store_to_db: _description_
        :type mock_store_to_db: _type_
        """
        mock_read_family_from_db.return_value = ()
        mock_read_gifts.return_value = [
            ("santa", "banta"),
            ("banta", "alexa"),
            ("alexa", "santa"),
        ]
        mock_store_to_db.return_value = True
        for _ in range(5):
            self.assertIn(
                self.family.secret_santa_matcher(),
                [{"santa": "alexa", "banta": "santa", "alexa": "banta"}],
            )

    @patch("secret_santa.src.dao_module.Dao.store_to_db")
    @patch("secret_santa.src.dao_module.Dao.read_gifts_from_db")
    @patch("secret_santa.src.dao_module.Dao.read_family_from_db")
    def test_secret_santa_matcher_part_2_match_with_3(
        self, mock_read_family_from_db, mock_read_gifts, mock_store_to_db
    ):
        """test_secret_santa_matcher_part_2_match_with_3 _summary_

        :param mock_read_family_from_db: _description_
        :type mock_read_family_from_db: _type_
        :param mock_read_gifts: _description_
        :type mock_read_gifts: _type_
        :param mock_store_to_db: _description_
        :type mock_store_to_db: _type_
        """
        mock_read_family_from_db.return_value = ()
        mock_read_gifts.side_effect = [
            [("santa", "banta"), ("banta", "alexa"), ("alexa", "santa")],
            [
                ("alexa", "banta"),
                ("banta", "santa"),
                ("santa", "alexa"),
                ("banta", "alexa"),
            ],
            [
                ("santa", "banta"),
                ("banta", "alexa"),
                ("alexa", "santa"),
                ("alexa", "banta"),
                ("banta", "santa"),
                ("santa", "alexa"),
            ],
        ]
        mock_store_to_db.return_value = True
        for _ in range(2):
            self.assertIn(
                self.family.secret_santa_matcher(),
                [
                    {"santa": "banta", "alexa": "santa"},
                    {"alexa": "banta", "banta": "santa", "santa": "alexa"},
                ],
            )
        self.assertRaises(ValueError, self.family.secret_santa_matcher)

    @patch("secret_santa.src.dao_module.Dao.store_to_db")
    @patch("secret_santa.src.dao_module.Dao.read_gifts_from_db")
    @patch("secret_santa.src.dao_module.Dao.read_family_from_db")
    def test_secret_santa_matcher_part_3_match_with_3(
        self, mock_read_family_from_db, mock_read_gifts, mock_store_to_db
    ):
        """test_secret_santa_matcher_part_3_match_with_3

        :param mock_read_gifts: _description_
        :type mock_read_gifts: _type_
        :param mock_store_to_db: _description_
        :type mock_store_to_db: _type_
        """

        mock_read_family_from_db.return_value = [("santa", "alexa")]
        mock_read_gifts.side_effect = [
            [],
            [("santa", "banta"), ("banta", "alexa")],
            [
                ("santa", "banta"),
                ("banta", "alexa"),
                ("alexa", "banta"),
                ("banta", "santa"),
            ],
        ]
        mock_store_to_db.return_value = True
        for _ in range(2):
            self.assertIn(
                self.family.secret_santa_matcher(),
                [
                    {"santa": "banta", "banta": "alexa"},
                    {"alexa": "banta", "banta": "santa"},
                ],
            )
        self.assertRaises(ValueError, self.family.secret_santa_matcher)


if __name__ == "__main__":
    unittest.main()
