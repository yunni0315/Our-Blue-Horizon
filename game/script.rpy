# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"
image leenayoung_basic:
    ("이나영_기본.png")
    zoom 0.15

define leenayoung = Character('이나영', color="#6bd8f3")
default leenayoung_affection = 0
define user = Character('[username]')
define rightCharacter = Position(xalign = 1.0, yalign = 1.0)

label start:

    $ username = renpy. input('당신의 이름은?',length = 32)
    
    user "몇년만이지? 초2때 이사가고 고2때 이사 왔으니깐 거의 10년 만이네"
    
    #골목길 배경 2023년 3월 1일
    user "???"
    user "뭐지?"
    show leenayoung_basic at rightCharacter
    "골목에서 한 여자아이가 괴롭힘(?)을 당하는 것을 보았다."
    

    user "그냥 모르는 척 하자..."

    
    #골목길 배경
    "다음날"
    user "전학생이라고 따돌리거나 하진 않겠지?"
    user "오늘은 3월 2일 반애들 끼리도 별로 안친할거야"
    user "아무일 없을 거야"
    
    "교실에 들어간다."

    "자리를 확인한다."

    "자리에 앉는다."
        

    "의자를 빼다 뒷자리 아이의 의자를 쳤다."
    "그로인해 샤프가 떨어졌다."

    "샤프를 주워 준다."

    user "'어? 이나영'"
    return
