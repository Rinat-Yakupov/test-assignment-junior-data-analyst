SELECT
    a.client_id,
	COALESCE(SUM(t.amount),0) AS total_spent
FROM account a
LEFT JOIN transaction t ON a.id = t.account_id
AND DATE_TRUNC('month',t.transaction_date) = DATE_TRUNC('month', current_date - INTERVAL '1 month' )
GROUP BY a.client_id
HAVING COALESCE(SUM(t.amount),0) < 5000;