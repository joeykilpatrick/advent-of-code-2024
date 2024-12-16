val map: List<List<Char>> = "...............3................d.................|.........................s..7......i.....e........|................C.......................e.........|...............Z.......m....................e.....|....................gC.....q......................|...............Q....s..........................A..|................................s........A........|...........n.....3.C..F......w..m...d.............|..E...............3.....m......d.i................|............f.3.......C....d........A.............|.........Z...........................n..A.........|....Q......p..............g.i.....................|.r......n...Q....p............S.7...........O.....|..........r......K....p.....M..........7....G.....|....................Fs...................G........|..z.........D..........G.g........................|rR.............F................M...............G.|.........I..c.nr...............M................O.|...I..............................................|...................f......I.......................|z.I...............f..K..........0................7|k...................K......u.........O............|.........Q...z.................ga......0.......o..|....E.5..F..................u..b.P......a.1.......|..........k9..................K.........H......1..|.E.........h..........................0......a...H|..........9...h..e........i......M....1...........|.c.............z.......................j.........T|c..D......................Pb.................2....|....................w.y......W......j.........T.2.|......ph...N..................y.......W.t.2.......|............9.................................o..1|.................Vq.......u....Pb.................|.......6R.........................................|........5............w...a.W.............H.j......|......Z.......Y..........V............H..2........|..........D.................v..y.........t...T..o.|.......5...................t......................|........8k...l...............v.........S....T...4.|......6....U......PR........b.B....y..............|..........6.V...U........................L........|.......8.........N....4.Vq.v..t......oJ.....L.....|N...........R.................w.JY................|............N.....................................|.....5Y.....................................j.....|.98........Y.....l.............B...........S...L..|.8...............U...............4................|..................W.........U4....................|...E........l..........B......................L..u|.....D............l....J..q.....................S."
    .split("|")
    .map { it.toCharArray().toList() }

data class Coordinate(val i: Int, val j: Int) {

    operator fun plus(other: Coordinate): Coordinate {
        return Coordinate(this.i + other.i, this.j + other.j)
    }

    operator fun minus(other: Coordinate): Coordinate {
        return Coordinate(this.i - other.i, this.j - other.j)
    }

    fun isInMap(): Boolean {
        return this.i in map.indices && this.j in map[this.i].indices
    }

}

val coords: List<List<Coordinate>> = buildList {
    for (i in map.indices) {
        val row: List<Coordinate> = buildList {
            for (j in map[i].indices) {
                add(Coordinate(i, j))
            }
        }
        add(row)
    }
}

val signals: Map<Char, MutableSet<Coordinate>> = buildMap {
    for (i in map.indices) {
        for (j in map[i].indices) {
            val signal: Char = map[j][i]
            if (signal != '.') {
                putIfAbsent(signal, mutableSetOf())
                get(signal)!!.add(coords[i][j])
            }
        }
    }
}

fun getAntinodes1(signal: Char): Set<Coordinate> {
    val signalCoords = signals[signal] ?: listOf()

    return buildSet {
        signalCoords.forEach { c1 ->
            signalCoords.forEach { c2 ->
                if (c1 === c2) {
                    return@forEach
                }
                val diff = c1 - c2

                if ((c1 + diff).isInMap()) {
                    add(c1 + diff)
                }
                if ((c2 - diff).isInMap()) {
                    add(c2 - diff)
                }
            }
        }
    }
}


fun getAntinodes2(signal: Char): Set<Coordinate> {
    val signalCoords = signals[signal] ?: emptySet()

    return buildSet {
        signalCoords.forEach { c1 ->
            signalCoords.forEach { c2 ->
                if (c1 === c2) {
                    return@forEach
                }
                val diff = c1 - c2

                var candidate: Coordinate = c1
                while (true) {
                    if (candidate.isInMap()) {
                        add(candidate)
                        candidate += diff
                    } else {
                        break
                    }
                }

                candidate = c2
                while (true) {
                    if (candidate.isInMap()) {
                        add(candidate)
                        candidate -= diff
                    } else {
                        break
                    }
                }
            }
        }
    }
}

val problem1Solution: Int = signals
    .keys
    .map(::getAntinodes1)
    .reduce { x, y -> x + y }
    .size
    .also(::println)

val problem2Solution: Int = signals
    .keys
    .map(::getAntinodes2)
    .reduce { x, y -> x + y }
    .size
    .also(::println)
