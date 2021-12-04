import java.io.File
import kotlin.math.*

fun readFileAsLinesUsingBufferedReader(fileName: String): List<String>
  = File(fileName).bufferedReader().readLines()

fun getMaxDims(wireOne: List<String>, wireTwo: List<String>): Pair<Pair<Int, Int>, Pair<Int, Int>> {
    var minY = Int.MAX_VALUE
    var maxY = Int.MIN_VALUE
    var minX = Int.MAX_VALUE
    var maxX = Int.MIN_VALUE

    var X = 0
    var Y = 0

    for (wire in listOf(wireOne, wireTwo)) {
        X = 0
        Y = 0
        for (it in wire) {
            val dir = it.get(0)
            val value = it.removeRange(0,1).toString().toInt()

            if (dir == 'L') {
                X -= value
                if (X < minX) { minX = X }
                if (X > maxX) { maxX = X }
            } else if (dir == 'R') {
                X += value
                if (X < minX) { minX = X }
                if (X > maxX) { maxX = X }
            } else if (dir == 'D') {
                Y -= value
                if (Y < minY) { minY = Y }
                if (Y > maxY) { maxY = Y }
            } else if (dir == 'U') {
                Y += value
                if (Y < minY) { minY = Y }
                if (Y > maxY) { maxY = Y }
            }
        }
    }

    println(minX)
    println(maxX)
    println(minY)
    println(maxY)

    var centralPortX = 0
    var centralPortY = 0
    if (minY < 0) {
        centralPortY = abs(minY) + 1
    }
    if (minX < 0) {
        centralPortX = abs(minX) + 1
    }
    val dims = Pair((abs(minX)+maxX)+2,(abs(minY)+maxY)+2)
    val centralPort = Pair(centralPortX, centralPortY)
    return Pair(dims, centralPort)
}

fun initDiagram(dims: Pair<Int, Int>, centralPort: Pair<Int, Int>): Array<Array<String>> {
    val x = dims.first
    val y = dims.second

    var array = arrayOf<String>()
    for (j in 0..y) {
        array += "."
    }

    var diagram = arrayOf<Array<String>>()
    for (i in 0..x) {
        diagram += array.copyOf()
    }

    // add central port
    diagram[centralPort.first][centralPort.second] = "o"

    return diagram
}

fun printDiagram(diagram: Array<Array<String>>): Unit {
    for (array in diagram) {
        for (value in array) {
            print("$value ")
        }
        println()
    }
}

fun addWire(wire: List<String>,
    diagram: Array<Array<String>>,
    centralPort: Pair<Int, Int>): Array<Array<String>> {
    var (x,y) = centralPort

    for (it in wire) {
        val dir = it.get(0)
        val value = it.removeRange(0,1).toString().toInt()

        if (dir == 'L') {
            for (i in 1..value) {
                x -= 1
                if (diagram[x][y] == "|") {
                    diagram[x][y] = "X"
                } else {
                    diagram[x][y] = "-"
                }
            }
        } else if (dir == 'R') {
            for (i in 1..value) {
                x += 1
                if (diagram[x][y] == "|") {
                    diagram[x][y] = "X"
                } else {
                    diagram[x][y] = "-"
                }
            }
        } else if (dir == 'D') {
            for (i in 1..value) {
                y -= 1
                if (diagram[x][y] == "-") {
                    diagram[x][y] = "X"
                } else {
                    diagram[x][y] = "|"
                }
            }
        } else if (dir == 'U') {
            for (i in 1..value) {
                y += 1
                if (diagram[x][y] == "-") {
                    diagram[x][y] = "X"
                } else {
                    diagram[x][y] = "|"
                }
            }
        }
    }

    return diagram
}

fun getWireSteps(wire: List<String>,
    diagram: Array<Array<String>>,
    centralPort: Pair<Int, Int>,
    theXs: MutableList<Pair<Int, Int>>): MutableMap<Pair<Int, Int>, Int> {

    var (x,y) = centralPort

    val mapXSteps = mutableMapOf<Pair<Int, Int>, Int>() 

    var steps = 0

    for (theX in theXs) {
        steps = 0
        x = centralPort.first
        y = centralPort.second

        val theXx = theX.first
        val theXy = theX.second

        for (it in wire) {
            val dir = it.get(0)
            val value = it.removeRange(0,1).toString().toInt()

            if (dir == 'L') {
                for (i in 1..value) {
                    x -= 1
                    steps += 1
                    if (x == theXx && y == theXy) {
                        break
                    }
                }
            } else if (dir == 'R') {
                for (i in 1..value) {
                    x += 1
                    steps += 1
                    if (x == theXx && y == theXy) {
                        break
                    }
                }
            } else if (dir == 'D') {
                for (i in 1..value) {
                    y -= 1
                    steps += 1
                    if (x == theXx && y == theXy) {
                        break
                    }
                }
            } else if (dir == 'U') {
                for (i in 1..value) {
                    y += 1
                    steps += 1
                    if (x == theXx && y == theXy) {
                        break
                    }
                }
            }

            if (x == theXx && y == theXy) {
                break
            }
        }

        mapXSteps.put(theX, steps)
    }

    return mapXSteps
}

fun findXs(diagram: Array<Array<String>>,
            dims: Pair<Int, Int>): MutableList<Pair<Int, Int>> {

    val x = dims.first
    val y = dims.second

    // find all X's
    val theXs = mutableListOf<Pair<Int, Int>>()
    for (i in 0..x) {
        for (j in 0..y) {
            if (diagram[i][j] == "X") {
                theXs.add(Pair(i,j))
            }
        }
    }

    return theXs
}

fun main(args: Array<String>) {
    // val inputList = readFileAsLinesUsingBufferedReader("input_test_1.txt")
    val inputList = readFileAsLinesUsingBufferedReader("input_1.txt")
    // println(inputList)

    val regex = "\\s*,\\s*".toRegex()
    var wireOne = inputList.get(0).split(regex).map { it.trim() }
    var wireTwo = inputList.get(1).split(regex).map { it.trim() }

    val (dims, centralPort) = getMaxDims(wireOne, wireTwo)
    println(dims)
    println(centralPort)

    var diagram = initDiagram(dims, centralPort)

    // printDiagram(diagram)

    println("*************")

    addWire(wireOne, diagram, centralPort)
    addWire(wireTwo, diagram, centralPort)
    val theXs = findXs(diagram, dims)
    println(theXs)
    // printDiagram(diagram)

    val stepsOne = getWireSteps(wireOne, diagram, centralPort, theXs)
    println(stepsOne)
    val stepsTwo = getWireSteps(wireTwo, diagram, centralPort, theXs)
    println(stepsTwo)

    val zipSteps = (stepsOne.keys + stepsTwo.keys).associateWith {
        setOf(stepsOne[it], stepsTwo[it]).filterNotNull().sum()
    }

    println(zipSteps)
    println(zipSteps.minBy{it.value})
}
