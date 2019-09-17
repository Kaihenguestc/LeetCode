import numpy

def dailyTemperatures(T):
    stack, r = [], [0] * len(T)
    for i, t in enumerate(T):
        while stack and T[stack[-1]] < t:
            r[stack.pop()] = i - stack[-1]
        stack.append(i)
    return r

if __name__ == '__main__':
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    print(dailyTemperatures(T))
