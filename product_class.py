import pandas as pd
from pandas.errors import MergeError
from datetime import datetime, timedelta
import math
from docplex.cp.model import *
class Quantity:
    def __init__(self, name, Y23W01, Y23W02, Y23W03, Y23W04,Y23W05, Y23W06, Y23W07, Y23W08, Y23W09, Y23W10, Y23W11,
                 Y23W12, Y23W13, Y23W14, Y23W15, Y23W16, Y23W17, Y23W18, Y23W19, Y23W20,Y23W21, Y23W22, Y23W23,
                 Y23W24,Y23W25, Y23W26, Y23W27, Y23W28, Y23W29, Y23W30, Y23W31,Y23W32, Y23W33, Y23W34, Y23W35,
                 Y23W36, Y23W37, Y23W38, Y23W39, Y23W40, Y23W41, Y23W42, Y23W43, Y23W44,Y23W45, Y23W46, Y23W47,
                 Y23W48, Y23W49, Y23W50, Y23W51,Y23W52):
        self.name = name
        self.Y23W01 = Y23W01
        self.Y23W02 = Y23W02
        self.Y23W03 = Y23W03
        self.Y23W04 = Y23W04
        self.Y23W05 = Y23W05
        self.Y23W06 = Y23W06
        self.Y23W07 = Y23W07
        self.Y23W08 = Y23W08
        self.Y23W09 = Y23W09
        self.Y23W10 = Y23W10
        self.Y23W11 = Y23W11
        self.Y23W12 = Y23W12
        self.Y23W13 = Y23W13
        self.Y23W14 = Y23W14
        self.Y23W15 = Y23W15
        self.Y23W16 = Y23W16
        self.Y23W17 = Y23W17
        self.Y23W18 = Y23W18
        self.Y23W19 = Y23W19
        self.Y23W20 = Y23W20
        self.Y23W21 = Y23W21
        self.Y23W22 = Y23W22
        self.Y23W23 = Y23W23
        self.Y23W24 = Y23W24
        self.Y23W25 = Y23W25
        self.Y23W26 = Y23W26
        self.Y23W27 = Y23W27
        self.Y23W28 = Y23W28
        self.Y23W29 = Y23W29
        self.Y23W30 = Y23W30
        self.Y23W31 = Y23W31
        self.Y23W32 = Y23W32
        self.Y23W33 = Y23W33
        self.Y23W34 = Y23W34
        self.Y23W35 = Y23W35
        self.Y23W36 = Y23W36
        self.Y23W37 = Y23W37
        self.Y23W38 = Y23W38
        self.Y23W39 = Y23W39
        self.Y23W40 = Y23W40
        self.Y23W41 = Y23W41
        self.Y23W42 = Y23W42
        self.Y23W43 = Y23W43
        self.Y23W44 = Y23W44
        self.Y23W45 = Y23W45
        self.Y23W46 = Y23W46
        self.Y23W47 = Y23W47
        self.Y23W48 = Y23W48
        self.Y23W49 = Y23W49
        self.Y23W50 = Y23W50
        self.Y23W51 = Y23W51
        self.Y23W52 = Y23W52

    def display_info(self):
        print("Product Name:", self.name)
        print("Y23W01:", self.Y23W01)
        print("Y23W02:", self.Y23W02)
        print("Y23W03:", self.Y23W03)
        print("Y23W04:", self.Y23W04)
        print("Y23W05:", self.Y23W05)
        print("Y23W06:", self.Y23W06)
        print("Y23W07:", self.Y23W07)
        print("Y23W08:", self.Y23W08)
        print("Y23W09:", self.Y23W09)
        print("Y23W10:", self.Y23W10)
        print("Y23W11:", self.Y23W11)
        print("Y23W12:", self.Y23W12)
        print("Y23W13:", self.Y23W13)
        print("Y23W14:", self.Y23W14)
        print("Y23W15:", self.Y23W15)
        print("Y23W16:", self.Y23W16)
        print("Y23W17:", self.Y23W17)
        print("Y23W18:", self.Y23W18)
        print("Y23W19:", self.Y23W19)
        print("Y23W20:", self.Y23W20)
        print("Y23W21:", self.Y23W21)
        print("Y23W22:", self.Y23W22)
        print("Y23W23:", self.Y23W23)
        print("Y23W24:", self.Y23W24)
        print("Y23W25:", self.Y23W25)
        print("Y23W26:", self.Y23W26)
        print("Y23W27:", self.Y23W27)
        print("Y23W28:", self.Y23W28)
        print("Y23W29:", self.Y23W29)
        print("Y23W30:", self.Y23W30)
        print("Y23W31:", self.Y23W31)
        print("Y23W32:", self.Y23W32)
        print("Y23W33:", self.Y23W33)
        print("Y23W34:", self.Y23W34)
        print("Y23W35:", self.Y23W35)
        print("Y23W36:", self.Y23W36)
        print("Y23W37:", self.Y23W37)
        print("Y23W38:", self.Y23W38)
        print("Y23W39:", self.Y23W39)
        print("Y23W40:", self.Y23W40)
        print("Y23W41:", self.Y23W41)
        print("Y23W42:", self.Y23W42)
        print("Y23W43:", self.Y23W43)
        print("Y23W44:", self.Y23W44)
        print("Y23W45:", self.Y23W45)
        print("Y23W46:", self.Y23W46)
        print("Y23W47:", self.Y23W47)
        print("Y23W48:", self.Y23W48)
        print("Y23W49:", self.Y23W49)
        print("Y23W50:", self.Y23W50)
        print("Y23W51:", self.Y23W51)
        print("Y23W52:", self.Y23W52)

