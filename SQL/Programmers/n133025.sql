-- Lv1 과일로 만든 아이스크림 고르기
-- https://school.programmers.co.kr/learn/courses/30/lessons/133025

SELECT O.FLAVOR
FROM FIRST_HALF AS O
INNER JOIN ICECREAM_INFO AS I
ON O.FLAVOR = I.FLAVOR
WHERE O.TOTAL_ORDER > 3000 AND INGREDIENT_TYPE LIKE 'fruit%'
ORDER BY O.TOTAL_ORDER DESC