import pandas as pd

df = pd.read_csv('Pokemon.csv')
df_add = pd.read_csv('names.csv')
rows = len(df)
# print(len(df))
kr_names = []
jp_names = []

for n in df['Name']:
    # print('df[Name]', n)
    check = df_add[df_add['eng'] == n]  # df_add의 eng컬럼에서 df의 Name컬럼과 같은 값이 있는지
    if check.empty:  # 없으면 None 추가
        # print('None')
        kr_names.append('None')
        jp_names.append('None')
    else:  # 있으면 한국어 이름과 일본어 이름 추가
        # idx = check.index[0]  # df_add에서 해당 인덱스
        # print('df[eng]', df_add['eng'][idx])  # 확인용
        kr_names.append(df_add['kr'][check.index[0]])
        jp_names.append(df_add['jp'][check.index[0]])

print(kr_names)
print(jp_names)

df.insert(2, 'Name_kr', kr_names)
df.insert(3, 'Name_jp', jp_names)

df.to_csv('Pokemon_edited.csv', encoding='utf-8')
