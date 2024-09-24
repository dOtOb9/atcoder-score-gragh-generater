import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')


df = pd.read_csv('atcoder_score_data.csv')

fig, ax = plt.subplots(1, 1)

# 成績のプロット
ax.plot(df['date'], df['performance'], marker='o', label='Performance')
ax.plot(df['date'], df['rate'], marker='o', label='Rate')

# レートの色付け
ax.axhspan(ymin=400, ymax=800, color='saddlebrown', alpha=0.2) # 茶色
ax.axhspan(ymin=800, ymax=1200, color='lime', alpha=0.2) # 緑色
ax.axhspan(ymin=1200, ymax=1600, color='skyblue', alpha=0.2) # 水色
ax.axhspan(ymin=1600, ymax=2000, color='blue', alpha=0.2) # 青色
ax.axhspan(ymin=2000, ymax=2400, color='gold', alpha=0.2) # 黄色
ax.axhspan(ymin=2400, ymax=2800, color='orange', alpha=0.2) # 橙色
ax.axhspan(ymin=2800, ymax=4000, color='red', alpha=0.2) # 赤色

ax.set_ylim(bottom=0, top=max(max(df['performance']), max(df['rate']))*1.2)

ax.set_title('AtCoder Score History')
ax.legend(loc='lower right')

plt.savefig('./output/fig.png')
plt.show()
