if __name__=="__main__":
    print(" Input the numbers of the first list : ")
    x = input().split()
    x = [int(i) for i in x]
    print("Input the numbers of the second list : ")
    x2 = input().split()
    x2 = [int(i) for i in x2]
    num = set(x2)
    disp_arr = []
    for i in num:
        if x.count(i)<x2.count(i):
            disp_arr.append(i)
    disp_arr.sort()
    print(disp_arr)