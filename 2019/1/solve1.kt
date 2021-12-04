import java.io.File
import kotlin.math.*

fun readFileAsLinesUsingBufferedReader(fileName: String): List<String>
  = File(fileName).bufferedReader().readLines()

fun main(args: Array<String>) {
    val inputList = readFileAsLinesUsingBufferedReader("input_1_1.txt")
    println(inputList)

    println(inputList.map{ floor(it.toDouble() / 3) - 2}.sum())
}
