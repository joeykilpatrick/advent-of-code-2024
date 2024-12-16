import re
from typing import Literal

lines: list[tuple[int, list[int]]] = [(5519591, [5, 519, 507, 83]), (28956735990, [2, 892, 65, 427, 3, 389]), (1325281, [995, 826, 828, 5, 7, 8, 1]), (215986656838, [545, 8, 9, 604, 20, 82]), (5790512, [8, 7, 16, 10, 91, 776]), (12246166, [2, 41, 72, 4, 30, 3, 722, 23]), (22104, [35, 604, 8, 1, 431, 520, 4]), (4337, [471, 53, 7, 8, 91]), (23499, [6, 1, 434, 7, 9]), (1645, [4, 1, 41, 5]), (28073866, [97, 562, 426, 4, 6, 3, 4]), (24060520, [74, 9, 47, 994, 745]), (126073415065, [44, 343, 917, 4, 8, 325, 62]), (69660488, [4, 9, 9, 3, 178, 5, 9, 2, 1, 953, 8]), (1223011, [3, 24, 8, 8, 62, 535]), (5573, [8, 3, 73, 959, 5]), (27461, [817, 7, 8, 33, 5]), (5900161307, [3, 5, 9, 2, 5, 3, 5, 62, 317, 4, 5, 8]), (2355395016051, [18, 56, 60, 79, 68, 780, 50]), (2513, [31, 3, 24, 760, 937]), (31624064, [2, 7, 2, 8, 1, 6, 23, 9, 3, 7, 4, 330]), (58896, [25, 5, 6, 545, 1, 8, 5, 16, 8, 9]), (128590289, [1, 164, 5, 18, 9, 3, 4, 6, 7, 947]), (2871206, [61, 18, 8, 649, 7, 30]), (73566917554, [8, 9, 4, 1, 175, 8, 4, 1, 9, 9, 15, 5]), (370800954, [8, 5, 1, 6, 8, 5, 515, 5, 62, 5, 8, 3]), (1960301, [20, 98, 301]), (526194, [8, 2, 4, 9, 3, 48, 7, 499, 92, 62]), (627726, [51, 6, 4, 2, 512, 5, 9]), (191124, [41, 96, 465, 3, 9]), (10619771820, [17, 30, 659, 518, 61]), (25179752, [313, 563, 552, 674, 52]), (11538986, [758, 869, 5, 709, 9]), (12830, [4, 6, 3, 981, 77]), (441251, [36, 1, 67, 7, 2, 18, 8, 538, 9]), (54315289, [5, 4, 3, 15, 287]), (338960, [89, 2, 4, 95]), (158412, [892, 992, 84, 152, 4]), (28014, [244, 1, 422, 6, 7]), (29554544831, [8, 3, 6, 21, 4, 3, 7, 873, 3, 3, 4, 3]), (11380, [6, 5, 278, 97, 7]), (32031558622, [344, 65, 89, 927, 625]), (212527, [6, 7, 52, 7, 97]), (1078, [6, 435, 1, 3, 92, 1, 1, 534, 8]), (754520868243, [16, 933, 702, 4, 9, 9, 30, 8, 2]), (1254803, [3, 8, 87, 480, 1]), (773455, [865, 894, 9, 6, 130]), (23107, [1, 4, 612, 41, 35, 20, 5, 87]), (2991431762, [2, 21, 73, 4, 7, 395, 7]), (256540285, [1, 2, 89, 27, 96, 6, 3, 2, 4, 891]), (1452, [8, 76, 7, 7, 859]), (36388852503, [357, 4, 1, 75, 2, 917, 74]), (4128752290, [1, 8, 8, 9, 730, 3, 665, 7, 7, 1, 5]), (3157473, [837, 92, 41, 304, 5]), (13981017, [5, 7, 9, 38, 430, 3]), (23557, [56, 4, 2, 1, 4, 2, 35, 1, 540, 5]), (248796641, [799, 25, 6, 47, 3, 66, 41]), (827904, [168, 8, 69, 13, 9, 767, 3, 64]), (27510852, [93, 8, 14, 789, 46]), (12384921612, [2, 9, 733, 6, 6, 128, 4, 5, 1, 7, 7]), (237713, [9, 7, 753, 5, 515, 3]), (6587, [565, 69, 19, 4, 53]), (576619, [6, 1, 7, 4, 9, 7, 7, 8, 564, 9, 4, 3]), (1298745, [4, 9, 622, 58, 9]), (378162, [242, 4, 9, 3, 8, 51]), (1505, [46, 2, 159, 3, 6, 5, 194, 4, 6, 1]), (107473, [20, 831, 663, 5, 3]), (81684867, [97, 8, 43, 4, 612, 4]), (47178110770, [306, 4, 14, 549, 702]), (100117140, [7, 4, 6, 6, 49, 6, 7, 444, 3, 5, 3]), (3380, [32, 26, 4, 52]), (4726568035, [96, 87, 9, 6, 3, 2, 2, 524]), (8987292, [8, 98, 668, 1, 613]), (86334943, [72, 3, 510, 24, 7, 4, 77, 43]), (13370067, [21, 74, 5, 5, 280, 5, 63]), (88921, [7, 6, 9, 760, 1]), (1895974, [3, 38, 8, 690, 28, 9, 56, 542]), (24263192304, [834, 3, 18, 6, 9, 7, 9, 72, 831]), (2922, [471, 6, 96]), (185244, [79, 2, 44, 917, 7, 3]), (40495, [9, 75, 3, 1, 1, 2, 6, 6, 9, 44, 5, 98]), (973328874083, [4, 84, 6, 7, 55, 7, 59, 5, 1, 7, 1, 5]), (60138299, [859, 5, 587, 6, 14]), (4339949, [6, 76, 7, 840, 9, 509]), (50541486, [67, 154, 5, 72, 68, 78]), (316803, [2, 732, 91, 6, 64]), (2691051, [1, 8, 15, 3, 9, 9, 9, 6, 6, 5, 861]), (30256, [678, 4, 1, 4, 546, 9, 51, 739]), (919800, [8, 76, 5, 30, 7]), (68711312621, [62, 774, 59, 33, 2, 2, 821, 2]), (4515217, [2, 4, 5, 7, 88, 9, 9, 303, 1, 4, 2, 8]), (4703754244, [502, 7, 3, 8, 8, 2, 8, 636, 9, 5]), (129956751, [7, 8, 7, 74, 774, 14, 9, 67]), (16340, [223, 477, 1, 22, 137, 19]), (4251139896, [900, 9, 71, 7, 88, 1, 57, 12]), (745312, [273, 3, 6, 153, 412, 4]), (100956094, [5, 1, 4, 83, 4, 940, 91]), (910396349, [2, 926, 4, 98, 563, 4, 8, 1, 51]), (2939300, [32, 8, 533, 86, 6, 884, 5]), (685751560, [30, 61, 4, 1, 4, 6, 249, 2, 7, 73]), (15819, [33, 6, 5, 9, 698]), (153737, [36, 102, 557, 2, 5]), (1387818, [3, 38, 37, 74, 1, 5, 26, 8]), (2155979, [2, 9, 348, 3, 3, 60]), (1571275328, [8, 934, 337, 5, 2, 39, 2, 68, 4]), (12350, [5, 1, 40, 200, 9, 8, 9, 3, 5, 1, 6, 2]), (622667659, [7, 4, 1, 27, 2, 69, 9, 32, 533]), (40606664, [9, 2, 3, 8, 7, 9, 274, 3, 920, 1, 7]), (5649620, [27, 6, 8, 618, 59, 92, 20]), (60076853, [1, 16, 8, 1, 6, 101, 2, 8, 13, 4]), (79488006, [11, 6, 2, 3, 3, 60, 2, 64, 75, 6]), (9108, [1, 2, 71, 7, 10, 8, 9]), (1863817523, [18, 631, 95, 621, 9, 6, 2, 1, 4]), (67239, [8, 33, 31, 17, 52, 263]), (1028, [78, 9, 922, 1, 19]), (274054982, [1, 82, 9, 278, 73, 616, 44, 3]), (181, [1, 3, 5, 80, 2]), (1066595, [7, 535, 7, 281, 481]), (630158, [2, 8, 1, 93, 8, 2, 697, 8, 4, 2, 5, 1]), (3991680, [962, 520, 8, 19, 5, 7, 48]), (147949279, [38, 933, 23, 79, 38]), (1147610, [3, 60, 4, 506, 9]), (371568, [180, 16, 16, 200, 166, 8]), (800016, [122, 91, 9, 1, 58, 16, 8, 7, 65]), (3160509357680, [658, 3, 6, 7, 9, 4, 495, 8, 6, 7, 6]), (2410331, [246, 221, 67, 4, 6, 1, 4, 77]), (7817155, [1, 8, 9, 68, 8, 5, 9, 63, 84, 509]), (2006, [4, 2, 958, 2, 3, 8, 7, 8, 9, 1, 39]), (1339, [21, 56, 89, 14, 59, 1]), (9063630, [65, 9, 9, 9, 8, 9, 2, 6, 7, 3, 534]), (3330, [2, 6, 24, 3, 3, 39, 4, 46, 9]), (932307723900, [6, 349, 9, 9, 5, 7, 206, 762, 9]), (41750571, [95, 8, 1, 3, 739, 528, 27]), (2908430208, [69, 35, 29, 7, 413, 34, 5]), (2807296, [9, 2, 5, 2, 7, 122, 7, 58, 894, 4]), (53960, [45, 18, 3, 810, 500]), (179460814, [259, 949, 45, 730, 532]), (2012449, [821, 70, 7, 5, 999]), (7380, [1, 3, 53, 1, 54, 89, 5, 36]), (13806768942, [4, 455, 8, 4, 94, 4, 890, 4, 3]), (159498192878, [4, 8, 79, 5, 8, 8, 9, 5, 168, 8, 7, 5]), (4348960, [703, 1, 3, 8, 770]), (5144470, [5, 56, 2, 918, 2]), (1164340401, [489, 65, 369, 78, 81, 21]), (6069, [5, 5, 7, 71, 3, 2, 5, 9]), (9542723, [899, 55, 26, 87, 4, 1, 22, 8]), (756, [1, 3, 46, 502, 86, 30]), (34799567, [915, 551, 1, 227, 1, 38]), (3065, [86, 11, 208, 1, 3]), (1697600540666, [9, 612, 6, 438, 866, 7, 72]), (23773629, [265, 29, 94, 74, 9, 1, 2, 46, 1]), (91798, [56, 3, 541, 908, 2]), (14604283, [3, 5, 94, 7, 290, 3, 22, 4, 459]), (45711, [50, 1, 1, 811, 52, 887]), (607674, [80, 94, 8, 607, 1]), (99417258019, [919, 51, 4, 4, 632, 839, 3]), (52756760160, [8, 9, 7, 723, 8, 7, 8, 3, 65, 393]), (1980, [18, 78, 65, 4, 12]), (862019, [4, 789, 7, 673, 8, 93, 9]), (907, [7, 3, 12, 7, 3, 412, 62, 45, 7]), (115585749, [53, 5, 930, 469, 606, 94]), (18374200, [44, 1, 871, 922, 41, 9, 1, 6, 4]), (2242172492626, [2, 68, 43, 86, 98, 75, 195]), (197279955, [4, 4, 27, 836, 59, 343, 3, 6, 8]), (930902, [623, 249, 2, 5, 7, 7, 6, 5, 2, 7]), (4698849, [7, 7, 5, 293, 39, 4, 4, 970, 1, 6]), (21723147, [99, 424, 618, 4, 51]), (132572531, [9, 6, 56, 411, 2, 9, 3, 4, 4, 1, 5, 6]), (339300, [67, 5, 5, 7, 6, 4, 450, 2]), (2898079, [72, 446, 6, 8, 5]), (2153061, [6, 264, 886, 9, 9]), (200775886, [741, 613, 4, 2, 5, 442, 38]), (724813338900, [22, 2, 89, 281, 50, 373, 7, 1]), (145095, [968, 107, 537, 95, 85]), (727712, [70, 662, 994, 52, 38, 4, 10]), (1684807, [16, 399, 6, 53, 577, 9, 60, 7]), (6779948, [7, 4, 261, 7, 496, 14, 62]), (45390, [93, 1, 98, 236, 314]), (14424060, [97, 466, 6, 61, 70]), (2173881554259, [21, 6, 6, 7, 88, 15, 47, 7, 259]), (577634740, [4, 843, 8, 60, 86, 294, 1, 4, 4]), (378375346801, [965, 9, 7, 6, 22, 56, 4, 495, 4]), (18109, [5, 92, 9, 7, 37, 339, 158]), (1975586, [377, 655, 5, 8, 8]), (19693, [74, 2, 37, 7, 9]), (43607606, [363, 2, 6, 3, 43, 7, 1, 1, 89, 3]), (22050876298, [3, 6, 875, 3, 4, 5, 7, 5, 1, 2, 5, 95]), (337314, [2, 1, 479, 2, 11, 8, 2, 87, 8, 3]), (2363943613, [3, 981, 4, 1, 3, 2, 7, 6, 3, 6, 1, 12]), (5842, [5, 13, 371, 15, 7]), (23135, [4, 759, 161, 7, 700, 47, 9]), (467865094, [951, 7, 8, 18, 7, 7, 4, 6, 3, 4, 7, 4]), (45711, [1, 1, 98, 4, 57, 11]), (135039537, [6, 501, 3, 6, 9, 7, 4, 1, 1, 89, 5, 3]), (53, [2, 6, 6, 35]), (650628, [6, 336, 976, 9, 2, 2, 2, 722, 6]), (14904862797, [343, 43, 434, 1, 798]), (867405597, [2, 57, 75, 679, 45, 41]), (329361694290, [2, 40, 77, 4, 246, 77, 48, 42]), (29996016, [71, 419, 7, 6, 6]), (1333863920, [8, 1, 938, 94, 26, 150, 18]), (118288866195, [76, 6, 143, 2, 8, 2, 73, 55, 9]), (7804, [7, 7, 3, 282, 636, 1, 8, 7, 23, 6]), (16913736, [19, 684, 8, 9, 39, 24]), (18713, [1, 408, 4, 43, 1, 1, 9, 6, 937]), (698194699, [7, 3, 45, 41, 5, 53, 144, 68, 7]), (2925659071123, [9, 60, 658, 5, 493, 8, 1, 7, 75]), (13510, [4, 9, 825, 74, 5, 8, 972, 9, 7, 7]), (19361994, [22, 698, 853, 21, 1, 575]), (13842114, [64, 6, 6, 1, 4, 49, 254, 5, 3, 6]), (10076, [1, 9, 3, 814, 9]), (3552628, [5, 9, 3, 2, 1, 3, 4, 63, 1, 9, 390, 5]), (31840715, [5, 788, 4, 77, 1, 98, 5, 16]), (135518349, [43, 9, 5, 955, 362, 4, 9, 7, 2, 7]), (94428, [967, 16, 96, 18, 56, 96, 6]), (1038, [29, 8, 2, 6, 1, 4, 1, 2, 8, 23, 45]), (3654147, [875, 8, 791, 5, 6, 67, 5, 78, 3]), (4275796229, [3, 769, 3, 526, 391, 9, 89]), (27000300819, [9, 808, 52, 5, 80, 31, 456, 6]), (30068648, [8, 9, 286, 78, 507, 41, 34, 4]), (294, [6, 7, 3, 33, 6]), (40795, [720, 84, 5, 29, 5, 191, 108]), (4221173, [586, 440, 692, 9, 91, 3, 47]), (63993713, [7, 272, 88, 87, 26]), (32806221, [457, 8, 5, 309, 29]), (18964414056, [510, 6, 15, 868, 6, 476]), (1979553, [7, 1, 569, 7, 7]), (2861695216, [808, 35, 336, 951, 1, 5, 99]), (231316, [8, 8, 6, 358, 48]), (86832537664, [93, 4, 60, 47, 620, 8, 1, 64]), (480653021, [4, 4, 452, 8, 25, 47, 292]), (8834532, [77, 455, 6, 1, 6, 3, 126, 6, 1, 7]), (126249, [215, 2, 4, 2, 285, 279]), (372359, [72, 6, 1, 2, 856]), (3254581, [84, 54, 630, 63, 1]), (379877325214, [8, 793, 9, 4, 8, 874, 6, 3, 5, 1, 5]), (438602095839, [712, 44, 7, 21, 7, 919, 2, 1]), (172277, [1, 692, 449, 5, 30, 5, 6, 77]), (1937000778, [8, 4, 3, 58, 2, 497, 52, 379]), (88823331, [295, 97, 7, 7, 3, 274, 7, 25, 7]), (856, [82, 297, 41, 8, 2]), (2504394, [6, 25, 14, 1, 601, 927, 567]), (43915781, [3, 825, 598, 53, 87]), (238361376, [4, 7, 836, 5, 1, 54, 5, 6, 2, 4, 2, 6]), (70020309511, [9, 2, 6, 4, 17, 733, 7, 473, 3]), (11333, [8, 96, 6, 2, 4, 2, 1, 9, 267, 89, 7]), (627423053070, [6, 2, 742, 305, 305, 2, 2]), (16010822, [6, 45, 473, 873, 5, 7, 2]), (5892, [75, 2, 825, 6, 42]), (711323, [74, 120, 8, 9, 911]), (1862712, [3, 8, 7, 7, 712]), (292796134, [6, 405, 71, 98, 61, 36]), (20038729465, [7, 93, 193, 4, 2, 5, 8, 7, 6, 5, 88]), (2344529, [9, 4, 8, 45, 8, 8, 629, 3, 1, 5, 2, 7]), (5355721, [783, 76, 9, 1, 3]), (10864450, [1, 39, 3, 5, 8, 8, 6, 83, 5, 1, 5, 3]), (1093, [62, 4, 3, 839, 3]), (27635370, [73, 530, 3, 3, 9, 714]), (666460, [7, 84, 823, 504, 470]), (127648, [15, 7, 7, 34, 9, 28, 8, 57, 6, 9, 8]), (181400, [16, 4, 10, 907]), (161606466, [24, 6, 671, 7, 979, 2]), (202782, [119, 4, 426, 6]), (1694080921, [8, 8, 70, 45, 9, 4, 2, 2, 9, 63, 7, 4]), (81910892, [799, 4, 34, 98, 7, 3, 174, 2, 1]), (55013437585, [623, 2, 415, 3, 707, 85]), (1123418796378, [5, 944, 7, 1, 9, 321, 2, 4, 2, 3]), (6020, [8, 644, 1, 779, 1, 87]), (400960, [9, 78, 14, 70, 8]), (727775823, [627, 921, 4, 584, 8, 47]), (21038643, [487, 72, 4, 1, 6]), (7449633, [964, 173, 468, 14, 9]), (16479831, [16, 47, 906, 77, 1]), (7846395, [7, 839, 6, 791, 607]), (41564174, [512, 820, 99, 13, 1]), (711807, [8, 650, 20, 797, 51]), (11304320, [2, 38, 2, 883, 11, 8, 1, 1, 7, 5, 4]), (1419060, [2, 3, 62, 2, 5, 6, 30, 3, 6, 3, 2, 3]), (24427890, [244, 271, 3, 76, 1]), (5658391, [9, 5, 4, 3, 8, 3, 444, 9, 4, 29, 22]), (35105871, [47, 1, 1, 85, 2, 36, 63]), (2645669, [70, 459, 1, 5, 96, 71]), (15210, [88, 6, 6, 95, 26, 3]), (8344859689595, [79, 22, 5, 6, 746, 8, 9, 593]), (3202, [8, 40, 2, 5, 2]), (13358, [7, 5, 104, 37, 4, 5, 7, 8, 371, 2]), (266718315450, [77, 31, 3, 4, 5, 3, 6, 315, 447]), (109361, [7, 919, 17]), (2970708941, [9, 1, 2, 258, 46, 7, 12, 7, 8]), (1016785964, [6, 5, 5, 1, 7, 8, 1, 55, 5, 591, 9, 8]), (1413126, [5, 1, 9, 40, 9, 3, 438, 3, 366]), (2085802307, [4, 8, 80, 46, 2, 9, 6, 5, 8, 3, 41]), (29808003, [99, 651, 4, 12, 828]), (30895, [95, 16, 780, 3, 7]), (21223121432, [8, 85, 6, 5, 2, 34, 9, 449, 7, 2, 1]), (825, [71, 10, 8, 67, 9, 31]), (3406646952, [336, 73, 393, 46, 1, 955]), (1011032, [863, 297, 871, 274, 398]), (3524400, [1, 36, 96, 62, 1, 51, 4, 1, 1, 4]), (80133640, [874, 9, 830, 97, 95]), (846826, [962, 3, 88]), (1564420, [9, 2, 1, 2, 124, 4, 7, 7, 1, 70, 5, 5]), (49744927008, [71, 804, 94, 21, 7, 864]), (4631, [52, 6, 1, 9, 69, 4, 4]), (27661378, [9, 212, 3, 7, 246, 77]), (1680246000, [3, 8, 486, 51, 76, 17, 50]), (46167, [9, 43, 877, 5, 558]), (6201770848, [33, 6, 2, 8, 161, 8, 56, 532]), (6454922355, [7, 4, 26, 5, 574, 7, 3, 6, 85, 7]), (62980477, [1, 64, 8, 3, 28, 80, 2]), (107372, [44, 9, 720, 806, 68]), (96006860, [9, 52, 6, 9, 10, 780, 906, 1, 2]), (948697045840, [1, 4, 7, 435, 686, 7, 268, 8, 5]), (563, [284, 35, 3, 28, 213]), (12928, [4, 97, 8, 16]), (329798034, [7, 726, 8, 76, 9, 740, 3, 1, 2, 9]), (74670, [202, 532, 6, 46, 95]), (12034380, [426, 75, 282, 30, 1]), (342406752, [631, 476, 8, 38, 3]), (10138676600, [83, 89, 5, 24, 3, 5, 65, 844]), (1022028, [84, 8, 21, 529]), (416304, [88, 3, 7, 75, 4, 59, 7, 14, 2, 9]), (2774595639437, [823, 315, 7, 148, 2, 337]), (2148988844616, [4, 8, 5, 7, 8, 2, 791, 553, 4, 7, 8]), (2250, [6, 49, 5, 53, 45, 345, 1, 337]), (5269, [1, 5, 3, 470, 11]), (73229, [78, 27, 80, 3, 38, 36, 9, 5]), (13574623594676, [8, 7, 56, 3, 2, 794, 8, 7, 467, 6]), (106251012, [938, 261, 31, 7, 2]), (784816457, [4, 3, 1, 60, 18, 7, 9, 403, 52]), (13383525449, [980, 1, 19, 9, 718, 772, 4, 8]), (292001, [62, 63, 3, 79, 73, 2, 875]), (125287360801, [380, 894, 8, 351, 6, 70, 40]), (15127, [3, 8, 3, 1, 6, 180, 7]), (44353646423, [4, 9, 4, 6, 22, 1, 92, 4, 84, 21]), (5833152, [62, 1, 21, 3, 59, 6, 98, 636, 4]), (553067, [506, 63, 972]), (290877960, [399, 81, 7, 7, 3, 9]), (433778524, [8, 189, 8, 800, 184, 86, 7, 4]), (296454440, [2, 8, 34, 4, 9, 2, 8, 2, 799, 5, 8, 6]), (91725, [9, 5, 476, 387, 2]), (92146, [9, 59, 2, 9, 4, 85, 771]), (1492682688, [59, 2, 102, 4, 476, 126]), (3084446, [4, 997, 92, 34, 83]), (7622, [66, 1, 97, 5, 33, 4]), (215355056, [6, 4, 6, 763, 5, 7, 4, 9, 63, 7, 7, 8]), (168794720, [6, 7, 6, 16, 3, 84, 62, 3, 223]), (121689166, [13, 26, 36, 91, 68]), (91225324921, [967, 3, 482, 11, 7, 94, 1]), (830209, [824, 5, 58, 2, 54, 7, 2]), (20163886648, [63, 2, 8, 1, 94, 33, 25, 2]), (7933698360, [5, 66, 46, 640, 251, 37, 9, 6]), (508248224, [8, 6, 7, 6, 7, 2, 2, 724, 2, 1, 2, 5]), (89733028, [48, 58, 46, 77, 239]), (5389174, [9, 356, 24, 5, 6, 4]), (507718477, [76, 167, 962, 8, 5]), (630799797, [5, 3, 34, 5, 7, 7, 7, 920, 97]), (461, [34, 280, 67, 71, 9]), (280919, [626, 14, 3, 4, 1, 1, 44, 8, 3, 4]), (1353584, [75, 373, 12, 8, 74, 248]), (649358, [69, 694, 85, 6, 802]), (24876, [9, 99, 76, 4, 1, 258, 25, 1]), (178750207, [245, 5, 11, 65, 204]), (114912876, [496, 6, 41, 7, 38, 8, 7, 5]), (96257, [6, 101, 1, 99, 9, 29]), (56213476, [147, 759, 669, 62, 1]), (2661, [693, 3, 6, 2, 542, 2, 17, 7, 1, 6]), (103154, [8, 8, 7, 921, 2]), (6028186, [4, 8, 8, 3, 88, 1, 59, 10, 9, 3, 4]), (95997975, [6, 45, 252, 575, 551]), (107237524, [177, 525, 30, 67, 76, 4]), (3595482764997, [6, 7, 150, 7, 2, 5, 200, 651, 3]), (3609, [433, 6, 865, 33, 16, 88, 9]), (1272075, [5, 8, 5, 613, 4, 3, 430, 7, 7, 75]), (189587, [465, 4, 9, 101, 8, 19, 791]), (6959258, [62, 5, 2, 48, 20, 92, 43, 8, 1, 4]), (86882, [23, 707, 356, 1, 80, 2]), (504405, [7, 5, 424, 7, 99]), (29210245, [44, 6, 2, 583, 46, 159, 86]), (124, [74, 1, 45, 5]), (1378125, [25, 735, 5, 5, 3]), (75346803, [7, 534, 680, 4]), (2781, [58, 41, 396, 7]), (412895142, [9, 1, 830, 81, 6, 2, 6, 7, 1, 3, 7, 7]), (1081, [6, 13, 9, 6, 13, 23]), (18500261, [50, 370, 262]), (1780893, [2, 48, 53, 175, 2, 93]), (29838, [11, 455, 21, 6, 41, 49, 64, 3]), (142472446, [11, 7, 97, 60, 116, 7, 89, 2]), (169187301, [26, 4, 4, 7, 8, 61, 2, 6, 8, 33, 70]), (7110, [5, 750, 597, 752, 8]), (454105638, [5, 5, 60, 204, 4, 3, 6, 1, 4, 4, 7, 1]), (8217, [3, 96, 83]), (2906167, [783, 4, 9, 646, 376, 61, 2]), (762266120, [7, 869, 473, 385, 302]), (85522, [311, 5, 507, 579, 61]), (683252112, [448, 8, 13, 3, 1, 6, 8, 2, 76, 4, 3]), (49942771271, [5, 8, 160, 9, 9, 2, 6, 6, 8, 56, 7, 4]), (1444, [14, 1, 2, 7, 25]), (669379, [2, 6, 94, 80, 9, 96, 832, 9, 67]), (13747499, [16, 7, 122, 83, 499]), (185531580, [3, 9, 71, 2, 8, 1, 4, 236, 7, 4, 57]), (98048, [4, 5, 95, 592, 8, 77, 64]), (3295, [4, 45, 20, 4, 6, 8, 130, 83, 5]), (851, [98, 5, 2, 557, 79, 89, 6, 6, 8, 1]), (143047813, [9, 5, 2, 893, 9, 1, 6, 7, 800, 15]), (384539472, [61, 2, 244, 80, 628]), (58055477921, [1, 29, 45, 54, 77, 891, 31]), (1364527645346, [7, 1, 51, 765, 2, 144, 9, 89]), (5031849600, [7, 1, 7, 9, 79, 4, 9, 5, 719, 9, 30]), (6512780, [2, 4, 5, 7, 5, 1, 73, 7, 3, 59, 419]), (48259, [19, 14, 643, 53, 82]), (1028931, [6, 4, 2, 1, 8, 7, 8, 3, 4, 80, 3, 33]), (2749379, [4, 91, 1, 13, 286, 63]), (26318038, [39, 900, 920, 28, 280]), (40839, [81, 9, 56, 14]), (7053223716, [717, 1, 7, 68, 198, 999, 7]), (18523493, [43, 49, 4, 8, 933, 9, 8, 7, 4, 6, 7]), (3750600, [48, 529, 88, 6, 940]), (21335428, [1, 1, 581, 9, 6, 8, 1, 91, 5, 3, 9, 3]), (4493352293, [6, 401, 18, 7, 5, 222, 5, 71]), (186905142723, [948, 4, 904, 94, 4, 545, 4]), (621138001, [3, 66, 80, 175, 643]), (565395559745, [503, 2, 53, 53, 98, 5, 8, 54, 5]), (32847, [8, 813, 5, 3, 82, 242]), (30196320, [9, 8, 788, 77, 57, 8]), (152458, [35, 484, 9]), (70700386182, [70, 700, 386, 1, 83]), (20558416, [4, 5, 51, 603, 1, 71, 951, 8]), (2897704683, [9, 97, 555, 51, 65, 92, 3]), (209386456, [7, 8, 4, 80, 21, 2, 520, 4, 33, 5]), (9418680019, [49, 27, 90, 34, 45, 9, 1, 9]), (21317877, [2, 28, 65, 3, 70, 48, 82, 13, 9]), (1938252527, [9, 3, 47, 2, 51, 41, 9, 5, 5, 2, 7]), (18674771882162, [8, 95, 7, 71, 8, 8, 71, 1, 8, 95, 6]), (758504479, [956, 894, 41, 4, 479]), (19059626, [3, 1, 410, 75, 9, 3, 603, 4, 6, 2]), (16018704000, [8, 2, 67, 23, 559, 8, 90, 398]), (151551, [4, 92, 225, 7, 351]), (234268265, [503, 863, 546, 539]), (78902565, [788, 1, 8, 5, 7, 4, 9, 3, 61, 9, 4]), (98612508, [54, 8, 1, 9, 7, 255, 9, 80, 7, 4, 2]), (199520175, [95, 21, 20, 1, 175]), (2556045, [18, 4, 968, 4, 4, 1, 5, 6, 15]), (1241391, [5, 4, 4, 40, 22, 849, 54, 99]), (42262704, [836, 936, 98, 48, 9, 6, 6]), (89345960, [3, 27, 282, 6, 4, 7, 7, 5, 5, 11, 8]), (207762, [768, 88, 867, 798, 3, 15]), (2511007008, [7, 6, 8, 551, 829, 9]), (5482195314, [3, 2, 47, 3, 9, 6, 9, 1, 6, 6, 57, 2]), (70862887, [20, 401, 9, 7, 95, 134, 88, 8]), (534619683, [6, 27, 17, 1, 201, 83]), (714, [8, 202, 437, 11, 56]), (49433449443, [802, 77, 37, 8, 118, 8, 6]), (4740120, [8, 8, 8, 764, 945, 6]), (2536147, [17, 8, 8, 983, 8]), (887132209824, [7, 268, 9, 9, 10, 31, 7, 84, 8]), (1376218876, [40, 3, 32, 218, 876]), (18454, [28, 1, 156, 5, 7]), (1636973792, [54, 580, 8, 508, 5, 8, 652, 2]), (2344547, [72, 7, 33, 97, 9, 5, 68, 474, 1]), (908676471, [874, 1, 99, 47, 1, 1, 5, 3, 7, 65]), (7762090140, [2, 1, 1, 5, 2, 37, 9, 437, 889, 6]), (61432588, [614, 320, 23, 508, 60]), (53530946876, [8, 884, 1, 8, 23, 6, 8, 8, 62, 3, 8]), (26409153, [934, 5, 3, 725, 932, 8, 1]), (97928, [668, 1, 4, 6, 1, 5, 6, 3, 89, 2, 8]), (313608, [6, 27, 5, 70, 38]), (17584, [586, 6, 5, 4]), (4179168, [2, 6, 6, 533, 7, 5, 7, 14, 4, 2, 6, 8]), (780098, [956, 51, 8, 1, 2]), (1042152, [8, 58, 6, 4, 3, 6, 3, 2, 5, 6, 251, 3]), (4095, [454, 9, 9]), (676961, [88, 8, 4, 1, 3, 6, 8, 4, 5, 2, 45, 94]), (247, [170, 2, 9, 2, 64]), (1646563114, [342, 662, 164, 3, 111]), (515, [22, 9, 5, 358, 2]), (1020767, [40, 567, 166, 630, 684, 7]), (67964144157, [1, 94, 767, 39, 259, 71]), (63739407, [8, 9, 7, 4, 63, 73, 9, 405, 2]), (80798, [7, 1, 10, 793, 5]), (3930150903, [4, 6, 788, 985, 16, 1, 5, 5, 1]), (55839, [73, 609, 481, 6, 8, 3, 12]), (3563566284, [197, 969, 5, 61, 3, 18, 84]), (170825200, [20, 6, 50, 65, 91, 95, 4]), (4598487, [66, 3, 59, 527, 308, 176]), (15936873526343, [159, 368, 735, 26, 343]), (397706, [3, 795, 978, 40, 3, 73, 2]), (15285950, [12, 38, 153, 753, 50]), (29839083031171, [9, 472, 724, 7, 7, 1, 8, 7, 45]), (88990234792, [5, 295, 7, 6, 2, 3, 7, 6, 3, 4, 7, 92]), (45606901, [8, 6, 9, 918, 115, 59, 601, 1]), (27411, [4, 854, 8, 83, 1]), (56660523, [49, 990, 584, 421, 2, 1]), (1381, [1, 125, 5, 754]), (3067442856838, [9, 1, 2, 583, 817, 2, 40, 7, 3, 8]), (18740, [620, 9, 3, 105, 8]), (18027, [299, 34, 6, 924, 6, 486, 7, 2]), (6351729615, [5, 9, 5, 6, 69, 3, 735, 3, 53, 99]), (94392, [943, 56, 2, 34]), (50028, [397, 13, 4, 9, 5, 77, 3, 13, 6]), (13390, [6, 247, 9, 3, 49]), (86048760, [96, 668, 3, 984, 445]), (9933, [5, 31, 63, 81, 87]), (45333, [63, 709, 6, 655, 5]), (331212, [786, 97, 5, 75, 87]), (60619, [1, 59, 621]), (95442295, [5, 4, 3, 2, 1, 4, 25, 74, 7, 6, 789]), (33955194, [689, 80, 88, 6, 119, 6, 51, 7]), (30250, [56, 540, 4, 6]), (534055, [58, 92, 4, 44, 12]), (614803, [7, 68, 5, 8, 3]), (203, [5, 8, 3, 5, 8]), (608, [7, 25, 19]), (72724, [63, 9, 1, 4, 5, 579]), (3242, [1, 473, 64, 6, 14]), (1681195, [2, 357, 65, 230, 452, 7, 2]), (56702639, [6, 204, 1, 8, 4, 4, 9, 713, 6, 3, 6]), (14535443156, [31, 25, 55, 9, 33, 341]), (27540, [696, 834, 6, 3]), (29021, [76, 38, 6, 3, 78]), (14633715049466, [2, 423, 9, 581, 9, 827, 67, 4]), (1243446865212, [6, 548, 4, 354, 149, 6, 9, 3, 4]), (8610630, [2, 39, 28, 817, 7, 626]), (29061, [134, 2, 21, 63, 817]), (1480320, [4, 2, 992, 19, 5, 6, 1, 6, 4, 15, 4]), (12917, [44, 400, 763, 84, 5]), (1188189365, [4, 757, 545, 1, 1, 2, 6, 4, 6, 5, 5]), (52099102, [8, 65, 990, 92, 7]), (46660096, [66, 189, 6, 3, 536, 4, 896]), (947, [7, 6, 871]), (9486280, [1, 3, 4, 53, 5, 1, 6, 6, 6, 47, 9, 5]), (74818884989, [8, 795, 2, 9, 7, 2, 7, 588, 9, 88]), (333527, [416, 8, 3, 69, 5]), (8945258, [580, 21, 1, 6, 734]), (1788675, [81, 17, 411, 634, 40]), (2672640, [84, 96, 10, 273, 3, 1, 1, 8, 40]), (652, [49, 9, 5, 45, 544]), (3191827755715, [8, 39, 7, 180, 2, 7, 7, 557, 13]), (10540843, [53, 71, 85, 843]), (14155842, [3, 768, 8, 384, 33, 2]), (2735067512148, [74, 462, 3, 439, 8, 148]), (84756, [8, 82, 8, 801, 5, 14]), (118727856, [235, 26, 9, 117, 2, 9, 24]), (360307808, [14, 93, 586, 390, 2, 472]), (31277443, [89, 183, 3, 8, 240, 8, 635]), (820894, [40, 40, 45, 228, 91]), (16111, [19, 60, 1, 88, 366, 7, 8, 93]), (92, [8, 3, 81]), (309014526, [2, 1, 76, 10, 26, 74, 4, 3, 8, 4, 4]), (45075188, [86, 7, 14, 3, 4, 1, 6, 75, 67, 79]), (1790745, [6, 2, 1, 3, 1, 721, 2, 3, 108, 55]), (794286, [99, 285, 8, 8]), (661986, [72, 84, 266, 700, 59, 8]), (17768, [4, 148, 2, 3]), (33778794, [2, 7, 8, 59, 272, 3, 5, 960, 14]), (2248580, [910, 4, 8, 7, 6, 88, 865, 7, 5, 7]), (270271440, [5, 9, 5, 8, 3, 5, 3, 229, 9, 9, 3, 12]), (13263717644, [58, 428, 54, 7, 6, 54, 47]), (2562, [5, 36, 7, 76, 4, 86]), (20, [8, 6, 6]), (3837431080, [9, 70, 7, 820, 742]), (3687032250, [4, 758, 85, 75, 759]), (13323699614, [8, 3, 82, 298, 4, 9, 9, 96, 1, 3, 1]), (7928, [72, 27, 8, 3, 7, 3, 638, 8, 9, 1, 7]), (1034, [1, 181, 1, 845, 7]), (1205704042, [844, 873, 51, 492, 435, 7]), (592553, [9, 583, 550]), (174496320, [429, 807, 8, 8, 8, 3, 7, 979, 9]), (2366, [2, 9, 5, 248, 7]), (1419, [19, 26, 253, 2, 823]), (5782415042, [7, 811, 8, 7, 414, 2, 7, 8, 5, 1, 3]), (286213096, [55, 2, 85, 18, 61]), (1399898, [828, 25, 9, 1, 7, 2, 4, 29, 3, 4, 3]), (30839454, [616, 789, 1, 5, 1]), (5910065520, [82, 970, 56, 66, 9, 19, 80]), (1434873348, [88, 61, 321, 11, 3, 41, 9]), (7228734, [7, 1, 22, 873, 4]), (34378948468, [2, 8, 649, 3, 4, 8, 6, 70, 9, 5, 71]), (2225626982, [91, 2, 46, 280, 527, 5, 85]), (9140039, [3, 6, 558, 13, 140, 1]), (3414064504, [2, 157, 8, 11, 70, 5, 90, 59, 4]), (2762, [30, 4, 23]), (70283778, [7, 100, 42, 241, 780]), (543851, [3, 51, 5, 2, 7, 568, 1, 251, 8]), (201181, [38, 961, 33, 979, 58, 20]), (165412, [75, 89, 934, 475, 4]), (631272, [116, 106, 80, 51, 96]), (448209370460, [10, 8, 584, 209, 9, 618, 3, 1]), (1789239, [4, 51, 559, 7, 335, 1, 4, 1]), (24958, [890, 4, 7, 38]), (127, [85, 8, 35]), (686, [5, 1, 9, 564, 77]), (20410187, [759, 4, 3, 262, 2, 7, 8, 2, 8]), (2109, [7, 5, 5, 5, 356]), (6180208128262, [933, 69, 4, 672, 24, 256, 4]), (2461489344, [8, 9, 7, 3, 665, 7, 6, 3, 3, 16, 36]), (29501756807, [3, 6, 4, 4, 66, 2, 1, 7, 70, 6, 80, 7]), (4462082487, [9, 1, 7, 504, 7, 8, 96, 248, 9]), (939853, [86, 78, 8, 1, 711, 4, 5, 5, 106]), (5633, [70, 3, 76, 8, 67, 10]), (23325120, [5, 8, 5, 7, 3, 1, 1, 6, 1, 60, 13, 8]), (3072887, [7, 9, 51, 39, 3, 392]), (86278491, [881, 3, 4, 244, 90]), (4589911933, [26, 51, 34, 6, 202, 84, 53, 8]), (839971111, [6, 3, 4, 13, 9, 4, 8, 9, 893, 2, 37]), (64720322, [7, 6, 82, 783, 1, 26, 1, 24, 26]), (4746755, [1, 53, 879, 18, 70, 66]), (41714392, [667, 6, 75, 7, 69, 58, 4, 37]), (217508398473, [5, 645, 4, 6, 3, 8, 602, 1, 2, 4]), (514996272, [917, 390, 2, 54, 7, 4, 36]), (6632640, [6, 3, 94, 980, 4]), (16425695, [34, 34, 337, 57, 715]), (209931480729, [252, 2, 72, 8, 4, 2, 562, 6, 3, 9]), (3369, [21, 68, 254, 2, 5]), (9821384, [2, 6, 923, 19, 8, 1, 35, 7, 6, 2, 8]), (1288, [51, 300, 937]), (29968431, [342, 162, 93, 54, 4, 5, 3]), (6965, [4, 7, 723, 4, 9]), (41070134, [73, 599, 873, 60, 10, 7, 5, 9]), (8599215, [8, 23, 1, 3, 290, 75, 98, 23, 7]), (1328427250, [7, 28, 8, 7, 1, 92, 3, 2, 4, 98, 7]), (147593, [6, 515, 56, 5, 624, 42, 215]), (5590, [72, 3, 974, 662, 6, 3, 16, 1]), (14096711201, [52, 555, 9, 49, 40, 745]), (1535364, [1, 152, 5, 3, 65]), (86037, [7, 661, 6, 888, 7, 4, 8, 3, 7, 3]), (206452579, [5, 2, 973, 7, 75, 3, 11, 59, 9]), (3339662, [4, 4, 54, 21, 285, 9, 1, 25, 5, 2]), (17689019, [176, 890, 20]), (16012647546, [20, 6, 3, 228, 20, 8, 8, 6, 259]), (9229940, [7, 4, 4, 3, 6, 1, 763, 83, 3, 38]), (177795087, [84, 12, 4, 2, 53, 416, 6, 9]), (12853, [86, 92, 8, 3, 3, 28, 9]), (429279, [8, 957, 8, 7, 538, 5]), (3566623752415, [2, 15, 259, 2, 3, 9, 2, 9, 9, 4, 18]), (93133040, [3, 124, 93, 728, 1]), (219282, [391, 177, 471, 4, 7, 6, 2, 4, 3]), (8771785, [437, 91, 1, 825, 206, 43, 5]), (1283, [1, 1, 468, 4, 5, 2, 788, 1, 7, 8]), (435585947, [58, 751, 528, 66, 7]), (490437076, [378, 3, 92, 4, 3, 70, 1, 4, 63, 2]), (14823800, [94, 83, 20, 19, 5]), (8771, [1, 987, 9, 9, 247, 7]), (4786834, [148, 321, 9, 6, 832]), (23909953914, [59, 774, 88, 479, 4]), (7731, [1, 3, 8, 927, 3, 59, 73, 9, 9, 7, 3]), (109969989, [4, 4, 516, 37, 4, 5, 6, 13, 6, 4, 3]), (7369091, [47, 663, 97, 107, 1]), (1596381609, [8, 651, 593, 483, 8, 6, 85, 9]), (15735841, [55, 14, 909, 2, 851, 11]), (2021, [47, 9, 10, 158, 9, 5]), (326292489, [6, 1, 1, 28, 9, 24, 7, 3, 88, 9, 8, 8]), (1744966, [4, 155, 27, 87, 31, 3, 4]), (9052512, [4, 7, 970, 674, 798]), (4455362430, [2, 9, 2, 2, 8, 5, 136, 2, 7, 9, 2]), (5822542, [5, 759, 63, 5, 43]), (3326630, [331, 6, 10, 56, 6, 7]), (69624, [32, 977, 69, 3]), (314075957, [7, 2, 5, 6, 294, 4, 4, 2, 7, 90, 4]), (236561952, [1, 984, 8, 5, 9, 660, 1, 9, 1, 6, 9]), (17080, [167, 7, 87, 676, 7]), (9612355, [37, 60, 9, 8, 539, 220, 687]), (24099328, [322, 55, 87, 20, 389, 16, 8]), (6233282992, [11, 893, 60, 661, 7, 4, 4]), (497193840209, [913, 12, 363, 15, 20, 9]), (959063380976, [3, 1, 9, 68, 77, 9, 36, 5, 8, 3, 2]), (6756, [48, 8, 46, 5, 5, 31, 759, 2, 1, 4]), (195643188, [91, 2, 701, 486, 507]), (1455717, [5, 53, 5, 4, 4, 812, 7, 1, 8, 604]), (2939031, [43, 751, 91, 349, 8, 11]), (338159036, [7, 8, 4, 9, 2, 3, 6, 51, 9, 59, 4, 1]), (57659, [7, 1, 1, 1, 5, 757, 2, 4, 29, 9, 81]), (2890, [77, 8, 17, 2]), (583, [1, 477, 2, 9, 95]), (18136774828, [6, 430, 82, 66, 3, 13, 94, 7]), (233, [4, 1, 41, 69]), (236520, [450, 3, 61, 460, 80]), (11911, [12, 9, 4, 7, 14]), (2577, [17, 1, 6, 835, 3]), (1801, [4, 2, 51, 64, 93, 9, 8]), (16268177163, [70, 42, 5, 77, 1, 7, 3, 64]), (738, [16, 2, 141, 4, 46]), (13811440268, [1, 7, 3, 2, 959, 5, 9, 8, 2, 4, 270]), (81913104, [987, 6, 76, 1, 2, 91]), (48236, [48, 2, 1, 3, 5]), (7476952, [46, 88, 9, 3, 62, 826]), (1676, [59, 6, 4, 660, 756]), (38591070, [7, 865, 654, 6, 755]), (15471432048, [837, 78, 966, 1, 739, 316]), (1134, [812, 66, 4, 252]), (99902, [29, 46, 74, 3, 6]), (890, [598, 289, 1, 1]), (83288449, [83, 28, 1, 84, 50]), (50952407, [5, 4, 78, 386, 408]), (576, [5, 60, 4, 507]), (46886622, [6, 823, 834, 381, 74]), (12161133149, [8, 8, 7, 5, 86, 321, 263]), (7523, [415, 18, 42, 7, 4]), (6301371594414, [600, 1, 3, 3, 5, 8, 1, 42, 7, 4, 1, 4]), (1535, [4, 29, 1, 17, 3, 6, 801, 144, 3]), (855785321, [161, 6, 8, 85, 87, 6, 9, 9]), (119486214, [4, 35, 63, 654, 46, 1, 9]), (150777, [4, 891, 7, 9, 989, 33]), (48, [1, 3, 9]), (1767766080, [95, 2, 576, 8, 6, 3, 5, 95, 3, 64]), (12328, [26, 1, 32, 7, 8, 15, 96, 4, 23]), (157182487, [9, 105, 9, 240, 17, 114, 77]), (40209272, [31, 30, 77, 1, 9, 8, 6, 8]), (126163008, [9, 4, 1, 9, 529, 3, 4, 4, 1, 54, 2, 3]), (82313, [6, 8, 50, 752, 4, 3, 5, 8, 6, 622]), (8194086412, [9, 8, 852, 51, 15, 189, 9, 5, 2]), (27897124818, [493, 79, 1, 826, 824, 59]), (142306, [50, 468, 309, 6, 52]), (19201498473, [935, 449, 462, 99, 3]), (2704430969, [3, 6, 30, 44, 27, 3, 965, 7]), (70405, [98, 778, 8, 8, 259]), (259354296, [80, 2, 4, 489, 7, 77, 72, 6]), (5027447, [5, 420, 46, 5, 7, 257, 12, 1]), (2550082496, [852, 1, 2, 34, 22, 1, 6, 6, 4, 1, 3]), (63378551, [1, 32, 5, 1, 575, 20, 7, 8, 5, 51]), (99436, [38, 26, 5, 55, 81]), (4751213813, [365, 108, 6, 1, 93, 8, 3, 6, 9]), (258695, [208, 5, 4, 5, 31]), (91658994623, [8, 8, 7, 4, 76, 7, 7, 9, 8, 4, 5, 806]), (475793, [494, 963, 9, 1, 61]), (33544917, [63, 751, 709]), (2435364, [9, 294, 9, 6, 3, 6, 47, 51, 2, 6, 6]), (43434131005, [127, 6, 285, 65, 2, 10, 90, 5]), (45065473559710, [95, 5, 1, 8, 1, 72, 7, 2, 30, 337]), (28974868, [174, 751, 1, 871, 73, 221]), (426214147, [425, 529, 684, 822, 325]), (5271382530, [1, 2, 4, 235, 2, 5, 1, 8, 3, 647, 7]), (45586, [739, 17, 3, 6, 1, 5, 8, 4, 5, 1, 2, 1]), (6698193597, [6, 3, 4, 628, 40, 840, 311]), (15504, [3, 243, 61, 1, 6, 491]), (5140, [4, 5, 257]), (220584, [7, 3, 5, 30, 2, 3, 6, 10, 728, 3]), (64685, [2, 55, 4, 3, 49, 5]), (124310160, [62, 1, 397, 6, 95, 4, 117, 6]), (290920903, [1, 33, 419, 6, 6, 6, 7, 9, 9, 9, 1, 7]), (3203484, [976, 91, 6, 38, 969, 11, 6]), (21780632, [9, 68, 5, 13, 1, 1, 45]), (19233, [93, 114, 3, 30, 575, 4, 8, 16]), (30784687823569, [9, 27, 2, 496, 1, 3, 324, 83, 4]), (954482, [86, 9, 44, 81]), (792144664294, [5, 2, 3, 2, 3, 163, 5, 2, 347, 7, 4]), (13523, [19, 706, 9, 3, 90, 7]), (8586, [9, 64, 807, 74, 9]), (91253, [9, 1, 255]), (278186, [11, 599, 19, 8, 2, 3, 20]), (845823426927, [4, 6, 38, 8, 54, 2, 64, 5, 30, 81]), (153471752, [7, 602, 7, 5, 9, 69, 6, 394, 8]), (461941850, [4, 97, 3, 2, 8, 26, 799, 31]), (509857, [9, 69, 13, 7, 9, 3, 2, 988, 265]), (2647266048, [96, 37, 978, 53, 8, 48]), (468054144, [278, 74, 8, 474, 6]), (1071273, [9, 1, 71, 337, 7, 367]), (1267937, [921, 86, 6, 254, 936]), (12864072, [3, 9, 5, 73, 3, 393]), (79654194, [7, 96, 5, 413, 2, 62]), (1719313023, [7, 1, 8, 3, 34, 301, 55, 47, 1, 3]), (561632609, [69, 7, 4, 233, 2, 7, 5, 9, 1, 4, 5, 8]), (166170, [970, 917, 29, 667, 3]), (61480543834, [736, 89, 9, 7, 7, 7, 6, 456, 10]), (32468717291, [3, 24, 687, 172, 89]), (3182817, [7, 3, 1, 5, 3, 554, 9, 1, 8, 99, 66]), (88670400, [80, 2, 59, 828, 9, 2, 8, 4, 49, 6]), (158562740, [9, 4, 7, 830, 6, 499, 91, 140]), (9555637, [95, 5, 5, 600, 40]), (131875, [2, 655, 92, 8, 3, 6]), (255437732053, [3, 33, 7, 29, 4, 9, 55, 2, 684, 3]), (199859, [282, 78, 269, 7, 29]), (4092, [22, 8, 45, 3, 42]), (19222508, [9, 99, 927, 8, 9, 6, 2, 2, 1, 2, 8, 6]), (947216, [51, 7, 85, 838, 18]), (12383, [20, 1, 98, 6, 8, 27]), (21360, [33, 54, 625, 5, 6]), (5596242979, [7, 44, 486, 67, 26, 6, 77, 6, 3]), (33805766, [982, 9, 13, 328, 7, 8, 718]), (33624180, [73, 796, 6, 48, 90, 71]), (319532, [1, 68, 58, 37, 68]), (409242, [2, 33, 62, 39, 1]), (14930, [44, 726, 5, 786, 96, 9, 9, 8]), (1265, [9, 6, 78, 95, 1]), (1156565692773, [431, 909, 773, 57, 67]), (1598, [63, 699, 197, 7, 632]), (14082480, [9, 349, 79, 4, 4, 3, 7, 52, 48]), (32449, [319, 4, 44, 2, 5, 45]), (17014074, [17, 37, 35, 453, 9]), (133560, [7, 6, 3, 7, 8, 6, 97, 146, 7, 4, 9]), (5352, [4, 903, 64, 6, 5, 467]), (32975657414, [443, 9, 383, 827, 3]), (738027, [5, 9, 2, 2, 3, 4, 205, 2, 5, 18, 7, 2]), (3529597412, [65, 543, 969, 36, 476]), (11708104, [9, 31, 44, 46, 788, 1]), (5875419661907, [9, 223, 57, 874, 7, 637, 68]), (20280, [4, 88, 48, 648, 6, 4]), (359, [4, 57, 105, 26]), (2649078578, [548, 9, 7, 482, 6, 541, 31, 6]), (24574752, [6, 6, 483, 4, 912, 9, 6]), (4759965610, [2, 555, 3, 621, 456, 61, 95]), (23796747000, [3, 93, 5, 78, 540, 9, 45]), (717729, [1, 75, 55, 95, 3]), (352719, [3, 3, 5, 3, 8, 3, 6, 1, 390, 119, 3]), (47428154, [63, 66, 584, 81, 53]), (418076, [914, 352, 4, 33, 150, 6, 8]), (59196215, [21, 7, 78, 16, 6, 269, 8, 65]), (11, [7, 3, 1]), (5097237, [441, 7, 8, 6, 7, 2, 9, 3, 7, 5, 5, 12]), (1028, [31, 47, 828, 33, 89]), (2439336, [301, 1, 3, 9, 4, 8, 222]), (17081603, [2, 18, 628, 340, 4, 1]), (30393, [6, 2, 41, 6, 87, 2]), (227311040, [249, 2, 257, 37, 6, 981, 7, 8]), (75510083, [925, 7, 9, 995, 26, 7, 14, 7, 5]), (714633, [95, 45, 664, 7, 3]), (1564, [9, 8, 2, 6, 963, 521]), (62681524, [62, 681, 47, 4, 50]), (161500557244, [8, 904, 4, 3, 3, 72, 3, 8, 59, 2, 6]), (278302617417, [837, 665, 231, 18, 365, 5]), (8484400, [28, 9, 1, 31, 947, 5, 222]), (6257035, [13, 682, 1, 223, 9, 31]), (1211, [3, 756, 19, 388, 45]), (123492, [19, 648, 36, 5, 9, 1]), (307359, [7, 6, 840, 4]), (24072, [8, 5, 33, 7, 6, 8]), (4017216, [737, 2, 1, 633, 6, 4, 122]), (5263312, [1, 24, 6, 4, 712, 8, 3, 9, 89, 6, 2]), (312474133265, [8, 223, 4, 95, 7, 6, 1, 32, 65]), (36852164, [6, 775, 3, 5, 3, 88, 2, 3, 3, 401]), (4342302390, [4, 986, 514, 3, 7, 2, 2, 7, 51, 6]), (444528, [2, 94, 24, 7, 9]), (537123825, [49, 372, 8, 93, 6, 93, 9, 35]), (168562, [7, 10, 397, 71, 228, 6, 28]), (4105154394360, [410, 51, 543, 943, 38, 22]), (1984845061, [989, 9, 21, 4, 2, 4, 50, 6, 3]), (22864, [55, 61, 197, 4, 8]), (578904148142, [965, 857, 924, 3, 9, 7, 7, 9]), (385142856, [4, 46, 790, 519, 802, 6, 2]), (205677585396, [2, 19, 741, 26, 25, 9, 2, 4, 9]), (3909, [7, 1, 279, 2, 3]), (1856, [85, 15, 8, 63, 699, 3, 983]), (91015969, [30, 308, 2, 985]), (9139618, [91, 3, 2, 7, 619]), (5071500, [33, 5, 87, 966, 42]), (566197, [56, 61, 66, 29, 4]), (238621122, [618, 9, 6, 65, 4, 866, 1, 3, 6]), (312646908244179, [3, 4, 738, 54, 53, 6, 9, 41, 7, 9]), (21660942534, [539, 53, 66, 7, 869])]

def valid_equation_exists(total: int, args: list[int], ops: list[Literal["+", "*", "||"]]) -> bool:
    if len(args) == 1:
        return total == args[0]

    init = args[0:-1]
    last = args[-1]

    exists = False

    # try equation where last operator is +
    if "+" in ops:
        exists = exists or valid_equation_exists(total - last, init, ops)

    # try equation where last operator is *
    if "*" in ops:
        exists = exists or (total % last == 0 and valid_equation_exists(total // last, init, ops))

    # try equation where last operator is ||
    if "||" in ops:
        exists = exists or (re.search(fr"{last}$", f"{total}") and valid_equation_exists(total // (10 ** len(f"{last}")), init, ops))

    return exists


problem1Solution = sum([total for (total, args) in lines if valid_equation_exists(total, args, ["+", "*"])])
problem2Solution = sum([total for (total, args) in lines if valid_equation_exists(total, args, ["+", "*", "||"])])

print(problem1Solution)
print(problem2Solution)
