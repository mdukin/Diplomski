import numpy as np
import sklearn
import matplotlib.pyplot as plt
from numpy import linalg
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def plot_2d_clf_problem(X, y, h=None):
    '''
    Plots a two-dimensional labeled dataset (X,y) and, if function h(x) is given,
    the decision surfaces.
    '''
    assert X.shape[1] == 2, "Dataset is not two-dimensional"
    if h!=None :
        # Create a mesh to plot in
        r = 0.04  # mesh resolution
        x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        xx, yy = np.meshgrid(np.arange(x_min, x_max, r),
                             np.arange(y_min, y_max, r))
        XX=np.c_[xx.ravel(), yy.ravel()]
        try:
            Z_test = h(XX)
            if Z_test.shape == ():
                # h returns a scalar when applied to a matrix; map explicitly
                Z = np.array(list(map(h,XX)))
            else :
                Z = Z_test
        except ValueError:
            # can't apply to a matrix; map explicitly
            Z = np.array(list(map(h,XX)))
        # Put the result into a color plot
        Z = Z.reshape(xx.shape)
        plt.contourf(xx, yy, Z, cmap=plt.cm.Pastel1)

    # Plot the dataset
    plt.scatter(X[:,0],X[:,1], c=y, cmap=plt.cm.tab20b, marker='o', s=50);
X = np.array([[-3,1],
             [-3,3],
            [10,1],
              [10, 2],
              [12, 0],
              [13, -1],
             [1,2],
             [2,1],
             [1,-2],
             [2,-3]])
y = np.array([0,0,1,1,1,1,1,1,
              2,2])

x0 = np.array([1,-1,3])


klase = [0,1,2]
fi = PolynomialFeatures(1).fit_transform(X)
for klasa in klase:
    y_new = np.zeros(len(y))
    for i in range(len(y)) :
        if y[i] == klasa:
            y_new[i]= 1

    w = np.dot(linalg.pinv(fi),y_new)
    h = np.dot(w,x0)
    print(klasa)
    print(w)
    print(h)
    model = LinearRegression().fit(X, y_new)
   # plot_2d_clf_problem(X,y,lambda x: model.predict(x) >= 0.5)
    plt.show()

for i in range(len(klase)):
    for j in range(i+1,len(klase)):
        y_new =[]; x_new = []
        for k in range(len(y)):
            if y[k] == klase[i]:
                x_new.append(X[k])
                y_new.append(1)
            if y[k] == klase[j]:
                y_new.append(0)
                x_new.append(X[k])
        print(x_new,y_new)
        fi = PolynomialFeatures(1).fit_transform(x_new)
        w = np.dot(linalg.pinv(fi), y_new)
        h = np.dot(w,x0)
        print(i,j)
        print(w)
        print(h)

        model = LinearRegression().fit(x_new, y_new)
        plot_2d_clf_problem(np.array(x_new), np.array(y_new)
                            , lambda x: model.predict(x) >= 0.5)
        plt.show()