-- IS312: Database Systems II
-- Practical Relational Query Examples

CREATE TABLE IF NOT EXISTS is312_records (
    id INT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    status VARCHAR(20) DEFAULT 'ACTIVE',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO is312_records (id, title, status) VALUES 
(1, 'Sample Record A', 'ACTIVE'),
(2, 'Sample Record B', 'PENDING'),
(3, 'Sample Record C', 'ACTIVE');

SELECT id, title, status 
FROM is312_records 
WHERE status = 'ACTIVE';
