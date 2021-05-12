# 프로그래머스, 완주하지 못한 선수

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        front_number_length = len(phone_book[i])
        if phone_book[i] == phone_book[i + 1][:front_number_length]:
            return False
    return True

if __name__ == '__main__':
    phone_book = ["119", "97674223", "1195524421"]  # False
    # phone_book = ["123", "456", "789"]  # True
    print(solution(phone_book))
