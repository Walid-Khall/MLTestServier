import models.model1, models.model2, models.model3
import os




def main():
    
    print('Pleas enter the model taht you want to train, evaluate  and save\n')
    
    print('choos model1, model2 or model3')
    
    modelname = input("Enter Your choice!")

    if modelname == 'model1':
        os.system("python models/model1.py data/dataset_single.csv models/model1.h5")
    elif modelname == 'model2':
        os.system("python models/model2.py data/dataset_single.csv models/model2.h5")
    elif modelname == 'model3':
        os.system("python models/model3.py data/dataset_multi.csv models/model3.pkl")
    else:
        print("There is no modele named:", modelname)

    
if __name__ == '__main__':
    main()
