import re

def writeToFile(text):
    open('CodeInst.txt', 'w').close()
    f = open("CodeInst.txt", "a")
    for item in text:
         f.write("%s\n" % item)

    f.close()


def instrmentationAtCodeStart(codeReadedLines,insertIndex):
    s1 ='using namespace std;\n'
    s2 ='using namespace std::chrono;\n'
    s3 ='ofstream Prof("Profiler.txt");\n'
    s4='ofstream Path("Path.txt");\n'
    s5='auto baseLineMilliseconds = high_resolution_clock::now();\n'
    s6=''
    codeInserted = [s1,s2,s3,s4,s5,s6]
    newIndex=insertIndex+len(codeInserted)
    for i in range(0, 5):
        codeReadedLines.insert(insertIndex+i+1,codeInserted[i])
    return codeReadedLines, newIndex

def instrmentationAtFunctionStart(codeReadedLines,insertIndex,codeName):
    s1 = ''
    if 'main' in codeName:
        s1='baseLineMilliseconds = high_resolution_clock::now();\n'
    s2 ='auto  startTime = high_resolution_clock::now();\n'
    s3 ='auto durationStart = duration_cast<microseconds>(startTime - baseLineMilliseconds).count();\n'
    s4 ='Prof << "Start '+codeName +' Function @" << durationStart << " microS" << endl;\n'
    s5=''
    codeInserted = [s1,s2,s3,s4,s5]
    newIndex=insertIndex+len(codeInserted)-1
    for i in range(0, len(codeInserted)-1):
        codeReadedLines.insert(insertIndex+i+1,codeInserted[i])
    return codeReadedLines, newIndex

def instrmentationAtFunctionEnd(codeReadedLines,insertIndex,codeName,functionType,argument):
    s1 = ''
    s5 = ''
    if (functionType == 'double'):
        s1 = 'double INSERTEDVALINSTR =' + argument
    elif (functionType == 'int'):
        s1 = 'int INSERTEDVALINSTR =' + argument
    elif (functionType == 'float'):
        s1 = 'float INSERTEDVALINSTR =' + argument

    s2 ='auto  endTime = high_resolution_clock::now();\n'
    s3 ='auto durationEnd = duration_cast<microseconds>(endTime - baseLineMilliseconds).count();\n'
    s4 ='Prof << "End '+codeName +' Function @" << durationEnd << " microS" << endl;\n'
    if not (functionType=='void'):
        s5 ='return INSERTEDVALINSTR ;'

    codeInserted = [s1,s2,s3,s4,s5]
    newIndex=insertIndex+len(codeInserted)
    for i in range(0, len(codeInserted)):
        codeReadedLines.insert(insertIndex+i+1,codeInserted[i])
    return codeReadedLines, newIndex

def functionStartEndIndexChecker (codeline):
    functionType=''
    foundval=False
    argument=''
    if('{' in codeline or '}' in codeline):
        foundval=True
    if ('void'in codeline):
        functionType='void'
    elif('int'in codeline):
        functionType = 'int'
    elif ('double' in codeline):
        functionType = 'double'
    elif ('float' in codeline):
        functionType = 'float'
    elif ('return' in codeline):
        argument= codeline.replace('return','')
        foundval=True

    return foundval , functionType,argument

def regexFunctionChecker(codeLine):
    patternToMatch = '(int |float |double |void )(.)+\((.)*\) *({)?'
    result = re.findall(patternToMatch, codeLine)
    if not result:
        return False
    else:
        return True

def readFileLineByLine():
    codeFile = open("TestCode.txt", "r")
    readedCode =codeFile.readlines()
    codeFile.close()
    return readedCode

def automatedCodeInstrumentation():
    starEndIndexing = []
    endFunctionCandidate =0
    startStateFlag = True
    codeReadedLines = readFileLineByLine()
    functionName=''
    isRegex = True
    index =0
    firstFunction= True
    foundVal = False
    functionType = ''
    argumentVal=''
    while index < (len(codeReadedLines) - 1):
        if regexFunctionChecker(codeReadedLines[index]):
            functionName=codeReadedLines[index]
            isRegex = False
            if firstFunction:
                firstFunction=False
                codeReadedLines, index = instrmentationAtCodeStart(codeReadedLines, index-1)
        if isRegex == False :
            foundVal,functionType,argument=functionStartEndIndexChecker(codeReadedLines[index])
            if not (argument== ''):
                argumentVal=argument
                codeReadedLines[index]='\n'

            if foundVal:
                if startStateFlag:
                    starEndIndexing.append(index)
                    codeReadedLines,index = instrmentationAtFunctionStart(codeReadedLines, index, functionName)
                    startStateFlag = False
                elif regexFunctionChecker(codeReadedLines[index]):
                    startStateFlag=True
                    starEndIndexing.append(endFunctionCandidate)
                    codeReadedLines,index=instrmentationAtFunctionEnd(codeReadedLines,endFunctionCandidate-1,functionName,functionType,argumentVal)
                    endFunctionCandidate = -1
                    isRegex = True
                    index-=1
                else:
                    endFunctionCandidate = index
        index = index + 1

    codeReadedLines, index = instrmentationAtFunctionEnd(codeReadedLines, endFunctionCandidate - 1, functionName, "int", argumentVal)
    starEndIndexing.append(endFunctionCandidate)


    writeToFile(codeReadedLines)




if __name__ == '__main__':
    automatedCodeInstrumentation()



