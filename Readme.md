# 📊 Municipal Bond Analytics Dashboard

Welcome to the **Municipal Bond Analytics Dashboard** — a data science project focused on analyzing municipal bond data using Python, Streamlit, and Plotly. This project is inspired by real-world finance use cases.

---

## 📌 Project Objective

To build an interactive dashboard that provides insights into **municipal bond portfolios**, focusing on:

- Yield and credit risk distribution
- Price vs duration relationship (risk assessment)
- Sector-wise bond issuance trends
- Simulated yield curves over time

This project demonstrates skills in **data visualization**, **Python development**, **financial analytics**, and **interactive dashboards** — aligning well with roles like **Data Scientist**, **Quant Analyst**, or **Python Developer** in finance.

---

## 📂 Dataset Overview: `muni_bonds_2000.csv`

This is a **synthetic but realistic dataset** of 2,000 municipal bonds. Each row represents a single bond. It includes:

| Column           | Description |
|------------------|-------------|
| `BondID`         | Unique identifier for each bond |
| `State`          | U.S. state where the bond was issued |
| `CreditRating`   | Credit quality: `AAA`, `AA`, `A`, `BBB` |
| `CouponRate`     | Annual interest rate paid on the bond |
| `Yield`          | Actual return to investors |
| `IssueDate`      | Date the bond was issued |
| `MaturityDate`   | Date the bond will mature |
| `Price`          | Current market price |
| `Duration`       | Duration in years (sensitivity to interest rate changes) |
| `Sector`         | Sector of issuance: Education, Utilities, Healthcare, etc. |

These attributes mimic real-world bond behavior and provide a strong basis for financial analysis.

---

## ⚙️ How to Run the Dashboard

### ✅ Requirements
Install required libraries:

```bash
pip install streamlit pandas plotly
```

### ▶️ Run the App

```bash
streamlit run app.py
```

Make sure the CSV is in the same folder or update the path in the script.

---

## 🧠 What the Dashboard Shows

### 1. 🔎 Filters
- Filter bonds by **State**, **Credit Rating**, or **Sector**

### 2. 📈 Key Metrics
- **Average Yield**
- **Average Price**
- **Total Bonds Displayed**

### 3. 📊 Visualizations

#### 🎯 Yield by Credit Rating
- Box plot showing yield ranges for each credit category
- Helps assess risk-reward tradeoffs across ratings

#### 📉 Price vs Duration
- Scatter plot showing bond price against duration
- Insight: Long-duration + low-price = higher interest rate sensitivity (risk)

#### 📆 Simulated Yield Curve
- Yield plotted against bond maturity year
- Shows how yields trend over time and by rating

#### 🏢 Sector Distribution
- Bar chart of how many bonds are issued in each sector

---

## 🌟 Why This Project?

This project showcases:
- Financial data analytics using Python
- Visual storytelling with Plotly and Streamlit
- Understanding of fixed income risk-return characteristics
- Real-world, resume-worthy finance tech stack

---

## 🧩 Future Enhancements

- 🔍 GenAI bot to summarize risky bonds (e.g., `BBB` rating)
- 📊 Power BI version for executive dashboards
- 🧠 ML model to predict bond yields based on features
- 🗄️ SQL-based exploration using DuckDB or pandasql
- 📤 Deployment on Streamlit Cloud or HuggingFace Spaces

---

## 🧱 Folder Structure

```
📁 muni-bond-dashboard/
│
├── app.py                  # Streamlit dashboard script
├── muni_bonds_2000.csv     # Main synthetic dataset
├── README.md               # Project overview and explanation
└── requirements.txt        # Dependencies
```

---

## 📦 Requirements

```text
streamlit
pandas
plotly
```

Create this with:

```bash
pip freeze > requirements.txt
```

---

## 👨‍💻 Author

**Vaibhav Sharma**  
💼 Aspiring Data & Applied Scientist  
📊 Portfolio: [GitHub/vaisharma16](https://github.com/vaisharma16)  

---

## 📎 License

This is a synthetic data project meant for educational and demonstrational purposes only.

