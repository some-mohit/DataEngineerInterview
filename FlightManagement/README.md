# Flight Analysis Project

## Overview
The Flight Analysis project is a Scala application designed to analyze flight and passenger data to generate reports for varioud scenarios like the longest consecutive run of non-UK countries visited by each passenger. 
The project leverages Apache Spark for distributed data processing and Scala.


## Project Structure

The project consists of the following components:

## Case Classes:
#### The Flight Case class :
Defines the structure of flight data, including fields for passengerId, flightId, from, to, and date.
Sample Data: The sample flight data is provided in a CSV file named flights.csv, containing the following columns: passengerId, flightId, from, to, and date.

```
passengerId,flightId,from,to,date
48,10,uk,iq,2017-01-01
48,20,iq,uk,2017-01-02
49,10,cn,iq,2017-01-03
49,20,iq,uk,2017-01-02
49,20,uk,in,2017-01-03
49,20,in,uk,2017-01-04
50,20,uk,uk,2017-01-05

```
#### The Passenger Case class :
The Passenger case class represents passenger data, including fields for passengerId, firstName, and lastName.
Sample Data: The sample passenger data is provided in a CSV file named passenger.csv, containing the following columns: passengerId, firstName, and lastName.
```
passengerId,firstName,lastName
14751,Napoleon,Gaylene
2359,Katherin,Shanell
5872,Stevie,Steven
3346,Margarita,Gerri
3704,Earle,Candis
```


## Scala Classes:
### The Main Scala class

`FlightAnalysisService.scala` This class provides services related to flight analysis, such as reading flight data, performing analysis, and generating reports.

### The Model Scala class:
`FlightAnalysis.scala` This class contains the main logic for analyzing flight data to identify the below :
##### 1. Finding flights per month.
##### 2. Finding top frequent flyers.
##### 3. Longest consecutive run of non-UK countries visited by each passenger. It utilizes Apache Spark for data processing.
##### 4. Find passengers on multiple flights together.

## Usage

1. To run the Flight Analysis project, follow these steps:

Ensure that you have Apache Spark installed and configured on your system.
Clone the project repository to your local machine on IDE(Intellij).
Place the flights.csv and passengers.csv file containing the flight & passenger data in the project directory at `src/resources/`.

2. Using SBT (Scala Build Tool)
   A. Ensure that you have SBT (Scala Build Tool) installed on your system.
   B. Navigate to the project directory.
   C. Use the following command to compile and run the project:

    ```bash
    sbt package
    sbt run
    ````
This will also install the required libraries on to your local system.

Run the FlightAnalysisService from IDE to generate csv files reports.

## Report Generation
All the flight and passenger data reports are stored/kept in output folder ```src/output```

## Dependencies
The project has the following dependencies:
Apache Spark (2.4.8): A fast and general-purpose cluster computing system.
SBT (Scala Build Tool): A build tool for Scala projects.
Scala Version : 2.12.10
