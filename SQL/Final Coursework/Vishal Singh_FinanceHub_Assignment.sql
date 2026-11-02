-- Q1: Customers with high credit score and income
SELECT CONCAT(first_name, ' ', last_name) AS customer_name,
       credit_score, annual_income, risk_profile
FROM Customers
WHERE credit_score > 700 AND annual_income > 80000
ORDER BY credit_score DESC;


-- Q2: Total transaction amount by category
SELECT category, SUM(amount) AS total_amount
FROM Transactions
WHERE YEAR(transaction_date) = 2024
GROUP BY category
HAVING SUM(amount) > 5000
ORDER BY total_amount DESC;


-- Q3: Active loans with customer details
SELECT CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
       l.loan_type, l.loan_amount, l.outstanding_balance, l.monthly_emi,
       (SELECT MAX(payment_date) FROM LoanPayments
        WHERE loan_id = l.loan_id) AS last_payment_date,
       (SELECT payment_status FROM LoanPayments
        WHERE loan_id = l.loan_id
        ORDER BY payment_date DESC LIMIT 1) AS payment_status
FROM Loans l
JOIN Customers c ON l.customer_id = c.customer_id
WHERE l.loan_status = 'Active'
ORDER BY l.outstanding_balance DESC;


-- Q4: Customers with above-average account balance
WITH CustomerBalances AS (
    SELECT c.customer_id, CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
           SUM(a.current_balance) AS total_balance, COUNT(a.account_id) AS total_accounts
    FROM Customers c
    JOIN Accounts a ON c.customer_id = a.customer_id
    GROUP BY c.customer_id, c.first_name, c.last_name
)
SELECT *
FROM CustomerBalances
WHERE total_balance > (SELECT AVG(total_balance) FROM CustomerBalances);


-- Q5: Customer investment segmentation
SELECT CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
       SUM(i.current_price) AS total_investment_value,
       CASE
           WHEN SUM(i.current_price) > 100000 THEN 'High Value'
           WHEN SUM(i.current_price) >= 50000 THEN 'Medium Value'
           WHEN SUM(i.current_price) >= 20000 THEN 'Low Value'
           ELSE 'New Investor'
       END AS segment
FROM Customers c
JOIN Investments i ON c.customer_id = i.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name;


-- Q6: Customers with accounts but no loans
SELECT c.customer_id, CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
       SUM(a.current_balance) AS total_balance, COUNT(a.account_id) AS total_accounts
FROM Customers c
JOIN Accounts a ON c.customer_id = a.customer_id
WHERE NOT EXISTS (SELECT 1 FROM Loans l WHERE l.customer_id = c.customer_id)
GROUP BY c.customer_id, c.first_name, c.last_name;


-- Q7: Employees and their managers
SELECT CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
       e.job_title, CONCAT(m.first_name, ' ', m.last_name) AS manager_name,
       e.department
FROM Employees e
LEFT JOIN Employees m ON e.manager_id = m.employee_id;


-- Q8: Credit card utilisation ranking
SELECT cc.card_type, CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
       cc.credit_limit, cc.current_balance,
       ROUND(cc.current_balance / cc.credit_limit * 100, 2) AS utilisation_percentage,
       RANK() OVER (PARTITION BY cc.card_type
                    ORDER BY cc.current_balance / cc.credit_limit DESC) AS card_rank
FROM CreditCards cc
JOIN Customers c ON cc.customer_id = c.customer_id;


-- Q9: Monthly transaction analysis
SELECT MONTHNAME(transaction_date) AS month, COUNT(*) AS total_transactions,
       SUM(amount) AS total_amount, AVG(amount) AS average_amount
FROM Transactions
WHERE YEAR(transaction_date) = 2024
GROUP BY MONTH(transaction_date), MONTHNAME(transaction_date)
ORDER BY MONTH(transaction_date);


-- Q10: Top 5 customers by travel spending
SELECT CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
       SUM(ct.amount) AS total_travel_spending,
       COUNT(*) AS total_transactions, SUM(ct.reward_points_earned) AS total_reward_points
FROM CardTransactions ct
JOIN CreditCards cc ON ct.card_id = cc.card_id
JOIN Customers c ON cc.customer_id = c.customer_id
WHERE ct.merchant_category = 'Travel'
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY total_travel_spending DESC
LIMIT 5;


