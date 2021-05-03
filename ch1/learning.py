import pandas as pd

df_customer_master = pd.read_csv('data/customer_master.csv')
item_master = pd.read_csv('data/item_master.csv')
transaction_1 = pd.read_csv('data/transaction_1.csv')
transaction_2 = pd.read_csv('data/transaction_2.csv')
transaction_detail_1 = pd.read_csv('data/transaction_detail_1.csv')
transaction_detail_2 = pd.read_csv('data/transaction_detail_2.csv')

print('---------------データの概要確認-------------------')
print('dataframeの行数・列数の確認==>\n', df_customer_master.shape)
print('index(行ラベル)の確認==>\n', df_customer_master.index)
print('column(列ラベル)の確認==>\n', df_customer_master.columns)
print('dataframeの各列のデータ型を確認==>\n', df_customer_master.dtypes)
print('---------------データの中身-------------------')
print(df_customer_master.values)
print('----------------------------------------------')

print('---------------listとして取得-------------------')
# index(行ラベル)
index_list = df_customer_master.index.tolist()
print(type(index_list))
print(index_list)
# column(列ラベル)
columns_list = df_customer_master.columns.tolist()
print(type(columns_list))
print(columns_list)
# データ
result_list = df_customer_master.values.tolist()
print(type(result_list))
print(result_list)
print('----------------------------------------------')


print('---------------値の取得・設定-------------------')
# 1列を取り出し(Series)
# df['列名']で列を選択
df_result = df_customer_master['customer_id']
print(df_result.head())
# 1列を取り出し(DataFrame)
# df[['列名']]で列を選択
df_result = df_customer_master[['customer_id']]
print(df_result.head())
# 任意の列を取り出し(DataFrame)
# df[['列名','列名']]で列を選択
df_result = df_customer_master[['customer_id', 'customer_name']]
print(df_result.head())

# atは行名と列名で位置を指定
print(df_result.at[2, 'customer_id'])
# 値の設定
df_result.at[2, 'customer_id'] = 'XX12345'
print(df_result.at[2, 'customer_id'])

# iatは行番号と列番号で位置を指定 ※行番号・列番号は0はじまり
print(df_result.iat[2, 0])
# 値の設定
df_result.iat[2, 0] = 'AS834628'
print(df_result.iat[2, 0])

# loc、iloc：単独、複数の要素の値を取得、変更
# locは行名と列名で位置を指定、ilocは行番号と列番号で位置を指定

# atと同様に行名と列名で位置を指定
print(df_result.loc[2, 'customer_id'])
# iatと同様に行番号と列番号で位置を指定
print(df_result.iloc[2, 0])
# indexが100の行だけ取り出し(Series)
print(df_customer_master.loc[100])

# listの指定の方法で範囲指定が可能
# 任意の範囲の行を取り出し
# ※locで指定した場合、stopの値も含まれる(100行目から106行目)
df_result = df_customer_master.loc[100:106]
print(df_result)
# ※ilocで指定した場合、stopの値は含まれない(100行目から105行目)
df_result = df_customer_master.iloc[100:106]
print(df_result)
# 特定の行を取り出し(100行目から110行目の偶数)
df_result = df_customer_master.iloc[100:111:2]
print(df_result)
# ilocで細かい行、列を指定可能
# 1,2,4 行目と 0-2 列目を取得
df_result = df_customer_master.iloc[[1, 2, 4], [0, 2]]
print(df_result)
# 検索条件を指定して取得
# ageが50より大きいデータを取得
df_result = df_customer_master[df_customer_master['age'] > 50]
print(df_result.head())
# queryメソッドを使うと、複数条件の指定で、特定カラムだけ出力
# ageが50より大きい かつ genderがFの'age', 'gender'列データを取得
df_result = df_customer_master[['age', 'gender']].query(
    'age > 50 and gender == "F"')
print(df_result.head())

