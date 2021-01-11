import matplotlib.pyplot as plt

dataFilePath = "lab02_poketmon/poketmon_data.txt"
indexFilePath = "lab02_poketmon/poketmon_index.txt"

index_lst = []
indexstream = open(indexFilePath, encoding="utf-8")
datastream = open(dataFilePath, encoding="utf-8")
indexcontent = indexstream.readlines()
for i in indexcontent:
   index_lst.append(i.strip()) 
print(index_lst)
datacount = []
datacontent = datastream.read()
for i in index_lst:
    datacount.append(datacontent.count(i))
 
data_all = {}
print(datacount) 
for i in range(8):
    data_all[index_lst[i]] = datacount[i]
print(data_all)
indexstream.close()
datastream.close()


# def setKFont():
#     from matplotlib import font_manager, rc
#     font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/HYBDAL.TTF").get_name()
#     rc('font', family=font_name)
#     plt.rcParams["font.size"] = 14
#     plt.rcParams["figure.figsize"] = (14, 8)

# setKFont()

# plt.subplot(2,1,1)
# plt.bar(index_lst, datacount, width=0.5, color="grey")
# plt.title("포켓몬 카운터 ver 2.0")
# plt.xlabel("Poketmon name")
# plt.ylabel("num of poketmon")
# plt.subplot(2,1,2)
# plt.plot(index_lst, datacount)

# plt.xlabel("Poketmon name")
# plt.ylabel("num of poketmon")

# plt.show()