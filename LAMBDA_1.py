def main():
    while True:
        name = str(input('Чтобы продолжить, не вводите off:'))
        genius = lambda name: print('genius', name)
        if name != 'off':
            genius(str(input()))
        else:
            break

if __name__ == "__main__":
  main()
