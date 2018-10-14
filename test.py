import matplotlib as mpl
#mpl.use('Agg')
import matplotlib.pyplot as plt


labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
fracs = [15, 30, 45, 10]
explode=(0, 0.05, 0, 0)

plt.pie(fracs, explode=explode, labels=labels,
                autopct='%1.1f%%', shadow=False, startangle=90)

plt.title('Raining Hogs and Dogs', bbox={'facecolor':'0.8', 'pad':5})
plt.savefig(str('graph.png'), format='png', dpi=300)
plt.show()