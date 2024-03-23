use t4vytcuaxuiqxjhk
create table bitcoin_conversion(
id int(3) auto_increment primary key,
currency varchar(10),
price_per_bitcoin int(100)
)
insert into bitcoin_conversion (currency,price_per_bitcoin) values('USD',57035.57)
insert into bitcoin_conversion (currency,price_per_bitcoin) values('INR',4723005.62)
insert into bitcoin_conversion (currency,price_per_bitcoin) values('EURO',52522.92)
insert into bitcoin_conversion(currency,price_per_bitcoin) values('NRP',100036)

create table Faq(
id int(3) auto_increment primary key,
question varchar(1000),
answer varchar(1000)
)
insert into Faq (question,answer) values('How does your model analyze historical Bitcoin data to provide predictions?','Our model utilizes advanced techniques to analyze historical Bitcoin data and identify patterns that may influence future price movements.');
insert into Faq(question,answer) values('What factors does your app consider when making predictions about Bitcoin prices?','Our model considers various factors such as historical price data, trading volume, and other relevant indicators to generate predictions.');
insert into Faq(question,answer) values('Can users customize the prediction timeframe or interval in your website?','Currently, our ML model can predict the price for only the next 10-15 days. We are continuously working to enhance our models capabilities and may offer more customization options in the future.');
insert into Faq(question,answer) values(' Are the predictions provided by your model reliable?','While we strive to provide accurate predictions, its important to note that cryptocurrency markets can be volatile. Our model offers informed estimates based on historical data and market analysis to assist users in making informed decisions.');

create table Query(
id int(3) auto_increment primary key,
name varchar(50),
email varchar(50),
message text
)


select * from Query