-- Q11: Accounts receiving deposits above $5000 in the last 60 days
SELECT a.account_number, a.account_type,
       CONCAT(c.first_name, ' ', c.last_name) AS customer_name, a.current_balance
FROM Accounts a
JOIN Customers c ON a.customer_id = c.customer_id
WHERE EXISTS (
    SELECT 1 FROM Transactions t
    WHERE t.account_id = a.account_id
      AND t.transaction_type = 'Deposit'
      AND t.amount > 5000
      AND t.transaction_date >= CURRENT_DATE - INTERVAL 60 DAY
      AND t.transaction_date < CURRENT_DATE + INTERVAL 1 DAY
);


-- Q12: All financial products of customer 1004
SELECT 'Account' AS product_type, account_number AS product_identifier,
       current_balance AS current_value
FROM Accounts WHERE customer_id = 1004
UNION ALL
SELECT 'Loan', CAST(loan_id AS CHAR), outstanding_balance
FROM Loans WHERE customer_id = 1004
UNION ALL
SELECT 'Credit Card', card_number, current_balance
FROM CreditCards WHERE customer_id = 1004
UNION ALL
SELECT 'Investment', investment_type, current_price
FROM Investments WHERE customer_id = 1004;


-- Q13: Running balance for account 5001
WITH TransactionDetails AS (
    SELECT transaction_id, transaction_date, transaction_type, amount, balance_after,
           CASE
               WHEN transaction_type IN ('Deposit', 'Transfer In') THEN amount
               WHEN transaction_type IN ('Withdrawal', 'Transfer Out') THEN -amount
               ELSE 0
           END AS amount_change
    FROM Transactions
    WHERE account_id = 5001 AND YEAR(transaction_date) = 2024
)
SELECT transaction_date, transaction_type, amount,
       FIRST_VALUE(balance_after - amount_change) OVER (
           ORDER BY transaction_date, transaction_id
       ) + SUM(amount_change) OVER (
           ORDER BY transaction_date, transaction_id
       ) AS running_balance
FROM TransactionDetails
ORDER BY transaction_date;


-- Q14: Loan performance by loan type
SELECT l.loan_type, COUNT(DISTINCT l.loan_id) AS total_loans,
       SUM(l.loan_amount) AS total_disbursed,
       SUM(l.outstanding_balance) AS total_outstanding,
       AVG(l.interest_rate) AS average_interest_rate,
       ROUND(SUM(COALESCE(p.total_paid, 0)) * 100.0 /
             NULLIF(SUM(l.loan_amount), 0), 2) AS payment_completion_percentage
FROM Loans l
LEFT JOIN (
    SELECT loan_id, SUM(amount_paid) AS total_paid
    FROM LoanPayments
    WHERE payment_status = 'Paid'
    GROUP BY loan_id
) p ON l.loan_id = p.loan_id
GROUP BY l.loan_type;


-- Q15: Branch performance report
SELECT b.branch_name, COUNT(DISTINCT e.employee_id) AS total_employees,
       COUNT(DISTINCT a.customer_id) AS total_customers,
       ROUND(COUNT(DISTINCT a.customer_id) * 100.0 /
             (SELECT COUNT(*) FROM Customers), 2) AS customer_percentage
FROM Branches b
LEFT JOIN Employees e ON b.branch_id = e.branch_id
LEFT JOIN Accounts a ON b.branch_code = a.branch_code
GROUP BY b.branch_id, b.branch_name;


-- Q16: Customers with more than 5 transactions
SELECT CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
       COUNT(t.transaction_id) AS total_transactions,
       SUM(t.amount) AS total_amount, AVG(t.amount) AS average_amount
FROM Customers c
JOIN Accounts a ON c.customer_id = a.customer_id
JOIN Transactions t ON a.account_id = t.account_id
GROUP BY c.customer_id, c.first_name, c.last_name
HAVING COUNT(t.transaction_id) > 5 AND AVG(t.amount) > 500;


