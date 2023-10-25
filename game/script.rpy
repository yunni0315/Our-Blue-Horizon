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
image leenayoung_embarrassing:
    ("이나영_부끄러움.png")
    zoom 0.3
image leenayoung_Totally_shameful:
    ("이나영_완전부끄러움.png")
    zoom 0.2
image leenayoung_vapor:
    ("이나영_침울.png")
    zoom 0.2

#일진 사진
image leesumin:
    ("이수민.png")
    zoom 0.6
image kimgayoung:
    ("김가영.png")
    zoom 0.6
image choienji:
    ("최은지.png")
    zoom 0.6
image triple:
    ("3인방.png")
    zoom 0.5

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
image cinema = "영화관.png"

define leenayoung = Character('이나영', color="#6bd8f3")
define user = Character('[username]')
define choi = Character('최은지', color = "#b46bf3")
define lee = Character('이수민', color = "#40e940")
define kim = Character('김가영', color = "#fcab42")

default leenayoung_affection = 0
define cneterCharacter = Position(xalign = 0.0, yalign = -0.05)
define cneterCharacter_for_embarrsing = Position(xalign = 0.5, yalign = 0.22)
define object_center = Position(xalign = 0.5, yalign = 0.65)
define leftChacter_for_first = Position(xalign = 0.3, yalign = -0.05)
define leftChacter = Position(xalign = 6.5, yalign = -0.05)
define rightCharacter = Position(xalign = -6.5, yalign = -0.05)
define rightvapor =  Position(xalign = 0.63, yalign = 0.7)

init:
    $ nayoung_point = 0



label start:

    $ username = renpy. input('당신의 이름은?',length = 32)

    scene afternoon
    
    "2023년 3월 1일"
    user "몇년만이지? 초2때 이사가고 고2때 이사 왔으니깐 거의 10년 만이네"
    
    #골목길 배경 2023년 3월 1일
    user "???"
    user "뭐지?"
    show leenayoung_vapor at rightvapor:
        zoom(0.3)
    "골목에서 한 여자아이가 괴롭힘(?)을 당하는 것을 보았다."
    

    user "그냥 모르는 척 하자..."
    hide leenayoung_vapor
    
    #골목길 배경
    
    scene morning
    "2023년 3월 2일"
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
    "2023년 3월 10일"
    #우당탕탕 하는 소리
    show leesumin at right
    lee " 아 씨~~~발 뭐하냐?!!"
    lee "아 진짜 야 내가 너 걸리적거리지 말라 그랬지"
    show leenayoung_embarrassed at cneterCharacter
    leenayoung "미..미안.. 내가 잘못했어.."
    hide leenayoung_embarrassed
    show leenayoung_cowardice at cneterCharacter
    hide leesumin
    show kimgayoung at left
    kim "아ㅋㅋ ㅁㅊ~ 존나 누가 보면 우리가 괴롭히는 줄 알겠어~"
    show choienji at right
    choi "됐어 야 평생 저렇게 살라그래"
    hide choienji
    hide kimgayoung
    hide leenayoung_cowardice
    menu Help_in_cafeteria:
        "어떡해야하지?"
        "'급식 쏟아진거 주워줘야하나?'":
            $ nayoung_point += 1
            jump th1
        "'그..그냥 가자...'":
            $ nayoung_point += 0
            jump march
return

label th1:
    show leenayoung_basic at cneterCharacter
    leenayoung "고마워...."
    leenayoung "근데 날 도와주지마.."
    hide leenayoung_basic
    jump march

label march:
    scene morning
    #날짜, 툭하는 소리
    "2023년 3월 13일"
    show note
    user "어 이거 떨어뜨리셨는데.."

    scene classroom
    show note at object_center:
        zoom(2.0)
    user "흠 다시 돌려드려야 하나"
    menu note_dilemma:
        "'한번 열어볼까?'":
            jump note_open
        "'음 그래도 다른 사람건데 열지 말자'":
            jump note_nopen

