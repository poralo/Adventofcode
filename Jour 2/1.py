def computing(sequence):
    list_seq = [int(val) for val in sequence.split(',')]
    for i in range(0, len(list_seq), 4):
        if list_seq[i] == 99:
            return list_seq
        elif list_seq[i] == 1:
            pos_a = list_seq[i + 1]
            pos_b = list_seq[i + 2]
            pos_r = list_seq[i + 3]
            list_seq[pos_r] = list_seq[pos_a] + list_seq[pos_b]
        elif list_seq[i] == 2:
            pos_a = list_seq[i + 1]
            pos_b = list_seq[i + 2]
            pos_r = list_seq[i + 3]
            list_seq[pos_r] = list_seq[pos_a] * list_seq[pos_b]
        else:
            print("Something went wrong !")
            return

if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        print(computing(f.readline()))