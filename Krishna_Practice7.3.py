#3. Create a class to find three elements that sum to zero from a set of n real numbers
#Input array: [-25,-10,-7,-3,2,4,8,10]
#Expected output: [[-10,2,8],[-7,-3,10]]


class Sum:
    set = set()
    list = []
    result = []
    def __init__(self, list):
        self.list = list
        for i in list:
            self.set.add(i)
    def solution(self):
        length = len(self.list)
        for i in range(length - 2):
            for j in range(i  + 1, length - 1):
                for k in range(j + 1, length):
                    if self.list[i] + self.list[j] + self.list[k] == 0:
                        self.result.append([self.list[i], self.list[j], self.list[k]])
        return self.result


s = Sum([-25,-10,-7,-3,2,4,8,10])
print(s.solution())