label note_nopen:
    scene classroom
    show note at object_center:
        zoom(2.0)
    menu really:
        "'궁금하니깐 한번 열어보자'":
            jump note_open
        "'음 그래도 다른 사람건데 열지 말자'":
            jump note_nopen

label note_open:
    scene classroom
    show notebook at object_center
    "첫 문장이 눈에 들어온다."
    "???" "\"20년 전의 나를 위하여, 20년 후의 내가\""

    user "'뭔소리지?'"
    "???" "\"2023년 3월 10일, 최은지네 무리가 나영이에게 급식실에서 해코지를 했다.왜 그들은 나영이에게 그러는 것일까?\""
    user "어? 이건..."

    "다음장을 넘겨보았다."
    "???" "\"2023년 3월 13일, 나영이가 나에게 정식으로 인사한 날, 나영이 덕분에 그동안 몰랐던 어렸을 때 추억이 떠올랐다...\""
    user "‘3월 13일.. 어 오늘이네? 뭐지..?’"

    #문열리는 소리 넣으셈 + 발자국 소리도
    play audio "문여는 소리.mp3"
    play audio "발자국 소리.mp3"
    user "'이게 진짜일까...?"
    
    leenayoung "안녕?"
    hide notebook
    show leenayoung_eye_smile at cneterCharacter
    user "어..! 어 그래 안녕!?"
    user "‘우연인가..? 아님 진짠가..?’"
    hide leenayoung_eye_smile
    show leenayoung_basic at cneterCharacter
    leenayoung "우리 어렸을 때 같이 동네에서 놀았었는데 기억나?"
    user "어 응.. 기억나지"
    leenayoung "다행이다 나만 기억하는 줄 알았어"
    user "하하.."
    "........"
    leenayoung "근데 왜 갑자기 이사갔던거야?"
    user "아 그때는 아빠 일때문에 갈 수 밖에 없었거든.." 
    user "근데 이젠 그 일도 다 끝나셔서  돌아온거지..!"
    hide leenayoung_basic
    show leenayoung_smile at cneterCharacter
    leenayoung "그렇구나! 이젠 어디 안가는 거지?"
    user "그렇다고 볼 수 있지.."
    hide leenayoung_smile 
    show leenayoung_embarrassing at cneterCharacter_for_embarrsing
    leenayoung "다행이야.. 친구가 생겨서"
    hide leenayoung_embarrassing
    #쾅 하고 문열리는 소리
    play audio "문여는 소리.mp3"
    show choienji at center
    choi "야 이나영 너 내가 일찍 오라그랬지"
    hide choienji
    show triple at center
    hide triple
    show leesumin
    lee "하 진짜~ 말도 지지리 안들어요"
    show kimgayoung
    kim "뭐냐 이 찔찔이는? 그새 친구도 사겼냐?"
    kim "끼리끼리 만나도 하필 이나영같은 애를 만나냐 ㅋㅋ"
    hide leesumin

    "나는 가영이를 째려보았다."
    kim "이 찐따새끼가 뭘 꼬라봐?"
    menu fight:
        "'히익 저 드러운 눈깔 좀 봐..  가만히 있어야지'":
            jump pastsceen
        "'뭐 찐따새끼? 이게..!'":
            jump realfight

label realfight:
    kim "뭘 꼬라봐?!"
    jump pastsceen

label pastsceen:            
    show leenayoung_embarrassed at cneterCharacter
    leenayoung "[user]\(이\)는 건들지마 내가 나갈게"
    hide leenayoung_embarrassed
    hide kimgayoung
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
    show notebook at object_center
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
    scene afterschool
    user "이 노트가 진짜 무슨 미래에서 온 노트이든, 걍 아무개가 쓴 미친 종이 쪼까리든.."
    user "나영이를 구해줘야 하는 건 변하지 않아."
    scene classroom
    "2023년 3월 14일"
    show kimgayoung
    kim "야 이나영, 나와"

    user "나영아!"
    show choienji
    choi " ..?뭐야 저 새낀"
    show leesumin
    lee "너 저번에 갠가? 걍 신경 끄고 가?"
    user "우리 발표 같은 조거든..? 같이 준비할게 있어"
    hide kimgayoung
    hide leesumin
    choi "허 ㅋㅋㅋㅋ 개어이털리네"
    show kimgayoung
    kim "우리가 우습지? 확씨그냥"
    hide kimgayoung
    hide choienji

    "선생님" "뭐야! 너네들 우리반 아닌 애들 다 나가!"
    show triple
    choi "하."
    hide triple
    show choienji
    "최은지가 입모양으로 뭐라 그런다."
    hide choienji
    play audio "문여는 소리.mp3"
    user "'우오오아?'"

    jump first_date

