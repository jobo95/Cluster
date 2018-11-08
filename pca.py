

from sklearn.decomposition import PCA



def EOF():
    import numpy as np
    cos=np.sqrt(np.cos((np.pi/180)*np.abs(y)-30))
    t=0
    for k in range(data.shape[0]):
        data[:,k]=data[:,k]*cos[t]
        if k>=(t+1)*lon[:].size:
            t=t+1

    pca=PCA(n_components=5)
    pca.fit(data)
    pc=pca.transformi(data)
