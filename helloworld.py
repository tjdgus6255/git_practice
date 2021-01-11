import numpy as np

def readtxt_returnlst(txtPath):
    ftream = open(txtPath, encoding="utf-8")
    rltList = ftream.readlines()
    ftream.close()
    return rltList

dataFilePath    = "lab02_poketmon/poketmon_data.txt"
indexFilePath   = "lab02_poketmon/poketmon_index.txt"

# index 파일을 읽어서 포켓몬 이름이 들어가 있는 리스트만들기
poketmon_name_list = list()

# fStream = open(indexFilePath,encoding="utf-8")
# temp_list = fStream.readlines()
# fStream.close()

temp_list = readtxt_returnlst(indexFilePath)
for i in temp_list :
    poketmon_name_list.append( i.strip() )
# 포켓몬 이름이 있는 리스트와 동일한 길이의 리스트를 만들고 0으로 초기화해두기
# poketmon_count_list = list()
# for i in poketmon_name_list :
#     poketmon_count_list.append(0)

poketmon_count_list = np.zeros([len(poketmon_name_list)], dtype=int)
print(len(poketmon_name_list))
print(len(poketmon_count_list))


# Data 파일을 읽어서 반복문을 돌면서 해당 포켓몬이 들어있는 index 값 찾기
all_poketmonData_list = readtxt_returnlst(dataFilePath)
for each in all_poketmonData_list :
    each_poketmon = each.strip()
    target_index = poketmon_name_list.index( each_poketmon )

    # 0으로 초기화 해두었던 list에 위에서 찾았던 index번호에 +1 해주기
    poketmon_count_list[target_index] += 1


print(poketmon_name_list)
print(poketmon_count_list)


# 이쁘게 출력하기
for i in range( len(poketmon_name_list) ) :
    print(poketmon_name_list[i], ":", poketmon_count_list[i])