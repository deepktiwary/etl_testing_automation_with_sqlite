import sqlite3

con = sqlite3.connect('etl_testing_automation.db')
cur = con.cursor()

cur.execute('''
drop table if exists sales
''')


cur.execute('''
create table if not exists sales(
sales_id INT PRIMARY KEY,
purchase_date DATE,
customer_id INT,
product_id INT,
purchase_quantity INT,
per_unit_price DECIMAL
)
''')

cur.executescript('''
insert into sales values (30097, '2023-12-04', 700123, '1001', 3, 300);
insert into sales values (30098, '2023-12-05', 700123, '1002', 2, 100);
insert into sales values (30099, '2023-12-06', 700123, '1003', 1, 150);


insert into sales values (40000, '2023-12-06', 700124, '1005', 3, 400);
insert into sales values (40001, '2023-12-07', 700124, '1002', 2, 100);
insert into sales values (40002, '2023-12-08', 700124, '1002', 1, 100);



insert into sales values (40003, '2024-02-04', 700125, '1001', 3, 300);
insert into sales values (40004, '2023-12-09', 700126, '1002', 2, 100);
insert into sales values (40005, '2023-12-10', 700127, '1003', 1, 150);


insert into sales values (40006, '2023-12-11', 700128, '1005', 3, 400);
insert into sales values (40007, '2023-12-12', 700129, '1006', 4, 250);
insert into sales values (40008, '2023-12-13', 700130, '1007', 1, 150);



insert into sales values (40009, '2024-02-04', 700131, '1001', 4, 300);
insert into sales values (40010, '2024-03-05', 700132, '1002', 2, 100);
insert into sales values (40011, '2024-10-06', 700133, '1003', 2, 150);


insert into sales values (40012, '2023-12-06', 700134, '1005', 3, 400);
insert into sales values (40013, '2023-12-07', 700135, '1002', 2, 100);
insert into sales values (40014, '2023-12-08', 700136, '1002', 1, 100);



insert into sales values (40015, '2024-03-04', 700125, '1001', 3, 300);
insert into sales values (40016, '2024-03-09', 700126, '1002', 2, 100);
insert into sales values (40017, '2024-03-10', 700127, '1003', 1, 150);


insert into sales values (40018, '2024-04-11', 700137, '1005', 3, 400);
insert into sales values (40019, '2024-05-12', 700138, '1006', 4, 250);
insert into sales values (40020, '2024-04-13', 700139, '1007', 1, 150);
insert into sales values (40021, '2024-04-13', 700139, '1004', 1, 75);



''')
result = cur.execute("select * from sales")

for items in result:
    print(items)

cur.execute('''
drop table if exists customer
''')

cur.execute('''
create table if not exists customer
(customer_id int PRIMARY KEY,
 customer_name varchar(50),
 cust_email varchar(100),
 cust_address varchar(100)
 );
''')


cur.executescript('''
 insert into customer values (700123, 'Deepak Tiwary', 'deepak.tiwary@yahoo.com', 'Pune');
 insert into customer values (700124, 'Vikash Sharma', 'vikash.sharma@gmail.com', 'Pune');

 
 insert into customer values (700125, 'Anand P', 'anand.p@yahoo.com', 'Pune') ;
 insert into customer values (700126, 'Bikas A', 'bikas.ahtyo@gmail.com', 'Pune');


 
 insert into customer values (700127, 'Deepak Kumar', 'deepak.k@yahoo.com', 'Pune') ;
 insert into customer values (700128, 'Deepak Yadav', 'deepak.y@gmail.com', 'Pune');

 
 insert into customer values (700129, 'Sandip Dighe', 'sandip.d@yahoo.com', 'Mumbai') ;
 insert into customer values (700130, 'Govind Wagh', 'govind.w@gmail.com', 'Mumbai');

 insert into customer values (700131, 'Sourav Nayak', 's.n@yahoo.com', 'Pune') ;
 insert into customer values (700132, 'Mani K', 'mani_k@gmail.com', 'Pune');

 
 insert into customer values (700133, 'Anand K', 'anand_k@rediff.com', 'Pune') ;
 insert into customer values (700134, 'Kanhaiya Jee', 'k.jee@gmail.com', 'Pune');


 
 insert into customer values (700135, 'Jay K', 'jay.k@yahoo.com', 'Bangalore') ;
 insert into customer values (700136, 'Bhushan Patil', 'bhushan.patil@gmail.com', 'Nagpur');

 
 insert into customer values (700137, 'Mohit Joshi', 'mj@yahoo.com', 'Patna') ;
 insert into customer values (700138, 'Satyam C', 'satyam.c@gmail.com', 'Kolkata');

 insert into customer values (700139, 'Satyam K', 'satyam.k@rediff.com', 'Ranchi');
''')

result1 = cur.execute("select * from customer")

for items in result1:
    print(items)

cur.execute('''
drop table if exists products
''')

cur.execute('''
create table if not exists products
 (product_id INT PRIMARY KEY,
 product_name VARCHAR(100),
 category VARCHAR(100));
''')

cur.executescript('''
 insert into products values (1001, 'Pen Drive', 'Electronics');
 insert into products values (1002, 'c type wire', 'Electronics');

 insert into products values (1003, 'Ball', 'Sports');
 insert into products values (1004, 'Pad', 'Sports');

 
 insert into products values (1005, 'Pen', 'Stationery');
 insert into products values (1006, 'Notebook', 'Stationery');
 insert into products values (1007, 'Hanging Leather Ball', 'Sports');
''')


