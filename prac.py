import numpy as np

R = np.array([[0.5, 0.7, 0.2],
                  [0.8, 0.6, 0.9]])

S = np.array([[0.6, 0.3],
                 [0.9, 0.4],
                 [0.5, 0.8]])

result = []

for i in range(len(R)):
    res = []
    for j in range(len(S[0])):
        elList = []
        for k in range(len(S)):
            el = np.minimum(R[i][k], S[k][j])
            elList.append(el)
        res.append(max(elList))
    result.append(res)
print(np.array(result))