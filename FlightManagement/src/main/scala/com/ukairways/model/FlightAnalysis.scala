package com.ukairways.model

import org.apache.spark.sql.{DataFrame, Dataset, SparkSession}
import org.apache.spark.sql.functions._

object FlightAnalysis {
  val spark = SparkSession.builder()
    .appName("FlightAnalysis")
    .master("local[*]")
    .getOrCreate()

  import spark.implicits._

  def findFlightsPerMonth(flightsDS: Dataset[Flight]): DataFrame = {
    val flightDataWithDate = flightsDS.withColumn("date", to_date($"date"))
    val flightDataWithMonth = flightDataWithDate.withColumn("month", month($"date"))
    val flightsPerMonth = flightDataWithMonth.groupBy("month").count().sort("month")
    flightsPerMonth
  }

  def findTopFrequentFlyers(passengersDS: Dataset[Passenger], flightsDS: Dataset[Flight]): DataFrame = {

    val joinedDS = passengersDS.joinWith(flightsDS, passengersDS("passengerId") === flightsDS("passengerId"))
    val passengerFlightCounts = joinedDS.groupByKey(_._1).count().map { case (passenger, count) => (passenger.passengerId, passenger.firstName, passenger.lastName, count) }
    val top100FrequentFlyers = passengerFlightCounts.sort($"_4".desc).limit(100).toDF("passengerId", "firstName", "lastName", "flightCount")
    top100FrequentFlyers
  }

  def findMaxCountriesWithoutUK(flightsDS: Dataset[Flight]): Dataset[(Int,Long)] = {
    // Filter out flights where both from and to are the UK
    val nonUKFlights = flightsDS.filter($"from" =!= "uk" && $"to" =!= "uk")
    nonUKFlights.show(100000)
    // Group flights by passengerId and collect the distinct countries visited
    val dataWithCountries = nonUKFlights.groupBy("passengerId")
      .agg(
        concat_ws(",", collect_list(col("from"))).alias("countries")
      )

    // Calculate the longest run of consecutive unique countries visited for each passenger
    val passengerLongestRuns = dataWithCountries.withColumn(
      "longest_run",
      size(split(regexp_replace(col("countries"), ",{2,}", ","), ","))
    )

    // Select the passengerId and longest_run columns
    val result = passengerLongestRuns.select($"passengerId", $"longest_run".as[Long])

    result.as[(Int, Long)]

  }

  def findPassengersOnMultipleFlightsTogether(flightsDS: Dataset[Flight], passengersDS: Dataset[Passenger]): DataFrame = {
    // Group flights by passengerId and flightId, and count the number of flights for each pair of passengers
    val passengerPairsFlightsCount = flightsDS.groupBy($"passengerId", $"flightId")
      .count()

    // Group the flights by passengerId to find the pairs who have flown together
    val passengerPairs = passengerPairsFlightsCount.as("flights1")
      .join(passengerPairsFlightsCount.as("flights2"),
        $"flights1.flightId" === $"flights2.flightId" &&
          $"flights1.passengerId" < $"flights2.passengerId")
      .groupBy($"flights1.passengerId", $"flights2.passengerId")
      .agg(count("*").alias("flightsTogether"))

    // Filter for pairs who have flown together more than 3 times
    val passengersOnMultipleFlights = passengerPairs.filter($"flightsTogether" > 3)

    passengersOnMultipleFlights

  }


  def findPassengersOnMultipleFlightsInRange(flightsDS: Dataset[Flight], from_date: String, to_flight_date: String, travelCount: Int): Dataset[(Int, Int, String, String, Long)] = {

    val spark = flightsDS.sparkSession
    import spark.implicits._

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

    val passengerPairTravelCount = result.filter($"flightsTogether"  > travelCount)
    passengerPairTravelCount.as[(Int, Int, String, String, Long)]
  }
}