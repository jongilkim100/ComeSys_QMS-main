import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('./db/qms_kunshan.db')
곤산_고품관리 = pd.read_sql("SELECT * FROM 곤산_고품관리;",conn,index_col='index')
곤산_클레임비용분석자료 = pd.read_sql("SELECT * FROM 곤산_클레임비용현황;",conn,index_col='index')
곤산_수입검사현황 = pd.read_sql("SELECT * FROM 곤산_수입검사현황;",conn,index_col='index')
곤산_공정검사현황 = pd.read_sql("SELECT * FROM 곤산_공정검사현황;",conn,index_col='index')
곤산_출하검사현황 = pd.read_sql("SELECT * FROM 곤산_출하검사현황;",conn,index_col='index')

곤산_고품관리 = 곤산_고품관리.sort_values(by='接收日접수일' ,ascending=False)
곤산_클레임비용분석자료 = 곤산_클레임비용분석자료.sort_values(by='일자' ,ascending=False)
곤산_수입검사현황 = 곤산_수입검사현황.sort_values(by='일자' ,ascending=False)
곤산_공정검사현황 = 곤산_공정검사현황.sort_values(by='일자' ,ascending=False)
곤산_출하검사현황 = 곤산_출하검사현황.sort_values(by='일자' ,ascending=False)

곤산_고품관리_dataframe = pd.DataFrame(곤산_고품관리)
곤산_클레임비용분석자료_dataframe = pd.DataFrame(곤산_클레임비용분석자료)
곤산_수입검사현황_dataframe = pd.DataFrame(곤산_수입검사현황)
곤산_공정검사현황_dataframe = pd.DataFrame(곤산_공정검사현황)
곤산_출하검사현황_dataframe = pd.DataFrame(곤산_출하검사현황)

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

st.markdown('<h4><div style="text-align: left;">1️⃣곤산_수입검사현황</div></h4>', unsafe_allow_html=True)
st.dataframe(곤산_수입검사현황_dataframe, 1400,240)
st.markdown('<h4><div style="text-align: left;">2️⃣곤산_공정검사현황</div></h4>', unsafe_allow_html=True)
st.dataframe(곤산_공정검사현황_dataframe, 1400,240)
st.markdown('<h4><div style="text-align: left;">3️⃣곤산_출하검사현황</div></h4>', unsafe_allow_html=True)
st.dataframe(곤산_출하검사현황_dataframe, 1400,240)
st.markdown('<h4><div style="text-align: left;">4️⃣곤산_고품관리</div></h4>', unsafe_allow_html=True)
st.dataframe(곤산_고품관리_dataframe, 1400,240)
st.markdown('<h4><div style="text-align: left;">5️⃣곤산_클레임비용</div></h4>', unsafe_allow_html=True)
st.dataframe(곤산_클레임비용분석자료_dataframe, 1400,240)