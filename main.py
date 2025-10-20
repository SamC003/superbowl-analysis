
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("superbowl.csv")
print()
print(list(df.columns))
print()
print(df.head())
print(df.info())


# graph for wins per team
win_count = df['Winner'].value_counts()
print(win_count)
win_count.plot(kind = 'bar')

plt.title('Super Bowl Wins by Team')
plt.xlabel("Team")
plt.ylabel("Wins")
plt.xticks(rotation=45, fontsize=7)
plt.show()


# graphs for winner pts
points_to_win = df["Winner Pts"].value_counts().sort_index()
points_to_win.plot(kind = 'bar')
plt.title('Super Bowl Wins by Points Scored')
plt.xlabel('Points')
plt.ylabel('Super Bowl Wins')
plt.show()


# graph for point difference
df["Point Diff"] = df["Winner Pts"] - df["Loser Pts"]
diff_counts = df["Point Diff"].value_counts().sort_index()
diff_counts.plot(kind = 'bar')
plt.title("Super Bowl Point Difference")
plt.xlabel('Points')
plt.ylabel('Super Bowl Points Difference')
plt.show()