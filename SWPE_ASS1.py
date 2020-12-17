import os
import re
def writeToFile(text):
    open('CodeInst_Output.cpp', 'w').close()
    f = open("CodeInst_Output.cpp", "a")
    for item in text:
         f.write("%s\n" % item)

    f.close()
    
def instrmentationAtCodeStart(codeReadedLines,insertIndex):
    s1='#include <iostream>\n'
    s2='#include<stdio.h>\n'
    s3='#include <chrono>\n'
    s4 ='#include <fstream>\n'
    s5 ='using namespace std;\n'
    s6 ='using namespace std::chrono;\n'
    s7 ='ofstream Prof("FunctionEventLog_Output.txt");\n'
    s8='ofstream Path("CCT_Output.txt");\n'
    s9='auto baseLineMilliseconds = high_resolution_clock::now();\n'
    s10=''
    codeInserted = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]
    newIndex=insertIndex+len(codeInserted)
    for i in range(0, len(codeInserted)):
        codeReadedLines.insert(insertIndex+i+1,codeInserted[i])
    return codeReadedLines, newIndex

def codeNameModifier(codeName):
    functionName=''
    state = False
    if ('void' in codeName):
        codeName=codeName.replace('void ', ' ')
    if ('int' in codeName):
        codeName=codeName.replace('int ',' ')
    if ('double' in codeName):
        codeName=codeName.replace('double ',' ')
    if ('float' in codeName):
        codeName= codeName.replace('float ',' ')
    if ('(' in codeName):
        codeName=codeName.replace('(', ' ')
    if (')' in codeName):
        codeName=codeName.replace(')', ' ')
    if ('{' in codeName):
        codeName=codeName.replace('{', ' ')
    for i in range(0,len(codeName)) :
        if codeName[i]==' ':
            state= True
        elif state:
            functionName=functionName+codeName[i]
            if codeName[i+1]==' ':
                break
    return functionName

def codeBracesStyler(codeLine,codeLines,index):
    i = 0
    countOpen=0
    countClose=0
    last=0
    codeLines[index] = ''
    while i < len(codeLine):
        codeLines[index] = codeLines[index]+codeLine[i]
        if (codeLine[i] == '{'):
            break
        i = i + 1
    codeLines.insert(index + 1, codeLine[i+1:len(codeLine)])

    if '}' in codeLines[index+1]:

       countClose= codeLines[index+1].count('}')
       countOpen =codeLines[index+1].count('{')
       if not(countClose-countOpen)==0:
           last=codeLines[index+1].rfind('}')
           codeLines[index+1]= codeLine[i+1:last+i+1]
           codeLines.insert(index + 2, '}')

    return codeLines

def instrmentationAtFunctionStart(codeReadedLines,insertIndex,codeName):
    s1 = ''
    if 'main' in codeName:
        s1='baseLineMilliseconds = high_resolution_clock::now();\n'
    s2 ='auto  startTime = high_resolution_clock::now();\n'
    s3 ='auto durationStart = duration_cast<microseconds>(startTime - baseLineMilliseconds).count();\n'
    s4 ='Prof << "Start '+codeName +' Function @" << durationStart << " microS" << endl;'
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
    changeName=True
    if ('{' in codeline or '}' in codeline):
        foundval = True
    elif ('return' in codeline):
        argument = codeline.replace('return', '')
        foundval = True
    for index in range(0,len(codeline)-1):
        if not (codeline[index]==' ') and changeName:
            functionType=functionType+codeline[index]
            if codeline[index+1] == ' ':
                changeName= False
        if codeline[index]==';':
            functionType = ''
            break

    if not(functionType=='void'or functionType=='int'or functionType=='double'or functionType=='float'):
        functionType=''
    return foundval , functionType,argument

def regexFunctionChecker(codeLine):
    patternToMatch = '((int |float |double |void )((?!=).)*\((.)*\) *){'
    result = re.findall(patternToMatch, codeLine)
    if result:
        return True
    else:
        return False

