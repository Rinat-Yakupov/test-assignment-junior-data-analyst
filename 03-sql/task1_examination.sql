SELECT
    id,
	scores,
	RANK() OVER (ORDER BY scores DESC) AS ranking
FROM examination;