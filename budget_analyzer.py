import pandas as pd
import statistics
import json
import logging
from datetime import datetime
from typing import List, Dict

logging.basicConfig(filename='budgetanalyzer.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    filemode='w')


class Transaction:
    """
    Represents a financial transaction.
    """

    def __init__(self, date: str, amount: float, category: str):
        """
        Constructor for creating Transaction objects.

        Defines attributes. These attributes can be accessed and used by other methods in the class
        or classes that interact with Transaction objects or takes in the the objects as an argument.
    
        Parameters:
        date (str): The date of the transaction
        amount (float): The transaction amount
        category (str): The category assigned to the transaction
    
        """
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.amount = amount
        self.category = category

    def __repr__(self):
        """
        Returns a readable string representation of the Transaction objects,
        useful for debugging and understanding the object's contents.
        """
        repr = f"<Transaction {self.amount} {self.category} on {self.date.date()}>"
        return repr  # noqa: E501

    def is_expense(self):
        """
        Checks for transactions amount < 0. i.e expenses
        """
        expense = self.amount < 0
        return expense


class BudgetAnalyzer:
    """
    Analyzes a list of transactions to produce financial insights.
    """

    def __init__(self, transactions: List[Transaction]):
        """
        Initializes the BudgetAnalyzer with a list of Transaction objects.

        Parameter:
        transactions (List[Transaction]): A list of Transaction instances to be analyzed
        """
        self.transactions = transactions 
        

    def total_spent(self) -> float:
        """
        Calculates sum total of expenses. i.e amounts less than 0

        Returns:
            float:The total expenses
        """
        total_spends = sum(t.amount for t in self.transactions if t.is_expense())
        return total_spends

    def total_earned(self) -> float:
        """
        Calculates sum total of amounts earned. i.e amounts > 0

        Returns:
            float: The total earnings
        """
        total_earning = sum(t.amount for t in self.transactions if not t.is_expense())
        return total_earning

    def spending_by_category(self) -> Dict[str, float]:
        """
        Calculates total spends for each category

        Returns: 
            Dict[str, float]: A dictionary where keys are categories and values are the 
                            total spend for each category
        """
        summary = {}
        for t in self.transactions:
            if t.is_expense():
                summary[t.category] = summary.get(t.category, 0) + abs(t.amount)  # noqa: E501
        return summary
    
    # New added methods
    def average_daily_spending(self) -> float:
        """
        Calculates the average daily spend

        It sums the total expenses for each day and then divides by the number of
        days 

        Returns:
            float: The average amount spent per day
        """
        avg_daily = {}
        for t in self.transactions:
            if t.is_expense():
                avg_daily[t.date] = avg_daily.get(t.date, 0) + abs(t.amount)
        
        daily_avg = sum(avg_daily.values()) / len(avg_daily)
        return daily_avg
        
    
    def Number_of_transactions_per_category(self) -> Dict[str, int]:
        """
        Calculates the number of transactions for each category

        Returns:
            Dict[str, int]: A dictionary where keys are categories and values are the 
                            number of transactions in each category
        """
        categories = {}
        for t in self.transactions:
            categories [t.category] = categories.get(t.category, 0) + 1
        return categories 
        
    
    def transaction_description(self) -> List[Transaction]:
        """
        Adds a description (Debit or Credit) to each transaction based on whether 
        it is an expense or not, and returns the updated list of transactions

        Returns:
            List[Transaction]: A list of transactions with added descriptions.    
        """
        descriptions = []
        for t in self.transactions:
            if t.is_expense():
                t.description = 'Debit'
                
            else:
                t.description = 'Credit'
            fields = f"Transaction {t.amount} {t.category} on {t.date.date()} - {t.description}"
            descriptions.append(fields)
        return descriptions 
        
    # Updated method to call new added methods and log them 
    def print_summary(self):
        """
        Calls methods and prints a summary of their outputs. Logs the results for tracking.
        """
        logging.info("------ Budget Summary ------")
        logging.info(f"Total Earned: ${self.total_earned():.2f}")
        logging.info(f"Total Spent:  ${abs(self.total_spent()):.2f}")
        logging.info("Spending by Category:")
        for category, amount in self.spending_by_category().items():
            logging.info(f"  {category}: ${amount:.2f}")
        logging.info(f"Average daily spend: ${self.average_daily_spending():.2f}")
        logging.info("Number of transactions per category:")
        for key in self.Number_of_transactions_per_category():
            values = self.Number_of_transactions_per_category()[key]
            logging.info(f"{key}: {values}")
        for t in self.transaction_description():
            logging.info(f" {t}")


def load_transactions(filepath: str) -> List[Transaction]:
    """
    Load transactions from a JSON file.
    JSON format:
    [
        {"date": "2024-05-01", "amount": -50.25, "category": "groceries"},
        {"date": "2024-05-02", "amount": 2000.00, "category": "salary"}
    ]
    """
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return [Transaction(**item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"Failed to load transactions: {e}")
        return []


def main():
    """
    This function calls the load_transactions function to load transactions from a JSON file,
    unpacks the transactions, and creates objects using the Transaction class as a blueprint.

    It checks whether any data was loaded, and if so, it creates an instance of the BudgetAnalyzer
    class (which contains methods to analyze transactions). Finally, it calls the print_summary
    method from the BudgetAnalyzer class to display a summary of the analysis.
    """
    filepath = "transactions.json"
    transactions = load_transactions(filepath)

    if not transactions:
        logging.warning("No transactions to analyze.")
        return
    

    analyzer = BudgetAnalyzer(transactions)
    analyzer.print_summary()


if __name__ == "__main__":
    """
    The main guard ensures that the main() function gets executed only in the main script. 
    """
    main()