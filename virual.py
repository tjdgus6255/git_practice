import pandas as pd
import matplotlib.pyplot as plt

num_series = pd.Series([1,2,3,4,5], index = ["index_0", "index_1", "index_2", "index_3", "index_4"])
num_df = pd.DataFrame([1,2,3,4,5], index = ["index_0", "index_1", "index_2", "index_3", "index_4"])

# print(num_series)
# print(num_df)

titanic_csv_filePath = "train.csv"
titanic_df = pd.read_csv(titanic_csv_filePath)
# print(titanic_df)
# print(titanic_df.info())

alive = titanic_df[titanic_df["Survived"] == 1]
dead = titanic_df[titanic_df["Survived"] == 0]

# print(len(alive) , "/" , len(titanic_df))
# print(len(dead) , "/" , len(titanic_df))

# plt.bar(["alive", "dead"], height=[len(alive), len(dead)], width = 0.5, color="green")
# plt.show()
dict = {"alive" : "green", "dead" : "red"}
# plt.scatter(alive["PassengerId"], alive["Fare"], c="b", marker="o")
# plt.scatter(dead["PassengerId"], dead["Fare"], c="r", marker="x")

# plt.xlabel("PassengerID")
# plt.ylabel("Fare")

# plt.show()

rich = titanic_df[titanic_df["Fare"] >= 50]
poor = titanic_df[titanic_df["Fare"] < 50]
# print(len(rich), "/", len(titanic_df), str(len(rich)/len(titanic_df)*100)[0:5])
# print(len(poor), "/", len(titanic_df), str(len(poor)/len(titanic_df)*100)[0:5])
alive_over_50 = rich[rich["Survived"] == 1]
alive_under_50 = poor[poor["Survived"] == 1]

# print(len(alive_over_50))
# print(len(alive_under_50))

def setKFont():
    from matplotlib import font_manager, rc
    font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/HYBDAL.TTF").get_name()
    rc('font', family=font_name)
    plt.rcParams["font.size"] = 14
    plt.rcParams["figure.figsize"] = (14, 8)

setKFont()

plt.subplot(2,1,1)
plt.xlabel("$50미만 생존 비율")
plt.pie([len(under50_alive_df), len(under50_df)-len(under50_alive_df)], colors=["green", "red"], labels=("Alive", "Dead"))
plt.subplot(2,1,2)
plt.xlabel("$50이상 생존 비율")
plt.pie([len(over50_alive_df), len(over50_df)-len(over50_alive_df)], colors=["green", "red"], labels=("Alive", "Dead"))
plt.show()