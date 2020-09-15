class Solution:
    def maxCandies(self, candies, coin, n):
        # write code here
        plus = [i * j for i, j in zip(candies, coin)]
        zy = [sum(plus[:n])]
        for i in range(n, len(plus)):
            zy.append(zy[-1] + plus[i] - plus[i - n])
        return sum(candies) - sum(plus) + max(zy)


res = Solution().maxCandies([3, 5, 7, 2, 8, 8, 15, 3], [1, 0, 1, 0, 1, 0, 1, 0], 3)
print(res)


class Solution:
    def getMaxArea(self, x1, y1, x2, y2, x3, y3, x4, y4):
        # write code here
        jx = [[1 for j in range(10)] for i in range(10)]
        # for i in range(10):
        #     for j in range(10):
        #         if x1 <= i < x2 and y1 <= j < y2:
        #             pass
        #         elif x3 <= i < x4 and y3 <= j < y4:
        #             pass
        #         else:
        #             jx[i][j] = 1
        for i in range(x1, x2):
            for j in range(y1, y2):
                jx[i][j] = 0
        for i in range(x3, x4):
            for j in range(y3, y4):
                jx[i][j] = 0
        res = 0

        # import numpy as np
        # jxn = np.array(jx)
        print('-------------------')
        for d in jx:
            print(d)
        print('-------------------')

        def nsum(a1, b1, c1, d1):
            lines = jx[a1:c1 + 1]
            r = 0
            for ll in lines:
                r += sum(ll[b1:d1 + 1])
            return r

        for a in range(10):
            for b in range(10):
                for c in range(a, 10):
                    for d in range(b, 10):
                        # print('nsum(a,b,c,d), np.sum(jxn[a:c + 1, b:d + 1]) ',
                        # nsum(a, b, c, d) == np.sum(jxn[a:c + 1, b:d + 1]), a, b, c, d, nsum(a, b, c, d),
                        # np.sum(jxn[a:c + 1, b:d + 1]), (c - a + 1) * (d - b + 1))
                        # if np.sum(jxn[a:c + 1, b:d + 1]) == (c - a + 1) * (d - b + 1):
                        if nsum(a, b, c, d) == (c - a + 1) * (d - b + 1):
                            res = max(res, (c - a + 1) * (d - b + 1))
        return res


res = Solution().getMaxArea(2, 0, 3, 8, 7, 7, 9, 10)
print(res)

# import numpy as np
#
# jx = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# jxn = np.array(jx)
# for a in range(3):
#     for b in range(3):
#         for c in range(a, 3):
#             for d in range(b, 3):
#                 print(a, b, c, d, np.sum(jxn[a:c + 1, b:d + 1]), (c - a + 1) * (d - b + 1))
#                 if np.sum(jxn[a:c + 1, b:d + 1]) == (c - a + 1) * (d - b + 1):
#                     print('==')
