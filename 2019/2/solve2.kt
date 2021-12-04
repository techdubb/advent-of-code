import java.io.File
import kotlin.math.*

fun readFileAsLinesUsingBufferedReader(fileName: String): List<String>
  = File(fileName).bufferedReader().readLines()

fun doNextOp(prog: MutableList<Int>, index: Int): Pair<MutableList<Int>, Boolean> {
    var exit = false
    val subProg = prog.subList(index, index+4)

    // println("-----")
    // println(subProg)
    // println("-----")

    if (subProg.get(0) == 1) {
        //add stuff
        val read1 = prog.get(subProg.get(1))
        val read2 = prog.get(subProg.get(2))
        val sum = read1 + read2
        // println(sum)
        prog.set(subProg.get(3), sum)
    } else if (subProg.get(0) == 2) {
        //multi stuff
        val read1 = prog.get(subProg.get(1))
        val read2 = prog.get(subProg.get(2))
        val prod = read1 * read2
        // println(prod)
        prog.set(subProg.get(3), prod)
    } else if (subProg.get(0) == 99) {
        exit = true
    }

    return Pair(prog, exit)
}

fun runProgram(program: MutableList<Int>, noun: Int, verb: Int): Int {
    var index = 0
    //replace
    program.set(1, noun)
    program.set(2, verb)

    var prog = program

    while (true) {
        var (prog, exit) = doNextOp(prog, index)
        // println(prog)
        // println(exit)

        index += 4
        if (exit) break
    }

    return program.get(0)
}

fun main(args: Array<String>) {
    // val inputList = readFileAsLinesUsingBufferedReader("input_test_1.txt")
    val inputList = readFileAsLinesUsingBufferedReader("input_2_1.txt")
    // println(inputList)

    val regex = "\\s*,\\s*".toRegex()
    // var program = inputList.get(0).split(regex).map { it.trim().toInt() }.toMutableList()
    // println(program)
    // println("**********")


    for (x in 0..99) {
        for (y in 0..99) {
            try {
                var program = inputList.get(0).split(regex).map { it.trim().toInt() }.toMutableList()
                val ans = runProgram(program, x, y)
                // println("ANSWER!!!")
                // println(ans)
                // println("!!!ANSWER")
                if (ans == 19690720) {
                    println(x)
                    println(y)
                    break
                }
            }
            catch (e: IndexOutOfBoundsException) {
                println(e)
                println(x)
                println(y)
                // handler
            }
        }
    }

}
