class TwoDimensionArray:
    def rotateImage(self, matrix):
        """
        Rotate the 2D matrix clockwise in place.

        Example:
            Given input matrix =
            [
            [ 5, 1, 9,11],
            [ 2, 4, 8,10],
            [13, 3, 6, 7],
            [15,14,12,16]
            ], 

            rotate the input matrix in-place such that it becomes:
            [
            [15,13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7,10,11]
            ]
        
        Parameters:
            matrix(List[List[int]]): 2D matrix

        Return:
            None. Rotate in place.
        """        
        # iterate each layer
        layer = len(matrix) // 2 
        for i in range(layer):             
            end = len(matrix) - i - 1
            self.swapLayer(matrix, i, end)
        return

    def swapLayer(self, matrix, start, end):
        """
        Swap pixels in one layer.
        Parameters:
            matrix: 2D array
            start(int): starting x position
            end(in): ending x position
        """            
        for i in range(end - start):
            tmp = matrix[start][start + i] # save top            
            matrix[start][start + i] = matrix[end - i][start] # left to top
            matrix[end - i][start] = matrix[end][end - i] # bottom to left
            matrix[end][end - i] = matrix[start + i][end]# right to bottom
            matrix[start + i][end] = tmp # top to right
        for line in matrix:
            print(line)
            

if __name__ == "__main__":
    test = [
        [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ],
        [
            [ 5, 1, 9,11],
            [ 2, 4, 8,10],
            [13, 3, 6, 7],
            [15,14,12,16]
        ],     
        [
            [1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15],
            [16,17,18,19,20],
            [21,22,23,24,25]
        ],
        [
            [2,29,20,26,16,28],
            [12,27,9,25,13,21],
            [32,33,32,2,28,14],
            [13,14,32,27,22,26],
            [33,1,20,7,21,7],
            [4,24,1,6,32,34]
        ]
    ]
    for arr in test:
        for line in arr:
            print(line)
        TwoDimensionArray().rotateImage(arr)
        print("----------")
        for line in arr:
            print(line)
        