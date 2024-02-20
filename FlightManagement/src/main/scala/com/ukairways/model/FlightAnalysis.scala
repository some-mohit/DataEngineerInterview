package com.ukairways.model

import org.apache.spark.sql.{DataFrame, Dataset, SparkSession}
import org.apache.spark.sql.functions._

object FlightAnalysis {
  val spark = SparkSession.builder()
    .appName("FlightAnalysis")
    .master("local[*]")
    .getOrCreate()

  import spark.implicits._

  def findFlightsPerMonth(flightsDS: Dataset[Flight]): Dataset[(String,Long)] = {
    val flightDataWithDate = flightsDS.withColumn("date", to_date($"date"))
    val flightDataWithMonth = flightDataWithDate.withColumn("month", month($"date"))
    val flightsPerMonth = flightDataWithMonth.groupBy("month").count().sort("month")
    flightsPerMonth.as[(String,Long)]
  }

  def findTopFrequentFlyers(passengersDS: Dataset[Passenger], flightsDS: Dataset[Flight]): Dataset[(String,String,String,Long)] = {

    val joinedDS = passengersDS.joinWith(flightsDS, passengersDS("passengerId") === flightsDS("passengerId"))
    val passengerFlightCounts = joinedDS.groupByKey(_._1).count().map { case (passenger, count) => (passenger.passengerId, passenger.firstName, passenger.lastName, count) }
    val top100FrequentFlyers = passengerFlightCounts.sort($"_4".desc).limit(100).toDF("passengerId", "firstName", "lastName", "flightCount")
    top100FrequentFlyers.as[(String,String,String,Long)]
  }

  def findMaxCountriesWithoutUK(flightsDS: Dataset[Flight]): Dataset[(Int, Long)] = {

    val nonUKFlights = flightsDS.filter(
      (lower($"from") === "uk" && lower($"to") =!= "uk") ||
        (lower($"from") =!= "uk" && lower($"to") === "uk") ||
        (lower($"from") =!= "uk" && lower($"to") =!= "uk")
    )

    // Step 2: Group by passengerId and collect distinct countries visited (excluding UK)
    val distinctCountries = nonUKFlights
      .select($"passengerId", explode(array($"from", $"to")).alias("country"))
      .where(lower($"country") =!= "uk")
      .distinct()
    distinctCountries.show()
    // Step 3: Calculate count of distinct countries visited for each passenger
    val countriesCount = distinctCountries
      .groupBy("passengerId")
      .agg(count("*").alias("longestRun"))
    countriesCount.show()

    // Step 4: Find maximum count of distinct countries visited for each passenger
    val longestRunForEachPassenger = countriesCount
      .groupBy($"passengerId")
      .agg(max("longestRun").alias("longestRun"))
    longestRunForEachPassenger.as[(Int, Long)]
  }

  def findPassengersOnMultipleFlightsTogether(flightsDS: Dataset[Flight]): Dataset[(Int,Int,Long)] = {

    // Group flights by passengerId and flightId, and count the number of flights for each pair of passengers
    val passengerPairsFlightsCount = flightsDS.groupBy($"passengerId", $"flightId")
      .count()

    // Join the DataFrame with itself to find the pairs who have flown together
    val passengerPairs = passengerPairsFlightsCount.as("flights1")
      .join(passengerPairsFlightsCount.as("flights2"),
        $"flights1.flightId" === $"flights2.flightId" &&
          $"flights1.passengerId" < $"flights2.passengerId")
      .groupBy($"flights1.passengerId".alias("passengerId1"), $"flights2.passengerId".alias("passengerId2"))
      .agg(count("*").alias("flightsTogether"))

    // Filter for pairs who have flown together more than 3 times
    val passengersOnMultipleFlights = passengerPairs.filter($"flightsTogether" > 3)

    passengersOnMultipleFlights.as[(Int,Int,Long)]

  }


  def findPassengersOnMultipleFlightsInRange(flightsDS: Dataset[Flight], from_date: String, to_flight_date: String, travelCount: Int): Dataset[(Int, Int, String, String, Long)] = {

    // Filter flights within the specified date range
    val filteredFlightsDS = flightsDS.filter($"date".between(from_date, to_flight_date))


    val passengerPairsFlightsCount = filteredFlightsDS.groupBy($"passengerId", $"flightId")
      .count()

    // Group the flights by passengerId to find the pairs who have flown together
    val passengerPairs = passengerPairsFlightsCount.as("flights1")
      .join(passengerPairsFlightsCount.as("flights2"),
        $"flights1.flightId" === $"flights2.flightId" &&
          $"flights1.passengerId" < $"flights2.passengerId")
      .groupBy($"flights1.passengerId", $"flights2.passengerId")
      .agg(count("*").alias("flightsTogether"))


    // Rename passengerId columns to avoid ambiguity
    val result = passengerPairs.join(filteredFlightsDS.as("flights"), $"flights1.passengerId" === $"flights.passengerId")
      .select($"flights1.passengerId".as("passengerId1"),
        $"flights2.passengerId".as("passengerId2"),
        lit(from_date).as("from_date"),
        lit(to_flight_date).as("to_date"),
        $"flightsTogether")

    val passengerPairTravelCount = result.filter($"flightsTogether" > travelCount)
    passengerPairTravelCount.as[(Int, Int, String, String, Long)]
  }
}