import java.io.File
import kotlin.math.*

fun readFileAsLinesUsingBufferedReader(fileName: String): List<String>
  = File(fileName).bufferedReader().readLines()

fun getFuelForModule(mass: Double): Double {
    var fuel = floor(mass / 3) - 2
    var totalFuel = fuel

    while (fuel > 0) {
        fuel = floor(fuel / 3) - 2
        if (fuel > 0) {
            totalFuel += fuel
        }
    }

    return totalFuel
}

fun main(args: Array<String>) {
    val inputList = readFileAsLinesUsingBufferedReader("input_1_1.txt")
    println(inputList)

    val fuelList = inputList.map{ getFuelForModule(it.toDouble()) }
    println(fuelList)

    println(fuelList.sum())

    // println(getFuelForModule(100756.0))
}
