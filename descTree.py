import pandas as pd
import math
import DecTreeClass

def getPlurality(rows):
    counter = {}
    for row in rows:
        if row[1] not in counter.keys():
            counter[row[1]] = 1
        else:
            counter[row[1]] = counter[row[1]] + 1
    value = max(counter, key=counter.get)
    return value


def calcEntropy(value):
    return -1 * (value * math.log2(value) + (1-value) * math.log2(1-value))

def calcInfoGain(attVal, results):
    branches = {}
    for i, j in zip(attVal, range(len(results))):
        if results[j][1] == 'yes':
            if i not in branches.keys():
                branches[i] = [1, 1]
            else:
                branches[i][0] = branches[i][0] + 1
                branches[i][1] = branches[i][1] + 1
        else:
            if i not in branches.keys():
                branches[i] = [0, 1]
            else:
                branches[i][1] = branches[i][1] + 1

    entropy = 0
    for attributeType in branches.keys():
        p = float(branches[attributeType][1] / len(results))
        value = float(branches[attributeType][0]) / float(branches[attributeType][1])

        if value != 0 and (value-1) != 0:
            entropy = entropy + (p * calcEntropy(value))

    informationGain = 1-entropy
    return informationGain


def treeInfo(rows):
    classification = rows[0][1]
    for i in range(len(rows)):
        if rows[i][1] != classification:
            return False
    return True

def parseFile(fileName):
    rows = []
    attributes = []
    file = pd.read_csv(fileName, header=0)
    columnNames = list(file.columns.values)

    rowMatrix = file[columnNames[0]].values
    attributeMatrix = file.drop([columnNames[0], columnNames[-1]], axis=1).values
    classMatrix = file[columnNames[-1]].values

    for x, y, z in zip(rowMatrix, attributeMatrix, classMatrix):
        rows.append((x, z))
        attributes.append(list(y))
    return rows, attributes, columnNames



if __name__ == '__main__':
    rows, attributes, columnNames = parseFile('restaurant.csv')

    DecTree = DecTreeClass.DecisionTree()
    finalDecisionTree = DecTree.decisionTree(rows, attributes, columnNames[1:], [], True)
    DecTree.printDecTree(finalDecisionTree)