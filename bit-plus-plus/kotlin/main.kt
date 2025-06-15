fun main() {
    var x = 0
    val n = runCatching { readln().toInt() }
        .getOrElse {
            println("Input is not a number")
            return
        }

    if (n !in 0..150) {
        println("Invalid n")
        return
    }

    repeat(n) {
        val op_str = readln()
        if (op_str.length != 3) {
            println("Invalid operation")
            return
        }
        val op = op_str[1]
        if (op == '+') {
            x += 1
        } else {
            x -= 1
        }
    }

    println(x)
}
