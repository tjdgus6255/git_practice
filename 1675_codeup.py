transform_list = ['x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',                   # 해독 후 문자 리스트 
'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w']
origin_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',                 # 해독 전 문자 리스트
 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = input()         
for i in range(len(text)):                                                            # 입력 받은 문자길이 만큼 for문을 돌림
    if text[i] >= 'a' and text[i] <= 'z':                                             # 입력 받은 문자가 a-z사이의 문자에 한해서
        print(transform_list[origin_list.index(text[i])], end='')                     # 입력 받은 문자를 orgin_list에서 찾고 
    else:                                                                             # origin_list의 index번호와 동일한 index를 가진 
        print(" ", end='')                                                            # transform_list값 출력
                                                                                      # a-z이외의 값은 띄어쓰기
# 설명
# 암호 해독 - 암호문에 쓰인 알파벳보다 3만큼 이동한 알파벳으로 치환