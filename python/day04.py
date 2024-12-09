import numpy as np

word_search: list[str] = [ "XMSSMXMSMXASAMMXMXMSSSMMSMMMSXMAXXMSMSMXMAXSXSXSMMXSXMSSXMAMXMMXXSXSAMXASXMXXAXSXSXXMMSAMSSSMSMSAMXXXSXSMSSXSXMSAXMMMSMXSAMXMXSAMXAMAMXMXXXX", "XSAAXAMMAXSAMSMSMSXAXAAXSAAAAMSSMMMAMAMXXMAMAMMSASXMASAXXSMXSSSMMSASAXXMSAMASXMMMSMXSAXAXMAMAAMMMSSMMSAAAMAASAMXSAAAXAMXMMMXSAMASXSSMSMMMXMM", "MMSSMSAMXMAAXXAAAXMASXMMSSMXSMAXMASASXSMMXSMAMAMAMXXMMMAXAMXXAAXAMMMMMMXSAMAXAAXAXAAMMSMMMAMMMSMAAAAAMMMMMMMMAMAMSSMSMSASAMXMMSMMAASAAAAAAAA", "XAAMAMSXMASMMMSMSMAMXAMMMASXAMAMMMSXSMMAXAMXSMSMSMMMAAXSAMXSMSMMSXMAAAXASAMAMSSMMSMMSXMMAMAMAAAMMSSMMSAXAAXMXMMMMAMAMXAASXSSXXAAMMMMSMXXSSSS", "MMXSAMMMMXMXAXXAAAXASXMAMAMSXMSASASASASXMXSAMXMAXAXSXMSXXMAXXXMAMASXSSMMMXMXMMAXXAAXXMASXMAMSMMSXMAXASMSMSSSXXAXMXSMAXXXMAMAXSSSMSXMXSSMXMAX", "AXMSMSAASAMSXMMSMSXMSAAMMSXMMMASMAMASMMXAAMXSAMXMSMSASXMAMSXSASXMMMMAMMMMSXMASXMMSSXSMMMAMSXXAAXMXAMXSASAMAMMSMSMAXMAXSAMAMMXMAAAXXXAXXAXXAM", "ASMMXSMXXAMMAMAMAXMASMMMAMAAASMMMSMMMMSMSMSASXMXAAAMMMASXMAAMAAXXAXMASAAASAMAAASXXMXXAAMXMMASMMMSMAXMMAMMMASAAXAMMSMSSXASAMXAMSMMMSMMMMSMMSS", "MXAMMMMSMSASMXSSXXMXSXSMXSSSMXXSAXXXAAAAASXMSAAXSMSMASAMAMMSMAMMMMMSAMXSXSAMXSAMMAMMSXMMAXMAMAMAXMXMAMAMXSASMSSSXMAAXMXMMMSSSXMAXAAMAAAAAXAM", "MSSMAXAAXXMXAMMXMXXXMASAXAAXAMSMMSMSSSMSMSXXSMSXMAXMXMAXSMAMXSAAAAAMASAMXSAMAMAASXSAMASXMXMASXMMSMMAMSASMMASAMAMASMSMSMSAMMMXMMMMMSSSSSMSMAS", "XAXSMMMSSSMMSMSASMXAMMMXMMSMSMSAXMAAMAMXXMMMMAMXMAMSMSSMMXXSAXXSSMMSMAAMASAMXSSXMXMMSAMASMSAMAAAAAASXSASXMAMXMAMMMAAXAXMAMXSAMSSSMXMAMMXXMMS", "MMXAXSMMMAAXAXSAAASAMXAXMXMAMASXSMMMXXMXAXAMMAMAASMSAAXXSAMMXSMMAMMMAMSMXSAMXMAXMAMAMASAMXMXSSMSMXSAXMAMMMXSSSMSAMSMSMSSSMMMXSAAAAXXSXSMSMSS", "SSMSMMAASXMMMXMSMXXAXMMXMAMXMXMASAXMASXMSSMXSASXSMAMMMSAMASAMXXSAMXXMXMMXXXXAXAAMAMAMXMXSXMMAMAMXMAMXMXMASAXXAASAMXXMXXAMXMSMMMXMMMAMAAAXXAS", "MAAMASXMMXAAXAAMXMMMXXAAXAMAMAMSXMAMAXAAMXXXSXSXXMSMMAXMMMMMSMMMAMMXXAASXMASMMSXMAXXSMMMMAXMASMSMXAMXMXSAMXSMMMMAXXMSMMAMMAAAAAASXMAMSMMMMMS", "SMMMAMXAAXSMMMMMAMAMMMSMMAMASXSAAMASXMMMMAMMMMSXMAXXSXXMAAAXAAMSSMAMSSXMAXAAAAAXSSSMAASASMSAMXAAMSMMXAAXASASXMASXMXAAASAMMSXSMSXSAMXMAMAAXAS", "SAMMSMMMSAMXMAMSMSAAAAAMSMXMSXSMASASAMAMMAMXAAXXXXMAMXASMMXSSXMAAMXMAAASMMSSMMSMXAAMSMMAAAAMXMMMMAASMMMXAMXXAMXSSSMMSXMXXXMXMAXMSAMXMAXSXSXS", "SAMSAMXAXMASMAMAAXMSMSSMASAAXAMXMAXMXMAXMASXMSSMMXMAXXXMMSMMMSMMSMMMSXMMAAXXMAXXMSMMMXMSMSMMSXSXMMXMAAXAXMSMSMSXAXAMXAMXSAASXMSXSAMXSMMXAMXS", "SMMSMSMMSMAMXMMMSMAMAAMMASMSMMMMMMAMASXXSASXMMAXAXMMSMAMAAAAAXXAMMSAMASXXSXAXSXMAXMAXAXXMMMMAASMXSASXMMSAAMAMXSMMMSMXAXAXMMXAXXMMAMAAAAMASAM", "XAAXMXAXXMASAMAAAMAMXMSMXMXAMXAAAXMSXXAXMXMASXMMMXMAAXAMSSSMSSMXSAMASAMSMMMSMAAXSXMMMSMAXAMMMXMAAAAXXAAXMAMSMMSAMAASMMMMMXAMMMSXSAMXMMMSAMAS", "XMMSSSSMMXAMASMSSSMSMAXMAMXMSXMXSSXMAMSMSAMXMAMSMSMSSSXMMAMXXXASMAMMMXMAXMAMASXMMMXMAXSMMXXAXAXSMMAMMMSSMAMAAASAMMSXMXAXAMXSMASAXSXSMMXMASXM", "XAAXXAAASMSXMMMAMAAAMMMMMMSXMASXMMAMMMMASAMSSSMAAAAMMMMMXAXMAMMMSXMAAMSMSXAXMXMAXAXMAXAXMMMSXXXAXXAXAMXXMASMMMSXMXMXMMXMXSAAMAMAMMMSAMSSMMAM", "MMMSMMMMMMMASXMMSMMMMAXXAXAAMAMMASXMAAMAMAMAAMXMMMMMAAMSSSMMAAMXXXMMSMAMSXMSMMSSSSSMSSSMMAXMASXSMXSSSMSSSMXMAMSXXAMAMSMAAXXXMASAMXASAMAAXSXS", "SASAAAMASASAMAAAAAMXMAXXASMXMAMSAMASXXXAMASMSMSSMSAXXMSMMMASMSSMMXSAAMAMMAXAAMAXMASAXXMAMSAMXMAMAAXAMAAAAMMSAMMMMSSXSAMSAMXXMASAXMMMAMSSMSAA", "MXSMSXSAMMMASXMSSMMSMAXXAMXMSSMMMSXMASMXSAMXMAAAASMSSMSAAXXMXMAXAAMSMSMSSMMSXMXSMMMXMASAMMMMSMMMMMMAMMMXMMAXXSMAXAAMSXMXAMXMMMXXXMSSXMXMXMAM", "MMXXAMMAMXSXMAAXAASMMAXAAXMASMXAMAXMXMAMMMMAMMMMMMASAASMMSXMASXMMMMAXAMAASAXMSMMMXMMSAMASMXAXMXXSMMSMMSSSMMSAMXSMMSMMASMMMAMSSSMMXAAXSMMMAMX", "XSAMXXXAMAXAXMMMSMMAMAXSAMMSMXSMMAXMMMXMAASAMXSAXASXMMMAXAASXSMASXXXSSSSMMSMXAAAXASXMASAMMMSSMSAMXMMAAAXAAAMAMAMXXAXSXMAXSASXAAAAMMSMSAAMMSM", "AMAMSASXSMASXAXXXMSSMMMXAXXXXMAAMSXSAAXMSMXXSAXXXSAMXASXMSXMXSASMMMXXAAAXSMXSXSMSXSASAMAMAAMSAMXMASXMMSSMMMSMMXSMXMASASMMSSSMSMMXSAMASMMSAAA", "MSAMMMSAAMAXMMMSMXAXAMSSMMSXMASXMXASMSMAAAMSMXMXMAMSXMXAMXASAXXAAAMASMSMMXMAXAAAMMXXMASXSMXSMMMSSMSXASAMMAAAXMXMASXMSAMMASASAMAAAMAMXMASMMSS", "XSXSAAMMMMMSAXAAXMASAMXXMAMAMXMXSMMMAMASMSMAASMSXMASASXMSSXMASXXSASXSAAXAAMAMSMMMMXSMMXMAMXMASAXMASMMMASXMSXSXMMMSXMMAMMSMAMXSAMXMAMASXMAMMM", "MXXXMSSSXMASMMSSMSAMXXXMASMXMAMXXAXMAMMMXXMMXMAAAMASAMAAXMAMAMXXMMAMMMMSSMMXXXAMXSAMASXSAMXSAMMSMAMAXSMMXAMASMMAASAMMSXSAMXMXSMMSSMSXSXMXSAM", "SXSXSAAMAMMSXMAAXMASMMSAAXMAMAXASXMMSSMXSASXSMSMMMASASMMMSMMASAAMSAXSXMXXSMMMSAMAMASMMASXMXMXSMAXSSSMSMMMSMAMASXSXMMAMMSASXMAMAAXAAMAMAMAMAX", "MAMMMSSSXMXMMMMXXXAMXXAMXXMMSSSMSAAXAAXAMXSAAAXAXMXXAXAAAAXASMMMAMMSMXMSMAMAMXMMASXMXMAMASXMXMMMXMAAAXAAAAMXSXMMAMSMMSASAMAMXSMMMAMMAMAMMMSM", "MAMAAMMMAXSXAXMASMMSSXSSSMMMMMAASASXSMMSMAMXMMSSMSASMSSMSSSMAXAMASXMXAXAAXMXSAXXAMXMAMASXMAXXMASXMSMMMSMSSSXMASMMMXAAMMSMSSMMMMMSMMMAMXSXAXS", "SSSMXSASAMASXXSAMAMXAAAAXMXAASMMMAXAAXSAMAXXXAAXASAMXAXAAAAMMMXMAMAASMSMSASAMAXSASASAXMSMSXMXSAXXAXMSAAAXAMMMAXMSMSMMSAMXXMASAAXAMSMXSMXMAXA", "XXXAASASAXMASXMASXMSSSMMMSSSXMASMMMSMMSASXSMMMSSMMAMMXMASMXMAAAMXXMMAAAAMMAAMAMSASMXSASMXSSXAXXSMXMXMXSXMMXAMMSMAMSAASXSMMSAMXSMSMSAASXMASAM", "SAMMMSMMMMXXAXMAMXAAAXXXAMAMASAMAXAAXXSXMXAXXAXMMAXXMXSMXMASMSMMSAXSMMMSMSSXMXMMAMXAXMAXAMMMMMSAMXSASAXASXMASMAMSSSMMSAXAAMASAXXMAMXMMAMAMAX", "SXMMAXMXSSSMASMSSMMMSMSMMXAMAMXMSMSXSMMSSSXSMMMSXMMSXAXMASAMXXAASAAMSMSXMMMMSXMMAMMMSXSMSMMAMSXMASXAMAXMMMXSSMSSMAXMSXXSMMSAMXSAMAMAXXXMASMM", "SAXSMSMSMAAMMMAXXXAXXMMAASMMSXMAXAXAMXAAMAAXXAASMSASMSMSAMXMSMMMSAMXAXMAMMSASAASASAXMAMAAASXSMMMMMMMMMMAAASAMXMAMXMXXAXXMAMASXXXSASMSMSSXSXA", "MAMAXAMAMSMSAMXMMXSXMASMMSXAMAMAMAMSMMMSSMSMSMMSAMXSAAMMMSAMXAMAXMASMMMAMXMAXXMAMSMSXXMMMXMMAMASASAAASXMMSMASMSXMAMMMMMMMXSXMAXMXXSAAAAAAMMM", "SAMMSXSAXAXSXSXAXMMAAXAMXXMMSAMSMMMAXSMMXXAAXXXMXMAMMMSAASXSXSASMXMMASXMMXMAMMAMXSMMMMMXSXSAMSMMASAMXXSAMXXASXMASXMAMXAXAXXMXSAXXAMMMXMMMMAX", "SMSXAASMSMXSMMMSXAMSMMASAMAXMXMXAXSASAMXMSSSMMXSXSXXAXSXXSAMXMAMMMSMAMASMSMAXSAMAMAAAASMSASMXSXMXMMSSMSMMXMMMASXMMSSSMSSMSAMXAAASXSAMXSSMSSS", "XAAMMXMAAXASASAMMSMAASAMMMAMMAMXXMASMXXSXAXAAXXXAMXMXMXSMMXMMMAMAAAMASMAAAMAMSAMSAXSXXXAMAMSAMAXSAAXMASXXSMMMAMXMAMMAXMAMMAMMMMMAAAASMMAAAAX", "MMMMSMMSMSASXMASAXMXMMASAMAMMAXSAXXXXMXAMXSMSMMMMMAMXAAXXAXMSAASMSSSMSXMMMMSXSXMXAMXXSMSMXMAMSAMMMMSMAMMSMAAMSMSMSSSSMSMMSAMAASXMMSXMASMMMSM", "MSAAAAAAAAMXASAMXSMSSXXMAMAXMASMXMMMAXSMMASAAMXAAXAXAMSMMMSXAXMAXAAMMMAXXSMMASMMMSMSAXAAXSMXXMASXAAXMASXAMMMXXAAXXMAAXSAASXMSMSXXMAXMMMMMXXA", "ASMSXXMMSMXSXMASXMAAAXSSSMASXXSXXMMMMMAXMAMXMASMSMSAMXMAAAXMMMSXMMSMMSSMASAMAMAXSAAMMMSMMMSMASXMXMMMXAMMXXSMMMSMSSMSMMSMMMXAAMMMMXMXMAXMMAXS", "AXXAXSAMMXAAAMSSMMMMSMAAXMAMXASAXSAASAMXMXMMXAXXXAAXAMXMMXSAAAXAXAXAAAAAASXMASMMMMMMXMXSXAASMMXAAXASXSSXSASAAXXMAXMAMAMXAMSSSXSAMAMMSSSXMXSX", "MAMAMSAMASMSMMMXAMMXMAMSMSMXMXMAMSSSSSXSMSSSMMSXMXMXMASXSXSXXSSSMMSSMSSMMSMSXMMAXAAMMMAMMXMSXAMSMSMSAAAAMAMXMXAMXXXMMAXMXMAAXMMMSASAAMXXXMXM", "SXMSXSXMASXXMAXXAMXAXMAXAXXXSXMXMXMMMMMAAAAXXMAXAAMXXSAXMAMXMXXMAXXXAAXXSXAXAMSXSMXSAMASAAMXMMXAAAXMMMMMMMMASMSMMSSSSSSMMMMSMSSXSMSMSSMXMMAA", "MXMMASXMASMMSASXXASMSSMMSMMASXMXMASAAASMMMSMMXSMSXSAMXXAMAMAMXSMSMXMMMMSAMXMSMSASAXSASXSMMMAMXSMSMMXMXXMASXMXAASAAAMXMAMASMMAXMASAMAMAXXAMSM", "AMXSAMMMMSMAMAXXMXMAAAAAMAMSXAMXSASXSMSXSXAXSAXAXAMMSSSMSASASXAMAAXSSXMXXXSXMAMAMAMSAMXSAMXSAMSXAXSMXMXSASAAMSMMMMSMMSXMXMAMSMMAMAMSMAMSSMXX", "SAAMAMAMXMASMSMASMSMSSMMSXMMSAMMMXSAMXMAXMAAMAMXMSMAAXAAAASASXMSSSMAMAMXMXMAMSMMMMMMAMXMAMXMASMMMMAXAAAMASMMMMAXXAMMAAASMSMMXAMMSXMAMAMSMXSA", "AMSSSMXSAMXMAMAXAAAAAAAXMMAXMXSXXASMMXMAMMMSMSMXXMMMSXMMMXMXXAXAMXAASAMMMAMXMAAXXXXXSXMSAMXSMMMAAAMSXSXMXMXSASMMMSSMMXMMAAXSXSAXSMMMSMXXAAMM", "MAMAAASMMMXXXXXMMSMMSSMSMSSXMSAMXMMAMMMSSXAMAMMSMXMAMXXAXXAASMMMSASASAMASASASMSMMMMMMAMMMXMAXASMXSXSAMXSXMXXAXAAAXXXSMAMSMMXAXXXMAXXXMSMMMSX", "XSMMMXSAASMSMMSMXXXMAMXSAAAASXMXSXSXMMAAXMXMAMXAAXMAXAMXXSMMAAXXMAMASXMXSAXXSAAMAAMAMXMAMSASXXSAAMAMAMAAAMSMMSMMXXMASXMMMXAMXMMMSXMASMAAAXMX", "XXAXSAMMMAAXAAAXMXAMXXAMMMSMMAXAMAMMSMMXMSXMASMMSSMSSSSSMXSMXMMMMXXMMMMMMMSAMXMMSSMAMSASMSAMMAMMMMAMAMSSMMAAXSXSSSMASAMMSMMMMAXAMAMAASMSMSSX", "ASMMMXSXMMXMMSXSMSSMSMSSSMXASXMSMAMAMMXSAAXSASAXAXAAXAAAXAXXMXMSASMXMAMAAMMMSSXMXXMASMAXXMAMMAMASMXMXAAXASXXMMAMAXMAXAMASXAASAMASXMXMMXMMSAS", "MXMAMXSAMSMSMXAAAAXAAAAAAASAMAAMMMXSAAAMXMXMASMMASMSMMSMMASMAAXXASAAMSMMMSAAAAASASMXMMAMMMMMXAXMMMMMMMMMXMMXSXMMMMSASXMAMMMMSAAMMXMMXMAMXSAM", "XAMASAMXMAASAMSMMMMSMSMSMMMXMMXMASMMMMMSAXXMXMXMMSXAAXAAMAXAXASMMMMMXXAAASXMMSMMASMSXMASAAASMMSSMSAXSASASXSAMAMXXAMAAXMSSXSAXMXAXAXAAMMSAMAM", "SXSSMMSAMMSMAAMMASXMAXXMAXMXSXXSASASMMAMMSAMXAXMAMXMSSSSMMXSAAMAAAXXASMMMSASXMXMXMASMMASMSMAASAMASAXSAXAXAMMSSMSASMMMMAMAAMAMSSMSMMSMXXMASMM", "MMMXAAAAMSXXMMMSASAMXMASXMXAXMAMXMXMAXSSXMASXSMMMSSXAAAAAMAXMMSMMSSMAXXAMXAMAXSSMMAMXSAXAXXSXMASAXXXMAMSMMMXMASAXMXSSXAMMMMXMAAXAMAMMMXXASAS", "MAAMSMMSMMAXMAMMMXXMAXMSAMMMMMMMAMSASAMXASAMXMMXXAAMMSMSMMMXXMAMSXXMASXMMMXMSMASAMXSAMASXMAXXSMMMSMXMAMXAASASMMMMMXMMSMSSMMSMSSMMMAXAASMXSAM", "SMSMXAAXMMXMMASMSMAXMXXXAMSAMMAMAXMAMMSSXMAMSXSSMXSAMMAAXAXMXMAMMASAMAMSASAAMMXMSXXMASAMAMXMAAXAXAAAMAMMSMSASXAAMAMAAMXAAAAXMMMMXMSSSMXSAMAM", "XAXXSMMSAMSXSMXAASAASMSSSMMAMMAMSSMAMAMMASAMAAAXMAXAAAMMSSSMXASXSAMAMAASASMSMSMMMMMSXMASAMMMAMXMMSMSMMMMMXMXMMMXMAMMXMMSSMMMMXAXXMAAASAMXSXM", "MXMXXAXSAMAAXAMSMMSSMAXAMXSAMSSMMAMXMASAAMAXMMMAMMSAMXXMXMAMSXXAMXXXSMMMXMAMMMAMXAAAMSXSXSAMSXSSXMAAMSAMSSMMSSSMSXSASXMMXAAAMMMMMMMSMMXSXMMS", "XAMXSXMSAMMMMXMAAXXXMMMSMAMAMAAASXMASXSMMSSMXSSSSMSMSMMMASAMXMMMMAMXXMSMMMSMXXSXXMMSASMMMMASMAAXAMXMASASAAAAASAAAAMAMAASXSSXSAAAXMAMXMMMAMAM", "MSSMMAASAMAAMXSMSMMMMSAMMSSXMMSMMAMXMMMXMAXMXMAMXAXAAAASMMASXAMASMXXASAAAMAAXSASXXMAMXAASXMMMMMMXMAAMSXMAXMMXMMMMXMASMMMMMAMSXSMMMASAXASAMAS", "SAAAMMMXMXSMSAAXMAXAAMAMAMMMSAMXXMXAXAMAMXSAMMASMMMMMSMSASAMMSMAXXASMMSSMMMSMMAAMMSSMXSMSAMXXAXAMSMSMSMSSSMSSMSSMXSAXMAAMMMMXAMASXMSMSXSAMAA", "MSXMXSMMSAAAMMSSSMMMMSXMMMAAMAMXMASXSMXMSAAAXXAMAXAMAMXSAMXXAMMXSMXMSAMXMXSAXMSMSXAAAXXXSAMXMMXSAAAXXXAAAAMAAAAAXXMASXSMXSXSMSMAMAAXASMMMSMM", "MAXXASAAMMMMSAAMXAAMMMAMAXSSMSSSMAAAXXASMMSSMMSSMMSMMSAXXMMSSSSMAMAMMMMAMXAAXXXXAXAMXMSASAMXAAAXMMSMMMMMSMMSXMXMMSMXMXXXMXAMAXMMSMMMXMASAAAX", "MSSMASAMXAASMMXSSSMSAMAMMXMAMAAXMMMXMMMSAXMAXAAAAAXASMMSASAAMAAAMMAXAAXAXAMXMXMMMXMXMAMXMAMSMSMSAMXAAXAXMXMMAMMSMMMMSAMAXMAMSMAXXXXMASXMXSXM", "SAXMAMAMMSMSAAAMXAXSASMXSASAMMSMXAMASXMSMMSMMMSSMMSSMAASAMMSSXMMMSXXMXSMSMXAAMSAMASAMSSMSSMXXXASXMSXMSMSMSAMXMAAAAAXMASAMXAMAXMMSMMSASAAMXMX", "AMMMXXXMXXSSMMXSAMXSAMMASASXSXXMSMSAXAAXAAXXXMAMAAXXMMMMMMMAMASXXXMASMMMAMSMMAXASASXSASMAXXXMMMMAMXMXAMMASXMAMXSSMMXSAMAXSASMMSAAMAMXXMMAMXM", "MXMXMASXXMASXXXMXMAMMMMAMMMASAMAAAMASMMSMMSMXMASMMXSMSXSAXMASAMAXMMAAAXSAXAAXSSMMMSXMAMMAMMSAAASASAMSAMXAMASXSAMMAAAMAMAMXAMAAMSSSSSSXMMAXAA", "XMMAAXMASMAMMSAMXMXSAXMASAAXSAMSMSMAXAXXXAAXAMXSASMAAAAXASXMMMSSMXMASXMAMMMSMMAMAAXAMAXMAAXSXSXXAMAXSAMMASXMAMAMMMMMSAMMMMSSMXMAMAXAAAXSXSXS", "XSSSSSXMXMXSAMAXAXAXXXMAXMSMMMMAAMMXSSXMASMSSSMSAXSMMMSMAMXAXAAAAXMMXMAXXMXXXMASXSSXSAXXAXXSAXASXSSMSXMXXMMMMMASXMSASAMSAAXAXSMAXSMMMSMSAMXM", "AXAAAAXXAXMMMSMMMMMSMSMSMSAAAMSMSMMAXMAMAAXSXAXMMMMMAAXMAMSMMMSSSSSMSMXXAMXMAMXSAAAASAMSSMMMAMAMAAXAMAMMSAMAMMMSAAMASAMMMMSMMSSSMXXXAXMMAMAM", "MMMMMMMSMMAAMAXMAAMAAXAAXMSSMXAXXAMMSSMMSSMMSAMXSAXXMSSSXMMMAXXAXXAASAASXMAXMXAMMMMXMAMAMMXMXMAMMMMXXAMXSAMMSAAMMMMAMAMMSXMXMMAXAXMMMSAMXSMS", "MAXXXMASXMXXSASMMSSMSMMMMXAXXSXMSAMAAAXAAAAXSXSAMXSAMXMASMMSXSMXMAXMMXMSASXSXMASAXXSSMMAXMAXSMXSXXXXXXXMSXMASMSMAXMASXMMSAMSXMAMMMSAMXAAAAMA", "MXMXXMASAXSAMMMAMXAXXXMASMAMMXMAXXMMXXMMSSMMMMMXMASMMMXAMMAXMAMXXMXSXXXSASAAXAMXMAMAASMMSSSSSMMSXMXMASMMMAMXMMMMAXXAXAMAXAMAXMASAASXMMXMXMSM", "SSSMXMASAMMAMXMXMSAMXAAAMMMMXXAMXSSSSXSAAMXMAAAAMXMAAAMXMXAXSAMXSMASXSAMAMXMXXMASXMAAMSAMXMAMAAMAMAAMAASMXMXSAMXMAMMMSMMSSMMMSAMMXSXMXMSMXMM", "XAAXXMXMXMMAMXASASXXSMMXSASAXMSMAMAAMAMMXSASXSSMSMSSXSMMSMSMSASXAMASAXAMXMXXMASAMXMMSMXMSXMAMMMXAMMSMSAMXMSSMMSAMSASAAAXAAMXXMMXSAMASAAAAAXA", "MSMMXSAMMMMSSMXSAMXXMASMAAMXMXAAAMMMMAMAASASAXMMAXMAMAXMAAMAMAMMAMXSMSMMMMMSSMMMMSXAXAAMSMSXSASMMXAXAAMAMXMAXAXAMXAMMSMMSSMSMMMAMXSAMMSMMXSM", "MAXAXXAMXSAAAXAMAMXXMAMAMMMXMSASMSMMSASAXMAMXMAMMMMASAASMSMSMSAMXAXSXAXAAAAMAAASASMSSMMMSAAAMAXAXMXSSMSAMASMMMSSMMXMAMAMXAASASMSXXMASAMXSMMM", "SMMSSSMMAMMSMMXMMMXMMASXXAMAMAXMAXMASXXXXMXMSMMMSASXMMMXAAAAXXXMXXXMASMSSMSSMMMMASAMXMMAMMMSMXXMMSAAAXSASASXXXAMXXSMMSAMSMMSSMAMMMSAMAMAAAAA", "XAAAAAAMAMMXXXSAMXAMSASASAMASMSMSMMMMMXMAMAMXMAAXMSXSAXMSMMMMXXSASMSMMAMAMXXXAXMAMAMSMMAXXMMMAAMAMMSMMSMMASAXMXSMMMAASAMXXAMXMAMAASASAMSSSMM", "MMMMXXMSMSMMMASAMMMMMASAXXSMMXXAAAAAAMAAASASASMSSXSAMXSXXASXSMAMMSAAXAAXASXMSASMASAMXXSSSSXAMSSMASAAXMMMMMMMMMASAASMMMXXMASAMXXSMMMMMXMAAXMM", "XSSMXSAMAAMASASAXSAAMMMXMMXMSSMSMSMSMMXXMMASXSAMAMMSMMMMXMMAXMAMXMXMMSMMMSAMSSMMMSASAMXAAXMXMAMMXMMSSXMAAXAXAMASXMMMAMSMSAMASMMMASXXAMXMSMSA", "MAAAAMXMSMMXMASXMSMMXAMXXMAMAAAXAXAXMSMSXSAMAMXMMSAXMSAAXSMMMSMSAASXMASMMSAMSAMXMSAMMMMMMMMSSSSSXSAMAASXSSMSMSASAMXMAMMAMXSAMAASMMXSAMXXMAMX", "AMMMMMAAMMMSMMMAXXASAMXSASAMMMXMMMSMMAAAAMAMSMSSXMASASXXMAAMAAAXMXSASASMAMXMSAMXXMMMMXMAAAMMAMAMAXSMSMMAMXAAMMMSXMAMMXMAMXMXMMMXAAXSMMAMMSMM", "SXMSSSSSMMAAAASXMMAMAMAMMMASXAXMAMAASMMMSMSMMAXAXMAMXMASXSMMSMSXMAMAMASMXXAMXAXXMASMMAMXSSXMSMMMMMMXMXMMMMXMSMMMXMXMMAMAXMSAXSSXMMMSMMXXAAAX", "AAMAAXAAMMSSSMXMAAMSXMASXSXMAAMXASMMMASAMXAAMAMMMMASMMMXAAXMXAXXMSSSMMMASMSMMXMMMXMXSAMXAMMMMAAMAASASXMXXMSMSAAMMXMASMSXSAMXMXAASAMXASXMXSMM", "SMMMSMSAMXMAAMXMSMMMAMXMMAAXSMXSASMXSAMXSSXSMAAXAXMXXAMMSMMMMSMAXAAMAMMXMAXAMSMSMAAAMAMSAMAAAMMSSXSASAMAMMAASXMSMSMAXMAAMXMAMMXMMASMMMAXAMXX", "XXXSXMXXAMMSMMAMAAAMXMXMASMMXAXMMMMXMXSSXMAAXXSMSSSMSASXMASXAAMAMMXXAMMXXAMXMXAAXMXMMAMSAMSSMSXXMMMXMAMASMMMMASXAXMXMMMMMASMSXMMSAMASXSMSSSS", "MMMSAMXSMMMAASMSSSMSAXXSAAXXMSMMSAMAMXMXAXMASXXAXAXAMXAAMSXMXMSMMXMXSSMSMXMASMSMSSMXSAMMAMXAASAMXAAAMMMASAMASXMMMMSAAAXASXSAAXMAMAXMMAMAXAAA", "XAXMAMMSAAXSXMAAAMASMMMASAMXMXAAXASASAXMXMXAMMMXMASXMSSSMMXSMMAXXAASXAAAASAXMAXAXAAAMXSSSMMMMMASMSSMXSAMMASASMMMAAMASMSXSASMMSAASAMSMMMSMMMM", "SSSSXMASMMXMAMMMSMAMAXXAXXXAMMMMSASASMSMSMMXSAMAMXMAMMMMAXAAMSAMSXSAMMMMXSAMXSMSMMMMSAMAMXMMASAMXMAMAXAMSXMMSASMMMSAMMSAMXMAAXMXMAXXAAAAMSXM", "SAAXSMXXMMASXMAMAMASMMMXMAMMSXXAAMMAMXAAAXSMSASMSSSSMAAMXMXMAMAXXMMMMSAXMSAMAXAAAXAAMMSAMAXSXSXSXSAMXSMMXAAMSAMMAAMASAXAMAMXMAXMSSSSSMSSXXAS", "MMMMMMSXMMASAMASASMSXAXMMSMSAMMSSXMAMSMSMXSAMXMAAAAMSMMSXMSXMSSMSMAAXMAXMMAMXMMMSSMXSASASAXSXMAMAMMMMXMASAMXMAMMSMMMMMMMSXSSMMXXAAMAAAAXMSMM", "SXAAAAXMSMMMXSASASASMXSXXAMXASAAMMSSXSXAXXMXMAMMMMMMAMSAMXAAMAMXXMMMMXMASXXMAMMSMMMMMMMMMMXMASXMSMMSAMMAAAXMSMMMAXAAAAXXAMXAAMAMXSMSMMMSAAAA", "ASXSMXSAXXAAXMXMAMAMMMMXMASMMMMXMAAMXMASMXMAMXSAXXXXAXXMAXMMMASMXXMASXSXSAMSSSMAAMSMSASXMASMXMASAAXAMSMSSSMAXMASMSSSSXSAMSSSMMAAAMMXXMASXSMM", "XSXMAAMXMSMSSMXMAMSMMAAXSAMXXSXSMMSSMMMMSMXAMXAMAMXSSSSSSMSASXMASXAAAAMAMXMAXAMSSMAAXAASXMXXMASXMSMMXMAAAAMSMSMXXMMAAAMXXXXAMSMSSSMSAMXMXMAM", "XSAMMMMAMAMMXMAMAXMASMXXAXXAMXAMXAAMMSAMASMSXSASMSAAXAAAAAAAMXMASXSAMXMAMXMMSSMMAXMSMMMXMASXMMXXMAMXSMMMSMMAAAAXSAMMMXMASMSMMAAXAAXXMXMMAMAM", "SMAMMAMASAXMAMSSSSSXMMMSMSMSSMMMMMMSAMASAMXAAMAMMMMMXMMSMMMAMAMMMAXMSASXMXAAAXASAMXAXAASXMXASASASMSASMAMAMXMMMSASMXXMAXAAAAAXMSMSMMXMAAMXSAM", "MSMMSAMXSASXSMAAMXMXMXXAXMMAAAXSAMXMXMAMMXMXMMMMSMSXXXXXMXMASASAMSMASMSAMSMMXSXMMXSMSXXMAXXXMASAMAMXSSXXASXSAAAMXAXAMMMSSMSSMAMAAMAAXXXAASAM", "XMMASMSMMAMAAXMXMASMMASMSSMSSMMSASAMSSSMAAXMMAMXMASMMXMASMSASAMXMAMXMAMXXMASASXAAXAXXMASMMMSMXMMMAMXMAXSAMASMSMXMMMMSMAMAXAAMAMMMSSMSMXMXMSS", "MSMASXAXMXMSMMXASMMAAAXXAAAAAAAXMSAMXAAMSXSAXASAMXMAMXMXMMMASASXSMSSMAMAASAMAXSXMXSMMSMAMAAAMXAMMAMMMAMMAMXMMXXXAXAXAMASXMSSMSSXMAMMAMSMSMAM", "AAMASXSSXSMMXAXMXMXAMSMMMXMMXMMSXSMMMSMMAMAXSMMASXSSMMSMMAMXMASAAXAXSAXXXAMMSMSMSMMMAAXASMSXSSMMSMSMMSSSMSMSXMMSSSMXMXASMAMAMAMMMASMAMSAAMAM", "SMSASAMSAAXAXSXSASMSAMASXMSSXAXMXMAMAXAMXSAMMXMAMXAAMAAAXMASMAMMSMSMSMXMXAXAMAXMAAMMSSSXSXMXAAXXAAAMSMAXAAAMMMAAMAMMMASXMASAMASAMXMMXSMSMSXS", "XXAXMASMXMMASMAMASMMASAMAMAASMMSAXMMASAMMMASXSASXMMMMSSSMXXXMXMSXAXAMMASXMMSMAXSMSMAAAMASAMMSMMSMSMMAMSMSMMMAMXMXAMMMXMASASXMMMMSMXSMMAMXXAA", "XAMXSSMMMXMXAMAMXMASXMASXMSXMSSSXSSMMMAMASXMASMXAMXXXXMMAMXMXSMMMSMSMSASAAAXMXMXAXMXSXMAMSMAXSMXAAMSSSMAMASMXSXMMASAMASAMXSASXAAXAMXAMAMAMAM", "XMXMXMAASXMSAXMSXMAMXMXMXAXXAXMXAAXAXSSMMMSMXMXSAMXMSAMXSMAMASAAAMXXAMASAMXMSSXMAMMAXAMXXXMSSMSMMMXMXAMAMXMMAMAASASASMSAMXMAAMMMXXMSSMASAMAA", "MMAMXSXMSAXSAMSAXMXSAXASMXMMAMMMSMSSMMXAXAXMASASMMAAMSMAMMXSASMMMSSMAMMMXSXSASXMASXMMXMSAMXXXAAXAMXMSXMMSSMMAMXMMASXMXXMMSMMMSSXSAMAXMASASXS", "ASASASAMMMMMMMMAMSASMSMSAAAAASAAAXAAAMXMMXMAAMASXSXXSAMXSSMMASXMXAAMMSMSAMXMASXXAMAMXSAMAMMMMSMSMSAMXXMASAASMSMXMMMMMSMMAXASXXAASXMXSMXSAMXX", "XSASASXMAAAAAXMMMMASXAMMXXSSMXMSXMXSMMASASMMSSMMXSAMSAMAMXASAMXSMXXMAAMMASMMMMAXXSASAMXSAMAAAAAAASASXXMMMMMAAXAMMAAXAAAMASAMSMMMMMMASAAMXSXS", "XMMMMMMSMSSSSMXMAMXMMSSMSXMAXMMXASMMAXXMASXAAAAMXMAMSXMAXMXMAXAXSMAMSSMXAMXMMMSMMAMMAMASXXXXSXSMMMASMMASASXSMSSSXSMMSSXMAMAMXXAAAAMMSMXMASAS", "MSMSAAXMXXAAXAMMAXSMSMAMSASAMMASXMASAMXMSMMMSSMMAMMMMXSMSSSSSMSAMXAMAMMMSMSSXMASAAMSXMXMMSSMMMMMXMMMASASMSAMXAAMAMXMAXAMXXXSMXSXSXSAMAMSAMAM", "AAASXSXSSMMMMSSXSSMMAMXMSAMMSMAXSAXSMSAXAXAMXXMMSXSASXMSAAAAXAXAASASASXMMAAMAMAMSAXXXMAAAAXAAXSAAMAXXMASMMMMMMSMAMAAAMXMAMXMXMMAXAMASAMMMMSM", "MMMMAXAXSXAAAXXAMAXAASMAMAMAAMMSMSMMXSAMMXSMMASAMXSASASMSMMMMSMSXSASMSAAMMMMMSAMXMASASXMMSSSMMMSSSXMSMXMASAXXMXMASMMSMAXASASAMXAMASAMMSMSAXS", "XXASAMXMMSSSSSMSMAASMSMASAMMXSXAAAXXAMXMSAXASXMAMAMMMMMMXSXXXMAAAXXXXSMMXMXXXMASXXAXMXXMAMAMAMAAMAMASAMXMMMASXSMAAAAXMAXASASAMMASXMMXSAMMASX", "MMXXASXSMAXMAAAAMXMXAXXAMASMMMMMSMXMXSSMXASAMXXAMAMXAAAMXMMMMMXMXMXMAXXMXSMMMSXMXMMSASXSSXMASMMMSAXXXXXXXMXMAAAAMMMSMSMXMMXMAMSMMMSAXSAXMMMX", "XMMSAMAMMMSSSMMMSMXMASMSSSMXAAAXAMXMAMAMMMMAMMSMSXSSMMMXAMMAAXAMAMMMXXXSAMAAAMAAXAAMAMAAXXXXXAXMMMXXMMSXMMAMMSMMMXMAAAMMMAAMAMAAAAMMAMAMSAMM", "AAAMMMAMMMAAAAXAAMXMMMAMXMASMSMMAMXMASAMAXMMXMAMAMXAAAMSMXASMSMSASXSMMMMMSSMMSSMXSAMMMMMMSMMSXMAAXSAAASASMXSAMXXMXMMSMSASXMSASMSMSSXAMSMSASX", "SMXSASMSMMMSMMMSSSXXAMXMAMAMMAXSMSMSAMXSMXXMASMSXSXMSMXASXAMXAASXSAMXAAAXMASAXAMAXAXSXMSAXAAMAMSMAASMMSAMXAMAXMASXMAMMSMSAMXASAAXMAMXSAASAMA", "XXAMAMAAXAAMXAAAAMMSXSMSXSAXXAXSAAAMMMMMAMSSMSASAXXMAXXAMXMSMMMMMMMMSXSMMSAMXSAMAMMMSAAMSSMMSAMAMXMMXAMAMMXMXAXSXMMASXMXMAAMAMMMMXMMMMMMMSMM", "SMSMSMSMSMSSMMXXSAMSASASAMXSMSSMSSSMSASMAMAAXMAMMMXMASMMMXMAMMAMAAAXMAMAMXSAMXXMASAASMMMAMMAMXSXMMXMSMSMMASXSMSMXAXASMMMASAXMASMXXAAAXMAAXMX", "XAXAMAXAAAAXXAXSMXSMAMSMAMAXXMAAAMAASXSSMSSMMMMMMXXSAMXAMAMAMSASMXSAMAMAMMMMXMSAMAMMMAAMXXAXSAXMXAAAXMAXSAXMMSAMSSMASAMAAXSXMASAASMMMSSMXSAM", "MSMAMSMSMSSSMMMXASXMXMXXXMASMSMMMSMMMMXAMAXXAXAAMMXMXMXASAXAMSASAAMMMXSXMSAXSAMXXMMSSSMSMSXMAXMSASMMSSMXMSSSXXMMAAMAMXMMSXMMSAMMMMSAMXXMSAMX", "SMSXMAMXXAAMASAMMSAMXAMXXMSAMXXMASMAAMMMMMSSMMSASXMMASMXSMMSAMXMMMMAMMMMAMXMAASAMXXAXMAXAAXSAMSXMAAAAAMSAMXMAMXMSSMASAMXMASAMASXMASMMXAXMASA", "XAAMSMSSMSMSAMXSASAMAAXMSMMMSMMMAXMSXSAXAXXASAXXXMASASMMMMAMASASXSMMMAAASXMMSMMXAAMMSMMMSMMMAMAMXSMMSSMMXSAMAMXMAAMXSMSAXAMAMAMAMASXMXMASXMM", "MXMAAXMAAAMMXSSMMSAMSMXMASAAAASMSSXMASMSMMSAMXSSMSXMAMMAMMXXMMMMAMASMSSXMASAMAXXMSSXAASXXASMMMASMMAAAAAAASASASXMXSMXXAMAMSSMMSSSMAXAXAMXMSSS", "ASMSSSMMSMXMAMXAXMMMAAMSASMMSSMAAAMSASXSAAAAXAXAXAMMSMSSSMSMXAXMAMAMAMXASXMASXMASAXXSSMASAMASXSMASMMSSMMMSXSXSXSAXAMMMSSXMAXAXAMMSSSMSXXMAMX", "SXAAXAXMMXMASASMMMSSMSMMASAAMAMMMSMXASASMMXXMXMASMSMMAMAXAAAMMSXSSMMXMXXMASAMAXMXXSAMAMXMXMMMXASAMAAXXAXXMXSAMAMAMSAAXAXMXMMXMSMMAAAAXAXMXSM", "XMMMSAMXMMSAMAXMASMSXAXMMMXMSAMMXAXXXMXMASMXMXSAXMAXMAMAMMMSAASMMAXMSSXMMAMMSMAMAAMMXAMXMAMAMSMMXSMSSSSMASAMAMMMXMASMMSXSASAMMAMMMSMSMMMSMAM", "MAAAAAAXXAAAMMMSMSAMSAMSAMXXSAMXSMMXSAXMAAXSAMMMSSSSSMMXSXAXMMMMSAMXAAXMMSXMAXAMAMSSSSSSSMXAMMSMAXAXAAMSMMASAMXMMAMAMXMASASAXSASXXAXXAAAXMAM", "SSMSSMMMMXMAMXAMMMMMMMASAXXAXMMXXAAASXSMSMSASXAXXAXXAXMASMSMXMAAMXMMMSSXAMASMSMSMMAAAAAAAASMSMAMMMMMMMMAXXAMXSAMSMMMSAMAMXSMMSXSXXMXSMMXSMSS", "MXMXMMASXSXAMAXMSMAXXSAMMSASAMSSSMMMSAMXMXAMXSMMMMMSAMMXXAXXXMASMMMAXAMMASAMAAAAMMMMMMMMMMXAAXXSAXMAXASXXSAMASMXAAAAXXSAMXXMASXMMMMMSXXAMAXA", "MAMXMSMSAMXSMMXMAAAXXMASAMXXAXAAMXMAMAMASMMXXAMXAAAMXASMMSMSMMAAASXAMASAMMXMXXMASXSAMXXXSMMSMMMSASMXMAXAASXMAMMXSSMSMASAXXAMASAXAAAAXAMSSSMA", "SMSAAAXXXMAMAMASMSXXAMXMMSSSMMMSMAMASAMASMXMSMMSSMSXSSMAXAAASMXSAMMMSAXMAMXMASMXXAXAXXSXAMMXMXXSAMAMMSMMXMSMSXSAAXAXMASMMSXMXSMMSMXXMXMAAASX", "AASMSMSXAMXSASAMXAASAMAMXAAAXAAAXASASAMASXAAAAMXMAAMSAMSSMSASMAMAXSAMXSMXSAMMXMMMMSMMMMSMSMAMSMMAMAXAXAXSAMXMAMMSMMMMASAAXAXAXXAMMSMXAMMSMAX", "MMMXAAXMAMXSAMXSMXMSASASXMSMMSSSSXSASAMXSXMSSSMAMMMMSAMMSXMASMXSXMSAMXMAASASAAAAAXAXAXAAXAMMSAASAMXMASAMXSMAMAMAAAASMASMMSXMMSMMSAAASXSAAXMS", "XSXSMSMXSMXMAMSAMMMSMSXSXXMAXAMMMASAMXMASMMAMXXSMXSAMXSMSXMAMMMAMXMXXMASMSAMMSSSMSAMXSSSSXSMSAMSSSXMAMXAMXSXSXMSSSMSAMXMXMASXXMSMMSMMMMXSSXM" ]

