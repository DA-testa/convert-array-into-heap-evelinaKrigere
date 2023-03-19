# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    for i in range(n//2,-1,-1):
        minimala(i,data,swaps)

    return swaps

def minimala(i,data,swaps):
    n=len(data)

    labais=2*i+2
    kreisais=2*i+1

    mazakais=i

    if labais<n and data[labais]<data[mazakais]:
        mazakais=labais
    if kreisais<n and data[kreisais]<data[mazakais]:
        mazakais=kreisais
    if mazakais !=i:
        data[i],data[mazakais]=data[mazakais],data[i]
        swaps.append((i,mazakais))
        minimala(mazakais,data,swaps)






def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    ievade = input()
    if "I" in ievade:
        n = int(input())
        data = list(map(int, input().split()))
    elif "F" in ievade:
        file_n = input()
        with open('test/'+file_n, 'r') as f:
            n = int(f.readline())
            data = list(map(int, f.readline()))


    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))

    assert len(swaps) <= 4 * n
    print(len(swaps))





    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
