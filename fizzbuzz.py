# fizz buzz fizzbuzz 셋 중 하나를 출력하는 함수
# 3 : fizz / 5 : buzz / 15 : fizzbuzz
def do_fizzbuzz(num):
    for i in range(1, num + 1):
        if i%15 == 0:
            print('fizzbuzz')
        elif i%3 == 0:
            print('fizz')
        elif i%5 == 0:
            print('buzz')
        else:
            print(f'{i}')

if __name__ == '__main__':
    do_fizzbuzz(16)