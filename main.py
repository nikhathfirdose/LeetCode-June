# Arrays and Stringd - 2D array
class Solution:
    def generate(self, num_rows):
        triangle = []

        for row_num in range(num_rows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num+1)]
            # print(row)
            row[0], row[-1] = 1, 1
            # print(row)

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]
                # print(row)
            triangle.append(row)

        return triangle