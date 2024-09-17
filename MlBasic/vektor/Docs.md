## Penjelasan Kode

```python
    ## Import Paket:
        numpy (diimpor sebagai np): Digunakan untuk operasi vektor dan array.
        matplotlib.pyplot (diimpor sebagai plt): Digunakan untuk membuat grafik dan plot.
```

```python
    # Definisi Vektor dan Faktor Skalar:
        v = np.array([1,2]): Mendefinisikan vektor dua dimensi [1, 2].
        sk = [-0.5, 1, 1.5, 3]: Mendefinisikan list faktor skalar yang berbeda.

    # Loop dan Plotting:
        Loop for i in sk mengiterasi setiap faktor skalar dalam list sk.
        sk_v = i * v menghitung vektor hasil perkalian skalar dengan vektor dasar.
        plt.plot([0, sk_v[0]], [0, sk_v[1]], 'o-', linewidth = 3, label='Skalar=%g' %i) menggambar garis dari titik (0,0) ke titik (sk_v[0], sk_v[1]) dengan label yang menunjukkan faktor skalar.
```

```python
    # Pengaturan Plot:
        plt.axis('square'): Mengatur agar sumbu x dan y memiliki skala yang sama.
        plt.grid(): Menambahkan grid ke plot.
        plt.legend(): Menampilkan legenda yang menjelaskan faktor skalar.
        plt.show(): Menampilkan grafik.
```

## IMport Paket

```python
import numpy as np
import matplotlib.pyplot as plt
```

- numpy (diimpor sebagai np):

    Digunakan untuk operasi numerik dan manipulasi array. Dalam kode ini, numpy digunakan untuk mendefinisikan dan mengalikan vektor.

- matplotlib.pyplot (diimpor sebagai plt):

    Digunakan untuk membuat grafik dan visualisasi data. Dalam kode ini, matplotlib digunakan untuk menggambar dan menampilkan grafik vektor.


```bash
pip install numpy matplotlib sympy
```