## -------------MENGCOPY NESTED LIST---------
# Mengcopy list di dalam list agar beda adress

data_0 = [1,2]
data_1 = [3,4]

data_2D = [data_0,data_1]
data_2D_copy = data_2D.copy()
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")

# mengambil

data = data_2D [0][1]
print(f"data= {data}")

# Makanya pakai deepcopy biar ga ikut berubah semua listnya

# firtstep harus import dulu

from copy import deepcopy

data_2D = [data_0,data_1]
data_2D_deepcopy = deepcopy(data_2D)

data_2D [0][1] = 19

print(f"data copy= {data_2D}")
print(f"data deepcopy = {data_2D_deepcopy}")
