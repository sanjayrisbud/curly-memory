"""Defines InsurancePoliciesParser class."""
from extractors.pdf_extractor import PDFExtractor
from models.bank_account import BankAccount
from parsers.parser import Parser


class InsurancePoliciesParser(Parser):
    """Parser for the insurance policies."""

    def __init__(self, filename, path, date):
        super().__init__(path, date)
        self.extractor = PDFExtractor(filename, self.path, self.date)

    def parse(self):
        """Parse the policies' information."""
        lines = self.extractor.raw_data[0].split("\n")

        # get only policy-relevant lines and clean up each one
        policy_lines = [
            line.replace("PHP", "").replace("Paid-up", "")[line.index("0") :].strip()
            for line in lines
            if " SUN " in line
        ]

        for line in policy_lines:
            policy_number, *policy_name, face_amount = line.split(" ")

            # since life insurance policies are currently mortgaged to PSBank
            # exclude them from list
            if policy_number.startswith("03"):
                continue

            record = BankAccount(
                self.date,
                "Sunlife",
                " ".join(policy_name).strip(),
                policy_number,
                face_amount.replace(",", ""),
            )
            self.parsed_data.append(record)
            self.total_amount += record.balance
