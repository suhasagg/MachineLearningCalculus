import numpy as np
# For plotting
import matplotlib.pyplot as plt
import seaborn as sns

dat = np.array([[0,3], [-1,0], [1,2], [2,1], [3,3], [0,0], [-1,-1], [-3,1], [3,1]])
labels = np.array([1, 1, 1, 1, 1, -1, -1, -1, -1])

def plot_x(x, t, alpha=[], C=0):
    sns.scatterplot(x=dat[:,0], y=dat[:,1], style=labels,
                    hue=labels, markers=['s','P'], palette=['magenta','green'])
    if len(alpha) > 0:
        alpha_str = np.char.mod('%.1f', np.round(alpha, 1))
        ind_sv = np.where(alpha > ZERO)[0]
        for i in ind_sv:
            plt.gca().text(dat[i,0], dat[i, 1]-.25, alpha_str[i] )

plot_x(dat, labels)
plt.show()
