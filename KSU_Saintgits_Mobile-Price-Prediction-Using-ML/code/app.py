import pickle
import warnings
import pandas as pd

warnings.filterwarnings("ignore")

rfmodel = pickle.load(open("randomforest.p","rb"))

class RunModel:
    def getResults(self,data):
        data = pd.DataFrame([data],columns=["sim_count","display_inches","core","clock_speed","front_cam_1","rear_cam_1","4g","5g","rom","ram","battery","os"])
        result = rfmodel.predict(data)
        return result
        
runmodel = RunModel()
while(True):
    print("Select an option:")
    print("1.Predict Price")
    print("2.Exit")
    try:
        option = int(input("1 or 2:"))
    except Exception as e:
        print(e)
        continue
    if(option==1):
        try:
            sim_count = int(input("Enter the number of sims: "))
            display_inches = float(input("Enter the display size in inches: "))
            core = int(input("Enter the number of cores: "))
            clock_speed = float(input("Enter the processor clock speed: "))
            front_cam_1 = int(input("Enter the size of primary front camera: "))
            rear_cam_1 = int(input("Enter the size of primary rear camera: "))
            fourg = int(input("4g(0 or 1): "))
            fiveg = int(input("5g(0 or 1): "))
            rom = int(input("Enter the size of internal storage: "))
            ram = int(input("Enter the size of ram: "))
            battery = int(input("Enter the size of battery: "))
            os = int(input("Operating system(0=android & 1=ios): "))
            data = [sim_count,display_inches,core,clock_speed,front_cam_1,rear_cam_1,fourg,fiveg,rom,ram,battery,os]
        except Exception as e:
            print("Error in input")
            continue
        result = runmodel.getResults(data)[0]
        if(result):
            print(f"The predicted price is: {round(result,2)}")
        else:
            print("Prediction Error")
            continue
    elif(option==2):
        print("Exiting...")
        exit(0)
    else:
        print("Invalid input")
        continue
    
    