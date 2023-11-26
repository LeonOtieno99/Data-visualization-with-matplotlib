import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('population_trends.csv', index_col=0)
df = pd.DataFrame(data)

#line chart
df.plot(kind='line')
plt.ylabel('Population')
plt.title('Line chart rep of the KE,TZ,UG Population trends')
plt.savefig('line_chart.png')

#bar chart
df.plot(kind='bar')
plt.ylabel('Population')
plt.title('Bar chart rep of the KE,TZ,UG Population trends')
plt.savefig('bar_chart.png')

plt.show()
