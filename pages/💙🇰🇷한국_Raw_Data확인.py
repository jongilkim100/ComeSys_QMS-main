import streamlit as st
import pandas as pd
import sqlite3

base = "dark"
primaryColor="#F63366"
backgroundColor="#000000"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"

conn = sqlite3.connect('./db/qms.db')
수입검사현황 = pd.read_sql("SELECT * FROM 수입검사현황_2023;",conn,index_col='index')
공정검사현황 = pd.read_sql("SELECT * FROM 공정검사현황_2023;",conn,index_col='index')
출하검사현황 = pd.read_sql("SELECT * FROM 출하검사현황_2023;",conn,index_col='index')
고객사라인부적합현황 = pd.read_sql("SELECT * FROM 인라인부적합현황_2023;",conn,index_col='index')
필드클레임현황 = pd.read_sql("SELECT * FROM 클레임비용현황_2023;",conn,index_col='index')
QCOST현황 = pd.read_sql("SELECT * FROM 고객불만품질비용_2023;",conn,index_col='index')

수입검사현황 = 수입검사현황.sort_values(by='일자' ,ascending=False)
공정검사현황 = 공정검사현황.sort_values(by='일자' ,ascending=False)
출하검사현황 = 출하검사현황.sort_values(by='일자' ,ascending=False)
고객사라인부적합현황 = 고객사라인부적합현황.sort_values(by='일자' ,ascending=False)
필드클레임현황 = 필드클레임현황.sort_values(by='일자' ,ascending=False)
QCOST현황 = QCOST현황.sort_values(by='일자' ,ascending=False)

수입검사현황_dataframe = pd.DataFrame(수입검사현황)
공정검사현황_dataframe = pd.DataFrame(공정검사현황)
출하검사현황_dataframe = pd.DataFrame(출하검사현황)
고객사라인부적합현황_dataframe = pd.DataFrame(고객사라인부적합현황)
필드클레임현황_dataframe = pd.DataFrame(필드클레임현황)
QCOST현황_dataframe = pd.DataFrame(QCOST현황)

st.set_page_config(layout = "wide", initial_sidebar_state = "expanded")
st.markdown("""
        <style>
               .block-container {
                    padding-top: 2rem;
                    padding-bottom: 1rem;
                    padding-left: 1rem;
                    padding-right: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)
st.markdown('<h4><div style="text-align: left;">1️⃣수입검사현황</div></h4>', unsafe_allow_html=True)
st.dataframe(수입검사현황_dataframe, 1400,240)
st.markdown('<h4><div style="text-align: left;">2️⃣공정검사현황</div></h4>', unsafe_allow_html=True)
st.dataframe(공정검사현황_dataframe, 1400,240)
st.markdown('<h4><div style="text-align: left;">3️⃣출하검사현황</div></h4>', unsafe_allow_html=True)
st.dataframe(출하검사현황_dataframe, 1400,240)
st.markdown('<h4><div style="text-align: left;">4️⃣고객사라인부적합현황</div></h4>', unsafe_allow_html=True)
st.dataframe(고객사라인부적합현황_dataframe, 1400,240)
st.markdown('<h4><div style="text-align: left;">5️⃣필드클레임현황</div></h4>', unsafe_allow_html=True)
st.dataframe(필드클레임현황_dataframe, 1400,240)
st.markdown('<h4><div style="text-align: left;">6️⃣QCOST현황</div></h4>', unsafe_allow_html=True)
st.dataframe(QCOST현황_dataframe, 1400,240)