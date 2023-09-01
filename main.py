import pandas as pd
import matplotlib.pyplot as plt

def exercise_0(file):
    df = pd.read_csv('transactions.csv')
    pass

def exercise_1(df):
    column_names = df.columns.tolist()
    pass

def exercise_2(df, k):
    return df.head(k)
    pass

def exercise_3(df, k):
    return df.sample(k)
    pass

def exercise_4(df):
    unique_transaction_types = df['type'].unique().tolist()
    pass

def exercise_5(df):
    top_destinations = df['nameDest'].value_counts().head(10)
    pass

def exercise_6(df):
    fraud_detected_rows = df[df['isFraud'] == 1]
    pass

def exercise_7(df):
    distinct_destinations_per_source = df.groupby('nameOrig')['nameDest'].nunique().sort_values(ascending=False).reset_index()
    distinct_destinations_per_source.columns = ['nameOrig', 'num_distinct_destinations']
    pass

def visual_1(df):
    def transaction_counts(df):
        return df['type'].value_counts()

    def transaction_counts_split_by_fraud(df):
        return df.groupby(['type', 'isFraud']).size().unstack()

    fig, axs = plt.subplots(2, figsize=(6, 10))
    transaction_counts(df).plot(ax=axs[0], kind='bar')
    axs[0].set_title('Transaction Type Counts')
    axs[0].set_xlabel('Transaction Type')
    axs[0].set_ylabel('Count')

    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar', stacked=True)
    axs[1].set_title('Transaction Type Counts Split by Fraud')
    axs[1].set_xlabel('Transaction Type')
    axs[1].set_ylabel('Count')
    axs[1].legend(title='IsFraud', labels=['Not Fraud', 'Fraud'])

    fig.suptitle('Transaction Type Analysis')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs:
        for p in ax.patches:
            ax.annotate(p.get_height(), (p.get_x(), p.get_height()))

    plt.show()
    return 'Visualization completed.'

    visual_1(df)
    pass

def visual_2(df):
    def query(df):
        cash_out_df = df[df['type'] == 'CASH_OUT']
        return cash_out_df

    plot = query(df).plot.scatter(x='newbalanceOrig', y='newbalanceDest')
    plot.set_title('Origin Account Balance Delta vs Destination Account Balance Delta (Cash Out)')
    plot.set_xlim(left=-1e3, right=1e3)
    plot.set_ylim(bottom=-1e3, top=1e3)
    plt.xlabel('Origin Account Balance Delta')
    plt.ylabel('Destination Account Balance Delta')
    plt.grid(True)
    plt.tight_layout()

    plt.show()
    return 'Visualization completed.'

    visual_2(df)
    pass

def exercise_custom(df):
    # Calculate the median transaction amount for each transaction type
    median_amounts = df.groupby('type')['amount'].median()

    return median_amounts
    
def visual_custom(df):
    median_amounts = exercise_custom(df)

    # Create a bar chart of median transaction amounts by transaction type
    plt.figure(figsize=(10, 6))
    median_amounts.plot(kind='bar')
    plt.title('Median Transaction Amounts by Transaction Type')
    plt.xlabel('Transaction Type')
    plt.ylabel('Median Transaction Amount')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    return 'Visualization completed.'
median_amounts = exercise_custom(df)
print(median_amounts)

# Calling the visual_custom function to generate the visual
visual_custom(df)