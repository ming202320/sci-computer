# Midterm Project: Simulated Stock Prices Using Python


## 1. Overview
In this mid-term project, I mainly use Python to generate, transform, analyze, and visualize the process of simulating stock price data. The goal is to simulate ggplot2 that we learn to use tidyverse and the analysis workflow we learned in R, and I want to translate some concepts into the Python data science ecosystem - mainly by using NumPy, pandas, and Matplotlib. In this project, I intend to simulate the prices of three stocks, x, y, and z, starting from January 1, 2009 and lasting for 10 days. The price of each stock fluctuates differently, which allows us to visualize how different levels of randomness affect short-term price movements, similar to the volatility of real financial markets.

Throughout the project, I want my code to implement:
*Use NumPy to generate reproducible random datasets
*Use Pandas to change wide format data to long format equivalent to the format in pivot_longer() 
*Aggregate data by category, plotting with matplotlib, Save table and graph outputs.


## 2. Data generation and setup
Start by importing the main library: 
```{python}
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
```
To make sure the results can be replicated, I use np.random.seed(1). This guarantees that the same random value is generated every time the code is run. This is a fundamental way in data science to ensure that results are verifiable and comparable.
Next, I create a DataFrame with three stocks and the corresponding time columns: x, y, z 
```{python}
stocks = pd.DataFrame({
    "time": pd.date_range("2009-01-01", periods=10),
    "x": np.random.normal(20, 1, 10),
    "y": np.random.normal(20, 4, 10),
    "z": np.random.normal(20, 4, 10)
})
```
Over here: mean of x is 20 and the standard deviation (σ) is 1. This means that its value fluctuates in a narrow range around the mean. y and z have a higher σ value of 4, generating broader and more realistic market volatility. This approach simulates short term changes in stock prices, providing us with a controlled environment to study changes and trends.


## 3.Data reshaping
We used to convert pivot_longer() wide-form data (multiple columns representing different stocks) to long-form data (one column representing the stock name and the other representing the price). In Python, the equivalent function is pd.melt(). 
```{python}
stocks_long = pd.melt(stocks, id_vars=["time"], var_name="stock", value_name="price")
```
 This generates a dataset where each row corresponds to a specific stock price on a specific day. Results are easier to group, summarize, and visualize. This flexible transition between long and wide formats illustrates how Pandas replicates Tidyverse data wrangling techniques in a concise, powerful syntax.


## 4. Visualization
Visualization is essential for understanding data patterns. I use Matplotlib to create a time series graph for each stock:
```{python}
plt.figure(figsize=(8, 5))
for stock, data in stocks_long.groupby("stock"):
    plt.plot(data["time"], data["price"], label=stock)
plt.title("Simulated Stock Prices Over Time")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.tight_layout()
plt.savefig("stocks_plot.png")
plt.show()
```
The final chart shows three different lines, each representing a stock's trajectory over time. While all stocks start at near the same level (about 20), stock X remains relatively stable, while stocks y and z fluctuate more widely, visually highlighting their higher standard deviations. This graph effectively translates statistical variations into visual narratives, showcasing how differences in volatility manifest as varying degrees of line smoothness or jagging.


## 5. Summary
Using pandas, the data was easily reshaped from wide to long format and summarized using the `groupby()` and `agg()` methods. Finally, the `.to_markdown()` function was used to print a clean Markdown table for documentation purposes.
Statistical Summary groupby() we can use Pandas' and agg() functions to calculate key statistics, such as the minimum and maximum prices for each stock:
```{python}
summary = (
    stocks_long.groupby("stock")
    .agg(min=("price", "min"), max=("price", "max"))
    .reset_index()
)
```

| stock   |     min |     max |
|:--------|--------:|--------:|
| x       | 17.6985 | 21.7448 |
| y       | 11.7594 | 25.8484 |
| z       | 15.5975 | 24.5789 |

These results show a clear difference in volatility. In line with my expectations, the price range of stock X remains narrow, while the price of Y and Z fluctuates greatly. This simulates that certain stocks or sectors in real-world financial data are inherently more volatile than others.


## 6. Application of actual data 
Simulation datasets can be extended to real-world applications. For example, using APIs to extract real financial data. Once the historical data is downloaded, the same analysis methods (changing charts, aggregations, and plots) can be applied to study the trend of stocks, compare them, and calculate averages.


## 7. Reflection and Comparison to R
In R, the workflow relied on:
-pivot_longer() / pivot_wider() from tidyr,
-group_by() and summarize() from dplyr,
-geom_line() and theme_classic() from ggplot2.

Python provides parallel functions:
-pd.melt() and pivot() for reshaping,
-groupby() and agg() for summarizing,
-matplotlib.pyplot for visualization.
Both languages embody the same data science principles: tidy data, vectorized operations, and reproducibility.


## 8. Conclusion
With this mid-term project, I was able to translate R-based concepts into Python workflows. Using simulated stock data, I explored data generation, manipulation, and visualization. The ability to switch between long and wide data formats, summarize grouped data, and generate clear visualizations enhances Python's analytical flexibility. Overall, whether simulating financial data or analyzing real datasets, the combination of NumPy, Pandas, and Matplotlib constitutes a powerful toolkit for solving data problems. I also learned how to convert R to Python.
