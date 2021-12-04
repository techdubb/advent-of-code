import java.io.File
import kotlin.math.*

fun readFileAsLinesUsingBufferedReader(fileName: String): List<String>
  = File(fileName).bufferedReader().readLines()

fun findLeastZeroLayer(layers: MutableMap<Int, List<Int>>): Int {
    var minZeros = Int.MAX_VALUE
    var minLayer = 0
    var zeroCount = 0

    for (l in layers) {
        zeroCount = l.value.count { it == 0 }
        if (zeroCount < minZeros) {
            minZeros = zeroCount
            minLayer = l.key
        }
    }

    return minLayer
}

fun getProductOfOneTwoCoutnts(layer: List<Int>): Int {
    val oneCount = layer.count { it == 1 }
    val twoCount = layer.count { it == 2 }

    return oneCount * twoCount
}

fun main(args: Array<String>) {
    // val inputList = readFileAsLinesUsingBufferedReader("input_test_1.txt")
    val inputList = readFileAsLinesUsingBufferedReader("input_2_1.txt")
    val input = inputList.get(0)
    // println(inputList)

    val w = 25
    val h = 6

    val inputSize = input.length
    // println(inputSize)
    var index = 0
    var layer = 1
    val layers: MutableMap<Int, List<Int>> = mutableMapOf()
    var pixelList: MutableList<Int> = ArrayList()

    while (index < inputSize) {
        for (i in 0..(h-1)) {
            for (j in 0..(w-1)) {
                pixelList.add(input.get(index).toString().toInt())
                index += 1
            }
            // println("===")
        }

        layers.put(layer, pixelList)
        layer += 1
        pixelList = ArrayList()
    }

    // println(layers)

    val leastZeroLayer = findLeastZeroLayer(layers)

    println(getProductOfOneTwoCoutnts(layers.getOrDefault(leastZeroLayer, ArrayList())))

}
