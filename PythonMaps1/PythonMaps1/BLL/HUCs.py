from PythonMaps1.DAL import hucs as DAL_hucs

class hucs_data:
    __hucs_data={}

    @classmethod
    def all_hucs_csv(cls, limit=None):
        # cls.__load_data()
        # stations=list(cls.__stations_data.values())
        hucs = DAL_hucs.hucs_data.all_hucs_csv(limit=limit)
        return hucs
