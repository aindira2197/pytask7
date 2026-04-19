CREATE TABLE Clients (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    surname VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE Accounts (
    id INT PRIMARY KEY,
    client_id INT,
    account_number VARCHAR(255),
    account_type VARCHAR(255),
    balance DECIMAL(10, 2),
    FOREIGN KEY (client_id) REFERENCES Clients(id)
);

CREATE TABLE Transactions (
    id INT PRIMARY KEY,
    account_id INT,
    transaction_type VARCHAR(255),
    amount DECIMAL(10, 2),
    date DATE,
    FOREIGN KEY (account_id) REFERENCES Accounts(id)
);

CREATE TABLE Payments (
    id INT PRIMARY KEY,
    account_id INT,
    payment_type VARCHAR(255),
    amount DECIMAL(10, 2),
    date DATE,
    FOREIGN KEY (account_id) REFERENCES Accounts(id)
);

INSERT INTO Clients (id, name, surname, email) 
VALUES (1, 'John', 'Doe', 'john@example.com'),
       (2, 'Jane', 'Doe', 'jane@example.com'),
       (3, 'Bob', 'Smith', 'bob@example.com');

INSERT INTO Accounts (id, client_id, account_number, account_type, balance) 
VALUES (1, 1, '123456789', 'Checking', 1000.00),
       (2, 1, '987654321', 'Savings', 500.00),
       (3, 2, '111111111', 'Checking', 2000.00),
       (4, 3, '222222222', 'Savings', 3000.00);

INSERT INTO Transactions (id, account_id, transaction_type, amount, date) 
VALUES (1, 1, 'Deposit', 500.00, '2022-01-01'),
       (2, 1, 'Withdrawal', 200.00, '2022-01-05'),
       (3, 2, 'Deposit', 1000.00, '2022-01-10'),
       (4, 3, 'Withdrawal', 500.00, '2022-01-15');

INSERT INTO Payments (id, account_id, payment_type, amount, date) 
VALUES (1, 1, 'Rent', 1000.00, '2022-01-01'),
       (2, 2, 'Utilities', 200.00, '2022-01-05'),
       (3, 3, 'Groceries', 500.00, '2022-01-10'),
       (4, 4, 'Entertainment', 1000.00, '2022-01-15');

CREATE VIEW AccountBalance AS 
SELECT A.id, A.account_number, A.balance, T.amount AS transaction_amount
FROM Accounts A
JOIN Transactions T ON A.id = T.account_id;

CREATE PROCEDURE UpdateAccountBalance 
AS
BEGIN
    UPDATE Accounts
    SET balance = balance + (SELECT transaction_amount FROM AccountBalance WHERE Accounts.id = AccountBalance.id)
    FROM AccountBalance
    WHERE Accounts.id = AccountBalance.id;
END;

CREATE FUNCTION GetClientAccounts 
(@client_id INT)
RETURNS TABLE
AS
RETURN
SELECT A.id, A.account_number, A.account_type, A.balance
FROM Accounts A
WHERE A.client_id = @client_id;

CREATE TRIGGER UpdateTransactionAmount 
ON Transactions
AFTER INSERT
AS
BEGIN
    UPDATE T
    SET T.amount = T.amount * 1.1
    FROM Transactions T
    JOIN inserted I ON T.id = I.id;
END;