label first_date:
    scene classroom
    "2023년 3월 24일"
    user "나영아..!"
    show leenayoung_basic at cneterCharacter
    leenayoung "어? 으응..?"
    user "이번주에 혹시 뭐 다른거 있어?"
    leenayoung "아니..  없어.. 왜?"
    user "그..이번 주말에 시간되나해서"
    leenayoung "..."
    hide leenayoung_basic
    show leenayoung_embarrassing at cneterCharacter_for_embarrsing
    leenayoung "?!?!"
    leenayoung "호...혹시.."
    leenayoung "이거....."
    leenayoung "데이트..?"
    hide leenayoung_embarrassing
    user "어?!"
    user "어...어떻게 보면 그렇지?"
    user "싫어?"
    show leenayoung_embarrassing at cneterCharacter_for_embarrsing
    leenayoung "아니"
    leenayoung "좋아..."
    hide leenayoung_embarrassing
    

    scene morning
    "2023년 3월 26일  일요일"
    user "아..  내가 먼저 말하긴 했는데 좀 떨리네.."
    
    user "'와..  오늘따라 진짜 이뻐보이네 평소랑 달라진건 없어보이는데..'"
    menu mind:
        "나영아 너 오늘 예쁘다":
            show leenayoung_smile at cneterCharacter
            leenayoung "아! 고마워 ㅎㅎ"

        "가. .갈까..??":
            show leenayoung_embarrassing at cneterCharacter_for_embarrsing
            leenayoung "어..  엉..!"
    
    scene cinema

    user "시작한다..!"
    leenayoung "응.."
    "나영을 뚫어져라 쳐다보다가 나영과 눈이 마주친다."
    show leenayoung_Totally_shameful at Position(xalign = -0.2, yalign= 0.7)
    leenayoung "...!"
    hide leenayoung_Totally_shameful
    "영화가 끝났다"
    user "재..재미있었어?"
    show leenayoung_basic at cneterCharacter
    leenayoung "응! 난 재밌었어 특히 주인공이 여주를 구해주는 장면이 정말 멋있더라"
    user "하하핫..! 나도 그장면 좋았어"
    hide leenayoung_basic
    show leenayoung_eye_smile at cneterCharacter
    leenayoung "ㅎㅎ…."
    user "집 데려다 줄게..!" 
    hide leenayoung_eye_smile
    scene night

    "어느새 나영의 집 앞에 도착한다"
    show leenayoung_basic at cneterCharacter
    leenayoung  "잘가 내일 학교에서 보자.."
    user "응.. 그러자!"
    leenayoung "어~ 들어가"
    hide leenayoung_basic
    menu see_you_next_time:
        " 다음에도 또 영화같이 볼래?":
            show leenayoung_smile at cneterCharacter
            leenayoung "그래!"
            hide leenayoung_smile

        "나도 즐거웠어 나영아 잘 들어가":
            show leenayoung_eye_smile at cneterCharacter
            leenayoung "어~" 
            hide leenayoung_eye_smile

    scene classroom
    "2023년 3월 27일"

    "선생님" "얘들아 어느새 3월 마지막 주지?"

    "학생들" "네~"

    "선생님" "4월달 들어서는 반장선거를 할 예정이니"
    "선생님" "혹시 반장선거에 나가고싶다면 교무실로 찾아와라~"

    "학생들" "넵~!"

    play audio "문여는 소리.mp3"

    "웅성웅성"

    "학생1" "야 너가 나가라~ ㅋㅋ"
    "학생2" "누가 하게 될까?"
    
    play audio "문여는 소리.mp3"


    show triple
    menu be_a_Class_monitor:
        "너네들 나가라 우리 반 아닌 애들은 특히..!":
            hide triple
            choi "또 너냐? 진짜 나대지 말라니까..!"
            show choienji
            user "그냥 나가지? 곧 종도 치는데" 
            user "그리고.." 
            user "아무리 너가 좀 잘나가고 그래도 난 너한테 안 맞고 다니지 안그래?"

            
            "반친구들" "뭐야 뭐야 주인공이 저런 애였어?"
            "웅성웅성"

            choi "허.,! 참..!"
            
            user "그냥 나가라 빨리 너도 쪽팔리잖아?"
            hide choienji
            play audio "문여는 소리.mp3"

            user "후.. 드디어 갔네"

        " 야 이나영-! 아까 선생님이 너랑 나랑 교무실로 오라셨어 지금 가야해":
            hide triple
            show choienji
            choi "야 너네 거기서라?"
            user "미안하지만 선생님이 부르셔서말이야"
            show kimgayoung
            kim "그건 나중에 가도 되잖아 나영이는 우리랑 할말 있다니까?"
            show leesumin
            lee "그래 찐따야 ㅋㅋ..  나중에 나영이랑 손잡고 가세요~"
            hide kimgayoung
            hide leesumin
            hide choienji
            jump be_a_Class_monitor

    user "후.. 드디어 갔네"
    show leenayoung_embarrassing at cneterCharacter_for_embarrsing
    leenayoung "..고마워"#(벌게진 표정으로) 
    user "아니야 전부터 시끄러웠었잖아"
    user "이번기회에 나도 걍 말한거지 뭐"
    hide leenayoung_embarrassing

    user "..?무슨 할말있어?"
    show leenayoung_basic at cneterCharacter
    leenayoung "[username]아. 이번 반장선거 말이야"
    user "아 응" 
    leenayoung "너가 나가보는 건 어때?"

    user "내,.내가??" 
    leenayoung "응! 너라면 잘해낼 수 있을것 같아서"
    hide leenayoung_basic

    show leenayoung_eye_smile at cneterCharacter
    #나영의 미소에 심장이 뛰는 주인공
    user "어..그래 한번 생각해볼게"
    hide leenayoung_eye_smile
    
    "2023년 4월 3일"

    #주인공은 평소대로 학교에 등교한다.
    #자리에 앉는 주인공

    play audio "의자끄는소리.mp3"

    show leenayoung_basic at cneterCharacter
    leenayoung "오늘 반장선거네?"
    user "그렇지.."
    leenayoung "너 나갈거지?" 
    user "흠… 나영아 너는 내가 꼭 나갔으면 좋겠어?"

    leenayoung "...."
    leenayoung "..응 너가 반장을 해준다면," 
    hide leenayoung_basic
    show leenayoung_smile at cneterCharacter
    leenayoung "나 이번학년은 진짜 행복할것같아" #(싱긋 웃는다)

    menu election:
        "너가 그렇게 말해준다면야..  당연히 나갈게!":
            hide leenayoung_smile
            leenayoung "응! 기대할게?"
            show leenayoung_eye_smile at cneterCharacter

        "그렇지 않아도 나갈려고 했거든?":
            leenayoung "아.. 어 고마워 ㅎㅎ 응원할게"
            hide leenayoung_basic

    play audio "문여는 소리.mp3"
    hide leenayoung_eye_smile

    "탁탁-"

    "선생님" "모두 주목-!" 
    "선생님" "오늘은 공지했던대로 4월달이 되었으니 반장선거를 할거다."

    "선생님" "근데 저번에 아무도 교무실을 안오더라~?"
    "선생님" "지금이라도 반장선거에 나가고 싶다면, 손들어" 

    "선생님" "누구 할 사람?"

    "학생1" "저요!"

    "선생님" "그래 또?"

    "학생2" "저요!" 

    "학생3" "저두요"

    "선생님" "또 없지? 이제 그만한ㄷ.."

    

    user "저요!"

    "선생님" "그래 그럼 주인공이 까지 하고 마무리하자"
    "선생님" "차례대로 나와서 공약 발표 해볼까?"

    "학생1" "저는 반장이 된다면~..."

    user "'아 떨린다..  막상 한다고 하니까 긴장이 되네..'"
    "나영과 눈을 마주쳤다."

    "나영이가 주인공을 향해 작은 목소리로 얘기한다."

    leenayoung "화이팅!"


    "선생님" "그래 마지막으로 [username]  나와서 말해볼까?"

    user "제가 만약…"

    "..."

    "~하교길~"
    scene afternoon
    show leenayoung_smile at cneterCharacter
    leenayoung "반장된거 축하해 00아! 너가 될줄 알았어"
    user "너 덕분이지 뭐.."
    leenayoung "아니야 너가 잘한거야"
    user "ㅎㅎ 고맙다"
    hide leenayoung_smile

    "터벅터벅.."
    show leenayoung_embarrassing at cneterCharacter_for_embarrsing

    leenayoung "00아.. 나 할말있어"
    user "왜?"
    leenayoung "그…  그게.. 뭐냐면.."
    hide leenayoung_embarrassing
    show leenayoung_basic at cneterCharacter
    user "응?"
    hide leenayoung_basic
    show leenayoung_embarrassing at cneterCharacter_for_embarrsing
    leenayoung "나랑 사귈래?"
    hide leenayoung_embarrassing
    user "응"
    user "...으으으으으응??????????"
    user "나..나랑?" 
    show leenayoung_embarrassing at cneterCharacter_for_embarrsing
    leenayoung "'끄던끄던'"#(부끄러운 표정으로) (끄덕끄덕)
    user "어어.."  
    hide leenayoung_embarrassing

    menu love_or_death:
        "사실 나도 널 좋아했었어.. 그래 사귀자!":
            jump love


        " 고백은 고맙지만....":
            jump death

