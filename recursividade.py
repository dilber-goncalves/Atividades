#recursividade

#formula geral para fatorial:
# fatorial(n) = n * fatorial(n-1)
# fatorial(0) = 1
# fatorial(1) = 1

#fatorial(n) = 1, se num for 0 ou se num for 1 - caso base

def fatorial(num):
    if num == 0 or num == 1:
        return 1
    return num * fatorial(num - 1)

while True:
    if __name__ == "__main__":
        x = int(input("Digite um número: "))
        if x == 0:
            print("==Fim do programa==")
            break
        else:
            print(f"\n  {x}! = {fatorial(x)}")
            print("\n")