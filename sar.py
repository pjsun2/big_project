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

def sar_home():
    st.title('조사')
    st.markdown('어떤 데이터를 수집했는지와 조사 방법에 대해 설명 페이지입니다') # see #*
    st.markdown('---')
    selected = option_menu(None, ['데이터', '조사 방법(설계)'],
                            icons=['house', 'bar-chart', 'file-spreadsheet'],
                            menu_icon='cast', default_index=0, orientation='horizontal',
                            styles={
                                'container' : {
                                'padding' : '0!important',
                                'background-color' : '#808080'},
                                'icon' : {
                                'color' : 'orange',
                                'font-size' : '25px'},
                                'nav-link' : {
                                'font-size' : '15px',
                                'text-align' : 'left',
                                'margin' : '0px',
                                '--hover-color' : '#eee'},
                                'nav-link-selected' : {
                                'background-color' : 'green'}
                                })
    if selected == '데이터' :
        data()
    elif selected == '조사 방법(설계)' :
        datasar()
    else:
        st.warning('잘못된 페이지입니다.')

def data():
    st.subheader('1.자동차등록대수현황')
    st.markdown("""
                - 아래 데이터는 전국(서울~부산) 자동차등록대수현황으로  
                1차분류 '시도명' 2차분류 '시군구'까지 전국을 대상으로 조사
                - 24년 4월기준 전국적 자동차 등록 대수는 '26,070,358'임을 확인할 수 있다.
                """)
    st.image(r"자동차등록대수현황.png"'')
    st.caption("통계청, 2011~2024, '자동차등록대수현황 시도별'")
    st.markdown('---')
    st.subheader('2.서울시 주차장+확보율')
    st.markdown("""
                - 23년 기준 '주차면수'를 확인할 수 있다.
                """)
    st.image(r"주차장+확보율.png")
    st.caption("김지연, 2011~2023, '서울시 주차장 확보율 통계', 통계청")

def datasar():
    st.subheader("이론")
    st.markdown("""
                - 서울시 불법주차의 원인을 분석하기 위해  
                '서울시_자동차등록대수현황'과'서울시 주차면수'를 비교해  
                주차면수가 부족한 건 아닌지  
                자동차등록대수가 너무 많은 건 아닌지  
                확인 가능하다면 원인을 분석하고  
                주차장 추가 설립 등 정책적으로 사용이 가능한 근거가 될 수 있지 않을까?
                """)
    st.image(r"비교자료.png")