class ConsumingTime:
    def __init__(self, name, Y23W01, Y23W02, Y23W03, Y23W04,Y23W05, Y23W06, Y23W07, Y23W08, Y23W09, Y23W10, Y23W11,
                 Y23W12, Y23W13, Y23W14, Y23W15, Y23W16, Y23W17, Y23W18, Y23W19, Y23W20,Y23W21, Y23W22, Y23W23,
                 Y23W24,Y23W25, Y23W26, Y23W27, Y23W28, Y23W29, Y23W30, Y23W31,Y23W32, Y23W33, Y23W34, Y23W35,
                 Y23W36, Y23W37, Y23W38, Y23W39, Y23W40, Y23W41, Y23W42, Y23W43, Y23W44,Y23W45, Y23W46, Y23W47,
                 Y23W48, Y23W49, Y23W50, Y23W51,Y23W52):
        self.name = name
        self.Y23W01 = Y23W01
        self.Y23W02 = Y23W02
        self.Y23W03 = Y23W03
        self.Y23W04 = Y23W04
        self.Y23W05 = Y23W05
        self.Y23W06 = Y23W06
        self.Y23W07 = Y23W07
        self.Y23W08 = Y23W08
        self.Y23W09 = Y23W09
        self.Y23W10 = Y23W10
        self.Y23W11 = Y23W11
        self.Y23W12 = Y23W12
        self.Y23W13 = Y23W13
        self.Y23W14 = Y23W14
        self.Y23W15 = Y23W15
        self.Y23W16 = Y23W16
        self.Y23W17 = Y23W17
        self.Y23W18 = Y23W18
        self.Y23W19 = Y23W19
        self.Y23W20 = Y23W20
        self.Y23W21 = Y23W21
        self.Y23W22 = Y23W22
        self.Y23W23 = Y23W23
        self.Y23W24 = Y23W24
        self.Y23W25 = Y23W25
        self.Y23W26 = Y23W26
        self.Y23W27 = Y23W27
        self.Y23W28 = Y23W28
        self.Y23W29 = Y23W29
        self.Y23W30 = Y23W30
        self.Y23W31 = Y23W31
        self.Y23W32 = Y23W32
        self.Y23W33 = Y23W33
        self.Y23W34 = Y23W34
        self.Y23W35 = Y23W35
        self.Y23W36 = Y23W36
        self.Y23W37 = Y23W37
        self.Y23W38 = Y23W38
        self.Y23W39 = Y23W39
        self.Y23W40 = Y23W40
        self.Y23W41 = Y23W41
        self.Y23W42 = Y23W42
        self.Y23W43 = Y23W43
        self.Y23W44 = Y23W44
        self.Y23W45 = Y23W45
        self.Y23W46 = Y23W46
        self.Y23W47 = Y23W47
        self.Y23W48 = Y23W48
        self.Y23W49 = Y23W49
        self.Y23W50 = Y23W50
        self.Y23W51 = Y23W51
        self.Y23W52 = Y23W52


def display_info(self):
        print("Product Name:", self.name)
        print("Y23W01:", self.Y23W01)
        print("Y23W02:", self.Y23W02)
        print("Y23W03:", self.Y23W03)
        print("Y23W04:", self.Y23W04)
        print("Y23W05:", self.Y23W05)
        print("Y23W06:", self.Y23W06)
        print("Y23W07:", self.Y23W07)
        print("Y23W08:", self.Y23W08)
        print("Y23W09:", self.Y23W09)
        print("Y23W10:", self.Y23W10)
        print("Y23W11:", self.Y23W11)
        print("Y23W12:", self.Y23W12)
        print("Y23W13:", self.Y23W13)
        print("Y23W14:", self.Y23W14)
        print("Y23W15:", self.Y23W15)
        print("Y23W16:", self.Y23W16)
        print("Y23W17:", self.Y23W17)
        print("Y23W18:", self.Y23W18)
        print("Y23W19:", self.Y23W19)
        print("Y23W20:", self.Y23W20)
        print("Y23W21:", self.Y23W21)
        print("Y23W22:", self.Y23W22)
        print("Y23W23:", self.Y23W23)
        print("Y23W24:", self.Y23W24)
        print("Y23W25:", self.Y23W25)
        print("Y23W26:", self.Y23W26)
        print("Y23W27:", self.Y23W27)
        print("Y23W28:", self.Y23W28)
        print("Y23W29:", self.Y23W29)
        print("Y23W30:", self.Y23W30)
        print("Y23W31:", self.Y23W31)
        print("Y23W32:", self.Y23W32)
        print("Y23W33:", self.Y23W33)
        print("Y23W34:", self.Y23W34)
        print("Y23W35:", self.Y23W35)
        print("Y23W36:", self.Y23W36)
        print("Y23W37:", self.Y23W37)
        print("Y23W38:", self.Y23W38)
        print("Y23W39:", self.Y23W39)
        print("Y23W40:", self.Y23W40)
        print("Y23W41:", self.Y23W41)
        print("Y23W42:", self.Y23W42)
        print("Y23W43:", self.Y23W43)
        print("Y23W44:", self.Y23W44)
        print("Y23W45:", self.Y23W45)
        print("Y23W46:", self.Y23W46)
        print("Y23W47:", self.Y23W47)
        print("Y23W48:", self.Y23W48)
        print("Y23W49:", self.Y23W49)
        print("Y23W50:", self.Y23W50)
        print("Y23W51:", self.Y23W51)
        print("Y23W52:", self.Y23W52)


