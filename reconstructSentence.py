import sys

def reconstruct_sentence(file1, file2):
    # Read contents of input files into lists
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        list1 = f1.readline().strip().split()
        list2 = f2.readline().strip().split()

    # Print the initial lists and lengths
    print("list1 is:", list1)
    print("list1Length:", len(list1))
    print("list2 is:", list2)
    print("list2Length:", len(list2))

    # Initialize the output list
    out = []

    # Get the length of each input list
    list1_length = len(list1)
    list2_length = len(list2)

    # Iterate through the lists to reconstruct the sentence
    for _ in range(max(list1_length, list2_length)):
        # Take a word from the end of each list
        if list1:
            out.append(list1.pop())
        if list2:
            out.append(list2.pop())

    # Reverse the output list to get the correct order
    out.reverse()

    # Print the output list
    print("The list out is:", out)

    # Write the output list to a file named output.txt
    with open('output.txt', 'w') as f3:
        for word in out:
            f3.write(word + ' ')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 reconstructSentence.py input1.txt input2.txt")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    reconstruct_sentence(file1, file2)

