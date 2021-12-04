import java.io.File
import kotlin.math.*

fun testDouble(i: Int): Boolean {
    var n = i
    while (n > 0) {
        val digit = n % 10
        n = n / 10
        if (n % 10 == digit) return true
    }

    return false
}

fun testNoDescend(i: Int): Boolean {
    var n = i
    while (n > 0) {
        val digit = n % 10
        n = n / 10
        if (n % 10 > digit) return false
    }

    return true
}

fun testNoLargerGroup(i: Int): Boolean {
    val ints = (0..9).toList()

    val freqMap = ints.map { e -> frequencyDigits(i, e) }

    println(freqMap)
    val greaterThanTwo = freqMap.any { e -> e > 2 }
    val equalToTwo = freqMap.any { e -> e == 2 }

    if (greaterThanTwo && equalToTwo)
        return true
    else if (equalToTwo)
        return true
    else
        return false
}

fun frequencyDigits(m: Int, d: Int): Int {
    var c = 0 
    var n = m
      
    while (n > 0) {
        if (n % 10 == d) c += 1
        n = n / 10
    }

    return c
} 

fun main(args: Array<String>) {

    val start = 137683
    val end = 596253

    var total = 0

    for (i in start..end) {
        if (testNoDescend(i) && testNoLargerGroup(i)) total += 1
    }
    println(total)

    // println(testNoLargerGroup(112233))
    // println(testNoLargerGroup(123444))
    // println(testNoLargerGroup(111122))
}
