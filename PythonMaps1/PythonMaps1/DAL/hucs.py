
import csv
import os
import uuid

class hucs_data:
    __hucs_data={}

    @classmethod
    def all_hucs_csv(cls, limit=None):
        __hucs_data = {}
        cls.__load_data()
        hucs = list( cls.__hucs_data.values() )
        if limit:
            hucs = hucs[:limit]
            return hucs
        else:
            return hucs

    @classmethod
    def __load_data(cls):
        if cls.__hucs_data:
            return

        file = os.path.join(
            os.path.dirname( __file__ ),
            '../data/HUCs_csv.csv'
        )

        with open( file, "r" ) as f:
            # convert file to list
            test = f.read().splitlines()

            print("len " + str(len(test)))

        # print( test )

        fileHandle = open( file, 'r' )

        for line in fileHandle:
            fields = line.split( '|' )

            for u in fields:
                print("u=" + u )
                row = {}
                key = str( uuid.uuid4() )
                row['id'] = key
                row['state1'] = fields[1]
                row['state2'] = fields[2]
                row['huc'] = fields[3]
                row['desc'] = fields[4]
                cls.__hucs_data[key] = row

            print( fields[0] )  # prints the first fields value
            print( fields[1] )  # prints the second fields value

        fileHandle.close()



        # with open( file, 'r', encoding='utf-8' ) as fin:
        #     # brand,name,price,year,damage,last_seen
        #     reader = csv.DictReader( fin )
        #     for row in reader:
        #         key = str( uuid.uuid4() )
        #         row['id'] = key
        #         cls.__hucs_data[key] = row