def readFileLineByLine():
    codeFile = open("InputCode.txt", "r")
    readedCode =codeFile.readlines()
    codeFile.close()
    return readedCode

def automatedCodeInstrumentation():
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
            codeReadedLines=codeBracesStyler(codeReadedLines[index],codeReadedLines,index)
            isRegex = False
            if firstFunction:
                firstFunction=False
                codeReadedLines, index = instrmentationAtCodeStart(codeReadedLines, index-1)

        if isRegex == False :
            foundVal,functionTypeDummy,argument=functionStartEndIndexChecker(codeReadedLines[index])
            if not (argument== ''):
                argumentVal=argument
                codeReadedLines[index]='\n'

            if foundVal:
                if startStateFlag:
                    functionName = codeReadedLines[index]
                    codeReadedLines, index = instrmentationAtFunctionStart(codeReadedLines, index, codeNameModifier(functionName))
                    startStateFlag = False
                elif regexFunctionChecker(codeReadedLines[index]):
                    startStateFlag=True
                    codeReadedLines , index=instrmentationAtFunctionEnd(codeReadedLines,endFunctionCandidate-1,codeNameModifier(functionName),functionType,argumentVal)
                    endFunctionCandidate = -1
                    isRegex = True
                    index-=1
                else:
                    endFunctionCandidate = index
            if not (functionTypeDummy == ''):
                functionType = functionTypeDummy
        index = index + 1

    codeReadedLines, index = instrmentationAtFunctionEnd(codeReadedLines, endFunctionCandidate - 1, codeNameModifier(functionName), "int", argumentVal)
    writeToFile(codeReadedLines)


def sim_cpp():
    os.system('g++ CodeInst_Output.cpp -o CodeInst_Compilation_Output.o')
    os.system('CodeInst_Compilation_Output.o')


def get_paths():
    codeFile = open("FunctionEventLog_Output.txt", "r")
    arr = codeFile.readlines()
    codeFile.close()
    pointerParent = None
    pointerChild = 0
    path = []
    m = 0
    queue = []
    testPath = ''
    queue.append("main")
    for i in range(1, len(arr)):
        a = arr[i].split()
        if (a[0] == "Start"):
            if (pointerParent == pointerChild):
                path.insert(m, testPath)
                m = m + 1
                testPath = ''
            testPath = queue[len(queue) - 1] + " calls " + a[1]
            queue.append(testPath)
            pointerParent = pointerChild
            pointerChild = i
        elif (a[0] == "End"):
            if (pointerChild == pointerParent):
                pointerParent = pointerParent - 1
            pointerChild = pointerParent
            if (len(queue) >= 1):
                queue.pop()
            if (len(queue) == 0):
                path.insert(m + 1, testPath )
    return path


def get_profiling(path):
    path.sort()
    count = [1]
    key_id = 0
    non_rep_path = []
    non_rep_path.append(path.pop())
    for k in range(len(path) - 1, -1, -1):
        if (non_rep_path[key_id] == path[k]):
            count[key_id] = count[key_id] + 1
            path.pop()
        else:
            key_id = key_id + 1
            count.append(1)
            non_rep_path.append(path.pop())
    return non_rep_path, count


def get_CCT(non_rep_path, count):
    file2 = open("CCT_Output.txt", "w")
    l = []
    l.extend("The Context Call Tree (CCT): \n")
    for j in range(len(non_rep_path)):
        l.append("Path " + str(non_rep_path[j]) + " is encoded as Path " + str(j) + " and is repeated " + str(
            count[j]) + " times.\n")
    file2.writelines(l)
    file2.close()
if __name__ == '__main__':
    automatedCodeInstrumentation()
    sim_cpp()
    path=get_paths()
    non_rep_path, count= get_profiling(path)
    get_CCT(non_rep_path, count)
