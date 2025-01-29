"""Defines InsurancePoliciesParser class."""
import re
from extractors.webpage_extractor import WebpageExtractor
from models.bank_account import BankAccount
from parsers.parser import Parser


class InsurancePoliciesParser(Parser):
    """Parser for the insurance policies."""

    def __init__(self, filename, path, date):
        super().__init__(path, date)
        self.extractor = WebpageExtractor(filename, self.path, self.date)

    def parse(self):
        """Parse the policies' information."""
        policy_rows = self.extractor.raw_data.find_all(
            "tr", attrs={"ng-repeat": re.compile(r".*policy.*")}
        )

        face_amounts = self.additional_data["policy_face_amounts"]
        for policy in policy_rows:
            tds = policy.find_all("td")
            policy_number = tds[0].text.strip()
            policy_name = tds[1].text.strip()
            face_amount = face_amounts.get(policy_number)

            if not face_amount:
                continue
            record = BankAccount(
                self.date,
                "Sunlife",
                policy_name,
                policy_number,
                face_amount,
            )
            self.parsed_data.append(record)
            self.total_amount += record.balance
