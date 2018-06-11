if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_score = 0
    b_score = 0
    for i in range(3):
        if a[i] > b[i]:
            a_score += 1
        elif b[i] > a[i]:
            b_score +=1
    print(a_score,b_score)
         
