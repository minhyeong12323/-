import streamlit as st

# 웹 서비스 제목
st.title('나의 성격 분석 웹 서비스!!')

# 사용자로부터 이름 입력 받기
name = st.text_input('이름을 입력해주세요 : ')

# 색깔 선택
color = st.selectbox('좋아하는 색깔을 선택해주세요:', 
                     ['빨강', '파랑', '초록', '노랑', '보라', '주황', '검정', '흰색'])

# 성격 설명 딕셔너리
color_traits = {
    '빨강': '빨간색은 강력한 에너지를 상징하며, 열정, 사랑, 힘, 그리고 생명력을 의미합니다. 이 색을 선호하는 사람은 대개 활력이 넘치고 자신감이 있으며, 강한 의지를 가지고 있습니다. 빨간색은 또한 모험심과 도전정신을 나타냅니다. 이 색을 좋아하는 사람은 대개 위험을 감수하고자 하며, 새로운 경험을 추구하는 경향이 있습니다. 그들은 목표 지향적이며, 어려운 상황에서도 결단력 있게 행동하는 능력을 가지고 있습니다.

빨강은 심리적으로 흥분과 자극을 유발하며, 때로는 공격적이고 경쟁적인 태도를 나타내기도 합니다. 빨간색을 좋아하는 사람들은 대개 감정적으로 강하고, 자신의 의견을 분명하게 표현하는 것을 중요시합니다. 이들은 종종 리더십을 발휘하며, 사람들을 이끄는 능력이 뛰어납니다. 그러나 지나치게 빨간색에 집착할 경우, 과도한 스트레스나 불안감을 느낄 수 있으며, 이러한 감정이 극단적으로 표출될 수 있습니다.

빨간색을 선호하는 사람들은 또한 다른 사람들과의 관계에서 열정적이며, 강한 애정을 표현하는 경향이 있습니다. 그들은 사랑에 있어서도 매우 열정적이며, 관계에 깊이 헌신하는 경향이 있습니다. 이들은 종종 사랑을 삶의 중요한 요소로 여기며, 이를 통해 큰 만족감을 느낍니다. 그러나 이러한 열정이 때로는 소유욕이나 질투로 변질될 수 있기 때문에, 자기 통제가 필요할 때도 있습니다.

빨간색은 또한 물리적인 에너지를 나타내며, 활동적이고 스포티한 성격을 가지고 있을 가능성이 큽니다. 이 색을 좋아하는 사람들은 보통 운동을 즐기고, 경쟁에서 승리하는 것을 목표로 삼습니다. 그들은 도전에 맞서고, 항상 최선을 다해 승리를 쟁취하려는 의지가 강합니다.',
    '파랑': '침착하고 신뢰할 수 있는 사람입니다. 논리적이고 사려 깊은 성격을 가지고 있으며, 평화를 중요시합니다.',
    '초록': '균형 잡힌 삶을 추구하는 사람입니다. 친환경적이며, 조화와 자연을 사랑하는 성격을 가지고 있습니다.',
    '노랑': '긍정적이고 밝은 성격의 소유자입니다. 창의적이고 낙천적인 성향을 가지고 있으며, 다른 사람들에게 에너지를 줍니다.',
    '보라': '신비롭고 영감을 주는 성격을 가지고 있습니다. 예술적이고 독창적인 성향을 가지며, 깊은 사색을 즐깁니다.',
    '주황': '사교적이고 활발한 성격을 가지고 있습니다. 열정적이며, 새로운 경험을 좋아하고 모험을 즐깁니다.',
    '검정': '강한 의지를 가지고 있으며, 권위적이고 고급스러운 성향을 가지고 있습니다. 신비로움을 추구하며, 깊이 있는 성격입니다.',
    '흰색': '순수하고 깔끔한 성격을 가지고 있습니다. 간결함을 추구하며, 새로운 시작을 의미하는 색깔을 선호합니다.'
}

# 인사말 생성 버튼 클릭 시
if st.button('성격 분석') :
    # 선택한 색깔에 대한 성격 설명 출력
    st.write(f"{name}님! 당신이 좋아하는 색깔은 {color}입니다. {color_traits[color]}")
