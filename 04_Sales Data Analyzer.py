# 
import numpy as np

# Rows = Products
# Columns = Week 1, 2, 3, 4

sales = np.array([
    [1200, 1500, 1800, 2000], #Product 1
    [900, 1100, 1300, 1600],  #Product 2
    [2000, 2200, 2500, 2800], #Product 3
    [800, 950, 1200, 1400],   #Product 4
    [1500, 1700, 1900, 2100]  #Product 5
])
total_sale=np.sum((sales),axis=0)
print(f"Total sale of each weak:{total_sale}")
every=np.sum((sales),axis=1)
print(f"Total sales of each product:{every} ")
highest_sale=np.max(every)
print(f"product with the highest total sales:{highest_sale}")
highest_week=np.max(total_sale)
print(f"week with the highest sales:{highest_week}")
weak_sale=np.mean(total_sale)
print(f"average weekly sales:{weak_sale}")
great_2000=sales[sales>=2000]
print(f"sales greater then 2000:{great_2000}")
sale_count=np.count_nonzero(sales<1200)
print(f"sales count below fo 1200 is:{sale_count}")
right_now=(sales*(10/100))
increased=right_now+sales
print(f"every sale 10% increased:{increased}")
product=np.sort(every)
print(f"product price low to hight:{product}")
w_low=np.argmin(total_sale)
print(f"lowest week sale:{w_low+1}week:{every[w_low]}")
h_sal=np.argmax(every)
print(f"highest total sale if product number:{h_sal+1}:{every[h_sal]}")