-- Q17: Month-over-month loan disbursement changes
WITH MonthlyLoans AS (
    SELECT DATE_FORMAT(disbursement_date, '%Y-%m') AS month,
           SUM(loan_amount) AS total_disbursed
    FROM Loans
    GROUP BY DATE_FORMAT(disbursement_date, '%Y-%m')
)
SELECT month, total_disbursed,
       LAG(total_disbursed) OVER (ORDER BY month) AS previous_month_amount,
       ROUND((total_disbursed - LAG(total_disbursed) OVER (ORDER BY month))
             * 100.0 / NULLIF(LAG(total_disbursed) OVER (ORDER BY month), 0), 2)
             AS percentage_change
FROM MonthlyLoans;


-- Q18: Fraud risk assessment
WITH FraudSummary AS (
    SELECT customer_id, COUNT(*) AS total_alerts,
           SUM(is_fraud_confirmed = TRUE) AS confirmed_fraud
    FROM FraudAlerts
    GROUP BY customer_id
),
CardSummary AS (
    SELECT customer_id,
           MAX(current_balance / NULLIF(credit_limit, 0) * 100) AS max_utilisation
    FROM CreditCards
    GROUP BY customer_id
)
SELECT CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
       COALESCE(f.total_alerts, 0) AS total_alerts,
       COALESCE(f.confirmed_fraud, 0) AS confirmed_fraud,
       ROUND(COALESCE(cc.max_utilisation, 0), 2) AS max_utilisation,
       'High' AS overall_risk_level
FROM Customers c
LEFT JOIN FraudSummary f ON c.customer_id = f.customer_id
LEFT JOIN CardSummary cc ON c.customer_id = cc.customer_id
WHERE COALESCE(f.total_alerts, 0) > 3
   OR COALESCE(f.confirmed_fraud, 0) > 0
   OR COALESCE(cc.max_utilisation, 0) > 80;
   
   
-- Q19: Customers with credit cards and active loans but no investments
SELECT c.customer_id, CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
       c.email, c.risk_profile
FROM Customers c
WHERE EXISTS (SELECT 1 FROM CreditCards cc WHERE cc.customer_id = c.customer_id)
  AND EXISTS (SELECT 1 FROM Loans l
              WHERE l.customer_id = c.customer_id AND l.loan_status = 'Active')
  AND NOT EXISTS (SELECT 1 FROM Investments i WHERE i.customer_id = c.customer_id);
  
  
-- Q20: Find transactions for account 5001 within a date range
SELECT transaction_id, account_id, transaction_type,
       transaction_date, amount, balance_after
FROM Transactions
WHERE account_id = 5001
  AND transaction_date >= '2024-01-01'
  AND transaction_date < '2024-04-01'
  AND amount > 1000
ORDER BY transaction_date;

-- Index suggestion (already created, so do not execute again)
-- CREATE INDEX idx_account_date_amount
-- ON Transactions(account_id, transaction_date, amount);


-- Q21: Employee management hierarchy
WITH RECURSIVE EmployeeHierarchy AS (
    SELECT employee_id, CONCAT(first_name, ' ', last_name) AS employee_name,
           manager_id, department, 1 AS employee_level
    FROM Employees
    WHERE manager_id IS NULL
    UNION ALL
    SELECT e.employee_id, CONCAT(e.first_name, ' ', e.last_name),
           e.manager_id, e.department, eh.employee_level + 1
    FROM Employees e
    JOIN EmployeeHierarchy eh ON e.manager_id = eh.employee_id
)
SELECT eh.employee_name, CONCAT(m.first_name, ' ', m.last_name) AS manager_name,
       eh.employee_level, eh.department
FROM EmployeeHierarchy eh
LEFT JOIN Employees m ON eh.manager_id = m.employee_id
ORDER BY eh.employee_level, eh.employee_name;


-- Q22: Percentile rank of customer account balance
WITH CustomerBalances AS (
    SELECT c.customer_id, CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
           c.risk_profile, COALESCE(SUM(a.current_balance), 0) AS total_balance
    FROM Customers c
    LEFT JOIN Accounts a ON c.customer_id = a.customer_id
    GROUP BY c.customer_id, c.first_name, c.last_name, c.risk_profile
)
SELECT customer_name, risk_profile, total_balance,
       ROUND(PERCENT_RANK() OVER (
           PARTITION BY risk_profile ORDER BY total_balance
       ), 2) AS percentile_rank
