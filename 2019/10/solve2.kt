import java.io.File
import kotlin.math.*

fun readFileAsLinesUsingBufferedReader(fileName: String): List<String>
  = File(fileName).bufferedReader().readLines()

fun mergeLayers(layers: MutableMap<Int, List<Int>>): List<Int> {
    // 0 is black, 1 is white, and 2 is transparent
    var merged: MutableList<Int> = layers.getOrDefault(1, ArrayList()).toMutableList()

    for (l in layers) {
        var pixels = l.value
        for (i in 0..(pixels.size - 1)) {
            var pixel = pixels.get(i)
            var mPixel = merged.get(i)

            if ((pixel == 0 || pixel == 1) && mPixel == 2) {
                merged.set(i, pixel)
            }
        }
    }

    return merged
}

fun main(args: Array<String>) {
    // val inputList = readFileAsLinesUsingBufferedReader("input_test_1.txt")
    val inputList = readFileAsLinesUsingBufferedReader("input_2_1.txt")
    val input = inputList.get(0)
    // println(inputList)

    val w = 25
    val h = 6

    val inputSize = input.length
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
    val merged = mergeLayers(layers)

    index = 0
    for (i in 0..(h-1)) {
        for (j in 0..(w-1)) {
            print(merged.get(index))
            index += 1
        }
        println()
    }

}
