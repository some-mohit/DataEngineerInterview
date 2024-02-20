package com.ukairways.service

import com.ukairways.model.{Flight, FlightAnalysis, Passenger}
import org.apache.spark.sql.functions.{collect_list, count,  struct}
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
    val flightsPerMonth = FlightAnalysis.findFlightsPerMonth(flightsDS)
    flightsPerMonth.repartition(1).write.mode("overwrite").option("header", "true").csv("src/output/flights-per-month/")

    val topFrequentFlyers = FlightAnalysis.findTopFrequentFlyers(passengersDS, flightsDS)
    topFrequentFlyers.repartition(1).write.mode("overwrite").option("header", "true").csv("src/output/top-frequent-flyer/")

    val maxCountriesWithoutUK = FlightAnalysis.findMaxCountriesWithoutUK(flightsDS)
    maxCountriesWithoutUK.repartition(1).write.mode("overwrite").option("header", "true").csv("src/output/passenger-longest-run/")


    val passengersOnMultipleFlights = FlightAnalysis.findPassengersOnMultipleFlightsTogether(flightsDS, passengersDS)
    passengersOnMultipleFlights.repartition(1).write.mode("overwrite").option("header", "true").csv("src/output/passenger-with-multiple-flights/")
    passengersOnMultipleFlights.show(10)
    passengersOnMultipleFlights.printSchema()
    spark.stop()

  }

}