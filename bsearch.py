def binary_search(seq, value):
    if len(seq) == 0:
        return False
    else:
        mid = len(seq) // 2
        if value == seq[mid]:
            return True
        elif value < seq[mid]:
            return binary(seq[:mid], value)
        elif value > seq[mid]:
            return binary(seq[mid + 1:], value)
