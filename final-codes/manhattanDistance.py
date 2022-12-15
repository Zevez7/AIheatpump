p = (1, 1)
q = (4, 3)
def get_manhattan_distance(p, q):
    """ 
    Return the manhattan distance between points p and q
    assuming both to have the same number of dimensions
    """
    # sum of absolute difference between coordinates
    distance = 0
    for p_i, q_i in zip(p, q):
        distance += abs(p_i - q_i)

    return distance
def main():
    print(get_manhattan_distance(p,q))
    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
        main()