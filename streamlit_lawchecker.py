import streamlit as st
import pandas as pd
import numpy as np
import csv
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup



lawname = [
    '녹색건축물 조성 지원법',
    '녹색건축물 조성 지원법 시행령',
    '녹색건축물 조성 지원법 시행규칙',
    '녹색건축 인증에 관한 규칙',
    '주택법',
    '건축물 에너지효율등급 인증 및 제로에너지건축물 인증에 관한 규칙',
    '에너지이용 합리화법',
    '에너지이용 합리화법 시행령',
    '에너지이용 합리화법 시행규칙',
    '주택건설기준 등에 관한 규칙',
    '주택건설기준 등에 관한 규정',
    '장애인ㆍ노인ㆍ임산부 등의 편의증진 보장에 관한 법률',
    '장애물 없는 생활환경 인증에 관한 규칙',
    '건축법',
    '지능형건축물의 인증에 관한 규칙',
    '교육환경 보호에 관한 법률',
    '교육환경 보호에 관한 법률 시행령',
    '교육환경 보호에 관한 법률 시행규칙',
    '인공조명에 의한 빛공해 방지법',
    '인공조명에 의한 빛공해 방지법 시행령',
    '인공조명에 의한 빛공해 방지법 시행규칙',
    '신에너지 및 재생에너지 개발ㆍ이용ㆍ보급 촉진법',
    '경관법',
    '경관법 시행령',
    '공공디자인의 진흥에 관한 법률',
    '공공디자인의 진흥에 관한 법률 시행령',
    '공공디자인의 진흥에 관한 법률 시행규칙',
]


df = pd.DataFrame([])
for i in lawname:
    url = 'https://www.law.go.kr/LSW/nwRvsLsPop.do?pg=1&chrIdx=0&lsKndCd=&cptOfi=&searchType=lsNm&lsNm='+quote_plus(i)+'&p_spubdt=&p_epubdt=&p_spubno=&p_epubno='
    # url = f'https://www.law.go.kr/LSW/nwRvsLsPop.do?pg=1&chrIdx=0&lsKndCd=&cptOfi=&searchType=lsNm&lsNm={quote_plus(i)}&p_spubdt=&p_epubdt=&p_spubno=&p_epubno='
    df1 = pd.read_html(url)[0]
    df = pd.concat([df, df1])

df = df.reset_index(drop=True)

df_01 = df[df['법령명'] == '녹색건축물 조성 지원법'].iloc[[0]]
df_02 = df[df['법령명'] == '녹색건축물 조성 지원법 시행령'].iloc[[0]]
df_03 = df[df['법령명'] == '녹색건축물 조성 지원법 시행규칙'].iloc[[0]]
df_04 = df[df['법령명'] == '녹색건축 인증에 관한 규칙'].iloc[[0]]
df_05 = df[df['법령명'] == '주택법'].iloc[[0]]
df_06 = df[df['법령명'] == '건축물 에너지효율등급 인증 및 제로에너지...'].iloc[[0]]
df_07 = df[df['법령명'] == '에너지이용 합리화법'].iloc[[0]]
df_08 = df[df['법령명'] == '에너지이용 합리화법 시행령'].iloc[[0]]
df_09 = df[df['법령명'] == '에너지이용 합리화법 시행규칙'].iloc[[0]]
df_10 = df[df['법령명'] == '주택건설기준 등에 관한 규칙'].iloc[[0]]
df_11 = df[df['법령명'] == '주택건설기준 등에 관한 규정'].iloc[[0]]
df_12 = df[df['법령명'] == '장애인ㆍ노인ㆍ임산부 등의 편의증진 보장에...'].iloc[[0]]
df_13 = df[df['법령명'] == '장애물 없는 생활환경 인증에 관한 규칙'].iloc[[0]]
df_14 = df[df['법령명'] == '건축법'].iloc[[0]]
df_15 = df[df['법령명'] == '지능형건축물의 인증에 관한 규칙'].iloc[[0]]
df_16 = df[df['법령명'] == '건축법'].iloc[[0]]
df_17 = df[df['법령명'] == '교육환경 보호에 관한 법률'].iloc[[0]]
df_18 = df[df['법령명'] == '교육환경 보호에 관한 법률 시행령'].iloc[[0]]
df_19 = df[df['법령명'] == '교육환경 보호에 관한 법률 시행규칙'].iloc[[0]]
df_20 = df[df['법령명'] == '인공조명에 의한 빛공해 방지법'].iloc[[0]]
df_21 = df[df['법령명'] == '인공조명에 의한 빛공해 방지법 시행령'].iloc[[0]]
df_22 = df[df['법령명'] == '인공조명에 의한 빛공해 방지법 시행규칙'].iloc[[0]]
df_23 = df[df['법령명'] == '신에너지 및 재생에너지 개발ㆍ이용ㆍ보급 ...'].iloc[[0]]
df_24 = df[df['법령명'] == '경관법'].iloc[[0]]
df_25 = df[df['법령명'] == '경관법 시행령'].iloc[[0]]
df_26 = df[df['법령명'] == '공공디자인의 진흥에 관한 법률'].iloc[[0]]
df_27 = df[df['법령명'] == '공공디자인의 진흥에 관한 법률 시행령'].iloc[[0]]
df_28 = df[df['법령명'] == '공공디자인의 진흥에 관한 법률 시행규칙'].iloc[[0]]
df_29 = df[df['법령명'] == '건축법'].iloc[[0]]
df_30 = df[df['법령명'] == '건축법'].iloc[[0]]



df_fin = pd.concat([
    df_01,
    df_02,
    df_03,
    df_04,
    df_05,
    df_06,
    df_07,
    df_08,
    df_09,
    df_10,
    df_11,
    df_12,
    df_13,
    df_14,
    df_15,
    df_16,
    df_17,
    df_18,
    df_19,
    df_20,
    df_21,
    df_22,
    df_23,
    df_24,
    df_25,
    df_26,
    df_27,
    df_28,
    df_29,
    df_30,
    ])


df_fin = df_fin.sort_values('시행일자' , ascending=False)
df_fin = df_fin.drop(columns=['번호','소관부처','법령종류','공포번호'])
df_fin = df_fin.reset_index(drop=True)

st.subheader('최신 법령')

st.dataframe(df_fin, use_container_width=False) 

st.text('EAN research unit')
