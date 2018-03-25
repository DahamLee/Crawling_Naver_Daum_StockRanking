import pandas as pd
import numpy as np
from datetime import datetime
import locale
import re

url_naver = "http://finance.naver.com/sise/lastsearch2.nhn"

df_naver = pd.read_html(url_naver, header=0)
df_naver = df_naver[1].dropna()

# df.set_index('순위', inplace=True)
df_naver.drop(['순위', '검색비율', '고가', '저가', 'PER', "ROE"], axis=1, inplace=True)
df_naver = df_naver.reindex_axis(['종목명', '등락률', '현재가', '전일비', '시가', '거래량'], axis=1)
# df_naver['등락률'] = df_naver['등락률'].str.replace('%', '').astype('float64')
# df_naver = df_naver.sort_values(by='등락률', axis=0, ascending=False)
# df = '{0:,}'.format(locale.format('%.3f',df['거래량']))
# print(df_naver)

url1 = "http://finance.daum.net/community/search.daum?page=1"
url2 = "http://finance.daum.net/community/search.daum?page=2"

df1 = pd.read_html(url1, header=0)
df2 = pd.read_html(url2, header=0)

df_daum = df1[0].append(df2[0])
df_daum.drop(['순위', '변동', '최신뉴스'], axis=1, inplace=True)

# df = pd.concat([df_naver, df_daum]).fillna(0)
df = pd.concat([df_naver, df_daum]).fillna(0).drop_duplicates(subset='종목명', keep='first')
df = df.reindex_axis(['종목명', '등락률', '현재가', '전일비', '시가', '거래량'], axis=1)
df['등락률'] = df['등락률'].str.replace('%', '').astype('float64')
df = df.sort_values(by='등락률', axis=0, ascending=False)

# print(df_daum)
print(df)
print(len(df))
now = datetime.now()
print(now)
df.to_csv(now.strftime("/Users/daham/Desktop/top-search/naver-top-search-%Y-%m-%d-%H-%M") + '.csv', encoding='utf-8')