# ユニークな値の取得
pref = df_customer_master['pref'].unique()
print(pref)
# 行方向で重複行を削除
df_customer_master.drop_duplicates()
# 要約統計量の表示
print(df_customer_master.describe())

print('---------------データの加工-------------------')
# インデックスの変更
# registration_date列をインデックスに変更
# 引数のinplaceをTrueにすると、元のDataFrameが変更される
print(df_customer_master.head())
print(df_customer_master.set_index('registration_date', inplace=True))
print(df_customer_master.head())
print(df_customer_master.index)

# カラム名の変更
# email→email_addressに変更
print(df_customer_master.columns)
df_customer_master.rename(columns={'email': 'email_address'}, inplace=True)
print(df_customer_master.columns)

# 列の並び替え
# age列を昇順で並び替え
# デフォルトは昇順。降順にしたい場合は引数ascendingをFalseにする
print(df_customer_master.head())
df_customer_master.sort_values(by='age', inplace=True)
print(df_customer_master.head())
# 複数列を基準にソート
# 引数ascendingをリストで指定すると、それぞれの列に対して昇順・降順を選択できる
df_customer_master.sort_values(['age', 'gender'], ascending=[True, False])

# インデックス列のデータ型を変更
# object→datetime64[ns]
print(df_customer_master.index)
df_customer_master.index = pd.to_datetime(
    df_customer_master.index, format='%Y-%m-%d %H:%M:%S')
print(df_customer_master.index)

# インデックス列に対してソート
# 日付がdatetime64[ns]型のため、日時でソート可能
df_customer_master.sort_index(inplace=True)
print(df_customer_master)

# 行列の入れ替え
# 新たなオブジェクトを生成したくない場合は元のオブジェクト自体に代入する
df = pd.DataFrame({'X': [0, 1, 2], 'Y': [3, 4, 5]}, index=['A', 'B', 'C'])
print(df)
#    X  Y
# A  0  3
# B  1  4
# C  2  5
print(df.T)
#    A  B  C
# X  0  1  2
# Y  3  4  5
print(df.transpose())

print('---------------データの結合(トランザクションデータ)-------------------')
# データを縦方向に結合する
# ignore_index:concatでデータフレームを結合した際にindexに付与された番号を無視する
df_transaction = pd.concat([transaction_1, transaction_2], ignore_index=True)
print(transaction_1.head())
df_validate_price = df_transaction

df_transaction_detail = pd.concat(
    [transaction_detail_1, transaction_detail_2], ignore_index=True)
print(df_transaction_detail.head())

# データを横方向に結合する
# df_transactionのデータフレームの'transaction_id', 'payment_date', 'customer_id'を取り出して
# transaction_idで左外部結合
df_transaction_detail = pd.merge(
    df_transaction_detail, df_transaction[['transaction_id', 'payment_date', 'customer_id']], on='transaction_id', how='left')
print(df_transaction_detail.head())

print('---------------欠損値の確認・修正-------------------')
# 列単位で 欠損値NaN(not a number)が入っている個数をカウントする
# （正確には、isnull()でtrueが返ってくる個数をカウントしている）
print(df_customer_master.isnull().sum())
# 'age'列にあるNaNを0に置き換える
df_customer_master.fillna(value={'age': 0}, inplace=True)
# 行ごと削除する場合
# NaN値(欠損値)をドロップ(除外)
df_customer_master.dropna(inplace=True)

print('---------------データ型の変換-------------------')
# 各列のデータ型を確認
print(df_transaction_detail.dtypes)
# detail_id列をint→strに変換
print(df_transaction_detail['detail_id'].map(type))
df_transaction_detail['detail_id'] = df_transaction_detail['detail_id'].astype(
    str)
print(df_transaction_detail.dtypes)
print(df_transaction_detail['detail_id'].map(type))
# 文字列strにキャストすると欠損値も文字列'nan'となる。
# 文字列'nan'は欠損値を処理するメソッドの対象とならないため注意
# キャストする前に欠損値の処理を行うか、replace()で文字列'nan'を欠損値に置き換えること
