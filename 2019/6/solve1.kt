import java.io.File
import kotlin.math.*

fun readFileAsLinesUsingBufferedReader(fileName: String): List<String>
  = File(fileName).bufferedReader().readLines()

class OrbitingObject(name: String) {
    val name = "$name"
    var parent: OrbitingObject? = null
    var orbits: MutableList<OrbitingObject> = ArrayList()

    fun addChild(node:OrbitingObject){
        orbits.add(node)
        node.parent = this
    }

    override fun toString(): String {
        var s = "${name}"
        if (!orbits.isEmpty()) {
            s += " {" + orbits.map { it.toString() } + " }"
        }
        return s
    }
}

fun countToCOM(orbit: OrbitingObject?): Int {
    var parent: OrbitingObject? = orbit?.parent
    var count:Int = 0

    while (parent != null) {
        count += 1
        parent = parent.parent
    }

    return count

}

fun main(args: Array<String>) {
    // val inputList = readFileAsLinesUsingBufferedReader("input_test_1.txt")
    val inputList = readFileAsLinesUsingBufferedReader("input_2_1.txt")
    // println(inputList)

    val orbs: MutableMap<String, OrbitingObject> = mutableMapOf()

    for (pairs in inputList) {
        var parts= pairs.split(")")

        val center = parts.get(0)
        val orbital = parts.get(1)

        var centerObj = orbs.get(center)
        var orbitalObj = orbs.get(orbital)

        if (centerObj == null) {
            centerObj = OrbitingObject(center)
            orbs.put(center, centerObj)
        }

        if (orbitalObj == null) {
            orbitalObj = OrbitingObject(orbital)
            orbs.put(orbital, orbitalObj)
        }

        centerObj.addChild(orbitalObj)
    }

    // println(orbs.get("COM"))

    val counts = orbs.keys.map { countToCOM(orbs.get(it)) }
    println(counts.sum())

    // println(countToCOM(orbs.get("COM")))


}
