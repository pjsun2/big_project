import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def clnhome():
    st.title('정리')
    st.markdown('설계를 바탕으로 이론 검증을 위한 페이지입니다')
    st.markdown('---')
    
    # park.csv 파일에서 데이터 불러오기
    df = pd.read_csv('park.csv')
    
    # 열 이름 수정
    df.columns = ['자치구(1)', '자치구(2)', '자동차등록대수', '주차면수', '주차장확보율 (%)']
     
    # 구 목록
    gu_list = df['자치구(2)'].unique().tolist()
    
    # 사이드바에 selectbox 추가
    selected_gu = st.sidebar.selectbox('구를 선택하세요:', gu_list, key='구 선택')
    
    # 선택된 구의 데이터 필터링
    if selected_gu == '총계':
        gu_data = df.sum(axis=0)
    else:
        gu_data = df[df['자치구(2)'] == selected_gu].iloc[0]
    
    # 선택된 구의 데이터 표시
    st.subheader(f'{selected_gu} 분석 결과')
    st.write(f'**자동차등록대수 (대)**: {gu_data["자동차등록대수"]}')
    st.write(f'**주차면수 (면수)**: {gu_data["주차면수"]}')
    st.write(f'**주차장확보율 (%):** {gu_data["주차장확보율 (%)"]}')
    
    # 선택된 구의 분석 내용 추가
    if selected_gu != "총계" and selected_gu != "자치구별(2)":
        st.write(f"### {selected_gu}의 주차장 확보 현황 분석")
        
        # 주차장 확보율을 실수로 변환하여 비교
        try:
            parking_ratio = float(gu_data["주차장확보율 (%)"])
            
            if parking_ratio >= 150:
                st.success(f"{selected_gu}는 주차장 확보율이 매우 높은 편입니다. 현재 주차장이 충분히 확보되어 있어 주차난이 비교적 적을 것으로 예상됩니다.")
            elif 130 <= parking_ratio < 150:
                st.info(f"{selected_gu}는 주차장 확보율이 양호한 편입니다. 다만, 일부 지역에서는 주차난이 발생할 수 있습니다.")
            else:
                st.warning(f"{selected_gu}는 주차장 확보율이 낮은 편입니다. 주차 공간 부족 문제가 있을 수 있으므로 주차장 확충이 필요합니다.")
        except ValueError:
            st.error("주차장 확보율 데이터를 숫자로 변환할 수 없습니다. 데이터를 확인해주세요.")
    else:
        st.write("### 총계 분석")
        st.write("서울시 전체적으로 주차장 확보율이 142.5%로 비교적 양호한 주차장 확보율을 보이고 있습니다. 하지만 구별로 편차가 존재하므로 각 구별 상황을 고려한 주차 정책이 필요합니다.")
    st.markdown("""
    | 주차장 확보율 범위 | 메시지 |
    |----------------------|----------|
    | >= 150% | 주차장 확보율이 매우 높습니다. |
    | 130% <= 주차장 확보율 < 150% | 주차장 확보율이 양호합니다. |
    | < 130% | 주차장 확보율이 낮습니다. 주차 공간 부족 문제가 있을 수 있습니다. |
    ---
                """)
    
    # 자동차 등록 대수와 주차 면수 비교 그래프
    font_path = "NanumGothic.ttf"
    fontprop = fm.FontProperties(fname=font_path, size=12)
    plt.figure(figsize=(10, 6))
    bars = plt.barh(['Car', 'Parking'], [gu_data["자동차등록대수"], gu_data["주차면수"]], color=['skyblue', 'lightgreen'])
    plt.title(f'{selected_gu} 자동차등록대수 vs. 주차면수', fontproperties=fontprop)
    plt.xlabel('수', fontproperties=fontprop)
    plt.ylabel('항목', fontproperties=fontprop)
    plt.xticks(rotation=45, fontproperties=fontprop)
    
    # Legend 추가
    plt.legend(bars, ['자동차등록대수', '주차면수'], prop=fontprop)
    
    st.pyplot(plt)
 
clnhome()
