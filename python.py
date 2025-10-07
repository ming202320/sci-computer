import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(1)


stocks = pd.DataFrame({
    "time": pd.date_range(start="2009-01-01", periods=10, freq="D"),
    "x": np.random.normal(20, 1, 10),
    "y": np.random.normal(20, 4, 10),
    "z": np.random.normal(20, 4, 10)
})


stocksL = stocks.melt(id_vars="time", var_name="stock", value_name="price")


plt.figure(figsize=(8, 5))
for stock, group in stocksL.groupby("stock"):
    plt.plot(group["time"], group["price"], label=stock)
plt.legend(title="Stock")
plt.xlabel("Time")
plt.ylabel("Price")
plt.title("Stock Prices Over Time")
plt.tight_layout()
plt.savefig("stocks_plot.png", dpi=300)
plt.close()


summary = stocksL.groupby("stock")["price"].agg(["min", "max"]).reset_index()


print(summary.to_markdown(index=False))


stocksW = stocksL.pivot(index="time", columns="stock", values="price").reset_index()


stocks.to_csv("stocks_original.csv", index=False)
stocksL.to_csv("stocks_long.csv", index=False)
stocksW.to_csv("stocks_wide.csv", index=False)
