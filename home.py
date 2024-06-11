import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

    # st.title('1.결과')
    # st.markdown('불법주차 근절을 위한 데이터 사용으로') # see #*
    # st.text('Fixed width text')
    # st.markdown('_Markdown_') # see #*
    # st.caption('Balloons. Hundreds of them...')
    # st.latex(r''' e^{i\pi} + 1 = 0 ''')
    # st.write('Most objects') # df, err, func, keras!
    # st.write(['st', 'is <', 3]) # see *
    # st.header('My header')
    # st.subheader('My sub')
    # st.code('for i in range(8): foo()')
    
#테이블 표
# data = {
#     "Language": ["python", "streamlit", "000"],
# }

def subhome() :
    #st.image(r"C:\Users\parkj\Desktop\13W\자산 2.png, caption='Example Image', use_column_width=True")
    st.title('1.불법주자 관리 시스템')
    st.markdown("""
                목적 : 불법주차 근절을 위해 '전국 주차면수'와 '시도별 차량등록' 데이터를 대조해  
                불법주차를 미리 예측, 예방 하는 것이 목적이다
                """) # see #*
    st.image(r"C:\Users\parkj\Desktop\13W\parking.jpg")
    st.caption("전성필, 2021, '소방차 막은 불법주차, 2년10개월 만에 첫 강제처분', 국민일보")
    st.markdown('---')
    st.title('2.목차')
    st.subheader('Ⅰ.HOME')
    st.markdown("""
                - 개요
                """)
    st.subheader('Ⅱ.조사')
    st.markdown("""
                - 데이터
                    - 자동차등록대수현황
                    - 서울시 주차장+확보율
                - 조사 방법(설계)
                    - 이론
                """)
    st.subheader('Ⅲ.정리')
    st.markdown("""
                - 구별 분석 결과
                - 구별 주차장 확보 현황 분석
                - 시각화
                """)
    st.subheader('Ⅳ.결과')
    st.markdown("""
                - 분석 결과
                - 향후 진행방향
                """)