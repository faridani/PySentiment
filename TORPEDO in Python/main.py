
from scipy.io import loadmat
x = loadmat('data\comments.mat')
comments = x['comments']
CommentsTexts = comments[:,3]
