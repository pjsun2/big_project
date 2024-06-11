import streamlit as st  
from streamlit_option_menu import option_menu

from home import subhome
from sar import sar_home
from cln import clnhome
from res import reshome

#참고링크
#https://cheat-sheet.streamlit.app/ 치트시트
#https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/ 이모지
#https://prophet.streamlit.app/ prophet
#https://docs.streamlit.io/get-started streamlit Documentation

#데이터
#https://kosis.kr/statHtml/statHtml.do?orgId=116&tblId=DT_MLTM_5498&vw_cd=MT_ZTITLE&list_id=M2_18&scrId=&seqNo=&lang_mode=ko&obj_var_id=&itm_id=&conn_path=MT_ZTITLE&path=%252FstatisticsList%252FstatisticsListIndex.do
#https://www.suwonudc.co.kr/park/PageLink.do?link=forward:/PageContent.do&menuNo=010000&subMenuNo=010600&thirdMenuNo=010602 수원시 주차장
#세대수
#세대별 차량 보유 현황

# st.checkbox('Check me out')
        # st.radio('Pick one:', ['nose','ear'])
        # st.selectbox('Select', [1,2,3])
        # st.multiselect('Multiselect', [1,2,3])
        # st.slider('Slide me', min_value=0, max_value=10)
        # st.select_slider('Slide to select', options=[1,'2'])
        # st.text_input('Enter some text') 
        # st.number_input('Enter a number')
        # st.text_area('Area for textual entry')
        # st.date_input('Date input')
        # st.time_input('Time entry')
        # st.file_uploader('File uploader')

def main():
    with st.sidebar:
        st.image(r"C:\Users\parkj\Desktop\13W\자산 2.png")
        st.markdown("""
                    20221670 | 박재선
                    """)
        selected = option_menu('목차', ['HOME', '조사', '정리', '결과'],
                               icons=['house', 'search', 'box-seam', 'clipboard2-heart'],
                               menu_icon='clipboard', default_index=0
                               )
        
        bg_color = st.color_picker('배경색 설정', '#122641')
        if st.button('적용'):
            st.session_state['bg_color'] = bg_color
    if 'bg_color' in st.session_state:
        bg_color = st.session_state['bg_color']
    else:
        bg_color = '#122641'
    # 마크다운과 HTML 사용하여 배경색 설정
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {bg_color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    if selected == 'HOME':
        subhome()
    elif selected == '조사':
        sar_home()
    elif selected == '정리':
        clnhome()
    elif selected == '결과':
        reshome()
    else :
        st.warning('잘못된 페이지입니다.')

        

if __name__ == "__main__":
    main()
