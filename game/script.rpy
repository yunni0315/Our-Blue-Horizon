﻿# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define leenayoung = Character('이나영', color="#6bd8f3")
define user = Character('[username]')

# 여기에서부터 게임이 시작합니다.
label start:

    $ username = renpy. input('당신의 이름은?',length = 32)
    

    return