DROP TABLE IF EXISTS cbr;

use cbr;

CREATE TABLE ValCurs (
`Date` varchar(255),
`Valute ID` varchar(255),
`NumCode` int(50),
`CharCode` varchar(255),
`Nominal` varchar(255),
`Name` varchar(255),
`Value` varchar(255)
) ENGINE = InnoDB;

LOAD XML LOCAL INFILE 'file.xml'
INTO TABLE ValCurs (Date,Valute ID,NumCode,CharCode,Nominal,Name,Value);

