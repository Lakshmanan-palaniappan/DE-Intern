#This is the first question
if __name__ == '__main__':
    N = int(input())
    my_list = []
    for _ in range(N):
        command = input().split()
        operation = command[0]
        if operation == "insert":
            i, e = int(command[1]), int(command[2])
            my_list.insert(i, e)
        elif operation == "print":
            print(my_list)
        elif operation == "remove":
            e = int(command[1])
            my_list.remove(e)
        elif operation == "append":
            e = int(command[1])
            my_list.append(e)
        elif operation == "sort":
            my_list.sort()
        elif operation == "pop":
            my_list.pop()
        elif operation == "reverse":
            my_list.reverse()
#This is the second question
#Find the Percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    result=sum(student_marks[query_name])/ len(student_marks[query_name])
    print(f"{result:.2f}")
#Second Largest
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    sec_max = sorted(set(arr))
    print(sec_max[-2])
