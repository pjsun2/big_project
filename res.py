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

def reshome() :
    st.title('결과')
    st.markdown('검증을 통한 결과를 분석하고 향후 진행방향을 논의하기 위한 페이지입니다')
    st.markdown('---')
    st.subheader('1.분석 결과')
    st.markdown('다음과 같은 결과를 도출했다')
    st.code("""
            1) '차량등록'보다 '주차면수'를 비교해 주차장확보율이 높은걸 보아  
            서울시 불법주차의 문제는 '외부요인'이 존재한다
            2) 외부요인이란 '타지역' 즉 '상경'의 원인이 있을 가능성이 있다
            3) 비용의 문제로 주차장을 이용하지 않는 '인식'에서 비롯될 수 있다
            """)
    st.markdown('---')
    st.subheader('2.향후 진행방향')
    st.code("""
                1) 서울시 뿐만 아니라 '수도권/지방' 등 '전국 주차면수 데이터를 실시간으로 확보'할 수 있다면  
                '주차 혼잡 문제를 해결'할 수 있을 것으로 기대된다.
                2) '불법주차의 원인은 주차장 부족이 아니므로' 벌금을 상승시켜  
                주차장 한 달 비용보다 높게 정책을 수정한다면 불법주차로 인한 문제를 해결이 가능할 것이다. 
                """)
    
