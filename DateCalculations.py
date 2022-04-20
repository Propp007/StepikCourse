while True:
    year = int(input("Enter year: "))
    day, month = map(int, input("Enter current date (D M) : ").split())
    day2, month2 = map(int, input("Enter second date (D M) : ").split())
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    m_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        is_leap = True
    else:
        is_leap = False

    summa_ny = sum(m[:month - 1]) + day - 1
    summa_ny2 = sum(m[:month2 - 1]) + day2 - 1
    summa_dd = (summa_ny - summa_ny2) if summa_ny >= summa_ny2 else (summa_ny2 - summa_ny)

    print("This year is", "leap" if is_leap else "not leap.")
    print(f"Your day is: {str(day).rjust(2, '0')}.{str(month).rjust(2, '0')}")
    print(f"Days from the New Year 01.01: {summa_ny}")
    print(f"Days from the first date: {summa_dd}")
