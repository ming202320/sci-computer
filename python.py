import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(1) #to do it randomly

stocks = pd.DataFrame({
    "time": pd.date_range(start="2009-01-01", periods=10, freq="D"),
    "x": np.random.normal(20, 1, 10),
    "y": np.random.normal(20, 4, 10),
    "z": np.random.normal(20, 4, 10)
})

x = np.array([20, 1 ,10])
y = np.array([20, 4, 10])
z = np.array([20, 4, 10])

stocksL = stocks.melt(id_vars="time", var_name="stock", value_name="price")

plt.figure(figsize=(8, 5))
for stock, group in stocksL.groupby("stock"):
    plt.plot(group["time"], group["price"], label=stock)
plt.legend(title="Stock")
plt.xlabel("Time")
plt.ylabel("Price")
plt.title("Stock Prices Over Time")
plt.tight_layout()
plt.savefig("stocks_plot.png")
plt.close()
import os
os.system("start stocks_plot.png")

summary = stocksL.groupby("stock")["price"].agg(["min", "max"]).reset_index()

print(summary.to_markdown())

stocksW = stocksL.pivot(index="time", columns="stock", values="price").reset_index()





