import random
import sys

def main():
    names = ['Alice', 'Bob', 'Fred', 'Jess', 'Logan', 'Anna', 'Hunter', 'Andrew', 'Dakota', 'Isabella', 'Jon']
    name_len = len(names)
    for _ in range(1, 100000):
        print('|'.join([names[random.randint(0, name_len-1)] for _ in range(10)]))
        print('This is an error', file=sys.stderr)
if __name__ == '__main__':
    main()
