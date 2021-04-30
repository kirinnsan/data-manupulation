import pandas as pd

customer_master = pd.read_csv('data/customer_master.csv')
item_master = pd.read_csv('data/item_master.csv')
transaction_1 = pd.read_csv('data/transaction_1.csv')
transaction_2 = pd.read_csv('data/transaction_2.csv')
transaction_detail_1 = pd.read_csv('data/transaction_detail_1.csv')
transaction_detail_2 = pd.read_csv('data/transaction_detail_2.csv')

# データの概要確認
print('---------------データの概要確認-------------------')
print('dataframeの行数・列数の確認==>\n', customer_master.shape)
print('indexの確認==>\n', customer_master.index)
print('columnの確認==>\n', customer_master.columns)
print('dataframeの各列のデータ型を確認==>\n', customer_master.dtypes)
print('--------------------------------------------------')

print('---------------データの中身確認-------------------')
# 先頭5行を読み込む
result = customer_master.head()
print(result)

result = item_master.head()
print(result)

result = transaction_1.head()
print(result)
print('--------------------------------------------------')


print('---------------データの結合(トランザクションデータ)-------------------')
# データを縦方向に結合する
# ignore_index:concatでデータフレームを結合した際にindexに付与された番号を無視する
df_transaction = pd.concat([transaction_1, transaction_2], ignore_index=True)
print(transaction_1.head())

df_transaction_detail = pd.concat(
    [transaction_detail_1, transaction_detail_2], ignore_index=True)
print(df_transaction_detail.head())

# データを横方向に結合する
# df_transactionのデータフレームの'transaction_id', 'payment_date', 'customer_id'を取り出して
# transaction_idで左外部結合
df_transaction_detail = pd.merge(
    df_transaction_detail, df_transaction[['transaction_id', 'payment_date', 'customer_id']], on='transaction_id', how='left')
print(df_transaction_detail.head())

print('---------------データの結合(マスターデータ)-------------------')
df_transaction_detail = pd.merge(df_transaction_detail, customer_master, on='customer_id', how='left')
df_transaction_detail = pd.merge(df_transaction_detail, item_master, on='item_id', how='left')

pd.set_option('display.max_rows', 10000)
pd.set_option('display.max_columns', 20)
print(df_transaction_detail.head())