from collections import Counter

def mode(num):
    try:
        num_value = len(num)
        count = Counter(num)
        result = dict(count)
        mode = [i for i, m in result.items() if m == max(list(count.values()))]
        if len(mode) == num_value:
            result = "mode has not generated"
        else:
            result = mode[0]
        return result

    except ZeroDivisionError:
        print("Watch out: You are dividing by Zero!")

