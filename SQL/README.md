# SQL & Relational Database Analytics

This directory contains database schemas, complex analytical queries, recursive CTEs, window functions, and business intelligence reports developed for the **FinanceHub Banking & Financial Services Database** during the **Sabudh Foundation Data Analytics & AI Fellowship (2026)**.

---

## 📁 Directory Structure

```text
SQL/
├── Final Coursework/
│   ├── Financial Services Database.sql              # Relational schema DDL & comprehensive seed data
│   ├── Vishal Singh_FinanceHub_Assignment.sql       # 25 production-grade SQL solutions & analytical queries
│   └── SQL Coursework_ FINANCIAL SERVICES DATABASE.pdf # Assignment specification & problem statements
└── README.md                                        # SQL module documentation
```

---

## 🏛 Database Schema: FinanceHub

The **FinanceHub** relational database models an integrated retail and commercial banking platform encompassing core banking, lending, card services, wealth management, and fraud monitoring:

| Table Name | Primary Key | Description |
|---|---|---|
| `Customers` | `customer_id` | Demographic data, credit scores, annual income, and risk profiles (`Low`, `Medium`, `High`) |
| `Accounts` | `account_id` | Checking, savings, and deposit accounts linked to branches and customers |
| `Transactions` | `transaction_id` | Ledger entries with deposits, withdrawals, transfers, and post-transaction balances |
| `Loans` | `loan_id` | Personal, home, and auto loan contracts with interest rates, EMIs, and outstanding balances |
| `LoanPayments` | `payment_id` | Historical loan installment payments, payment dates, and payment status tracking |
| `CreditCards` | `card_id` | Card issuance details, credit limits, current balances, and available credit |
| `CardTransactions` | `card_transaction_id` | Point-of-sale and online card purchases, merchant categories, and reward points |
| `Investments` | `investment_id` | Stocks, bonds, mutual funds, purchase prices, and current valuations |
| `Employees` | `employee_id` | Organizational staff with self-referential manager assignments and departments |
| `Branches` | `branch_id` | Regional bank branch locations, branch codes, and customer allocations |
| `FraudAlerts` | `alert_id` | Security monitoring alerts, alert types, severity levels, and fraud confirmations |

---

## 💡 Key SQL Techniques & Query Catalog

The solution script [`Vishal Singh_FinanceHub_Assignment.sql`](Final%20Coursework/Vishal%20Singh_FinanceHub_Assignment.sql) addresses 25 business and data engineering questions:

### 1. Basic & Advanced Filtering & Aggregations
- **High-Value Credit Scoring (`Q1`)**: Filters customers with credit score $> 700$ and annual income $> \$80,000$.
- **Category Volume Filtering (`Q2`)**: Aggregates yearly transactions by category with `HAVING SUM(amount) > 5000`.
- **Top Travel Spenders (`Q10`)**: Multi-table join linking customers, credit cards, and card transactions filtered by merchant category.
- **Active Loan Monitoring (`Q3`)**: Correlated scalar subqueries retrieving the latest payment date and status per loan.

### 2. Common Table Expressions (CTEs) & Segmentation
- **Above-Average Balance Identification (`Q4`)**: Two-stage CTE computing account aggregates and isolating customers exceeding the global average.
- **Customer Investment Tiering (`Q5`)**: Evaluates portfolio valuations with `CASE` expressions into segments: `High Value` ($>\$100\text{k}$), `Medium Value`, `Low Value`, and `New Investor`.
- **Cross-Selling Identification (`Q19`)**: Evaluates customers possessing active loans and credit cards but zero investments using `EXISTS` and `NOT EXISTS`.

### 3. Window Functions & Time-Series Analytics
- **Credit Card Utilisation Ranking (`Q8`)**: Uses `RANK() OVER (PARTITION BY card_type ORDER BY utilisation DESC)` to evaluate credit exposure per product line.
- **Monthly Trend Breakdown (`Q9`)**: Monthly transaction volumes, total amounts, and moving averages.
- **Running Ledger Balance (`Q13`)**: Calculates dynamic running balances for account `5001` using `FIRST_VALUE()` combined with `SUM(amount_change) OVER (ORDER BY transaction_date, transaction_id)`.
- **Month-over-Month Growth (`Q17`)**: Computes monthly percentage growth in loan disbursements using `LAG() OVER (ORDER BY month)`.
- **Wealth Distribution Percentiles (`Q22`)**: Evaluates statistical percentiles of customer balances within risk tiers using `PERCENT_RANK() OVER (PARTITION BY risk_profile ORDER BY total_balance)`.

### 4. Advanced Relational Logic & Data Integrity
- **Polymorphic Product Consolidation (`Q12`)**: Aggregates accounts, loans, credit cards, and investments for a given customer via `UNION ALL`.
- **Organizational Hierarchy (`Q21`)**: Uses **Recursive Common Table Expressions** (`WITH RECURSIVE`) to traverse employee-to-manager reporting chains and calculate hierarchy depth (`employee_level`).
- **Data Integrity & Anomaly Auditing (`Q24`)**: Detects corrupt records including negative balances, loans where outstanding exceeds principal, negative available credit, and ledger balance discrepancies where actual balance does not match previous balance plus transaction delta.
- **Executive BI Dashboard (`Q25`)**: Combines customer risk distributions, monthly cash flow (deposits vs. withdrawals), card utilization rates, loan health (on-time percentages), and top transaction categories into a single unified report.

---

## 🚀 How to Run

### Option 1: MySQL CLI
```bash
# 1. Create and populate the database
mysql -u root -p < "SQL/Final Coursework/Financial Services Database.sql"

# 2. Run the assignment queries
mysql -u root -p FinanceHub < "SQL/Final Coursework/Vishal Singh_FinanceHub_Assignment.sql"
```

### Option 2: GUI Clients (DBeaver, MySQL Workbench, DataGrip)
1. Open and execute `Financial Services Database.sql` to initialize the database schema and sample records.
2. Open `Vishal Singh_FinanceHub_Assignment.sql` and run individual queries or execute the entire script.
