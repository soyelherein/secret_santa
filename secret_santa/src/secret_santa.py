""" defines core logic for the secret santa application

    the application:
    imagine that every year your extended family does a "Secret Santa" gift exchange.
    For this gift exchange, each person draws another person at random
    and then gets a gift for them.
    This program that will choose a Secret Santa for everyone
    given a list of all the members of your extended family.
    Obviously, a person cannot be their own Secret Santa.
"""

from collections import Counter, defaultdict
from datetime import date
from random import choices
from typing import Dict, Set
from ..src import dao_module


class Family:
    """Class to act as a model for generating secret santa match"""

    def __init__(self, member_names: Set[str]):
        """Constructor method"""
        self.member_names = member_names
        self.db_con = dao_module.Dao()

    def _prepare_exclusion(self, year):
        """_prepare_exclusion method that prepares the past matches to be excluded from
        matching in the current year.

        :param year: matching year
        :type year: int
        :return: already_matched_dict
        :rtype: dict
        """
        already_matched = self.db_con.read_gifts_from_db(year)
        already_matched_dict = defaultdict(set)
        for giver, receiver in already_matched:
            already_matched_dict[giver].add(receiver)
        return already_matched_dict

    def secret_santa_matcher(self, year =1990) -> Dict:
        """Creates secret santa pairs among the family members.
        Returns gift giver and receiver pairs and any unmatched members

        :return: dictionary of {gift_giver:gift_receiver}
        :rtype: Dict
        """
        matched_pairs = dict()  # who got gift from whom {gift_giver:gift_receiver}
        # reading the past matches, that would be excluded from matching process
        past_matched_pairs = self._prepare_exclusion(
            year
        )  # preparing past gift history
        for member in self.member_names:
            # excluding gift giver to accidentally receiving it from himself/herself,
            # excluding people who have already received gifts.
            eligible_gift_receivers = self.member_names.difference(
                {member}.union(set(matched_pairs.values()))
            )

            eligible_gift_receivers_after_exclusion = list(
                eligible_gift_receivers.difference(past_matched_pairs.get(member, {}))
            )
            # putting more weights who has not given or received gift yet
            # this is to ensure the system maximize the match by diversifying the match
            weights_of_gift_receivers = [
                0 if eligible_gift_receiver in matched_pairs else 1
                for eligible_gift_receiver in eligible_gift_receivers_after_exclusion
            ]
            if eligible_gift_receivers_after_exclusion:
                matched_pairs[member] = choices(
                    eligible_gift_receivers_after_exclusion,
                    weights=weights_of_gift_receivers,
                )[0]
        if matched_pairs:
            self.db_con.store_to_db(table_name = 'secret_santa_pairs',
             val = map(lambda x: (year,x[0],x[1]), matched_pairs.items()))
            return matched_pairs
        raise ValueError("No Matching pairs found")

    def unmatched_members(self, matched_pairs: dict) -> Set:
        """Returns the unmatched members
        :param: matched pairs
        :type: Dict
        :return: unmatched members
        :rtype: Set
        """
        return self.member_names.difference(
            set(matched_pairs.keys()).union(set(matched_pairs.values()))
        )


class Main:
    """Class for taking inputs, parsing it for the model, rendering the output."""

    @classmethod
    def _read_input(cls):
        """_read_input read input from console

        :return: member_name
        :rtype: str
        """
        return str(input())

    @classmethod
    def get_family_details(cls) -> Set:
        """method handles input, data cleaning and validation.

        :return: Name of family members
        :rtype: Set
        """
        input_names = list()
        print(
            """Please enter the names of family members
            enter blank line to generate the match"""
        )
        while True:
            member_name = Main._read_input()
            if member_name:
                input_names.append(member_name)
            else:
                break

        #  removing leading and trailing blanks from names
        # validating the name if alphanumeric only
        list_of_members = [
            member.strip()
            for member in input_names
            if member.strip() and member.strip().replace(" ", "").isalpha()
        ]

        if len(list_of_members) > len(set(list_of_members)):
            raise ValueError(
                f"Cannot redefine name: {Counter(list_of_members).most_common(1)[0][0]}"
            )
        if len(set(list_of_members)) < 3:
            raise ValueError("At least 3 members needed for secret santa")
        return set(list_of_members)

    @classmethod
    def run_secret_santa(cls) -> None:
        """Method to run the application"""
        generate_match_flag = "y"
        year = date.today().year
        family_member_names = cls.get_family_details()
        family = Family(family_member_names)
        while generate_match_flag in ("y", "Y"):
            matched_pairs = family.secret_santa_matcher(year=year)
            print(f"Matched pairs: {matched_pairs}")
            unmatched_members = family.unmatched_members(matched_pairs)
            if unmatched_members:
                print(f"Unmatched members: {unmatched_members}")
            year += 1
            print(f"Press Y key to simulate match for {year}")
            generate_match_flag = cls._read_input()
        return True


if __name__ == "__main__":
    Main.run_secret_santa()
