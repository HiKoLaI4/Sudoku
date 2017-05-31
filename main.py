import numpy as np
import time

#плохая идея работатьчерез глобальнуюпеременную, нопокадругих нет
res = 0
#значения res: 
#0 все ОК
#1 повтор в строке
#2 повтор в столбце
#3 повтор в регионе
#5 решено


#функция оптимизации судоку
def Optimaze (Sud, n, m):
    #убрать в своем списке
    for i in range(1, 10): 
        Sud[n][m][i] = 0
    
    #убрать в своей строке и столбце
    for i in range(0, 9):
        Sud[n][i][Sud[n][m][0]] = 0
        Sud[i][m][Sud[n][m][0]] = 0
    
    #убрать в своем регионе
    for i in range(0, 3):
        for j in range(0, 3):
            Sud[(n//3)*3 + i][(m//3)*3 + j][Sud[n][m][0]] = 0
    
    return Sud

#проверка на противоречия
def Prover(Sud):
    global res
    res=0
    #проверяемая линия
    line = list()
    
    #проверка строк
    for i in range(0, 9):
        line = []
        for j in range(0, 9):
            if (Sud[i][j][0] != 0):
                if (Sud[i][j][0] in line):
                    res = 1
                    i = 9
                    j = 9
                else:
                    line.append(Sud[i][j][0])
    
    #проверка столбцов
    if (res == 0):
        for j in range(0, 9):
            line = []
            for i in range(0, 9):
                if (Sud[i][j][0] != 0):
                    if (Sud[i][j][0] in line):
                        res = 2
                        i = 9
                        j = 9
                    else:
                        line.append(Sud[i][j][0])    
    #проверка региона
    if (res == 0):
        #циклы по регионам
        for n in range(0, 3):
            for m in range(0, 3):
                line= []
                #циклы по цифрам внутри региона
                for i in range(0, 3):
                    for j in range (0, 3):
                        if (Sud[(n*3)+i][(m*3)+j][0] !=0):
                            if (Sud[(n*3)+i][(m*3)+j][0] in line):
                                res = 3
                                i = 3
                                j = 3
                                n = 3
                                m = 3
                            else:
                                line.append(Sud[(n*3)+i][(m*3)+j][0])
    #проверка оставшихся вариантов
    for i in range(0, 9):
        for j in range (0, 9):
            s = 0
            for n in range(0,10):
                s+=Sud[i][i][n]
            if (s == 0):
                res = 4
                i = 9
                j = 9
                n = 10
                
    #значения res: 
    #0 все ОК
    #1 повтор в строке
    #2 повтор в столбце
    #3 повтор в регионе
    #5 решено
    
    return res

def Predpoloj(Sud):
    
    return Sud

#вывод судоку
def SudokuPrint(Sud):
    for i in range(0,9):
        for j in range(0,9):
            print (Sud[i][j][0], end = ' ')
            if ((j+1)%3 == 0):
                print('|', end = '')
        if ((i+1)%3 == 0):
            print('\n---------------------', end = '')
        print ('\n')

    return



def Reshen(Sud):
    #rechen - результат проверки
    global res
    #проверяем варианты вынужденного решения
    progress = 0
    for i in range(0, 9):
        for j in range(0, 9):
            s = 0
            if (Sud[i][j][0]==0):
                for n in range(1,10):
                    s += Sud[i][j][n]
                    if (s>1):
                        n=10
                if (s == 1):
                    for n in range(0, 10):
                        if (Sud[i][j][n] == 1):
                            t = n
                    Sud[i][j][0] = t
                    Sud = Optimaze(Sud, i, j)
                    progress += 1
    SudokuPrint(Sud)
    print(res)
    print('=================================================')
    
    #проверяем решено ли
    res = 5
    for i in range (0, 9):
        for j in range(0, 9):
            if (Sud[i][j][0] == 0):
                res = 0
                break
        if (res == 0):
            break
                
    if(res == 5):
        return Sud
    else:
    #если вынужденные решения были то проверяем еще раз
        if (progress > 0 ):
            Sud = Reshen(Sud)
        else:
            p = Prover(Sud)
            if (p ==0):
                Sud = Predpoloj(Sud)
            else:
                return Sud
        
        
    return Sud



#начальная инициализация
Sudoku = np.array([[[0,1,1,1,1,1,1,1,1,1] for i in range(0,9)] for j in range(0,9)])

    
# вывод судоку и решалок
#print (Sudoku)
#print('\n\n')
#Sudoku[строка][столбец][цифра]    


# вводим судоку
#for i in range(0, 9):
#    line = input('строка \n')
#    for j in range(0, 9):
#        Sudoku[i][j][0] = line[j]
#11145
Sudoku[0][0][0] = 9
Sudoku[0][5][0] = 5
Sudoku[0][8][0] = 7

Sudoku[1][1][0] = 2
Sudoku[1][5][0] = 8
Sudoku[1][6][0] = 4

Sudoku[2][0][0] = 4
Sudoku[2][2][0] = 6
Sudoku[2][3][0] = 2
Sudoku[2][4][0] = 9
Sudoku[2][6][0] = 8
Sudoku[2][7][0] = 3

Sudoku[3][1][0] = 9
Sudoku[3][5][0] = 4
Sudoku[3][6][0] = 5
Sudoku[3][8][0] = 2

Sudoku[4][2][0] = 2
Sudoku[4][4][0] = 3
Sudoku[4][6][0] = 9

Sudoku[5][0][0] = 6
Sudoku[5][2][0] = 7
Sudoku[5][3][0] = 9
Sudoku[5][5][0] = 1
Sudoku[5][7][0] = 4

Sudoku[6][1][0] = 8
Sudoku[6][2][0] = 9
Sudoku[6][4][0] = 7
Sudoku[6][5][0] = 2
Sudoku[6][6][0] = 1
Sudoku[6][8][0] = 6

Sudoku[7][2][0] = 1
Sudoku[7][3][0] = 8
Sudoku[7][7][0] = 9

Sudoku[8][0][0] = 5
Sudoku[8][3][0] = 6
Sudoku[8][8][0] = 3
        
# вывод судоку
print('\n\n')
SudokuPrint(Sudoku)

TimeWork = time.time()
#первое приблежение
for i in range(0, 9):
    for j in range(0, 9):
        if (Sudoku[i][j][0] != 0):
            Sudoku = Optimaze(Sudoku, i, j)

print('========================================================')
p = Prover(Sudoku)

#рекурсивный поиск решения
if (p != 0):
    print('\n ',p)
else:
    Sudoku = Reshen(Sudoku)

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
if(res == 5):
    SudokuPrint(Sudoku)
    print (res)

TimeWork = -(TimeWork - time.time())
print(TimeWork)
#5306
#008030005
#600001000
#007000020
#050002004
#040600090
#700000050
#020000600
#000900001
#800060300