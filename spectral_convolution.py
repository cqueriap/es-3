#Cresencio Quereapa
#CS-327-1, Spring 2018

from collections import Counter
import heapq
import collections


def read_input(file):
    with open(file, 'r') as f:
        M = int(f.readline().rstrip('\n'))
        experimental_spectrum = f.readline().rstrip('\n').split(" ")
        experimental_spectrum = [int(i) for i in experimental_spectrum]
        experimental_spectrum.sort()
        answer_from_file = f.readline().rstrip('\n')

    m_list = convolution(M, experimental_spectrum)

    check(m_list, answer_from_file)






def check(answer_convo, answer_file):
    answer = answer_file.split(" ")
    answer_list = list(map(int, answer))
    answer_list.sort()
    answer_convo.sort()
    if answer_list == answer_convo:
        print("Passed")
    else:
        print("Fail")




def convolution(M, experimental_spectrum):
    top_M_list = []
    for i in experimental_spectrum:
        for j in experimental_spectrum:
            difference = i - j
            if 50 <= difference <= 200:
                top_M_list.append(difference)

    temp = Counter(top_M_list)
    convo_dict = collections.defaultdict(list)
    for counts, val in temp.items():
        convo_dict[val].append(counts)
    most_M = heapq.nlargest(M, convo_dict.keys())

    m_list = []
    for top_count in most_M:
        if len(m_list) <= M:
            m_list += convo_dict[top_count]

    return m_list


if __name__ == "__main__":
    read_input("P1_short.txt")
    read_input("P1_long.txt")
