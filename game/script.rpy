#이나영 일러스트
image leenayoung_basic:
    ("이나영_기본.png")
    zoom 0.4
image leenayoung_smile:
    ("이나영_웃음.png")
    zoom 0.4
image leenayoung_eye_smile:
    ("이나영_눈웃음.png")
    zoom 0.4
image leenayoung_embarrassed:
    ("이나영_당황.png")
    zoom 0.4
image leenayoung_cowardice:
    ("이나영_겁.png")
    zoom 0.4

#소품 이미지
image note = "낡은노트.png"
image notebook:
    ("notebook.png")
    zoom 1.25


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
define leftChacter = Position(xalign = 0.3, yalign = 1.1)
init:
    $ nayoung_point = 0
    $ dday = 2023
    $ month = 3
    $ day = 1
    screen date:
            frame:
                xfill False
                hbox:
                    xalign .3 spacing 10
                    text '[dday]년 [month]월 [day]일'


label start:

    $ username = renpy. input('당신의 이름은?',length = 32)

    scene afternoon
    show screen date
    user "몇년만이지? 초2때 이사가고 고2때 이사 왔으니깐 거의 10년 만이네"
    
    #골목길 배경 2023년 3월 1일
    user "???"
    user "뭐지?"
    show leenayoung_cowardice at leftChacter:
        zoom(0.3)
    "골목에서 한 여자아이가 괴롭힘(?)을 당하는 것을 보았다."
    

    user "그냥 모르는 척 하자..."
    hide leenayoung_cowardice
    hide screen date
    
    #골목길 배경
    $ day + 1
    show screen date
    scene morning
    "--다음날--"
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
    user "아..여기 있어"
    #종소리


    #대충 몇일 지남 날자 표시하기로 알 수 있게끔
    scene cafeteria
    #우당탕탕 하는 소리
    "일진 2" " 아 씨~~~발 뭐하냐?!!"
    "일진 2" "아 진짜 야 내가 너 걸리적거리지 말라 그랬지"
    show leenayoung_embarrassed at rightCharacter
    leenayoung "미..미안.. 내가 잘못했어.."
    hide leenayoung_embarrassed
    show leenayoung_cowardice at rightCharacter
    "일진 3" "아ㅋㅋ ㅁㅊ~ 존나 누가 보면 우리가 괴롭히는 줄 알겠어~"
    "일진 1" "됐어 야 평생 저렇게 살라그래"
    hide leenayoung_cowardice
    menu Help_in_cafeteria:
        "어떡해야하지?"
        "'급식 쏟아진거 주워줘야하나?'":
            $ nayoung_point += 1
            jump th1
        "'그..그냥 가자...'":
            $ nayoung_point += 0
            jump march
    
    label th1:
        show leenayoung_basic at rightCharacter
        leenayoung "고마워...."
        leenayoung "근데 날 도와주지마.."
        hide leenayoung_basic
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
            "'한번 열어볼까?'":
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
        user "‘3월 13일.. 어 오늘이네? 뭐지..?’"

        #문열리는 소리 넣으셈 + 발자국 소리도
        user "'이게 진짜일까...?"
        
        leenayoung "안녕?"
        hide notebook
        show leenayoung_eye_smile at rightCharacter
        user "어..! 어 그래 안녕!?"
        user "‘우연인가..? 아님 진짠가..?’"
        hide leenayoung_eye_smile
        show leenayoung_basic at rightCharacter
        leenayoung "우리 어렸을 때 같이 동네에서 놀았었는데 기억나?"
        user "어 응.. 기억나지"
        leenayoung "다행이다 나만 기억하는 줄 알았어"
        user "하하.."
        "........"
        leenayoung "근데 왜 갑자기 이사갔던거야?"
        user "아 그때는 아빠 일때문에 갈 수 밖에 없었거든.." 
        user "근데 이젠 그 일도 다 끝나셔서  돌아온거지..!"
        hide leenayoung_basic
        show leenayoung_smile at rightCharacter
        leenayoung "그렇구나! 이젠 어디 안가는 거지?"
        user "그렇다고 볼 수 있지.."
        hide leenayoung_smile 
        show leenayoung_basic at rightCharacter
        leenayoung "다행이야.. 친구가 생겨서"

        #쾅 하고 문열리는 소리
        "이수민" "하 진짜~ 말도 지지리 안들어요"
        "김가영" "뭐냐 이 찔찔이는? 그새 친구도 사겼냐?"
        "김가영" "끼리끼리 만나도 하필 이나영같은 애를 만나냐 ㅋㅋ"

        "나는 가영이를 째려보았다."
        "김가영" "이 찐따새끼가 뭘 꼬라봐?"
        leenayoung "[user]\(이\)는 건들지마 내가 나갈게"

        "일진들이 나영이를 데리고 나갔다."
        user "어? 옛날에도 한번 이런적이.."

        "--6살때--"
        scene afternoon
        user "아악~! 하지마"
        "동네장난꾸러기들" "캬하하 이 바보 맨날 당하기만하고~"
        "어린 이나영" "뭐야 너네들!"
        "동네장난꾸러기들" "으악!! 도망가!!!"
        "어린 이나영" "괜찮아?"
        user "흑.. 고마오"
        "어린 이나영" "쟤네들이 또 괴롭히면 말해 내가 언제든 도와줄게!!"

        "--다시 현재--"
        scene classroom
        user "그래.. 나영이가 날 도와줬었어 어릴때부터.."
        show notebook at character_center
        "???" "\"누군가 나에게 지금까지 후회되는 일이 있냐고 묻는다면..\"" 
        "???" "\"20년전 나영이를 도와주지 못한것이다.. 그때 나영이를 알아봤다면 결말은 달라졌을까?\""
        "???" "\"......나영이가 떠나기 전으로 돌아가고 싶다\""
        hide notebook
        menu what:
            "'뭐지..? 나영이가 떠난다고?'"
            "이거 진짜 무슨 노트지?":
                jump save_nayoung
            "이건 대체....":
                jump save_nayoung
        
    label save_nayoung:
        user "이 노트가 진짜 무슨 미래에서 온 노트이든, 걍 아무개가 쓴 미친 종이 쪼까리든.."
        user "나영이를 구해줘야 하는 건 변하지 않아."

        hide classroom
        "--다음날--"
        

    return
