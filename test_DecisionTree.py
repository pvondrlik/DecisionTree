import main from main


""""
This file shows th
You can change values in the test_decicionTree.py document in the main() function. For more information have a look in to the Readme

#examples:
#main(df, "drugC")
You can also try to use your own data but (have a look at the Data requirenments in the Imput format section).
For more information have a look in to the Readme
""""


if __name__ == "__main__":
    data = "data/drug200.csv"
    data2 = "data/pokemon_no_duplicates.csv"
    data3 = "data/student-mat.csv"
    df = np.loadtxt(data3, dtype=str, delimiter=',')

    main(df)
    #examples:
    #main(df, "drugC")
    main(df

    pass
