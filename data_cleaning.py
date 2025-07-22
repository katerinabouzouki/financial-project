import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\PC\Desktop\supermarket_sales.csv", sep=";")

df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')

print(df.head())

print(df.dtypes) 

total_sales = df['Sales'].sum()
print("Total Sales: ", total_sales)

sales_by_city = df.groupby('City')['Sales'].sum().sort_values(ascending=False)
print("Sales by city: ")
print(sales_by_city.head(10))

top_products = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False)
top10_cities = sales_by_city.head(10)
print("Top products: ")
print(top10_cities)

plt.figure(figsize=(10,6))
sns.barplot(x=top_products.index, y=top_products.values, palette="viridis")
plt.xticks(rotation=45)
plt.title("Total Sales by Sub-Category")
plt.ylabel("Sales")
plt.xlabel("Sub-Category")
plt.tight_layout()
plt.show()



