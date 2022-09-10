import json
import pickle
import numpy as np
__vehical = None
__fuel = None
__seller = None
__transmission = None
__owner = None
__data_columns = None
__model = None

def get_estimated_price(Carname,Caryear,KM_driven,FuelType,SellerType,Transmission,Owner,Milage,Engine,Seate):
    try:
       loc_index1 = __data_columns.index(Carname.lower())
       loc_index2 = __data_columns.index(FuelType.lower())
       loc_index3 = __data_columns.index(SellerType.lower())
       loc_index4 = __data_columns.index(Transmission.lower())
       loc_index5 = __data_columns.index(Owner.lower())
    except:
        loc_index1 =-1
        loc_index2 =-1
        loc_index3 =-1
        loc_index4 =-1
        loc_index5 =-1

    x = np.zeros(len(__data_columns))
    x[0] = Caryear
    x[1] = KM_driven
    x[2] = Milage
    x[3] = Engine
    x[4] = Seate
    if loc_index1 >= 0:
        x[loc_index1] = 1
    if loc_index2 >= 0:
        x[loc_index2] = 1
    if loc_index3 >= 0:
        x[loc_index3] = 1
    if loc_index4 >= 0:
        x[loc_index4] = 1
    if loc_index5 >= 0:
        x[loc_index5] = 1

    return round(__model.predict([x])[0],2)

def get_vehical_names():
    return __vehical

def get_fuel_type():
    return __fuel

def get_seller_type():
    return __seller

def get_transmission_type():
    return __transmission
def get_owner_type():
    return __owner

def load_saved_artifects():
    print("Loarding saved artifects....start")
    global __data_columns
    global __vehical
    global __fuel
    global __seller
    global __transmission
    global __owner

    with open("./artifects/columns.json",'r') as f:
        __data_columns= json.load(f)['data_columns']
        __vehical= __data_columns[6:37]
        __fuel= __data_columns[37:40]
        __seller= __data_columns[40:43]
        __transmission= __data_columns[43:45]
        __owner= __data_columns[45:]

    global __model
    with open("./artifects/Used_car_price_model.pickle",'rb') as f:
         __model = pickle.load(f)
    print("Loading saved artifects is done")
if __name__ =='__main__':
    load_saved_artifects()
    print(get_vehical_names())
    print(get_fuel_type())
    print(get_seller_type())
    print(get_transmission_type())
    print(get_owner_type())
    print(get_estimated_price('Maruti',2014, 145654,'Petrol','Individual','Manual','First_Owner',24.12,1248,5))
