import pandas as pd
import matplotlib.pyplot as plt
#reading the database
data = pd.read_csv("Studentsperformances.csv")
#bar chart with day against tip
plt.bar(data['gender'],data['math score'])
plt.title("Bar Chart")
#Setting X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')
plt.show()
