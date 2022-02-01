"""Defines the StatementWriter class."""
from openpyxl import load_workbook

from misc.file_processor import FileProcessor


class StatementWriter(FileProcessor):
    """Class used to write out the financial statement."""

    def run(self, data):
        """Perform class logic."""
        template = load_workbook(self.file_object.parent / "template.xlsx")
        self.populate_summary_sheet(template["Summary"], data)
        self.populate_details_sheet(template["Details"], data)
        template.save(self.file_object)
        return self.archive()

    def populate_summary_sheet(self, sheet, data):
        """Populate summary sheet with the mined data."""
        sheet["A2"] = "Sanjay Risbud"
        sheet["A3"] = self.date.strftime("%B %Y")
        sheet["B26"] = self.date.strftime("%m/%d/%Y")

        relevant_cells = {
            "BankAccounts": "B6",
            "Portfolio": "B8",
            "MutualFunds": "B9",
            "InsurancePolicies": "B11",
            "RealEstate": "B12",
            "AmortizationSchedule": "B18",
        }
        for asset_class in data.get("asset_parsers", []):
            type_ = asset_class.__class__.__name__.replace("Parser", "")
            sheet[relevant_cells[type_]] = asset_class.total_amount
        for liability_class in data.get("liability_parsers", []):
            type_ = liability_class.__class__.__name__.replace("Parser", "")
            sheet[relevant_cells[type_]] = liability_class.total_amount

        if data.get("credit_card", None):
            sheet["B16"] = data["credit_card"].balance

    def populate_details_sheet(self, sheet, data):
        """Populate details sheet with the mined data."""
