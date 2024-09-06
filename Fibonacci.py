def belong_fibonacci (n):
    if n == 0 or n == 1:
        return True

    a, b = 0, 1
    while b <= n:
        if b == n:
            return True
        a, b = b, a+b
    return False

num = int(input("Digite um número: "))


if belong_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci")