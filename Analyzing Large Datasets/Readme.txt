As a part of Forage Virtual Experience program, analyzed a recently acquired dataset of mobile money transactions from a financial services provider. 

The dataset is a subset of https://www.kaggle.com/ealaxi/paysim1/version/2 which was originally generated as part of the following research:

E. A. Lopez-Rojas , A. Elmir, and S. Axelsson. "PaySim: A financial mobile money simulator for fraud detection". In: The 28th European Modeling and Simulation Symposium-EMSS, Larnaca, Cyprus. 2016
The provided dataset has five types of transactions:
CASH-IN is any deposit.
CASH-OUT is any withdrawal.
DEBIT is a specific type of withdrawal in which the money is sent to the user’s bank account.
PAYMENT is the purchase of goods or services. 
TRANSFER involves moving money from one user’s account to another user’s account.
There are two fields related to fraud tagging. IsFlaggedFraud is fraud detected by their automation system while IsFraud is fraud that truly occurred.

In this project, the following exercises have been completed.

1. Read the dataset (`transactions.csv`) as a Pandas dataframe. Note that the first row of the CSV contains the column names.

2. Return the column names as a list from the dataframe.

3. Return the first k rows from the dataframe.

4. Return a random sample of k rows from the dataframe.

5. Return a list of the unique transaction types.

6. Return a Pandas series of the top 10 transaction destinations with frequencies.

7. Return all the rows from the dataframe for which fraud was detected.

8. Return a dataframe that contains the number of distinct destinations that each source has interacted with to, sorted in descending order. 

Created graphs for the following. 
1. Transaction types bar chart, Transaction types split by fraud bar chart
1. Origin account balance delta v. Destination account balance delta scatter plot for Cash Out transactions

Ensured that the graphs have the following:
 - Title
 - Labeled Axes

Visualized large datasets to gain critical information for which areas need additional investment. 
This was not limited to financial systems but internal computer information systems as well.