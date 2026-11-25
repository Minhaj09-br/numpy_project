import numpy as np

choies=int(input("choies is your 1-100 every one has different tempratur data: "))
rrg=np.random.default_rng(choies)

tempratur=rrg.normal(
    loc=30,
    scale=5,
    size=30
)
# print(tempratur)

hig=np.max(tempratur)
print(f"highest tempratur day:{hig:.2f}C")
low=np.min(tempratur)
print(f"lowest tempratur day:{low:.2f}C")
avrage=np.mean(tempratur)
print(f"average tempratur day:{avrage:.2f}C")
count=np.count_nonzero(tempratur>30)
print(f"tempratur greaterthan>>>30C:{count}")
meadle=np.median(tempratur)
print(f"the meadle tempratur:{meadle}C")
