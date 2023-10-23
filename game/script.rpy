# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"


image leenayoung_basic:
    ("이나영_기본.png")
    zoom 0.4

image note = "낡은노트.png"
image notebook:
    ("notebook.png")
    zoom 0.3


#배경 이미지
image classroom = "교실_오전.png"
image afterschool = "교실_노을.png"
image morning = "골목.png"
image afternoon = "골목_노을.png"
image night = "골목_저녁.png"
image cafeteria = "급식실.png"


define leenayoung = Character('이나영', color="#6bd8f3")
default leenayoung_affection = 0
define user = Character('[username]')
define rightCharacter = Position(xalign = 0.0, yalign = -0.05)
define character_center = Position(xalign = 0.5, yalign = 0.65)
init:
    $ nayoung_point = 0
    
label start:

    $ username = renpy. input('당신의 이름은?',length = 32)

    scene afternoon
    
    user "몇년만이지? 초2때 이사가고 고2때 이사 왔으니깐 거의 10년 만이네"
    
    #골목길 배경 2023년 3월 1일
    user "???"
    user "뭐지?"
    show leenayoung_basic at rightCharacter
    "골목에서 한 여자아이가 괴롭힘(?)을 당하는 것을 보았다."
    

    user "그냥 모르는 척 하자..."
    hide leenayoung_basic
    
    #골목길 배경
    scene morning
    "다음날"
    user "전학생이라고 따돌리거나 하진 않겠지?"
    user "오늘은 3월 2일 반애들 끼리도 별로 안친할거야"
    user "아무일 없을 거야"
    
    "교실에 들어간다."
    scene classroom


    "자리를 확인한다."
    play audio "의자끄는소리.mp3"
    "자리에 앉는다."

    "의자를 빼다 뒷자리 아이의 의자를 쳤다."
    play audio "연필떨어지는소리.mp3"
    "그로인해 샤프가 떨어졌다."

    "샤프를 주워 준다."

    user "'어? 이나영'"
    user "“아..여기 있어”"
    #종소리


    #대충 몇일 지남 날자 표시하기로 알 수 있게끔
    scene cafeteria
    #우당탕탕 하는 소리
    "일진 2" " 아 씨~~~발 뭐하냐?!!"
    "일진 2" "아 진짜 야 내가 너 걸리적거리지 말라 그랬지"
    leenayoung "미..미안.. 내가 잘못했어.."
    "일진 3" "아ㅋㅋ ㅁㅊ~ 존나 누가 보면 우리가 괴롭히는 줄 알겠어~"
    "일진 1" "됐어 야 평생 저렇게 살라그래"
    menu Help_in_cafeteria:
        "어떡해야하지?"
        "'급식 쏟아진거 주워줘야하나?'":
            $ nayoung_point += 1
            jump th1
        "'그..그냥 가자...":
            $ nayoung_point += 0
            jump march
    
    label th1:
        leenayoung "고마워...."
        leenayoung "근데 날 도와주지마.."
        jump march
    
    label march:
        scene morning
        #날짜, 툭하는 소리
        show note
        user "어 이거 떨어뜨리셨는데.."

        scene classroom
        show note at character_center:
            zoom(2.0)
        user "흠 다시 돌려드려야 하나"
        menu note_dilemma:
            "'한번 열어볼까'?":
                jump note_open
            "'음 그래도 다른 사람건데 열지 말자'":
                jump note_nopen
    
    label note_nopen:
        scene classroom
        show note at character_center:
            zoom(2.0)
        menu really:
            "'궁금하니깐 한번 열어보자'":
                jump note_open
            "'음 그래도 다른 사람건데 열지 말자'":
                jump note_nopen

    label note_open:
        scene classroom
        show notebook at character_center
        "첫 문장이 눈에 들어온다."
        "???" "\"20년 전의 나를 위하여, 20년 후의 내가\""

        user "'뭔소리지?'"
        "???" "\"2023년 3월 10일, 최은지네 무리가 나영이에게 급식실에서 해코지를 했다.왜 그들은 나영이에게 그러는 것일까?\""
        user "어? 이건..."

        "다음장을 넘겨보았다."
        "???" "\"2023년 3월 13일, 나영이가 나에게 정식으로 인사한 날, 나영이 덕분에 그동안 몰랐던 어렸을 때 추억이 떠올랐다...\""

    return
