import random

def main():
    seed = 987
    play_bulls_and_cows(seed)

def contains(a, b):
    for i in range(len(a)):
        if a[i] == b:
            return True
    return False

def generate_secret_digits(seed):
    random.seed(seed)
    digits = [-1, -1, -1, -1]
    a = random.randint(0, 9)
    for i in range(len(digits)):
        while True:
            if contains(digits, a):
                a = random.randint(0, 9)
            else:
                digits[i] = a
                break
    return digits

def get_num_of_bulls(a, b):
    counter_bulls = 0
    try:
        if len(a) != len(b):
            raise ValueError()
        else:
            for i in range(len(a)):
                if a[i] == b[i]:
                    counter_bulls += 1
    except ValueError:
        print("Arrays must have the same length")
    return counter_bulls

if __name__ == "__main__":
    main()
