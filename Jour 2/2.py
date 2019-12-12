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

def change_input(inp, noun, verb):
    new_input = inp.split(',')
    new_input[1] = str(noun)
    new_input[2] = str(verb)
    return ','.join(new_input)

if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        basic_input = f.readline()
        for i in range(0, 99):
            for j in range(0, 99):
                inp = change_input(basic_input, i, j)
                output = computing(inp)
                if output[0] == 19690720:
                    print(f'noun = {output[1]}; verb = {output[2]}')
                    print(100 * output[1] + output[2])
                    break