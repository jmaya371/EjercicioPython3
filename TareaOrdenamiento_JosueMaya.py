import random


def BubbleSort(List):
    for i in range(1, len(List)):
        for j in range(len(List)-i):
            if List[j] > List[j+1]:
                List[j], List[j+1] = List[j+1], List[j]
    print("BubbleSort:      ", List)


def InsertionSort(List):

    for i in range(1, len(List)):
        ElemAct = List[i]
        j = i
        while j > 0 and List[j-1] > ElemAct:
            List[j] = List[j-1]
            j -= 1
        List[j] = ElemAct
    print("InsertionSort:   ", List)


def MergeSort(List):
    LeftCnt = 0
    RightCnt = 0
    NewList = []

    if len(List) > 1:
        Med = len(List) / 2
        Left = List[:int(Med)]
        Right = List[int(Med):]

        Left = MergeSort(Left)
        Right = MergeSort(Right)

        while LeftCnt < len(Left) and RightCnt < len(Right):
            if Left[LeftCnt] < Right[RightCnt]:
                NewList.append(Left[LeftCnt])
                LeftCnt += 1
            else:
                NewList.append(Right[RightCnt])
                RightCnt += 1

        while LeftCnt < len(Left):
            NewList.append(Left[LeftCnt])
            LeftCnt += 1

        while RightCnt < len(Right):
            NewList.append(Right[RightCnt])
            RightCnt += 1

        return NewList
    else:
        return List


def SelectionSort(List):
     for i in range(len(List)-1):
        ElemMin = i
        for j in range(i+1, len(List)):
            if List[j] < List[ElemMin]:
                ElemMin = j

        List[i], List[ElemMin] = List[ElemMin], List[i]
     print("SelectionSort:   ", List)


if __name__ == '__main__':
    FirstList = random.sample(range(100), 15)
    print("Lista desordenada: ",FirstList)
    print()

    BubbleSort(list(FirstList))
    InsertionSort(list(FirstList))
    SelectionSort(list(FirstList))
    print("MergeSort:       ", MergeSort(list(FirstList)))