result2 = cur.execute("select * from products")

for items in result2:
    print(items)

cur.execute('''
 drop table if exists date_dim
 ''')

cur.execute('''
 create table if not exists date_dim(
 date_id INT PRIMARY KEY,
 date_ DATE,
 month_ VARCHAR(3),
 quarter_ INT,
 year_ INT
 );
''')

cur.executescript('''
insert into date_dim values (2023124, '2023-12-04', 'DEC', 4, 2023);
 insert into date_dim values (2023125, '2023-12-05', 'DEC', 4, 2023);
 insert into date_dim values (2023126, '2023-12-06', 'DEC', 4, 2023);

 insert into date_dim values (2023127, '2023-12-07', 'DEC', 4, 2023);
 insert into date_dim values (2023128, '2023-12-08', 'DEC', 4, 2023);
 insert into date_dim values (2023129, '2023-12-09', 'DEC', 4, 2023);

 insert into date_dim values (20231210, '2023-12-10', 'DEC', 4, 2023);
 insert into date_dim values (20231211, '2023-12-11', 'DEC', 4, 2023);
 insert into date_dim values (20231212, '2023-12-12', 'DEC', 4, 2023);

 insert into date_dim values (20231213, '2023-12-13', 'DEC', 4, 2023);

 insert into date_dim values (202424, '2024-02-04', 'FEB', 1, 2024);
 insert into date_dim values (202434, '2024-03-04', 'MAR', 1, 2024);
 insert into date_dim values (202435, '2024-03-05', 'MAR', 1, 2024);

 insert into date_dim values (202439, '2024-03-09', 'MAR', 1, 2024);
 insert into date_dim values (2024310, '2024-03-10', 'MAR', 1, 2024);
 
 insert into date_dim values (2024411, '2024-04-11', 'APR', 2, 2024);
 insert into date_dim values (2024413, '2024-04-13', 'APR', 2, 2024);

 
 insert into date_dim values (2024512, '2024-05-12', 'MAY', 2, 2024);
 insert into date_dim values (2024106, '2024-10-06', 'OCT', 4, 2024);

''')

result3 = cur.execute("select * from date_dim")

for items in result3:
    print(items)

cur.execute('''
 drop table if exists sales_fact
 ''')

cur.execute('''
 create table if not exists sales_fact(
 sales_id INT PRIMARY KEY REFERENCES sales(sales_id),
 date_id INT REFERENCES date_dim(date_id),
 customer_id INT REFERENCES customer(customer_id),
 product_id INT REFERENCES products(product_id),
 quantity INT,
 unit_price INT,
 total_revenue INT
 
 );
''')

cur.executescript('''
insert into sales_fact values(30097,2023124,700123,1001,3,300,900);
insert into sales_fact values(30098,2023125,700123,1002,2,100,200);
insert into sales_fact values(30099,2023126,700123,1003,1,150,150);
insert into sales_fact values(40000,2023126,700124,1005,3,400,1200);
insert into sales_fact values(40001,2023127,700124,1002,2,100,200);
insert into sales_fact values(40002,2023128,700124,1002,1,100,100);
insert into sales_fact values(40003,202424,700125,1001,3,300,900);
insert into sales_fact values(40004,2023129,700126,1002,2,100,200);
insert into sales_fact values(40005,20231210,700127,1003,1,150,150);
insert into sales_fact values(40006,20231211,700128,1005,3,400,1200);
insert into sales_fact values(40007,20231212,700129,1006,4,250,1000);
insert into sales_fact values(40008,20231213,700130,1007,1,150,150);
insert into sales_fact values(40009,202424,700131,1001,4,300,1200);
insert into sales_fact values(40010,202435,700132,1002,2,100,200);
insert into sales_fact values(40011,2024106,700133,1003,2,150,300);
insert into sales_fact values(40012,2023126,700134,1005,3,400,1200);
insert into sales_fact values(40013,2023127,700135,1002,2,100,200);
insert into sales_fact values(40014,2023128,700136,1002,1,100,100);
insert into sales_fact values(40015,202434,700125,1001,3,300,900);
insert into sales_fact values(40016,202439,700126,1002,2,100,200);
insert into sales_fact values(40017,2024310,700127,1003,1,150,150);
insert into sales_fact values(40018,2024411,700137,1005,3,400,1200);
insert into sales_fact values(40019,2024512,700138,1006,4,250,1000);
insert into sales_fact values(40020,2024413,700139,1007,1,150,150);
insert into sales_fact values(40021,2024413,700139,1004,1,75,75);
''')

result4 = cur.execute("select * from sales_fact")

for items in result4:
    print(items)

cur.execute('''
 drop table if exists sales_agg
 ''')


cur.execute('''
 create table if not exists sales_agg(
 customer_id INT PRIMARY KEY REFERENCES customer(customer_id),
 total_quantity INT,
 total_revenue INT
 );''')

cur.execute('''
 insert into sales_agg
 select customer_id, coalesce(sum(quantity), 0), coalesce(sum(total_revenue), 0) from sales_fact
 group by customer_id;
''')

result5 = cur.execute("select * from sales_agg")

for items in result5:
    print(items)

def run_sql_query_for_validation(sql_query_to_be_run):
    cur.execute(sql_query_to_be_run)
    print("===================================")
    print(f"Running Requested Query: {sql_query_to_be_run}")
    print("-----------------------------------")
    print("End of the Query")
    data = cur.fetchall()
    return data
