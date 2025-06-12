# PYTHON CODE READING

## Project Summary:
The aim of this project was to analyze monthly inflows and outflows to gain financial insights. It breaks down how much was earned, how much was spent, total spending by category, average daily spend, and the number of transactions per category. Additionally, it consolidates each transaction with an appropriate description (debit or credit). This helps individuals understand their earnings, spending habits, and what their average daily spend is, while also identifying categories with the highest expenditures.

## Summary of What the Code Does
A JSON file containing transaction records is read, parsed, and unpacked. The data is then passed into a class to create instances of individual transactions using the Transaction class as a blueprint, with defined attributes and methods used for analysis. Below is a breakdown of the classes and functions:

#### **1. The Transaction Class**
The Transaction class serves as a blueprint for creating financial transaction objects. It takes in attributes such as the transaction amount, category, and date. It then defines methods that:
-	Provide a readable representation of the object using _____repr_____, making it easy to understand
- Identify debit transactions i.e., transactions where the amount is less than 0 (expenses)

#### **2. The BudgetAnalyzer Class**
This class accepts a list of Transaction objects as input. It defines various methods such as total_spent, total_earned, and spending_by_category, which return insights into the user’s financial activity including total earnings, total expenses, spending patterns by category, and average daily spending

#### **3. The load_transactions function**
This function takes a file path as a parameter, reads the JSON file, and converts its content into a list of dictionaries. It then loops through this list, unpacks each dictionary, and creates a list of Transaction objects using the Transaction class as a blueprint

#### **4. The Main Function**
The main() function serves as the exceutor, the one where all the classes, function are called in other to analyze . The main function begins by assigning the file path to a variable. It then uses load_transactions to convert the file contents into transaction objects. If the file contains no data, it logs a warning and exits. Otherwise, it creates an instance of BudgetAnalyzer using the list of transactions and calls its method to print out financial summaries using logging statements

#### The main guard then ensures that the main() function only runs when the script is executed directly, and not when the module is imported into another script

## What I learnt from reading the code: 
-	I got a deeper understanding of class. For example, I learned how the __repr__ method provides a readable string representation of an object, and how class attributes can be accessed and used within methods.
-	I now understand how class execution works. When a Python script that contains a class or function runs, it reads and stores the definitions (like a snapshot), and only executes the class, methods, and functions when they are explicitly called. This also helped me understand that the order in which classes or functions are defined in a script doesn't matter as long as they are not called before being defined.
-	I learned the difference in emptiness checks. For instance,
  
      *For lists, dicts, or sets: use if not my_list:*
  
      *For pandas DataFrames: use if df.empty:*


## What I found clever:
The code’s reusability. By using the main guard, it ensures that certain parts of the script only run when the script is executed directly. This preserves the script’s reusability, allowing its classes and functions to be imported and used in other modules without unintended side effects.




