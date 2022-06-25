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

        face_amounts = {
            "030021198": 250_000,
            "031300038": 560_000,
            "0800121961": 44_368,
            "0800261739": 25_000,
            "0808250019": 275_000,
        }
        for policy in policy_rows:
            tds = policy.find_all("td")
            policy_number = tds[0].text.strip()
            policy_name = tds[1].text.strip()
            face_amount = face_amounts[policy_number]

            # since life insurance policy is currently mortgaged to PSBank
            # exclude them from list
            if policy_number == "031300038":
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
