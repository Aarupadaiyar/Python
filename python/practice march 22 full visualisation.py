#histogram for total bill
#bar graph of day and tip
#scatter plot for
#lineplot for tip and size
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("tips-1.csv")
#print top 10 rows
print(data.head(10))
plt.bar(data['day'],data['tip'])
plt.show()
#i want to group total tips of single day using sum 
agg_data=data.groupby('day')['tip'].sum()
print(type(agg_data))
#as we sum all the tip of single day , now dataframe converted into series
#so we are using index and values as x and y
plt.bar(agg_data.index,agg_data.values,color='skyblue')
plt.title("Bar Chart")
plt.xlabel('Day')
plt.ylabel('Tips')
plt.show()
#Line plot
plt.plot(data['tip'],data['size'])
plt.show()
plt.plot(data['tip'])
plt.plot(data['size'])
plt.title("Line chart")
plt.xlabel('Tip')
plt.ylabel('Size')
plt.show()
#scatterplot
plt.scatter(data['day'],data['size'])
plt.xlabel("Date")
plt.ylabel("Size")
plt.colorbar()
plt.show()
#histogram
plt.hist(data['total_bill'])
