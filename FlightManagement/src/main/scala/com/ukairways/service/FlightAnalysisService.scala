package com.ukairways.service

import com.ukairways.model.{Flight, FlightAnalysis, Passenger}
import org.apache.spark.sql.{Dataset, SparkSession}
import org.apache.spark.sql.functions._
object FlightAnalysisService {

  def main(args: Array[String]): Unit = {
    // Create SparkSession
    val spark = SparkSession.builder()
      .appName("FlightAnalysis")
      .master("local[*]")
      .getOrCreate()

    import spark.implicits._

    // Read passengers.csv and flightData.csv
    val passengersDS: Dataset[Passenger] = spark.read
      .option("header", "true")
      .option("inferSchema", "true")
      .csv("src/resources/passengers.csv")
      .as[Passenger]

    val flightsDS: Dataset[Flight] = spark.read
      .option("header", "true")
      .option("inferSchema", "true")
      .csv("src/resources/flightData.csv")
      .as[Flight]


    // Perform flight analysis tasks using FlightAnalysis object methods
    //val flightsPerMonth = FlightAnalysis.findFlightsPerMonth(flightsDS)
    //val topFrequentFlyers = FlightAnalysis.findTopFrequentFlyers(passengersDS, flightsDS)
    //val maxCountriesWithoutUK = FlightAnalysis.findMaxCountriesWithoutUK(flightsDS)
    //val passengersOnMultipleFlights = FlightAnalysis.findPassengersOnMultipleFlightsTogether(flightsDS, passengersDS)
    val passengersOnMultipleFlightsInRange = FlightAnalysis.findPassengersOnMultipleFlightsInRange(flightsDS, "2017-01-09" , "2017-02-19", 6)
    passengersOnMultipleFlightsInRange.show(100000)
    passengersOnMultipleFlightsInRange.printSchema()
    // Show the results or write to files as required
    /*
    flightsPerMonth.show()

    flightsPerMonth.printSchema()

    topFrequentFlyers.show()
    topFrequentFlyers.printSchema()

    println(maxCountriesWithoutUK)

    */




    // Stop SparkSession
    spark.stop()
  }

}