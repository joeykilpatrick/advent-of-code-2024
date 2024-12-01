import kotlin.math.abs

val pairs: List<Pair<Int, Int>> = listOf(Pair(87501, 76559), Pair(70867, 16862), Pair(12959, 38527), Pair(56898, 81917), Pair(80416, 13287), Pair(28886, 54457), Pair(79252, 30354), Pair(47576, 88490), Pair(43354, 37397), Pair(89248, 74846), Pair(39921, 24805), Pair(98636, 51185), Pair(33277, 31605), Pair(45307, 13417), Pair(33326, 72874), Pair(14449, 42023), Pair(64412, 40326), Pair(12630, 40326), Pair(35665, 41197), Pair(35932, 59560), Pair(22757, 76636), Pair(97387, 91997), Pair(83599, 74846), Pair(33718, 54077), Pair(20879, 65995), Pair(42419, 35638), Pair(50241, 41197), Pair(94123, 27231), Pair(82872, 65149), Pair(41378, 85282), Pair(81233, 65415), Pair(98875, 21219), Pair(21517, 81917), Pair(36314, 65845), Pair(64212, 43331), Pair(94404, 34854), Pair(42166, 87444), Pair(13351, 12627), Pair(53796, 47507), Pair(19837, 28551), Pair(59598, 71749), Pair(47765, 93643), Pair(11282, 91997), Pair(71285, 69206), Pair(27075, 56104), Pair(11470, 50196), Pair(75795, 17345), Pair(77811, 85578), Pair(56347, 74690), Pair(54911, 35921), Pair(26533, 96584), Pair(75314, 58859), Pair(49216, 30077), Pair(94855, 14154), Pair(10775, 91997), Pair(58190, 81917), Pair(38228, 85154), Pair(88321, 21470), Pair(99407, 38527), Pair(39166, 13647), Pair(22369, 96563), Pair(61678, 29486), Pair(94911, 64616), Pair(99565, 66640), Pair(64630, 86818), Pair(60973, 22185), Pair(83684, 27341), Pair(44345, 22530), Pair(43964, 11793), Pair(13207, 62913), Pair(20848, 30354), Pair(43944, 38527), Pair(48992, 38527), Pair(44659, 10142), Pair(93179, 96119), Pair(80123, 86215), Pair(46758, 75732), Pair(34750, 18011), Pair(38136, 92652), Pair(25072, 58141), Pair(99637, 96563), Pair(42591, 32117), Pair(48968, 60830), Pair(68846, 15876), Pair(63257, 19695), Pair(20217, 69184), Pair(50862, 86772), Pair(35900, 31605), Pair(61185, 10607), Pair(41487, 98125), Pair(29962, 81917), Pair(44777, 73031), Pair(40743, 25415), Pair(57518, 13407), Pair(89369, 36534), Pair(36269, 31605), Pair(59657, 27902), Pair(72361, 51185), Pair(71609, 15589), Pair(76578, 19417), Pair(35670, 18977), Pair(99141, 95960), Pair(30841, 55313), Pair(91034, 30354), Pair(70937, 81509), Pair(65910, 12959), Pair(62321, 74690), Pair(39367, 79276), Pair(39883, 23467), Pair(15590, 54077), Pair(70456, 26094), Pair(21706, 97640), Pair(91933, 26097), Pair(88390, 65845), Pair(24955, 91997), Pair(87059, 71437), Pair(33177, 86262), Pair(57578, 84284), Pair(24831, 21219), Pair(19693, 74846), Pair(87500, 20041), Pair(88393, 50151), Pair(18468, 69184), Pair(61548, 69184), Pair(75166, 74739), Pair(80975, 52736), Pair(54909, 58854), Pair(85260, 61330), Pair(86203, 15355), Pair(75868, 81154), Pair(57081, 81917), Pair(44633, 41212), Pair(53395, 92203), Pair(38922, 84627), Pair(45580, 22005), Pair(11492, 12959), Pair(13813, 23052), Pair(77790, 31605), Pair(97416, 41197), Pair(60784, 40326), Pair(91432, 12377), Pair(64293, 74468), Pair(53735, 54077), Pair(11377, 23052), Pair(35848, 57154), Pair(29067, 57838), Pair(14215, 61664), Pair(72068, 30354), Pair(23691, 58540), Pair(17111, 28991), Pair(66651, 12959), Pair(35155, 25057), Pair(76500, 74690), Pair(59018, 78562), Pair(51786, 64460), Pair(12770, 80286), Pair(41212, 53868), Pair(85299, 46294), Pair(58892, 21646), Pair(46842, 31347), Pair(80228, 82547), Pair(21816, 41197), Pair(63096, 69071), Pair(55837, 74130), Pair(13699, 99276), Pair(88678, 23052), Pair(17917, 65679), Pair(42692, 28551), Pair(42536, 90759), Pair(29227, 74130), Pair(44887, 47070), Pair(14869, 96563), Pair(62941, 87555), Pair(96430, 52517), Pair(92100, 96563), Pair(69859, 65845), Pair(78066, 55780), Pair(71937, 80440), Pair(79682, 46524), Pair(90428, 37542), Pair(17489, 76606), Pair(12443, 48973), Pair(92963, 12959), Pair(13845, 39796), Pair(27104, 19295), Pair(84047, 92652), Pair(17026, 54077), Pair(16587, 14154), Pair(38434, 61664), Pair(96992, 78286), Pair(60514, 74130), Pair(76740, 31347), Pair(77040, 71639), Pair(57707, 69864), Pair(18252, 74823), Pair(50362, 92774), Pair(87527, 54077), Pair(18024, 62644), Pair(16185, 99146), Pair(15836, 31347), Pair(71453, 22056), Pair(81519, 20539), Pair(92269, 41197), Pair(89510, 98904), Pair(64230, 65845), Pair(44965, 69184), Pair(97898, 50122), Pair(33394, 71749), Pair(51205, 31347), Pair(29970, 91997), Pair(18703, 38527), Pair(95881, 85733), Pair(78977, 65679), Pair(44185, 42353), Pair(59579, 79102), Pair(98081, 88026), Pair(75176, 28551), Pair(23052, 25529), Pair(23648, 86507), Pair(68646, 65149), Pair(81344, 94453), Pair(89002, 23057), Pair(91635, 92652), Pair(83079, 54077), Pair(19710, 96563), Pair(55515, 31857), Pair(94625, 45828), Pair(95178, 40326), Pair(43069, 41940), Pair(32573, 48931), Pair(28551, 28551), Pair(71918, 31605), Pair(64790, 25534), Pair(70603, 80997), Pair(98971, 60973), Pair(26316, 45940), Pair(56050, 47638), Pair(70043, 86262), Pair(89213, 96563), Pair(19535, 86236), Pair(75037, 86262), Pair(56394, 30161), Pair(10420, 38501), Pair(97325, 34627), Pair(79627, 38019), Pair(90943, 64789), Pair(89009, 65149), Pair(41714, 74846), Pair(56219, 30354), Pair(67414, 33426), Pair(70637, 91997), Pair(65116, 68219), Pair(65081, 92652), Pair(30062, 28551), Pair(53883, 74846), Pair(82201, 35608), Pair(30366, 36832), Pair(92536, 34251), Pair(41242, 23208), Pair(28183, 95131), Pair(95821, 20974), Pair(70104, 53868), Pair(92750, 81866), Pair(19452, 31605), Pair(63808, 40326), Pair(48841, 74690), Pair(78057, 28551), Pair(18349, 23052), Pair(49722, 69184), Pair(47153, 92162), Pair(87301, 17834), Pair(62420, 60858), Pair(77680, 46524), Pair(27690, 17204), Pair(59409, 92652), Pair(42268, 28551), Pair(63330, 17663), Pair(36144, 77627), Pair(31999, 23179), Pair(63097, 44128), Pair(32578, 30185), Pair(37261, 39103), Pair(75864, 10428), Pair(49682, 64324), Pair(19524, 86615), Pair(21013, 57384), Pair(28003, 14804), Pair(69912, 23052), Pair(56391, 16437), Pair(55578, 63279), Pair(66306, 38527), Pair(50485, 97228), Pair(17388, 69184), Pair(68640, 51185), Pair(34002, 69184), Pair(53182, 74846), Pair(26868, 30764), Pair(54480, 21219), Pair(78677, 30346), Pair(63487, 49614), Pair(96563, 41212), Pair(63947, 86772), Pair(95430, 19044), Pair(66914, 70185), Pair(17750, 12959), Pair(44339, 31260), Pair(91997, 85956), Pair(19858, 81917), Pair(39187, 14154), Pair(31250, 11742), Pair(81979, 11075), Pair(43865, 93422), Pair(41577, 12959), Pair(59486, 26106), Pair(84822, 67408), Pair(83663, 28563), Pair(53342, 88705), Pair(88483, 31347), Pair(26040, 64385), Pair(59222, 22924), Pair(28173, 52034), Pair(47265, 12959), Pair(98279, 23813), Pair(74690, 53868), Pair(50359, 17936), Pair(24495, 97323), Pair(67473, 74690), Pair(31605, 86772), Pair(47293, 69495), Pair(78146, 54077), Pair(62042, 74130), Pair(22969, 81917), Pair(86262, 41212), Pair(20100, 14154), Pair(31926, 51869), Pair(83586, 20705), Pair(78067, 87533), Pair(15120, 80541), Pair(60964, 74514), Pair(25983, 86772), Pair(22555, 85287), Pair(82691, 41212), Pair(33704, 54077), Pair(60332, 65149), Pair(88891, 54077), Pair(11798, 54077), Pair(33296, 95893), Pair(21560, 71749), Pair(72107, 23992), Pair(99423, 16437), Pair(74019, 53868), Pair(11793, 31347), Pair(24580, 57047), Pair(29058, 41212), Pair(13516, 65325), Pair(45127, 65149), Pair(78583, 68013), Pair(47357, 26483), Pair(74336, 54077), Pair(73563, 89201), Pair(48046, 22056), Pair(99277, 40534), Pair(51620, 22865), Pair(26126, 50197), Pair(39198, 46524), Pair(99101, 38128), Pair(53868, 57894), Pair(60036, 79056), Pair(98998, 14506), Pair(33596, 49268), Pair(96813, 97654), Pair(63461, 51185), Pair(44286, 31605), Pair(32282, 65845), Pair(40326, 21219), Pair(31739, 99276), Pair(86081, 64405), Pair(17565, 11401), Pair(98499, 52794), Pair(54371, 51185), Pair(64366, 91997), Pair(22558, 44849), Pair(80145, 80748), Pair(55344, 30354), Pair(82390, 78198), Pair(67477, 52858), Pair(41679, 65845), Pair(26759, 61664), Pair(25479, 24285), Pair(84759, 94740), Pair(23922, 31734), Pair(69409, 32214), Pair(16130, 14154), Pair(17075, 41197), Pair(26992, 88528), Pair(75638, 14608), Pair(40799, 31367), Pair(70389, 65387), Pair(48822, 91997), Pair(82741, 65149), Pair(53111, 75593), Pair(96714, 91408), Pair(61824, 98553), Pair(80721, 68977), Pair(14154, 26094), Pair(65521, 21219), Pair(62357, 65149), Pair(17248, 33364), Pair(62195, 96563), Pair(31347, 69184), Pair(21582, 96563), Pair(67200, 15744), Pair(32845, 70938), Pair(69303, 16437), Pair(43616, 94424), Pair(70647, 32249), Pair(37198, 29513), Pair(56883, 86314), Pair(55553, 74130), Pair(44144, 29558), Pair(93899, 31605), Pair(94230, 96563), Pair(92309, 65679), Pair(69517, 91305), Pair(30628, 21219), Pair(14181, 15109), Pair(86696, 59832), Pair(92793, 79552), Pair(26915, 12959), Pair(32013, 99276), Pair(81917, 11773), Pair(85533, 91997), Pair(10291, 57895), Pair(47306, 86262), Pair(40182, 86772), Pair(78380, 96563), Pair(14074, 31347), Pair(29716, 51680), Pair(34074, 69184), Pair(83682, 79659), Pair(32571, 81917), Pair(24215, 65845), Pair(14613, 30354), Pair(86190, 46524), Pair(22056, 77073), Pair(47602, 77596), Pair(40618, 22388), Pair(61777, 69973), Pair(83610, 86262), Pair(41123, 74442), Pair(14249, 55123), Pair(49493, 94023), Pair(42659, 94250), Pair(38055, 92652), Pair(49301, 72817), Pair(92652, 96746), Pair(96637, 41212), Pair(63286, 53868), Pair(64698, 19412), Pair(48939, 65149), Pair(77435, 42058), Pair(86082, 97780), Pair(56906, 31605), Pair(18370, 69184), Pair(55583, 96944), Pair(10163, 99796), Pair(57905, 99276), Pair(62348, 28809), Pair(84711, 81543), Pair(14792, 31605), Pair(27680, 69184), Pair(90559, 55495), Pair(56049, 23052), Pair(30776, 23052), Pair(25298, 89829), Pair(72656, 86262), Pair(74027, 34083), Pair(79517, 31376), Pair(70497, 36800), Pair(67662, 65845), Pair(71206, 47116), Pair(14457, 17103), Pair(79508, 31347), Pair(69184, 24527), Pair(18264, 85310), Pair(16462, 81917), Pair(48031, 53868), Pair(85157, 82675), Pair(12794, 67521), Pair(56636, 69184), Pair(63663, 23052), Pair(83754, 12959), Pair(90766, 27743), Pair(48559, 15605), Pair(95519, 43790), Pair(24578, 14154), Pair(13264, 29964), Pair(72984, 53868), Pair(23859, 27144), Pair(52266, 14154), Pair(74332, 27923), Pair(40908, 37044), Pair(45622, 65679), Pair(97941, 41197), Pair(29959, 72533), Pair(75077, 76897), Pair(43027, 69795), Pair(75223, 54077), Pair(46175, 41212), Pair(60194, 78373), Pair(63100, 51133), Pair(41845, 19241), Pair(33956, 85483), Pair(71994, 81917), Pair(32196, 30354), Pair(26319, 55110), Pair(52113, 38527), Pair(45378, 17528), Pair(29872, 15275), Pair(45386, 92652), Pair(50436, 51185), Pair(59375, 77172), Pair(29944, 96563), Pair(80342, 40326), Pair(10493, 16437), Pair(97587, 64996), Pair(59750, 65664), Pair(88477, 53868), Pair(95607, 53868), Pair(81650, 60061), Pair(89497, 21219), Pair(60828, 69184), Pair(18759, 41212), Pair(25409, 86772), Pair(42395, 73365), Pair(42537, 71749), Pair(23075, 15595), Pair(33176, 92903), Pair(61312, 77585), Pair(49549, 16437), Pair(13037, 30354), Pair(22694, 27763), Pair(55457, 40372), Pair(41517, 74846), Pair(62998, 69981), Pair(33002, 81778), Pair(19731, 50866), Pair(37666, 72519), Pair(44046, 80344), Pair(16308, 34728), Pair(39639, 35278), Pair(52166, 58851), Pair(18885, 51185), Pair(52717, 16437), Pair(54738, 51185), Pair(30354, 23052), Pair(71905, 83743), Pair(53902, 53981), Pair(49202, 45117), Pair(29053, 53704), Pair(73107, 93596), Pair(10814, 81917), Pair(47137, 81917), Pair(14681, 46524), Pair(23659, 19157), Pair(41523, 19877), Pair(37342, 74712), Pair(14677, 35820), Pair(80367, 30354), Pair(29514, 68638), Pair(92987, 44546), Pair(53999, 13219), Pair(53071, 12959), Pair(18116, 30354), Pair(41120, 21219), Pair(24265, 13890), Pair(74236, 12238), Pair(16153, 40253), Pair(29225, 16518), Pair(77153, 69767), Pair(11156, 15109), Pair(17676, 72608), Pair(97762, 69184), Pair(14294, 74130), Pair(20945, 53868), Pair(89054, 69842), Pair(50026, 92308), Pair(11773, 35864), Pair(43398, 46524), Pair(81325, 76898), Pair(72450, 94665), Pair(73264, 14831), Pair(11738, 45600), Pair(47816, 33630), Pair(96440, 38527), Pair(49621, 26094), Pair(99276, 86262), Pair(83302, 66242), Pair(44195, 82631), Pair(72375, 19298), Pair(62769, 30354), Pair(24836, 41212), Pair(54126, 12959), Pair(56172, 53521), Pair(40147, 84315), Pair(15109, 48388), Pair(36959, 44227), Pair(72676, 50902), Pair(29907, 57407), Pair(17101, 59056), Pair(27776, 92652), Pair(33908, 38484), Pair(31997, 41212), Pair(60558, 60338), Pair(76898, 29376), Pair(66530, 12210), Pair(55325, 74690), Pair(14813, 81185), Pair(65149, 86262), Pair(64181, 42618), Pair(13236, 75101), Pair(85280, 25972), Pair(23433, 27380), Pair(76693, 28959), Pair(27598, 65845), Pair(85215, 16437), Pair(69326, 31605), Pair(73527, 54077), Pair(83772, 50003), Pair(13383, 90621), Pair(74846, 86772), Pair(76968, 51536), Pair(67965, 99132), Pair(75669, 71623), Pair(11827, 13380), Pair(65958, 99706), Pair(27705, 54077), Pair(29880, 83668), Pair(64798, 37851), Pair(15552, 20138), Pair(81369, 86262), Pair(16035, 13132), Pair(19559, 34135), Pair(58504, 41212), Pair(53208, 96563), Pair(72798, 44868), Pair(63911, 54077), Pair(73341, 86272), Pair(57970, 81361), Pair(34600, 40326), Pair(32884, 85531), Pair(71749, 49989), Pair(16407, 39922), Pair(48023, 47921), Pair(55208, 38527), Pair(87016, 88919), Pair(61959, 71284), Pair(14403, 20794), Pair(61664, 74846), Pair(84201, 12488), Pair(73175, 16437), Pair(75814, 65638), Pair(91655, 98512), Pair(33948, 23052), Pair(80300, 69184), Pair(70886, 76898), Pair(41410, 65149), Pair(78044, 16437), Pair(32339, 58862), Pair(16859, 18026), Pair(10047, 30354), Pair(23013, 31605), Pair(37757, 22056), Pair(28383, 39425), Pair(88083, 23844), Pair(91191, 21148), Pair(21219, 53868), Pair(68359, 54326), Pair(36728, 81111), Pair(83279, 55929), Pair(30823, 72588), Pair(94846, 60851), Pair(45506, 40326), Pair(33240, 21219), Pair(65845, 61445), Pair(45314, 95859), Pair(94477, 91997), Pair(41623, 91997), Pair(18698, 81917), Pair(26025, 96563), Pair(67139, 28719), Pair(70864, 20565), Pair(63628, 86772), Pair(82479, 12959), Pair(56207, 23052), Pair(18780, 68150), Pair(61220, 53868), Pair(94501, 47083), Pair(58257, 10169), Pair(16437, 38161), Pair(89620, 44175), Pair(74771, 46524), Pair(99455, 32934), Pair(77273, 91997), Pair(20854, 40324), Pair(43825, 74130), Pair(89584, 41212), Pair(86772, 87585), Pair(16169, 40326), Pair(23079, 91997), Pair(20347, 12771), Pair(33162, 53321), Pair(77049, 61664), Pair(52391, 11773), Pair(98777, 19105), Pair(86182, 77697), Pair(84991, 76064), Pair(46587, 14887), Pair(13200, 76667), Pair(76967, 65149), Pair(56719, 38542), Pair(77987, 41197), Pair(74246, 78717), Pair(68857, 23052), Pair(92089, 65845), Pair(79803, 44983), Pair(16391, 86083), Pair(85511, 82407), Pair(14130, 31605), Pair(20211, 65845), Pair(51868, 35534), Pair(11881, 17074), Pair(43073, 87808), Pair(74013, 95379), Pair(63581, 91997), Pair(67718, 75679), Pair(95358, 38527), Pair(78186, 12888), Pair(35563, 61664), Pair(63140, 92652), Pair(11832, 54077), Pair(11698, 58297), Pair(22084, 11865), Pair(98044, 64989), Pair(26094, 35964), Pair(45393, 92652), Pair(38527, 93080), Pair(66819, 46524), Pair(31166, 52386), Pair(39568, 79757), Pair(94063, 77614), Pair(16452, 83128), Pair(24171, 91977), Pair(74980, 12959), Pair(47814, 38527), Pair(71716, 45179), Pair(34263, 14154), Pair(43631, 53868), Pair(47023, 99276), Pair(56699, 27179), Pair(13150, 41212), Pair(65739, 46524), Pair(87085, 60735), Pair(67283, 21219), Pair(23771, 32301), Pair(65647, 55281), Pair(50600, 45366), Pair(88186, 54121), Pair(48164, 86262), Pair(34469, 21705), Pair(76035, 97022), Pair(91266, 69184), Pair(55549, 65149), Pair(34832, 38480), Pair(72693, 74690), Pair(66050, 65149), Pair(50769, 63440), Pair(34690, 91929), Pair(58125, 37769), Pair(16861, 65845), Pair(26369, 65845), Pair(31834, 74130), Pair(24724, 76898), Pair(35677, 46524), Pair(79253, 16437), Pair(29593, 31347), Pair(29695, 51028), Pair(18196, 96563), Pair(33927, 74846), Pair(24378, 16437), Pair(37505, 47616), Pair(70048, 31232), Pair(27708, 53750), Pair(14952, 92748), Pair(37930, 53868), Pair(41197, 28551), Pair(77433, 38527), Pair(77320, 54519), Pair(37592, 82995), Pair(73963, 65149), Pair(67891, 66894), Pair(71199, 71879), Pair(13884, 73982), Pair(97681, 33048), Pair(44494, 21083), Pair(56856, 62395), Pair(56521, 48031), Pair(11077, 40326), Pair(98851, 49244), Pair(19484, 46916), Pair(51325, 19011), Pair(74821, 65679), Pair(90241, 78808), Pair(24897, 60176), Pair(40386, 30354), Pair(66435, 10877), Pair(17691, 88972), Pair(17430, 96495), Pair(76735, 57514), Pair(23936, 46524), Pair(86656, 86003), Pair(81533, 46524), Pair(23473, 14374), Pair(44831, 17013), Pair(73390, 53868), Pair(20456, 38527), Pair(47304, 43209), Pair(95484, 26094), Pair(40033, 92652), Pair(49629, 65845), Pair(11518, 94552), Pair(99642, 28659), Pair(46027, 38527), Pair(93133, 99640), Pair(88453, 69184), Pair(52465, 87482), Pair(65679, 96563), Pair(51133, 86262), Pair(82072, 24993), Pair(65019, 81577), Pair(73181, 20846), Pair(25682, 74846), Pair(89215, 23052), Pair(75313, 28895), Pair(59429, 99506), Pair(95353, 98713), Pair(14199, 71449), Pair(28894, 21219), Pair(34814, 77228), Pair(12462, 81917), Pair(77803, 10891), Pair(54077, 25857), Pair(56105, 87001), Pair(49225, 91997), Pair(33427, 23052), Pair(28144, 53868), Pair(44230, 74256), Pair(64121, 38385), Pair(44223, 94238), Pair(91417, 28551), Pair(27420, 43632), Pair(49221, 41212), Pair(37139, 31605), Pair(65039, 36279), Pair(40544, 97794), Pair(70621, 62790), Pair(89720, 12494), Pair(93652, 70171), Pair(99679, 77510), Pair(48132, 65845), Pair(27910, 63372), Pair(61906, 54077), Pair(79192, 88515), Pair(52071, 15109), Pair(68413, 40326), Pair(38094, 65845), Pair(85325, 22914), Pair(34519, 60686), Pair(18347, 62726), Pair(74130, 86262), Pair(22266, 70119), Pair(24902, 79593), Pair(58897, 53868), Pair(67166, 94563), Pair(86035, 54859), Pair(32151, 51640), Pair(19735, 28551), Pair(86835, 65845), Pair(48502, 69184), Pair(98335, 65461), Pair(85776, 61664), Pair(31060, 41212), Pair(51185, 25984), Pair(10538, 61666), Pair(89716, 70800), Pair(93969, 46524), Pair(87113, 41212), Pair(94835, 43501), Pair(31171, 61231), Pair(63678, 83332), Pair(27983, 36115), Pair(31882, 66078), Pair(69310, 21182), Pair(57748, 69184), Pair(34236, 61664), Pair(22019, 53868), Pair(40783, 74204), Pair(11443, 65306), Pair(61587, 74130), Pair(32107, 20837), Pair(42950, 75914), Pair(30318, 28551), Pair(71868, 21219), Pair(11717, 29036), Pair(15069, 54142), Pair(46368, 23052), Pair(19544, 53868), Pair(96045, 10501), Pair(70708, 90926), Pair(66286, 14154), Pair(93443, 46524), Pair(22988, 52299), Pair(59398, 87705), Pair(54189, 79654), Pair(44636, 47669), Pair(34569, 12959), Pair(75207, 88665), Pair(57213, 81917), Pair(17661, 76365), Pair(76744, 41550), Pair(18525, 81729), Pair(44095, 89137), Pair(47905, 69184), Pair(64998, 70782), Pair(94932, 14154), Pair(79764, 85179), Pair(94708, 22056), Pair(97002, 11773), Pair(65044, 71749), Pair(81636, 90224), Pair(67614, 31605), Pair(69858, 12959), Pair(37652, 86650), Pair(59098, 35258), Pair(26949, 46653), Pair(19239, 21219), Pair(46003, 58379), Pair(77640, 55716), Pair(92129, 51133), Pair(46524, 60031), Pair(11683, 44416), Pair(72664, 86772), Pair(80935, 81071), Pair(12683, 86262), Pair(47561, 41319), Pair(97326, 32695), Pair(91545, 31605), Pair(50527, 99276), Pair(78000, 61404), Pair(58880, 14154), Pair(47352, 89525), Pair(64943, 54678), Pair(34249, 12959), Pair(90703, 52069), Pair(42396, 21732), Pair(17077, 72444), Pair(40369, 16956), Pair(17581, 39897), Pair(18310, 46524), Pair(93377, 20361), Pair(21337, 41798), Pair(31532, 65845), Pair(63298, 78248), Pair(39119, 46524), Pair(53668, 38527), Pair(50927, 96563), Pair(57380, 47367), Pair(68451, 16437), Pair(96725, 28551), Pair(49778, 86415), Pair(46687, 12305), Pair(93651, 84334), Pair(17709, 46524), Pair(36657, 38527), Pair(67669, 20743), Pair(18254, 55605), Pair(99194, 12959), Pair(51889, 29126), Pair(11292, 35259), Pair(39589, 74690), Pair(14716, 54077), Pair(71832, 67905), Pair(54150, 55806), Pair(36451, 46524), Pair(14806, 96563), Pair(63718, 74103), Pair(58557, 95632), Pair(98671, 95757), Pair(48004, 65149), Pair(20103, 21592))

fun main() {
    val (left, right) = pairs.unzip()
    val leftSorted = left.toMutableList().apply { this.sort() }
    val rightSorted = right.toMutableList().apply { this.sort() }

    val problem1Solution = leftSorted.zip(rightSorted).map { (i, j) -> abs(i - j) }.sum().also(::println)
    val problem2Solution = leftSorted.map { left -> left * rightSorted.count { left == it } }.sum().also(::println)
}
