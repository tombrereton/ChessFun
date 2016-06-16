def main():

    # initialise board
    def BoardStructure():
        import numpy as np
        BoardArray = np.zeros((12, 12))
        print(BoardArray)

        # make the bordering two rows illegal for movement
        BoardArray[np.r_[0:2, -2:0]] = None
        BoardArray[:, :2] = None
        BoardArray[:, -2:] = None
        print(BoardArray)

    BoardStructure()

if __name__ == "__main__":
    print("Runnning chess...")

    main()