FROM CustomerBalances;


-- Q23: Total monthly EMI for a customer
SET @customer_id = 1001;
SELECT loan_type, monthly_emi,
       SUM(monthly_emi) OVER () AS total_monthly_emi
FROM Loans
WHERE customer_id = @customer_id AND loan_status = 'Active';
-- This query can be converted into a stored procedure using customer_id as an IN parameter.


-- Q24: Identify data integrity issues
SELECT 'Negative Account Balance' AS issue_type, account_id AS record_id,
       CONCAT('Balance: ', current_balance) AS details
FROM Accounts
WHERE current_balance < 0
UNION ALL
SELECT 'Invalid Loan Balance', loan_id,
       CONCAT('Outstanding: ', outstanding_balance, ', Original: ', loan_amount)
FROM Loans
WHERE outstanding_balance > loan_amount
UNION ALL
SELECT 'Negative Available Credit', card_id,
       CONCAT('Available Credit: ', available_credit)
FROM CreditCards
WHERE available_credit < 0
UNION ALL
SELECT 'Transaction Balance Mismatch', transaction_id,
       CONCAT('Actual: ', balance_after, ', Expected: ', expected_balance)
FROM (
    SELECT transaction_id, balance_after, transaction_type,
           LAG(balance_after) OVER (
               PARTITION BY account_id ORDER BY transaction_date, transaction_id
           ) +
           CASE
               WHEN transaction_type IN ('Deposit', 'Transfer In') THEN amount
               WHEN transaction_type IN ('Withdrawal', 'Transfer Out') THEN -amount
               ELSE 0
           END AS expected_balance
    FROM Transactions
) t
WHERE expected_balance IS NOT NULL
  AND transaction_type IN ('Deposit', 'Withdrawal', 'Transfer In', 'Transfer Out')
  AND ABS(balance_after - expected_balance) > 0.01;
  
  
-- Q25: Comprehensive financial dashboard
WITH RiskSummary AS (
    SELECT risk_profile, COUNT(*) AS total_customers
    FROM Customers
    GROUP BY risk_profile
),
MonthlyFlow AS (
    SELECT
        SUM(CASE WHEN transaction_type = 'Deposit' THEN amount ELSE 0 END) AS total_deposits,
        SUM(CASE WHEN transaction_type = 'Withdrawal' THEN amount ELSE 0 END) AS total_withdrawals
    FROM Transactions
    WHERE YEAR(transaction_date) = YEAR(CURRENT_DATE)
      AND MONTH(transaction_date) = MONTH(CURRENT_DATE)
),
CardUtilisation AS (
    SELECT card_type,
           ROUND(AVG(current_balance / NULLIF(credit_limit, 0) * 100), 2) AS average_utilisation
    FROM CreditCards
    GROUP BY card_type
),
LoanHealth AS (
    SELECT ROUND(AVG(payment_status = 'Paid') * 100, 2) AS on_time_percentage
    FROM LoanPayments
),
CategoryVolume AS (
    SELECT category, COUNT(*) AS total_transactions,
           ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC) AS category_rank
    FROM Transactions
    GROUP BY category
)
SELECT 'Customer Risk' AS section, risk_profile AS metric,
       CAST(total_customers AS CHAR) AS value
FROM RiskSummary
UNION ALL
SELECT 'Monthly Transactions', 'Total Deposits', CAST(total_deposits AS CHAR)
FROM MonthlyFlow
UNION ALL
SELECT 'Monthly Transactions', 'Total Withdrawals', CAST(total_withdrawals AS CHAR)
FROM MonthlyFlow
UNION ALL
SELECT 'Monthly Transactions', 'Net Flow',
       CAST(total_deposits - total_withdrawals AS CHAR)
FROM MonthlyFlow
UNION ALL
SELECT 'Card Utilisation', card_type, CAST(average_utilisation AS CHAR)
FROM CardUtilisation
UNION ALL
SELECT 'Loan Health', 'On-Time Payment Percentage', CAST(on_time_percentage AS CHAR)
FROM LoanHealth
UNION ALL
SELECT 'Top Transaction Categories', category, CAST(total_transactions AS CHAR)
FROM CategoryVolume
WHERE category_rank <= 3;