class Product:
    def __init__(self, name, materials, length, inner_diameter, weaving_machine, processing_machine
                 , needle_circle, speed, family = None, quantity = Quantity (0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                 consuming_time = ConsumingTime (0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)):

        self.name = name
        self.materials = materials
        self.length = length
        self.inner_diameter = inner_diameter
        self.weaving_machine = weaving_machine
        self.processing_machine = processing_machine
        self.needle_circle = needle_circle
        self.speed = speed
        self.family = family
        self.quantity = quantity
        self.consuming_time = consuming_time

    def display_info(self):
        print("Product Name:", self.name)
        print("Materials:", self.materials)
        print("Length:", self.length)
        print("Inner Diameter:", self.inner_diameter)
        print("Weaving Machine:", self.weaving_machine)
        print("Processing Machine:", self.processing_machine)
        print("Needle Circle:", self.needle_circle)
        print("Speed:", self.speed)
        print("Family:", self.family)


def import_products_from_excel(file_path):

    merged_data = pd.read_excel(file_path, sheet_name = 'Product')


    products = []

    merged_data.dropna(axis=0,subset=['Speed'],inplace=True)
    # Iterate over each row of data
    for i in range(len(merged_data)):
        # Extract the value of each field
        name = merged_data['Name'].iloc[i]
        materials = merged_data['Material'].iloc[i]
        length = merged_data['Length'].iloc[i]
        inner_diameter = merged_data['Diameter'].iloc[i]
        weaving_machine = merged_data['Weaving_machine'].iloc[i]
        processing_machine = merged_data['Processing_machine'].iloc[i]
        needle_circle = merged_data['Needle_type'].iloc[i]
        speed = merged_data['Speed'].iloc[i]
        try:
            Y23W01 = merged_data['Y23W01'].iloc[i]
        except KeyError:
            Y23W01 = 0
        try:
            Y23W02 = merged_data['Y23W02'].iloc[i]
        except KeyError:
            Y23W02 = 0
        try:
            Y23W03 = merged_data['Y23W03'].iloc[i]
        except KeyError:
            Y23W03 = 0
        try:
            Y23W04 = merged_data['Y23W04'].iloc[i]
        except KeyError:
            Y23W04 = 0
        try:
            Y23W05 = merged_data['Y23W05'].iloc[i]
        except KeyError:
            Y23W05 = 0
        try:
            Y23W06 = merged_data['Y23W06'].iloc[i]
        except KeyError:
            Y23W06 = 0
        try:
            Y23W07 = merged_data['Y23W07'].iloc[i]
        except KeyError:
            Y23W07 = 0
        try:
            Y23W08 = merged_data['Y23W08'].iloc[i]
        except KeyError:
            Y23W08 = 0
        try:
            Y23W09 = merged_data['Y23W09'].iloc[i]
        except KeyError:
            Y23W09 = 0
        try:
            Y23W10 = merged_data['Y23W10'].iloc[i]
        except KeyError:
            Y23W10 = 0
        try:
            Y23W11 = merged_data['Y23W11'].iloc[i]
        except KeyError:
            Y23W11 = 0
        try:
            Y23W12 = merged_data['Y23W12'].iloc[i]
        except KeyError:
            Y23W12 = 0
        try:
            Y23W13 = merged_data['Y23W13'].iloc[i]
        except KeyError:
            Y23W13 = 0
        try:
            Y23W14 = merged_data['Y23W14'].iloc[i]
        except KeyError:
            Y23W14 = 0
        try:
            Y23W15 = merged_data['Y23W15'].iloc[i]
        except KeyError:
            Y23W15 = 0
        try:
            Y23W16 = merged_data['Y23W16'].iloc[i]
        except KeyError:
            Y23W16 = 0
        try:
            Y23W17 = merged_data['Y23W17'].iloc[i]
        except KeyError:
            Y23W17 = 0
        try:
            Y23W18 = merged_data['Y23W18'].iloc[i]
        except KeyError:
            Y23W18 = 0
        try:
            Y23W19 = merged_data['Y23W19'].iloc[i]
        except KeyError:
            Y23W19 = 0
        try:
            Y23W20 = merged_data['Y23W20'].iloc[i]
        except KeyError:
            Y23W20 = 0
        try:
            Y23W21 = merged_data['Y23W21'].iloc[i]
        except KeyError:
            Y23W21 = 0
        try:
            Y23W22 = merged_data['Y23W22'].iloc[i]
        except KeyError:
            Y23W22 = 0
        try:
            Y23W23 = merged_data['Y23W23'].iloc[i]
        except KeyError:
            Y23W23 = 0
        try:
            Y23W24 = merged_data['Y23W24'].iloc[i]
        except KeyError:
            Y23W24 = 0
        try:
            Y23W25 = merged_data['Y23W25'].iloc[i]
        except KeyError:
            Y23W25 = 0
        try:
            Y23W26 = merged_data['Y23W26'].iloc[i]
        except KeyError:
            Y23W26 = 0
        try:
            Y23W27 = merged_data['Y23W27'].iloc[i]
        except KeyError:
            Y23W27 = 0
        try:
            Y23W28 = merged_data['Y23W28'].iloc[i]
        except KeyError:
            Y23W28 = 0
        try:
            Y23W29 = merged_data['Y23W29'].iloc[i]
        except KeyError:
            Y23W29 = 0
        try:
            Y23W30 = merged_data['Y23W30'].iloc[i]
        except KeyError:
            Y23W30 = 0
        try:
            Y23W31 = merged_data['Y23W31'].iloc[i]
        except KeyError:
            Y23W31 = 0
        try:
            Y23W32 = merged_data['Y23W32'].iloc[i]
        except KeyError:
            Y23W32 = 0
        try:
            Y23W33 = merged_data['Y23W33'].iloc[i]
        except KeyError:
            Y23W33 = 0
        try:
            Y23W34 = merged_data['Y23W34'].iloc[i]
        except KeyError:
            Y23W34 = 0
        try:
            Y23W35 = merged_data['Y23W35'].iloc[i]
        except KeyError:
            Y23W35 = 0
        try:
            Y23W36 = merged_data['Y23W36'].iloc[i]
        except KeyError:
            Y23W36 = 0
        try:
            Y23W37 = merged_data['Y23W37'].iloc[i]
        except KeyError:
            Y23W37 = 0
        try:
            Y23W38 = merged_data['Y23W38'].iloc[i]
        except KeyError:
            Y23W38 = 0
        try:
            Y23W39 = merged_data['Y23W39'].iloc[i]
        except KeyError:
            Y23W39 = 0
        try:
            Y23W40 = merged_data['Y23W40'].iloc[i]
        except KeyError:
            Y23W40 = 0
        try:
            Y23W41 = merged_data['Y23W41'].iloc[i]
        except KeyError:
            Y23W41 = 0
        try:
            Y23W42 = merged_data['Y23W42'].iloc[i]
        except KeyError:
            Y23W42 = 0
        try:
            Y23W43 = merged_data['Y23W43'].iloc[i]
        except KeyError:
            Y23W43 = 0
        try:
            Y23W44 = merged_data['Y23W44'].iloc[i]
        except KeyError:
            Y23W44 = 0
        try:
            Y23W45 = merged_data['Y23W45'].iloc[i]
        except KeyError:
            Y23W45 = 0
        try:
            Y23W46 = merged_data['Y23W46'].iloc[i]
        except KeyError:
            Y23W46 = 0
        try:
            Y23W47 = merged_data['Y23W47'].iloc[i]
        except KeyError:
            Y23W47 = 0
        try:
            Y23W48 = merged_data['Y23W48'].iloc[i]
        except KeyError:
            Y23W48 = 0
        try:
            Y23W49 = merged_data['Y23W49'].iloc[i]
        except KeyError:
            Y23W49 = 0
        try:
            Y23W50 = merged_data['Y23W50'].iloc[i]
        except KeyError:
            Y23W50 = 0
        try:
            Y23W51 = merged_data['Y23W51'].iloc[i]
        except KeyError:
            Y23W51 = 0
        try:
            Y23W52 = merged_data['Y23W52'].iloc[i]
        except KeyError:
            Y23W52 = 0

        # Create Quantity Object
        demand_quantity = Quantity(name, Y23W01, Y23W02, Y23W03, Y23W04,Y23W05, Y23W06, Y23W07, Y23W08, Y23W09, Y23W10, Y23W11,
                 Y23W12, Y23W13, Y23W14, Y23W15, Y23W16, Y23W17, Y23W18, Y23W19, Y23W20,Y23W21, Y23W22, Y23W23,
                 Y23W24,Y23W25, Y23W26, Y23W27, Y23W28, Y23W29, Y23W30, Y23W31,Y23W32, Y23W33, Y23W34, Y23W35,
                 Y23W36, Y23W37, Y23W38, Y23W39, Y23W40, Y23W41, Y23W42, Y23W43, Y23W44,Y23W45, Y23W46, Y23W47,
                 Y23W48, Y23W49, Y23W50, Y23W51, Y23W52)

        # Create ConsumingTime Object
        consuming_time = ConsumingTime(name, Y23W01*length/speed, Y23W02*length/speed, Y23W03*length/speed,
        Y23W04*length/speed, Y23W05*length/speed, Y23W06*length/speed, Y23W07*length/speed,
        Y23W08*length/speed, Y23W09*length/speed, Y23W10*length/speed, Y23W11*length/speed,
        Y23W12*length/speed, Y23W13*length/speed, Y23W14*length/speed, Y23W15*length/speed,
        Y23W16*length/speed, Y23W17*length/speed, Y23W18*length/speed, Y23W19*length/speed,
        Y23W20*length/speed, Y23W21*length/speed, Y23W22*length/speed, Y23W23*length/speed,
        Y23W24*length/speed, Y23W25*length/speed, Y23W26*length/speed, Y23W27*length/speed,
        Y23W28*length/speed, Y23W29*length/speed, Y23W30*length/speed, Y23W31*length/speed,
        Y23W32*length/speed, Y23W33*length/speed, Y23W34*length/speed, Y23W35*length/speed,
        Y23W36*length/speed, Y23W37*length/speed, Y23W38*length/speed, Y23W39*length/speed,
        Y23W40*length/speed, Y23W41*length/speed, Y23W42*length/speed, Y23W43*length/speed,
        Y23W44*length/speed, Y23W45*length/speed, Y23W46*length/speed, Y23W47*length/speed,
        Y23W48*length/speed, Y23W49*length/speed, Y23W50*length/speed, Y23W51*length/speed, Y23W52*length/speed)

        # Create Product Object
        product = Product(name, materials, length, inner_diameter, weaving_machine, processing_machine\
                          , needle_circle, speed, None, demand_quantity, consuming_time)


        products.append(product)

    return products

def calculate_consuming_time(product):
    # Create ConsumingTime Object
    consuming_time = ConsumingTime(product.name, product.quantity.Y23W01*product.length/product.speed,
    product.quantity.Y23W02 * product.length/product.speed, product.quantity.Y23W03*product.length/product.speed,
    product.quantity.Y23W04 * product.length/product.speed,product.quantity.Y23W05*product.length/product.speed,
    product.quantity.Y23W06 * product.length/product.speed, product.quantity.Y23W07*product.length/product.speed,
    product.quantity.Y23W08 * product.length/product.speed, product.quantity.Y23W09*product.length/product.speed,
    product.quantity.Y23W10 * product.length/product.speed, product.quantity.Y23W11*product.length/product.speed,
    product.quantity.Y23W12 * product.length/product.speed, product.quantity.Y23W13*product.length/product.speed,
    product.quantity.Y23W14 * product.length/product.speed, product.quantity.Y23W15*product.length/product.speed,
    product.quantity.Y23W16 * product.length/product.speed, product.quantity.Y23W17*product.length/product.speed,
    product.quantity.Y23W18 * product.length/product.speed, product.quantity.Y23W19*product.length/product.speed,
    product.quantity.Y23W20 * product.length/product.speed, product.quantity.Y23W21*product.length/product.speed,
    product.quantity.Y23W22 * product.length/product.speed, product.quantity.Y23W23*product.length/product.speed,
    product.quantity.Y23W24 * product.length/product.speed,product.quantity.Y23W25*product.length/product.speed,
    product.quantity.Y23W26 * product.length/product.speed, product.quantity.Y23W27*product.length/product.speed,
    product.quantity.Y23W28 * product.length/product.speed, product.quantity.Y23W29*product.length/product.speed,
    product.quantity.Y23W30 * product.length/product.speed, product.quantity.Y23W31*product.length/product.speed,
    product.quantity.Y23W32 * product.length/product.speed, product.quantity.Y23W33*product.length/product.speed,
    product.quantity.Y23W34 * product.length/product.speed, product.quantity.Y23W35*product.length/product.speed,
    product.quantity.Y23W36 * product.length/product.speed, product.quantity.Y23W37*product.length/product.speed,
    product.quantity.Y23W38 * product.length/product.speed, product.quantity.Y23W39*product.length/product.speed,
    product.quantity.Y23W40 * product.length/product.speed, product.quantity.Y23W41*product.length/product.speed,
    product.quantity.Y23W42 * product.length/product.speed, product.quantity.Y23W43*product.length/product.speed,
    product.quantity.Y23W44 * product.length/product.speed, product.quantity.Y23W45*product.length/product.speed,
    product.quantity.Y23W46 * product.length/product.speed, product.quantity.Y23W47*product.length/product.speed,
    product.quantity.Y23W48 * product.length/product.speed, product.quantity.Y23W49*product.length/product.speed,
    product.quantity.Y23W50 * product.length/product.speed, product.quantity.Y23W51*product.length/product.speed,
    product.quantity.Y23W52 * product.length/product.speed)

    return consuming_time

def classify_into_families(products):
    # Sort products according to inner diameter from largest to smallest
    products.sort(key=lambda x: x.inner_diameter, reverse=True)

    # Create family Dictionary
    families = {}
    family_counter = 1

    for product in products:
        found_family = False

        # Find products similar to the current product in the existing family
        for family in families.values():
            reference_product = family[0]

            # Judgment conditions to determine if they are in the same family
            if (
                product.materials == reference_product.materials
                and product.weaving_machine == reference_product.weaving_machine
                and product.processing_machine == reference_product.processing_machine
                and product.needle_circle == reference_product.needle_circle
                and (
                    (product.inner_diameter - reference_product.inner_diameter <= 2
                     and reference_product.inner_diameter > 30)
                    or (reference_product.inner_diameter - product.inner_diameter <= 1
                        and reference_product.inner_diameter <= 30)
                )
            ):
                # Add the current product to the same family
                family.append(product)
                product.family = reference_product.family
                found_family = True
                break

        # If no similar family is found, a new family is created.
        if not found_family:
            new_family = [product]
            product.family = family_counter
            families[family_counter] = new_family
            family_counter += 1

    return families

def filter_products_by_family(products, next_week_index):
    filtered_products = []
    families = {}  # Used to store the total manufacturing time for each family

    # Iterate through the list of products and calculate the total manufacturing time for each family
    for product in products:
        family = product.family
        if family not in families:
            families[family] = 0
        families[family] += getattr(product.consuming_time, next_week_index)

    # Check if the total manufacturing time of the FAMILY
    # that each product belongs to is greater than or equal to 2 hours, if so add it to the new list
    for product in products:
        family = product.family
        if families[family] >= 120 and getattr(product.consuming_time, next_week_index) != 0:
            filtered_products.append(product)

    return filtered_products

def extract_consuming_time(products, next_week_index):
    consuming_times = []  # New list for storing manufacturing time

    # Extract the manufacturing time for each product and add it to the new list
    for product in products:
        consuming_times.append(getattr(product.consuming_time, next_week_index))

    return consuming_times

def calculate_changeover_time(product1, product2):
    if product1.processing_machine=='A' and product2.processing_machine=='A':
        if product1.materials != product2.materials:
            return 55
        elif max(product1.inner_diameter,product2.inner_diameter) > 30 \
            and abs(product1.inner_diameter - product2.inner_diameter) >= 2:
            if product1.needle_circle != product2.needle_circle or \
                    product1.weaving_machine != product2.weaving_machine:
                return 50
            else:
                return 37
        elif max(product1.inner_diameter,product2.inner_diameter) <= 30 \
            and abs(product1.inner_diameter - product2.inner_diameter) >= 1:
            if product1.needle_circle != product2.needle_circle or \
                    product1.weaving_machine != product2.weaving_machine:
                return 50
            else:
                return 37
        else:
            if product1.needle_circle != product2.needle_circle or \
                    product1.weaving_machine != product2.weaving_machine:
                return 25
            else:
                return 0


    elif product1.processing_machine=='B' and product2.processing_machine=='B':
        if product1.materials != product2.materials:
            return 55
        elif max(product1.inner_diameter,product2.inner_diameter) > 30 \
            and abs(product1.inner_diameter - product2.inner_diameter) >= 2:
            if product1.needle_circle != product2.needle_circle or \
                    product1.weaving_machine != product2.weaving_machine:
                return 50
            else:
                return 30
        elif max(product1.inner_diameter,product2.inner_diameter) <= 30 \
            and abs(product1.inner_diameter - product2.inner_diameter) >= 1:
            if product1.needle_circle != product2.needle_circle or \
                    product1.weaving_machine != product2.weaving_machine:
                return 50
            else:
                return 30
        else:
            if product1.needle_circle != product2.needle_circle or \
                    product1.weaving_machine != product2.weaving_machine:
                return 27
            else:
                return 0
    else:
        return None

def calculate_changeover_matrix(products):
    matrix = []

    for product1 in products:
        row = []
        for product2 in products:
            changeover_time = calculate_changeover_time(product1, product2)
            row.append(changeover_time)
        matrix.append(row)

    return matrix

def calculate_changeover_dataframe(products):
    matrix = []

    for product1 in products:
        row = []
        for product2 in products:
            changeover_time = calculate_changeover_time(product1, product2)
            row.append(changeover_time)
        matrix.append(row)

    df = pd.DataFrame(matrix, columns=[product.name for product in products], \
                      index=[product.name for product in products])

    return df

def calculate_changeover_time_A(product1, product2):

    if product1.materials != product2.materials:
        return 55
    elif max(product1.inner_diameter,product2.inner_diameter) > 30 \
        and abs(product1.inner_diameter - product2.inner_diameter) >= 2:
        if product1.needle_circle != product2.needle_circle or \
                product1.weaving_machine != product2.weaving_machine:
            return 50
        else:
            return 37
    elif max(product1.inner_diameter,product2.inner_diameter) <= 30 \
        and abs(product1.inner_diameter - product2.inner_diameter) >= 1:
        if product1.needle_circle != product2.needle_circle or \
                product1.weaving_machine != product2.weaving_machine:
            return 50
        else:
            return 37
    else:
        if product1.needle_circle != product2.needle_circle or \
                product1.weaving_machine != product2.weaving_machine:
            return 25
        else:
            return 0

def calculate_changeover_time_B(product1, product2):
    if product1.materials != product2.materials:
        return 55
    elif max(product1.inner_diameter,product2.inner_diameter) > 30 \
        and abs(product1.inner_diameter - product2.inner_diameter) >= 2:
        if product1.needle_circle != product2.needle_circle or \
                product1.weaving_machine != product2.weaving_machine:
            return 50
        else:
            return 30
    elif max(product1.inner_diameter,product2.inner_diameter) <= 30 \
        and abs(product1.inner_diameter - product2.inner_diameter) >= 1:
        if product1.needle_circle != product2.needle_circle or \
                product1.weaving_machine != product2.weaving_machine:
            return 50
        else:
            return 30
    else:
        if product1.needle_circle != product2.needle_circle or \
                product1.weaving_machine != product2.weaving_machine:
            return 27
        else:
            return 0

def calculate_changeover_dataframe_A(products):
    matrix = []

    for product1 in products:
        row = []
        for product2 in products:
            changeover_time = calculate_changeover_time_A(product1, product2)
            row.append(changeover_time)
        matrix.append(row)

    df = pd.DataFrame(matrix, columns=[product.name for product in products], \
                      index=[product.name for product in products])

    return df

def calculate_changeover_dataframe_B(products):
    matrix = []

    for product1 in products:
        row = []
        for product2 in products:
            changeover_time = calculate_changeover_time_B(product1, product2)
            row.append(changeover_time)
        matrix.append(row)

    df = pd.DataFrame(matrix, columns=[product.name for product in products], \
                      index=[product.name for product in products])

    return df

def calculate_changeover_matrix_A(products):
    matrix = []

    for product1 in products:
        row = []
        for product2 in products:
            changeover_time = calculate_changeover_time_A(product1, product2)
            row.append(changeover_time)
        matrix.append(row)

    return matrix

def calculate_changeover_matrix_B(products):
    matrix = []

    for product1 in products:
        row = []
        for product2 in products:
            changeover_time = calculate_changeover_time_B(product1, product2)
            row.append(changeover_time)
        matrix.append(row)

    return matrix

def classify_processing_machine(products):
    products_B = []
    products_A = []

    for product in products:
        if product.processing_machine == 'B':
            products_B.append(product)
        elif product.processing_machine == 'A':
            products_A.append(product)


    return products_B, products_A

def get_monday_of_week(year, week):
    # Calculate the day of the week in which January 1 falls in the given year.
    first_day = datetime(year, 1, 1, hour = 0, minute = 0)
    first_day_weekday = first_day.weekday()

    # Calculate the date range for the first week
    if first_day_weekday <= 3:
        first_week_start = first_day - timedelta(days=first_day_weekday)
    else:
        first_week_start = first_day + timedelta(days=7 - first_day_weekday)

    # Calculate the date range for the target week
    target_week_start = first_week_start + timedelta(weeks=week - 2)
    target_week_end = target_week_start + timedelta(days=6)

    return target_week_start

def plan_to_excel_B(target, products, next_week, next_week_index, current_year):
    tar_products = []
    for product in products:
        if product.name in target:
            tar_products.append(product)
    end_time = get_monday_of_week(current_year, next_week)
    end_time = end_time + timedelta(hours=7)
    df_plan = pd.DataFrame(columns=['Material', 'Total quantity', 'Name', 'length(m)/pcs', 'consume time(H)',
                                    'speed(m/min)', 'Weaving_machine', 'Needle_type', 'Diameter', 'change_diameter_time',
                                    'change_weaving_machine_time', 'change_material_time', 'turn_on_machine_time',
                                    'turn_off_machine_time', 'total_time', 'end_time'])

    length = len(tar_products)
    global changeover_start_B
    changeover_start_B = 0
    global total_changeover_B
    total_changeover_B = 0

    for i, elm in enumerate(tar_products):
        if i == 0:

            total_changeover_B = calculate_changeover_time_B(elm, tar_products[i + 1])
            change_material = 0
            change_diameter = 0
            change_weaving = 0
            changeover_start_B = elm.inner_diameter

            if total_changeover_B == 55:
                change_material = 55
                changeover_start_B = tar_products[i + 1].inner_diameter

            elif total_changeover_B == 50:
                change_diameter = 30
                change_weaving = 20
                changeover_start_B = tar_products[i + 1].inner_diameter

            elif total_changeover_B == 30:
                change_diameter = 30
                changeover_start_B = tar_products[i + 1].inner_diameter

            elif total_changeover_B == 27:
                change_weaving = 27

            if changeover_start_B != tar_products[i + 1].inner_diameter:
                if max(changeover_start_B, tar_products[i + 1].inner_diameter) <= 30 \
                and abs(changeover_start_B - tar_products[i + 1].inner_diameter) < 1:
                    pass
                elif max(changeover_start_B, tar_products[i + 1].inner_diameter) > 30 \
                and abs(changeover_start_B - tar_products[i + 1].inner_diameter) < 2:
                    pass
                else:
                    changeover_start_B = tar_products[i + 1].inner_diameter
                    if total_changeover_B == 27:
                        total_changeover_B = 50
                        change_diameter = 30
                        change_weaving = 20
                    elif total_changeover_B == 0:
                        total_changeover_B = 30
                        change_diameter = 30


            consuming_time = getattr(elm.consuming_time, next_week_index)
            quantity = getattr(elm.quantity, next_week_index)
            total_time = consuming_time + 38 + total_changeover_B
            end_time = end_time + timedelta(hours=total_time // 60, minutes=total_time % 60)

            new = pd.DataFrame({'Material': elm.materials, 'Total quantity': quantity, 'Name': elm.name,
                                'length(m)/pcs': elm.length, 'consume time(H)': consuming_time,
                                'speed(m/min)': elm.speed,
                                'Weaving_machine': elm.weaving_machine, 'Needle_type': elm.needle_circle,
                                'Diameter': elm.inner_diameter, 'change_diameter_time': change_diameter,
                                'change_weaving_machine_time': change_weaving, 'change_material_time': change_material,
                                'turn_on_machine_time': 38, 'turn_off_machine_time': 0,
                                'total_time': total_time, 'end_time': end_time}, index=[0])
            df_plan = df_plan._append(new, ignore_index=True)

        elif (i + 1) < length:

            total_changeover_B = calculate_changeover_time_B(elm, tar_products[i + 1])
            change_material = 0
            change_diameter = 0
            change_weaving = 0
            consuming_time = getattr(elm.consuming_time, next_week_index)
            quantity = getattr(elm.quantity, next_week_index)
            if total_changeover_B == 55:
                change_material = 55
                changeover_start_B = tar_products[i + 1].inner_diameter

            elif total_changeover_B == 50:
                change_diameter = 30
                change_weaving = 20
                changeover_start_B = tar_products[i + 1].inner_diameter

            elif total_changeover_B == 30:
                change_diameter = 30
                changeover_start_B = tar_products[i + 1].inner_diameter

            elif total_changeover_B == 27:
                change_weaving = 27

            if changeover_start_B != tar_products[i + 1].inner_diameter:
                if max(changeover_start_B, tar_products[i + 1].inner_diameter) <= 30 \
                        and abs(changeover_start_B - tar_products[i + 1].inner_diameter) < 1:
                    pass
                elif max(changeover_start_B, tar_products[i + 1].inner_diameter) > 30 \
                        and abs(changeover_start_B - tar_products[i + 1].inner_diameter) < 2:
                    pass
                else:
                    changeover_start_B = tar_products[i + 1].inner_diameter
                    if total_changeover_B == 27:
                        total_changeover_B = 50
                        change_diameter = 30
                        change_weaving = 20
                    elif total_changeover_B == 0:
                        total_changeover_B = 30
                        change_diameter = 30

            total_time = consuming_time + total_changeover_B
            end_time = end_time + timedelta(hours=total_time // 60, minutes=total_time % 60)
            new = pd.DataFrame({'Material': elm.materials, 'Total quantity': quantity, 'Name': elm.name,
                                'length(m)/pcs': elm.length, 'consume time(H)': consuming_time,
                                'speed(m/min)': elm.speed,
                                'Weaving_machine': elm.weaving_machine, 'Needle_type': elm.needle_circle,
                                'Diameter': elm.inner_diameter, 'change_diameter_time': change_diameter,
                                'change_weaving_machine_time': change_weaving, 'change_material_time': change_material,
                                'turn_on_machine_time': 0, 'turn_off_machine_time': 0,
                                'total_time': total_time, 'end_time': end_time}, index=[0])
            df_plan = df_plan._append(new, ignore_index=True)
        else:
            consuming_time = getattr(elm.consuming_time, next_week_index)
            quantity = getattr(elm.quantity, next_week_index)
            total_time = consuming_time + 38
            end_time = end_time + timedelta(hours=total_time // 60, minutes=total_time % 60)
            new = pd.DataFrame({'Material': elm.materials, 'Total quantity': quantity, 'Name': elm.name,
                                'length(m)/pcs': elm.length, 'consume time(H)': consuming_time,
                                'speed(m/min)': elm.speed,
                                'Weaving_machine': elm.weaving_machine, 'Needle_type': elm.needle_circle,
                                'Diameter': elm.inner_diameter, 'change_diameter_time': change_diameter,
                                'change_weaving_machine_time': change_weaving, 'change_material_time': change_material,
                                'turn_on_machine_time': 38, 'turn_off_machine_time': 38,
                                'total_time': total_time, 'end_time': end_time}, index=[0])
            df_plan = df_plan._append(new, ignore_index=True)

    df_plan.to_excel('Production_Plan_Machine_B.xlsx')



def plan_to_excel_A(targets, products, next_week, next_week_index, current_year):
    tar_products = []
    for target in targets:
        for product in products:
            if product.name == target:
                tar_products.append(product)

    end_time = get_monday_of_week(current_year, next_week)
    end_time = end_time + timedelta(hours=7)
    df_plan = pd.DataFrame(columns=['Material', 'Total quantity', 'Name', 'length(m)/pcs', 'consume time(H)',
                                    'speed(m/min)', 'Weaving_machine', 'Needle_type', 'Diameter', 'change_diameter_time',
                                    'change_weaving_machine_time', 'change_material_time', 'turn_on_machine_time',
                                    'turn_off_machine_time', 'total_time', 'end_time'])

    length = len(tar_products)
    global changeover_start_A
    changeover_start_A = 0
    global total_changeover_A
    total_changeover_A = 0

    for i, elm in enumerate(tar_products):
        if i == 0:

            total_changeover_A = calculate_changeover_time_A(elm, tar_products[i + 1])
            change_material = 0
            change_diameter = 0
            change_weaving = 0
            changeover_start_A = elm.inner_diameter

            if total_changeover_A == 55:
                change_material = 55
                changeover_start_A = tar_products[i + 1].inner_diameter

            elif total_changeover_A == 50:
                change_diameter = 37
                change_weaving = 13
                changeover_start_A = tar_products[i + 1].inner_diameter

            elif total_changeover_A == 37:
                change_diameter = 37
                changeover_start_A = tar_products[i + 1].inner_diameter

            elif total_changeover_A == 25:
                change_weaving = 25

            if changeover_start_A != tar_products[i + 1].inner_diameter:
                if max(changeover_start_A, tar_products[i + 1].inner_diameter) <= 30 \
                and abs(changeover_start_A - tar_products[i + 1].inner_diameter) < 1:
                    pass
                elif max(changeover_start_A, tar_products[i + 1].inner_diameter) > 30 \
                and abs(changeover_start_A - tar_products[i + 1].inner_diameter) < 2:
                    pass
                else:
                    changeover_start_A = tar_products[i + 1].inner_diameter
                    if total_changeover_A == 25:
                        total_changeover_A = 50
                        change_diameter = 37
                        change_weaving = 13
                    elif total_changeover_A == 0:
                        total_changeover_A = 37
                        change_diameter = 37


            consuming_time = getattr(elm.consuming_time, next_week_index)
            quantity = getattr(elm.quantity, next_week_index)
            total_time = consuming_time + 38 + total_changeover_A
            end_time = end_time + timedelta(hours=total_time // 60, minutes=total_time % 60)

            new = pd.DataFrame({'Material': elm.materials, 'Total quantity': quantity, 'Name': elm.name,
                                'length(m)/pcs': elm.length, 'consume time(H)': consuming_time,
                                'speed(m/min)': elm.speed,
                                'Weaving_machine': elm.weaving_machine, 'Needle_type': elm.needle_circle,
                                'Diameter': elm.inner_diameter, 'change_diameter_time': change_diameter,
                                'change_weaving_machine_time': change_weaving, 'change_material_time': change_material,
                                'turn_on_machine_time': 38, 'turn_off_machine_time': 0,
                                'total_time': total_time, 'end_time': end_time}, index=[0])
            df_plan = df_plan._append(new, ignore_index=True)

        elif (i + 1) < length:

            total_changeover_A = calculate_changeover_time_A(elm, tar_products[i + 1])
            change_material = 0
            change_diameter = 0
            change_weaving = 0
            consuming_time = getattr(elm.consuming_time, next_week_index)
            quantity = getattr(elm.quantity, next_week_index)
            if total_changeover_A == 55:
                change_material = 55
                changeover_start_A = tar_products[i + 1].inner_diameter

            elif total_changeover_A == 50:
                change_diameter = 37
                change_weaving = 13
                changeover_start_A = tar_products[i + 1].inner_diameter

            elif total_changeover_A == 37:
                change_diameter = 37
                changeover_start_A = tar_products[i + 1].inner_diameter

            elif total_changeover_A == 25:
                change_weaving = 25

            if changeover_start_A != tar_products[i + 1].inner_diameter:
                if max(changeover_start_A, tar_products[i + 1].inner_diameter) <= 30 \
                        and abs(changeover_start_A - tar_products[i + 1].inner_diameter) < 1:
                    pass
                elif max(changeover_start_A, tar_products[i + 1].inner_diameter) > 30 \
                        and abs(changeover_start_A - tar_products[i + 1].inner_diameter) < 2:
                    pass
                else:
                    changeover_start_A = tar_products[i + 1].inner_diameter
                    if total_changeover_A == 25:
                        total_changeover_A = 50
                        change_diameter = 37
                        change_weaving = 13
                    elif total_changeover_A == 0:
                        total_changeover_A = 37
                        change_diameter = 37

            total_time = consuming_time + total_changeover_A
            end_time = end_time + timedelta(hours=total_time // 60, minutes=total_time % 60)
            new = pd.DataFrame({'Material': elm.materials, 'Total quantity': quantity, 'Name': elm.name,
                                'length(m)/pcs': elm.length, 'consume time(H)': consuming_time,
                                'speed(m/min)': elm.speed,
                                'Weaving_machine': elm.weaving_machine, 'Needle_type': elm.needle_circle,
                                'Diameter': elm.inner_diameter, 'change_diameter_time': change_diameter,
                                'change_weaving_machine_time': change_weaving, 'change_material_time': change_material,
                                'turn_on_machine_time': 0, 'turn_off_machine_time': 0,
                                'total_time': total_time, 'end_time': end_time}, index=[0])
            df_plan = df_plan._append(new, ignore_index=True)
        else:
            consuming_time = getattr(elm.consuming_time, next_week_index)
            quantity = getattr(elm.quantity, next_week_index)
            total_time = consuming_time + 38
            end_time = end_time + timedelta(hours=total_time // 60, minutes=total_time % 60)
            new = pd.DataFrame({'Material': elm.materials, 'Total quantity': quantity, 'Name': elm.name,
                                'length(m)/pcs': elm.length, 'consume time(H)': consuming_time,
                                'speed(m/min)': elm.speed,
                                'Weaving_machine': elm.weaving_machine, 'Needle_type': elm.needle_circle,
                                'Diameter': elm.inner_diameter, 'change_diameter_time': change_diameter,
                                'change_weaving_machine_time': change_weaving, 'change_material_time': change_material,
                                'turn_on_machine_time': 0, 'turn_off_machine_time': 38,
                                'total_time': total_time, 'end_time': end_time}, index=[0])
            df_plan = df_plan._append(new, ignore_index=True)

    df_plan.to_excel('Production_Plan_Machine_A.xlsx')




def plan_optimizer(consuming_time, filtered_products, changeover_matrix):
    mdl = CpoModel(name='singleMachineScheduling')
    jobs = [*range(0, len(consuming_time))]
    # define production processing interval of each job at each machine
    processing_itv_vars = [mdl.interval_var(size=consuming_time[j],
                                            name="{}".format(filtered_products[j].name)) for j in jobs]
    for j in jobs:
        print(processing_itv_vars[j])

    # minimize makespan
    objective = mdl.max([mdl.end_of(processing_itv_vars[j]) for j in jobs])
    mdl.add(mdl.minimize(objective))
    # Sequencing and No Overlap constraints
    sequence_vars = mdl.sequence_var([processing_itv_vars[j] for j in jobs], types=[j for j in jobs], name="sequences")
    mdl.add(mdl.no_overlap(sequence_vars, changeover_matrix))

    msol = mdl.solve(log_output=True, TimeLimit=60)
    return msol

def return_target(msol):
    allvars = msol.solution.get_all_var_solutions()
    vval = allvars[-1].get_value()
    target = [iv.get_name() for iv in vval]
    return target