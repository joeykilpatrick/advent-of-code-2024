from dataclasses import dataclass
from itertools import combinations
from typing_extensions import Self

map_string: str = "...............3................d.................|.........................s..7......i.....e........|................C.......................e.........|...............Z.......m....................e.....|....................gC.....q......................|...............Q....s..........................A..|................................s........A........|...........n.....3.C..F......w..m...d.............|..E...............3.....m......d.i................|............f.3.......C....d........A.............|.........Z...........................n..A.........|....Q......p..............g.i.....................|.r......n...Q....p............S.7...........O.....|..........r......K....p.....M..........7....G.....|....................Fs...................G........|..z.........D..........G.g........................|rR.............F................M...............G.|.........I..c.nr...............M................O.|...I..............................................|...................f......I.......................|z.I...............f..K..........0................7|k...................K......u.........O............|.........Q...z.................ga......0.......o..|....E.5..F..................u..b.P......a.1.......|..........k9..................K.........H......1..|.E.........h..........................0......a...H|..........9...h..e........i......M....1...........|.c.............z.......................j.........T|c..D......................Pb.................2....|....................w.y......W......j.........T.2.|......ph...N..................y.......W.t.2.......|............9.................................o..1|.................Vq.......u....Pb.................|.......6R.........................................|........5............w...a.W.............H.j......|......Z.......Y..........V............H..2........|..........D.................v..y.........t...T..o.|.......5...................t......................|........8k...l...............v.........S....T...4.|......6....U......PR........b.B....y..............|..........6.V...U........................L........|.......8.........N....4.Vq.v..t......oJ.....L.....|N...........R.................w.JY................|............N.....................................|.....5Y.....................................j.....|.98........Y.....l.............B...........S...L..|.8...............U...............4................|..................W.........U4....................|...E........l..........B......................L..u|.....D............l....J..q.....................S."

chars: list[list[str]] = [list(line) for line in map_string.split("|")]

@dataclass(frozen=True)
class Coordinate:
    i: int
    j: int

    def __add__(self, other: Self) -> Self:
        return Coordinate(self.i + other.i, self.j + other.j)

    def __sub__(self, other: Self) -> Self:
        return Coordinate(self.i - other.i, self.j - other.j)


coords: list[list[Coordinate]] = []
signals: dict[str, list[Coordinate]] = {}

for i in range(len(chars)):
    coords.append([])
    for j in range(len(chars[i])):
        char = chars[i][j]
        coord = Coordinate(i, j)

        coords[i].append(coord)

        if char != '.':
            if char not in signals:
                signals[char] = []
            signals[char].append(coord)


def is_coordinate_in_map(coord: Coordinate) -> bool:
    return coord.i in range(len(coords)) and coord.j in range(len(coords[coord.i]))


def get_antinodes_1(signal: str) -> set[Coordinate]:
    pairs = combinations(signals[signal], 2)

    antinodes: set[Coordinate] = set()
    for (x,y) in pairs:
        diff = x - y

        possibilities: list[Coordinate] = [
            x + diff,
            y - diff,
        ]

        for pos in possibilities:
            if is_coordinate_in_map(pos):
                antinodes.add(pos)

    return antinodes


def get_antinodes_2(signal: str) -> set[Coordinate]:
    pairs = combinations(signals[signal], 2)

    antinodes: set[Coordinate] = set()
    for (x,y) in pairs:
        diff = x - y

        candidate = x
        while True:
            if is_coordinate_in_map(candidate):
                antinodes.add(candidate)
                candidate += diff
            else:
                break

        candidate = y
        while True:
            if is_coordinate_in_map(candidate):
                antinodes.add(candidate)
                candidate -= diff
            else:
                break

    return antinodes


problem1Solution = len(set.union(*map(get_antinodes_1, signals)))
problem2Solution = len(set.union(*map(get_antinodes_2, signals)))

print(problem1Solution)
print(problem2Solution)
