import descTree
import math

valuesMap = {}
class DecisionTree:

    def decisionTree(self, rows, attValues, attNames, initData, first):
        global valuesMap
        if len(rows) == 0:
            return descTree.getPlurality(initData)
        elif descTree.treeInfo(rows):
            classification = rows[0][1]
            return classification
        elif len(attValues) == 0:
            return descTree.getPlurality(rows)
        else:
            gains = []
            for attribute in range(len(attValues[0])):
                values = []
                attributeValue = []

                for row in range(len(rows)):
                    attributeValue.append(attValues[row][attribute])
                    if attValues[row][attribute] not in values:
                        values.append(attValues[row][attribute])

                if first:
                    valuesMap[attNames[attribute]] = values
                gains.append((attribute, attNames[attribute], descTree.calcInfoGain(attributeValue, rows)))
            biggestGain = ('Place_Holder', 'Place_Holder', -math.inf)

            for gain in gains:
                if gain[2] > biggestGain[2]:
                    biggestGain = gain

            tree = [(biggestGain[0], biggestGain[1])]
            index = biggestGain[0]
            vals = valuesMap[biggestGain[1]]

            for val in vals:
                examples = []
                i = 1
                for att in attValues:
                    if att[index] == val:
                        examples.append((i, att))
                    i = i + 1

                newExamples = []
                newAttributes = []

                for i in range(len(examples)):
                    newExamples.append((examples[i][0], rows[examples[i][0] - 1][1]))
                    newAttributes.append(examples[i][1])
                subTree = self.decisionTree(newExamples, newAttributes, attNames, rows, False)
                tree.append(((biggestGain[1] + ', Type: ' + val), subTree))

            return tree

    def printDecTree(self, tree):
        printTree = []
        for i in tree:
            if 'Attribute: ' in i[1]:
                print(i[0], i[1])
            elif 'yes' in i[1] or 'no' in i[1]:
                print(i[0] + ', Decision: ' + i[1])
            else:
                printTree.append((i[0], i[1]))

        for i in printTree:
            print(i[0] + 'Decision => ')
            self.printDecTree(i[1])