label love:
    show leenayoung_embarrassed at cneterCharacter
    leenayoung "지...진짜?"
    leenayoung "나랑 사귄다고?"
    hide leenayoung_embarrassed 
    leenayoung "진짜?"
    show leenayoung_Totally_shameful at Position(xalign = -0.2, yalign= 0.7)
    user "나도 너를 좋아해서"
    user "정말 기뻤어"
    hide leenayoung_Totally_shameful
    show leenayoung_embarrassing at cneterCharacter_for_embarrsing
    leenayoung "그..그럼"
    leenayoung "오늘부터 1일이다!!!"
    jump credits_happy


label death:
    show leenayoung_cowardice at cneterCharacter
    user "나는..." 
    user "그런 말을 나에게 해준게 너무 고마워" 
    user "하지만 나는 지금 그런 관계를 맺을 준비가 되지 않은 것 같아"
    user "우리가 계속해서 친구로 지내는 건 어떨까?"
    leenayoung "그...그치"
    leenayoung "그래도....."
    leenayoung "그래도...."
    hide leenayoung_embarrassed
    show leenayoung_basic at cneterCharacter
    leenayoung "나랑 계속 친구로 지네 줄 거지?"
    user "물론이지..!"
    jump credits_friends
        

label credits_happy:
    $ credits_speed = 25 #scrolling speed in seconds
    scene black #replace this with a fancy background
    with dissolve
    show Day_1_From_Today:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide Day_1_From_Today
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks
    return

label credits_friends:
    $ credits_speed = 25 #scrolling speed in seconds
    scene black #replace this with a fancy background
    with dissolve
    show Lets_be_Friends:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide Lets_be_Friends
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks
    return

init python:
    credits = ('Backgrounds', 'Airgoof'), ('Backgrounds', 'Dorktwerp'), ('Sprites and CG', 'Ballclown'), ('GUI', 'Cuddlywad'), ('Writing', 'Dorktwerp'), ('Writing', 'Fingerpookie'), ('Programming', 'Dorktwerp'), ('Music', 'Grumblemuck'), ('Music', 'Headwookum')
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}Ren'py\n6.15.7.374" #Don't forget to set this to your Ren'py version
    
init:
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}The end", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)