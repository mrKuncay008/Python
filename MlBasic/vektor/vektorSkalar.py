import numpy as np # type: ignore
import sympy as sym # type: ignore
import matplotlib.pyplot as plt # type: ignore
from IPython.display import Math # type: ignore
## Di jalankan di jupyterNotebook

# Mendefinisikan vektor dasar dan faktor skalar
v = np.array([1,2])
sk = [-0.5, 1, 1.5, 3]

# Membuat plot untuk setiap faktor skalar
for i in sk:
    sk_v = i * v
    plt.plot([0, sk_v[0]], [0, sk_v[1]], 'o-', linewidth = 3, label='Skalar=%g' %i)

# Mengatur tampilan plot
plt.axis('square')
plt.grid()
plt.legend()
plt.show()
