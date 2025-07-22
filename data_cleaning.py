import pandas as pd

# Φόρτωσε το CSV (προσαρμόζεις το όνομα του αρχείου)
df = pd.read_csv(r"C:\Users\PC\Downloads\deutsche_bank_financial_performance.csv")

# Δες ποιες στήλες υπάρχουν
print(df.columns.tolist())

# Υπολόγισε δείκτες (όνομα στηλών ανάλογα με το dataset)
df["NetProfitMargin"] = df["Net Income"] / df["Revenue"]
df["ROE"] = df["Net Income"] / df["Total Shareholder Equity"]

# Αποθήκευσε το τελικό αρχείο
df.to_csv("financial_with_ratios.csv", index=False)
print("Οι δείκτες υπολογίστηκαν και το αρχείο deutsche_bank_financial_performance.csv αποθηκεύτηκε!")