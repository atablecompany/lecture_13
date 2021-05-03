
def recursive_nth_fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        output = recursive_nth_fibo(n - 1) + recursive_nth_fibo(n - 2)
        return output


def main():
    print(recursive_nth_fibo(n=7))


if __name__ == '__main__':
    main()
