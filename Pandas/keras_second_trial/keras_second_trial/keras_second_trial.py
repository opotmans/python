
import pandas as pd
import matplotlib.pyplot as plt1
import seaborn as sb


# Read in white wine data test
white = pd.read_csv ("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv", sep=';')
# Read in red wine data 
red = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep=';')
#print
print ("white")
print (white.describe())

fig, ax = plt1.subplots(1, 2, figsize=(8, 4))

ax[0].scatter(red['quality'], red['alcohol'], color="red")
ax[1].scatter(white['quality'], white['alcohol'], color="white", edgecolors="black", lw=0.5)

ax[0].set_title("Red Wine")
ax[1].set_title("White Wine")
ax[0].set_xlabel("Quality")
ax[1].set_xlabel("Quality")
ax[0].set_ylabel("Alcohol")
ax[1].set_ylabel("Alcohol")
ax[0].set_xlim([0,9])
ax[1].set_xlim([0,9])
ax[0].set_ylim([0,15])
ax[1].set_ylim([0,15])
fig.subplots_adjust(wspace=0.5)
fig.suptitle("Wine Quality by Amount of Alcohol")

plt1.show()

red['type'] = 1
white['type'] = 0
wines = red.append(white, ignore_index=True)

print (wines.describe())

corr = wines.corr()
sb.heatmap(corr)
plt1.show()


