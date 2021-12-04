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

fun countToNode(orbit: OrbitingObject?, node: OrbitingObject?): Int {
    var parent: OrbitingObject? = orbit?.parent
    var count:Int = 0

    while (parent != node) {
        count += 1
        parent = parent?.parent
    }

    return count
}

fun leastCommonAncestor(nodeA: OrbitingObject?, nodeB: OrbitingObject?): OrbitingObject? {
    var parent: OrbitingObject? = nodeA?.parent
    val nodeList: MutableList<String> = ArrayList()

    while (parent?.name != null) {
        nodeList.add(parent.name)
        parent = parent.parent
    }

    parent = nodeB?.parent
    while (!nodeList.contains(parent?.name)) {
        parent = parent?.parent
    }

    return parent
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

    val lca = leastCommonAncestor(orbs.get("YOU"), orbs.get("SAN"))
    // println(lca)

    val youCount = countToNode(orbs.get("YOU"), lca)
    val sanCount = countToNode(orbs.get("SAN"), lca)
    
    println(youCount + sanCount)


}
