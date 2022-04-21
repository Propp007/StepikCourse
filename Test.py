set_proof = {chr(s) for s in range(ord('a'), ord('z') + 1)} | {str(s) for s in range(0, 10)} | {'@', '.', '_'}


def check_adress(text):
    s = set(text)
    print('ДА' if s <= set_proof and {'@', '.'} <= s else 'НЕТ')


a = input().lower()
check_adress(a)
