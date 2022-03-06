import search

'''
לפי היורסטיקה של המעבדה ישנו בממצוע לפי 1000 פעמים הרצה
[total state,max state]
[35.37, 17.508]
לפי היורסיטקה של השיעורי בית ישנו בממצוע לפי 1000 פעמיים הרצה
[total state,max state]
[28.442, 14.817]

'''
def avg(n):
    sumTotal = 0
    sumMax = 0
    for i in range(n):
        sumTotal += search.search(3)[1]
        sumMax += search.search(3)[2]
    return [sumTotal / n, sumMax / n]


if __name__ == "__main__":
    print(avg(1000))
