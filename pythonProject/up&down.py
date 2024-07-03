import random

random_number = random.randint(1, 100)
# print(random_number)
attempts = 0


while True:
    try:
        guess = int(input("1부터 100사이의 숫자를 유추해보세요. :"))
        attempts += 1

        if guess > 100 or guess < 1:
            print("1-100중의 숫자를 입력하세요.")
            continue

        if guess < random_number:
            print("더 큰 수 입니다.")
        elif guess > random_number:
            print('더 작은 수 입니다.')
        else:
            print(f"정답! {attempts}번 만에 숫자를 맞췄어요.")
            play_again = input("게임을 다시 시작하시겠습니까? (yes/no): ")

            if play_again.upper() == 'yes':
                random_number = random.randint(1, 100)
                # print(random_number)
                attempts = 0
                print("새로운 게임을 시작합니다.")
                continue

            else:
                print("게임을 종료합니다.")
                break

    except ValueError:
        print("1-100중의 숫자를 입력하세요.")




