SELECT if(s0.id is not null, s0.id, s1.id) as id, s1.student
FROM seat s1
LEFT JOIN seat s0 ON s0.id = if(s0.id % 2 = 0, s1.id + 1, s1.id - 1)
ORDER BY id