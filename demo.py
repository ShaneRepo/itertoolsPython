import itertools

skuTable = ["5410", "5411", "5512", "5513", "5515", "6113", "6119", "6122", "6125", "6131", "6135", "6206", "6271",
            "6294", "6309", "6312", "6325", "6420", "7120", "7215", "7225", "7510", "7555", "9091",
            "9092", "T855", "T875", "T01D", "T01C", "T01B", "T02D", "T02C", "T02B", "T03D", "T03C",
            "T03B", "T04D", "T04C", "T04B", "T05D", "T05C", "T05B", "T06D", "T06C", "T06B", "T07D",
            "T07C", "T07B", "T08D", "T08C", "T08B", "T50D", "T50C", "T50B", "T51D", "T51C", "T51B",
            "T52D", "T52C", "T52B", "T103", "T105", "T113", "T237", "T399", "T401", "T724", "T725",
            "T734", "T735", "T744", "T745", "T756", "T780", "T781", "T782", "T783", "T785", "6200",
            "6290", "6418", "7203", "7207", "7403", "7404", "7406", "7407", "7408", "7410", "7411",
            "7412", "7413", "7414", "7415", "7417", "7418", "7419", "7420", "7421", "7422", "7425",
            "7426", "7427", "7432", "7433", "7436", "7437", "7438", "8004", "T874", "5412", "5415",
            "5416", "5420", "6014", "6016", "6017", "6020", "6025", "6033", "6034", "6103", "6104",
            "6111", "6112", "6114", "6115", "6117", "6118", "6120", "6121", "6123", "6124", "6129",
            "6130", "6133", "6204", "6205", "6272", "6273", "6274", "6275", "6276", "6291", "6292",
            "6293", "6315", "6320", "6321", "6322", "6410", "6412", "6414", "6416", "7216", "7218",
            "7219", "7220", "7224", "7513", "7514", "7516", "7548", "7551", "7552", "7554", "9080",
            "9085", "T870", "T872", "5520", "CF01", "CF02", "CF03", "CF04", "CF06", "CF07", "CF08",
            "CF09", "CF10", "CF11", "CF12"]
skuDesk = ["1210", "1215", "1220", "1225", "1230", "1235"]
skuChair = ["C222", "C227", "C305", "C306", "C326", "C330", "C441", "C442", "C485", "C486", "C561",
            "C562", "C735", "C736", "C761", "C762", "C802", "C803", "C805", "C806", "C826", "C830",
            "C850", "C851", "C852", "C853", "C856", "C857", "C860", "C861", "C862", "C863", "C864",
            "C865", "C946", "C947", "C956", "C957", "C961", "C962", "C966", "C967", "C978", "C979",
            "C980", "C981", "C996", "C997", "C114", "C115", "C210", "C412", "C413", "C440", "C469",
            "C504", "C505", "C560", "C765", "C800", "C801", "C900", "C915", "C950", "C955"]
skuBench = ["M204", "M212", "M214", "M215", "M216", "M222", "M223", "M231", "M232", "M233", "M234",
            "M235", "M251", "M252", "M253", "M254", "M255", "M256", "M257", "M258", "M301", "M302",
            "M310", "M315"]
skuRack = ["1734", "6706", "H423", "6013", "6018", "6023"]
skuBed = ["9113", "9114", "9130", "9131", "9132", "9133", "9138", "9140", "9141", "9154", "9155",
          "9158", "9160", "9161", "9170", "9171", "9172", "9173", "9178", "9304", "9305"]
stdMetalFinish = ["70", "73", "78", "79", "83", "87", "94"]
woodFinish = ["M-AP", "M-B", "M-C", "M-CC", "M-N", "M-OY", "M-R", "M-S", "O-AP", "O-B", "O-C", "O-D", "O-N",
              "O-R", "O-S", "O-W"]
premiumMetalFinish = ["11", "53", "15", "58", "59", "19", "31"]
woodDistressing = ["ND", "HP"]
stoneTop = ["GC", "GW"]
premiumGlass = ["GLC", "GL2", "GLF", "GLM"]
fabric = ["F27", "F28", "F29", "F30", "F31", "F32", "F33", "F34", "F35", "F36", "F37", "F38", "F39", "F40", "F41",
          "F42", "F43", "F44", "F45", "L101", "L102", "L103", "L104", "L105", "L106",
          "L107", "L108", "L202", "L203", "L204"]
counter = 0

# A function that takes a sku with wood tabletop and spits out permutations
def getComboWoodTop(skuNum):
    for combination in itertools.product(skuNum, premiumMetalFinish, woodDistressing, woodFinish, stdMetalFinish):
        print('-'.join(combination))
        global counter
        counter += 1
        print(counter)

# A function that takes a sku with glass tabletop and spits out permutations
def getComboGlassTop(skuNum):
    for combination in itertools.product(skuNum, premiumMetalFinish, premiumGlass, stdMetalFinish):
        print('-'.join(combination))
        global counter
        counter += 1
        print(counter)

# A function that takes a sku with stone tabletop and spits out permutations
def getComboStoneTop(skuNum):
    for combination in itertools.product(skuNum, premiumMetalFinish, stoneTop, stdMetalFinish):
        print('-'.join(combination))
        global counter
        counter += 1
        print(counter)

# A function that takes a sku "chair product" and spits out permutations
def getChair(skuNum):
    for combination in itertools.product(skuNum, fabric, stdMetalFinish, premiumMetalFinish):
        print('-'.join(combination))
        global counter
        counter += 1
        print(counter)

# A function that takes a sku "rack product" and spits out permutations
def getRack(skuNum):
    for combination in itertools.product(skuNum, woodFinish, woodDistressing, stdMetalFinish, premiumMetalFinish):
        print('-'.join(combination))
        global counter
        counter += 1
        print(counter)

# A function that takes a sku "bed product" and spits out permutations
def getBed(skuNum):
    for combination in itertools.product(skuNum, woodFinish, woodDistressing, stdMetalFinish, premiumMetalFinish,
                                         fabric):
        print('-'.join(combination))
        global counter
        counter += 1
        print(counter)

# Calling these functions to show the output of the combinations
#getComboGlassTop(skuDesk)
#getComboStoneTop(skuDesk)
#getComboWoodTop(skuDesk)
#getChair(skuBench)
#getRack(skuRack)
#getBed(skuBed)