grid: np.array = np.array(list(map(list, word_search)))

def matrix_diagonals(mat: np.array) -> list[list[any]]:
    return [mat.diagonal(i).tolist() for i in range((mat.shape[0] * -1) + 1, mat.shape[1])]

rows = grid.tolist()
columns = grid.T.tolist()
forward_diagonals = matrix_diagonals(grid)
backward_diagonals = matrix_diagonals(np.fliplr(grid))

omnidirectional_slices = rows + columns + forward_diagonals + backward_diagonals
omnidirectional_slices += list(map(lambda x: list(reversed(x)), omnidirectional_slices))

needle = ['X', 'M', 'A', 'S']
haystack: list[list[int]] = [h[i:i+len(needle)] for h in omnidirectional_slices for i in range(len(h) - len(needle) + 1)]

problem1Solution = len(list(filter(lambda x: x == needle, haystack)))

print(problem1Solution)

needle = ['M', 'A', 'S']
subgrids = [grid[i:i+3, j:j+3] for i in range(grid.shape[0] - len(needle) + 1) for j in range(grid.shape[1] - len(needle) + 1)]

def grid_contains_xmas(subgrid: np.array) -> bool:
    return subgrid[1][1] == 'A' and sorted([subgrid[0][0], subgrid[2][2]]) == ['M', 'S'] and sorted([subgrid[0][2], subgrid[2][0]]) == ['M', 'S']

problem2Solution = len(list(filter(grid_contains_xmas, subgrids)))

print(problem2Solution)
